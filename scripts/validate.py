#!/usr/bin/env python3
"""Validate the design-psychology-foundations skill and its knowledge base.

Checks that SKILL.md, the principle files, cluster indexes, graph and state agree,
that required fields exist, and that no private paths or links leaked in.

Usage: python scripts/validate.py        (exit code 1 on errors)
"""
import json
import pathlib
import re
import sys
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parent.parent
KB = ROOT / "kb"
GRADE = {"S": "Strong", "M": "Moderate", "P": "Practitioner", "C": "Contested"}
CYCLE = {"F": "info", "I": "meaning", "A": "time", "R": "memory"}
REQUIRED_FIELDS = ["- Definition:", "- Evidence grade:", "- Contexts:"]
MAX_PFILE_BYTES = 6500
LEAK_PATTERNS = [r"[A-Z]:\\\\", r"claude\.ai/artifact", r"/mnt/user-data", r"/home/claude"]
# Optional: one regex per line in .private-terms (git-ignored) for names that must never be published.
PRIVATE = ROOT / ".private-terms"
if PRIVATE.exists():
    LEAK_PATTERNS += [l.strip() for l in PRIVATE.read_text(encoding="utf-8").splitlines() if l.strip() and not l.startswith("#")]

errors, warnings = [], []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def slug(name):
    ascii_name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", ascii_name.lower().replace("'", "")).strip("-")


def main():
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")

    # 1. frontmatter
    fm = re.match(r"^---\n(.*?)\n---\n", skill, re.S)
    if not fm:
        err("SKILL.md: missing YAML frontmatter")
    else:
        meta = dict(re.findall(r"^(\w+):\s*(.+)$", fm.group(1), re.M))
        if meta.get("name") != "design-psychology-foundations":
            err(f"SKILL.md: unexpected name {meta.get('name')!r}")
        desc = meta.get("description", "")
        if not desc:
            err("SKILL.md: missing description")
        elif len(desc) > 1024:
            err(f"SKILL.md: description is {len(desc)} chars (max 1024)")

    # 2. principle index in SKILL.md
    index = re.findall(r"^- (.+?) \(([FIAR])·([SMPC])\) (.+?)(?: ⟂ (.+))?$", skill, re.M)
    names = [n for n, *_ in index]
    if len(names) != 106:
        err(f"SKILL.md index lists {len(names)} principles (expected 106)")
    if len(set(names)) != len(names):
        err("SKILL.md index has duplicate principles")

    graph = json.loads((KB / "graph.json").read_text(encoding="utf-8"))
    nodes = {n["id"]: n for n in graph["nodes"] if n.get("kind") == "principle"}
    state = json.loads((KB / "state.json").read_text(encoding="utf-8"))

    for name, cyc, g, _tag, tensions in index:
        path = KB / "p" / f"{slug(name)}.md"
        if not path.exists():
            err(f"{name}: missing {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        head = re.search(r"evidence: (\w+)", text)
        if not head or head.group(1) != GRADE[g]:
            err(f"{name}: SKILL.md grade {GRADE[g]} ≠ file header {head.group(1) if head else 'none'}")
        node = nodes.get(name)
        if not node:
            err(f"{name}: not a principle node in graph.json")
        else:
            if node.get("grade") != GRADE[g]:
                err(f"{name}: SKILL.md grade {GRADE[g]} ≠ graph grade {node.get('grade')}")
            if node.get("cycle") != CYCLE[cyc]:
                err(f"{name}: SKILL.md cycle {cyc} ≠ graph cycle {node.get('cycle')}")
        st = state.get("principles", {}).get(name)
        if not st:
            err(f"{name}: missing from state.json principles")
        elif st.get("grade") != GRADE[g]:
            err(f"{name}: SKILL.md grade {GRADE[g]} ≠ state.json grade {st.get('grade')}")
        for field in REQUIRED_FIELDS:
            if field not in text:
                err(f"{name}: missing field '{field.strip('- :')}'")
        if len(text.encode()) > MAX_PFILE_BYTES:
            warn(f"{name}: {len(text.encode())} bytes (guideline ≤ {MAX_PFILE_BYTES})")
        for t in filter(None, (tensions or "").split(", ")):
            if t not in nodes:
                warn(f"{name}: tension target '{t}' is not a principle")

    # 3. playbooks and tensions reference real principles
    for line in re.findall(r"^- \*\*[^*]+\*\*: (.+)$", skill, re.M):
        for n in line.split(", "):
            if n not in nodes:
                err(f"context playbook references unknown principle '{n}'")

    # 4. clusters: every principle in exactly one, files exist and agree
    seen = {}
    for c in graph["clusters"]:
        cfile = KB / c["file"]
        if not cfile.exists():
            err(f"cluster file missing: {c['file']}")
            continue
        ctext = cfile.read_text(encoding="utf-8")
        for m in c["members"]:
            seen[m] = seen.get(m, 0) + 1
            line = re.search(r"\*\*" + re.escape(m) + r"\*\* \[(\w+)\]", ctext)
            if not line:
                err(f"{c['id']}: {m} missing from cluster file")
            elif nodes.get(m) and line.group(1) != nodes[m]["grade"]:
                err(f"{c['id']}: {m} grade {line.group(1)} ≠ graph {nodes[m]['grade']}")
    for n in nodes:
        if seen.get(n) != 1:
            err(f"{n}: appears in {seen.get(n, 0)} clusters (expected 1)")

    # 5. graph edges point to known nodes
    known = {n["id"] for n in graph["nodes"]}
    bad = [e for e in graph["edges"] if e["s"] not in known or e["d"] not in known]
    if bad:
        err(f"graph.json: {len(bad)} edges reference unknown nodes (e.g. {bad[0]})")

    # 6. required KB files
    for f in ["frameworks.md", "CHANGELOG.md", "UPDATE_PROTOCOL.md", "cycle.json"]:
        if not (KB / f).exists():
            err(f"kb/{f} missing")
    for f in ["growth-design-case-studies.md", "uxtools-articles.md", "uxtools-challenges-tools.md",
              "uxtools-survey.md", "uxtools-episodes.md"]:
        if not (KB / "sources" / f).exists():
            err(f"kb/sources/{f} missing")

    # 7. leak scan (private paths / links)
    for path in [ROOT / "SKILL.md", ROOT / "README.md", *KB.rglob("*.md"), *KB.rglob("*.json"),
                 ROOT / "docs" / "index.html", ROOT / "scripts" / "map_template.html"]:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for pat in LEAK_PATTERNS:
            if re.search(pat, text):
                err(f"{path.relative_to(ROOT)}: matches private pattern {pat}")

    # report
    grades = {}
    for n in nodes.values():
        grades[n["grade"]] = grades.get(n["grade"], 0) + 1
    print(f"principles: {len(nodes)} · clusters: {len(graph['clusters'])} · edges: {len(graph['edges'])} · grades: {grades}")
    for w in warnings:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    print("OK" if not errors else f"FAILED with {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
