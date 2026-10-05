# Design Psychology Foundations

A Claude skill and open knowledge base that grounds design decisions in product psychology. It turns 123 cognitive biases, UX and aesthetic principles into a **semantic network**: each principle has a definition, the mechanism behind it, cited research, an **evidence grade**, concrete design moves with metrics, real product examples, an enterprise note, ethical watch-outs, typed links to other principles, and links to practitioner sources.

It is meant as a base for improving a designer's process: suggest the right principles for a design, audit a flow, and check how solid the science really is before you lean on it.

**[Open the interactive map →](docs/index.html)** (enable GitHub Pages on `/docs` to browse it online)

## What's inside

| | |
|---|---|
| 123 principles | organised on the decision cycle **Filter → Interpret → Act → Remember** (Buster Benson's Cognitive Bias Codex, as used by growth.design) |
| 11 clusters | perception & attention · cognitive load · interaction clarity · value & choice architecture · social influence · triggers & habits · autonomy & ownership · memory & time · user judgment biases · designer/research biases · **aesthetics & visual culture** |
| 14 frameworks | dual-process theory, B.I.A.S./Psych, Fogg & Hook, Prospect Theory, Cialdini, Gestalt, Norman, Cognitive Load Theory, Nielsen/Jakob/Laws of UX, Kano/JTBD/peak-end, Self-Determination Theory, dark-pattern ethics & regulation, replication caveats, empirical aesthetics |
| 15 art & design movements | Renaissance perspective → Arts & Crafts → Art Nouveau → De Stijl → Constructivism → Bauhaus → Isotype → Swiss style → corporate modernism → Pop Art → Postmodernism/Memphis → digital skeuomorphism/flat, plus Japanese Ma & Mingei, Islamic geometry and Brazilian Concrete art — each with original intent, what it signals today, what got lost on the way to digital, and `lineage-of` links to principles |
| ~1,500 typed edges | `supports`, `tension`, `mechanism-of`, `counteracts`, `special-case-of`, `measured-by`, `organises`, `illustrated-by`, `lineage-of` |
| ~1,000 linked sources | growth.design case studies and course outline; uxtools.co articles, practice challenges, tool surveys and podcast episodes |
| Evidence grades | **Strong** 47 · **Moderate** 43 · **Practitioner** 18 · **Contested** 15 — contested principles (failed or mixed replications) are flagged, never presented as settled |

```
SKILL.md                  the skill: modes, loading protocol, playbooks, tensions, principle index
kb/p/<principle>.md       one file per principle (1–6 KB)
kb/clusters/*.md          cluster indexes with grades, tensions and source counts
kb/frameworks.md          the theory backbone
kb/lineage.md             art & design movement cards (intent, signal, digital transmission)
kb/sources/*.md           summarised source library (paraphrased, with links)
kb/graph.json             nodes, typed edges and resources
kb/state.json             update state: seen URLs, review queue, last run
kb/UPDATE_PROTOCOL.md     how to extend the knowledge base
kb/CHANGELOG.md           evidence updates and grade changes
docs/index.html           interactive map (generated)
scripts/validate.py       consistency and leak checks
scripts/build_map.py      rebuilds docs/index.html from kb/
```

## Install

**Claude Code / Claude desktop (local skills):** copy this folder to `~/.claude/skills/design-psychology-foundations/` (keep `kb/` next to `SKILL.md`).

**Claude.ai:** zip the folder (with `SKILL.md` at the root of the zip) and upload it under *Settings → Capabilities → Skills*.

The skill is token-lean: it answers from `SKILL.md` first and loads a single 1–6 KB principle file only when it needs depth.

## How to use it

- **Support** — "Which principles should shape this onboarding for a field-service app?" → 3–7 principles across the cycle, each with a design move, a metric, its evidence grade, and any tensions between them.
- **Validate** — share a screenshot, Figma frame or flow → step-by-step audit (Filter / Interpret / Act / Remember), an ethics gate for dark patterns, a scorecard and the top 3 fixes.
- **Deep research** — "How solid is the Decoy Effect?" → mechanism, evidence and replications, when it applies, design implications and citations.
- **Style & lineage** — "We want it to feel Swiss / handmade / playful" → which movement that comes from, its original intent, what it signals today, what got lost in digital, and the aesthetic principles (with grades) that keep it alive — golden ratio and rule of thirds are flagged as contested.

## Keeping it current

`kb/UPDATE_PROTOCOL.md` describes a monthly pass: scan uxtools.co and growth.design for new content, re-research the weakest-evidence principles, update grades only on strong evidence (meta-analysis, multi-lab replication or ≥ 2 independent studies), then rebuild and validate:

```bash
python scripts/build_map.py
python scripts/validate.py
```

Contributions that add better evidence, correct a grade or add product examples are welcome — please cite sources you actually read and keep principle files under ~6 KB.

## Credits and sources

- Principle set and structure: [growth.design/psychology](https://growth.design/psychology) (Dan Benoni, Louis-Xavier Lavallée) and Buster Benson's *Cognitive Bias Cheat Sheet* / Codex.
- Practitioner sources: [uxtools.co](https://www.uxtools.co) (Tommy Geoco and team) and [growth.design case studies](https://growth.design/case-studies).
- Research citations are listed in each principle file.

All summaries are paraphrased and link back to the originals. This project is independent and not affiliated with or endorsed by growth.design or UX Tools; their names and trademarks belong to their owners.

## License

Text and data in this repository: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Scripts: MIT. See [LICENSE](LICENSE).
