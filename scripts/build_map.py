#!/usr/bin/env python3
"""Build the animated semantic map (docs/index.html) from kb/.

Usage:
  python scripts/build_map.py                      # kb/ -> docs/index.html
  python scripts/build_map.py --kb PATH --out FILE  # any KB copy -> any file
  python scripts/build_map.py --fragment            # omit <html>/<head> wrapper
"""
import argparse
import json
import pathlib
import re
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parent.parent

FRAMEWORK_LABELS = {
    "Dual-process": "Dual-process & heuristics",
    "Cognitive Bias Codex": "Bias Codex · B.I.A.S. · Psych",
    "Fogg": "Fogg B=MAP · Hook · Skinner",
    "Prospect Theory": "Prospect Theory",
    "Cialdini": "Cialdini's influence",
    "Gestalt": "Gestalt perception",
    "Norman": "Norman's design principles",
    "Cognitive Load Theory": "Cognitive Load Theory",
    "Nielsen": "Nielsen · Jakob · Laws of UX",
    "Kano": "Kano · JTBD · Peak-end",
    "Self-Determination": "Self-Determination Theory",
    "Ethics": "Dark-pattern ethics",
    "Replication": "Replication caveats",
}
CYCLE = {"info": "Filter", "meaning": "Interpret", "time": "Act", "memory": "Remember"}


def slug(name):
    ascii_name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", ascii_name.lower().replace("'", "")).strip("-")


def fw_label(raw):
    for key, label in FRAMEWORK_LABELS.items():
        if key.lower() in raw.lower():
            return label
    return raw[:32]


def build(kb: pathlib.Path):
    graph = json.loads((kb / "graph.json").read_text(encoding="utf-8"))
    state = json.loads((kb / "state.json").read_text(encoding="utf-8")) if (kb / "state.json").exists() else {}
    fw_text = (kb / "frameworks.md").read_text(encoding="utf-8")
    fw_sections = {}
    for sec in re.split(r"\n(?=## \d+\. )", fw_text):
        m = re.match(r"## \d+\. (.+)", sec)
        if not m:
            continue
        d = re.search(r"\*\*Definition\.\*\*\s*(.+)", sec)
        model = re.search(r"\*\*Core model in words\.\*\*\s*(.+)", sec)
        grade = re.search(r"\*\*Evidence grade\.\*\*\s*(.+)", sec)
        fw_sections[fw_label(m.group(1))] = dict(
            title=m.group(1).strip(),
            desc=(d.group(1).strip() if d and d.group(1).strip() else (model.group(1).strip() if model else ""))[:900],
            grade=(grade.group(1).strip()[:300] if grade else ""))

    clusters = graph["clusters"]
    nodes, edges = [], []
    principle = {n["id"]: n for n in graph["nodes"] if n.get("kind") == "principle"}
    for c in clusters:
        for name in c["members"]:
            n = principle[name]
            md = (kb / "p" / f"{slug(name)}.md").read_text(encoding="utf-8")
            nodes.append(dict(id=name, label=name, cat=c["id"], tag=n.get("tag", ""), grade=n["grade"],
                              cycle=CYCLE.get(n.get("cycle"), ""), ctx=n.get("ctx", []),
                              md=md.split("\n- Linked sources")[0],
                              res=[[r["title"], r["url"], r["type"], r["why"]]
                                   for r in graph.get("resources", {}).get(name, [])][:15],
                              nres=len(graph.get("resources", {}).get(name, []))))
    fw_ids = {}
    for n in graph["nodes"]:
        if n.get("kind") == "framework":
            label = fw_label(n["id"][3:])
            fw_ids[n["id"]] = "fw:" + label
            sec = fw_sections.get(label, {})
            nodes.append(dict(id="fw:" + label, label=label, cat="fw", desc=sec.get("desc", ""),
                              title=sec.get("title", label), fgrade=sec.get("grade", "")))
    contexts = sorted({c for n in principle.values() for c in n.get("ctx", []) if "(" not in c})
    for c in contexts:
        nodes.append(dict(id="ctx:" + c, label=c, cat="ctx"))

    seen = set()
    for e in graph["edges"]:
        s, d, t = e["s"], e["d"], e["t"]
        if t in ("illustrated-by", "measured-by"):
            continue
        s = fw_ids.get(s, s)
        if s not in principle and not s.startswith("fw:"):
            continue
        if d not in principle:
            continue
        key = (s, d, t) if t != "tension" else (min(s, d), max(s, d), t)
        if key in seen or s == d:
            continue
        seen.add(key)
        edges.append(dict(s=s, t=d, rel=t, **({"note": e["note"]} if e.get("note") else {})))
    for name, n in principle.items():
        for c in n.get("ctx", []):
            if "(" not in c:
                edges.append(dict(s=name, t="ctx:" + c, rel="applies-in"))

    cats = [[c["id"], c["name"]] for c in clusters] + [["fw", "Theory frameworks"], ["ctx", "Design contexts"]]
    return dict(cats=cats, nodes=nodes, edges=edges,
                meta=dict(last_run=state.get("last_run", ""), sources=sum(len(v) for v in graph.get("resources", {}).values())))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kb", default=str(ROOT / "kb"))
    ap.add_argument("--out", default=str(ROOT / "docs" / "index.html"))
    ap.add_argument("--fragment", action="store_true", help="write page content without the <html>/<head> wrapper")
    a = ap.parse_args()
    data = build(pathlib.Path(a.kb))
    tpl = (ROOT / "scripts" / "map_template.html").read_text(encoding="utf-8")
    page = tpl.replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
    if not a.fragment:
        page = ('<!doctype html>\n<html lang="en"><head><meta charset="utf-8">'
                '<meta name="viewport" content="width=device-width, initial-scale=1">\n' + page + "\n</html>\n")
    out = pathlib.Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size // 1024} KB · {len(data['nodes'])} nodes · {len(data['edges'])} relations)")


if __name__ == "__main__":
    main()
