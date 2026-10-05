---
name: design-psychology-foundations
description: Ground design work in product psychology — a semantic network of 123 cognitive biases, UX and aesthetic principles, 14 theory frameworks, 15 art & design movements, evidence grades and ~1,000 linked sources (growth.design case studies, uxtools.co). Use to suggest principles for a design, validate or audit a flow or screen, research the science behind a design decision, or trace what a visual style signals and where it comes from.
---

# Design Psychology Foundations

A **semantic network**, not a list. Nodes: 123 principles · 11 clusters · 14 frameworks · 15 art & design movements · 21 design contexts · ~1,000 linked sources (growth.design case studies, uxtools.co articles/challenges/survey/episodes). Edges (typed): `mechanism-of`, `supports`, `tension` (⟂), `counteracts`, `special-case-of`, `measured-by`, `organises`, `illustrated-by`, `lineage-of` (movement → principle).

Every interaction runs the **B.I.A.S. cycle** (Benson's codex as used by growth.design): **F**ilter/Block → **I**nterpret → **A**ct → **R**emember/Store. Each principle carries its cycle step, cluster and evidence grade: **S** strong · **M** moderate · **P** practitioner heuristic · **C** contested (failed or mixed replications — never present as settled).

## When to use
- A designer is creating or reviewing a screen, flow, onboarding, pricing page, design-system component, brand touchpoint or product catalogue and wants the psychology behind it.
- Questions like "why does this work / not work", "what principle supports this", "validate/audit this", "research the foundations of X".
- A design decision needs evidence-based rationale for stakeholders.

## Token-lean loading protocol (cheapest first, stop as soon as the answer is solid)
1. **This file only** — name principles, pick from a context playbook, resolve tensions. Most quick asks end here.
2. **One principle file** (~1–4 KB): definition, mechanism, cited evidence, grade, design moves with metrics, product examples, B2B note, ethics, typed edges, top linked sources. Path `kb/p/<slug>.md`; slug = lowercase ASCII, apostrophes dropped, other non-alphanumerics → `-` (Hick's Law → `hicks-law`, Fitts's Law → `fittss-law`, Aha! Moment → `aha-moment`, Law of Prägnanz → `law-of-pragnanz`). Load ≤3 per turn; follow edges by loading neighbours only when needed.
3. **Cluster index** `kb/clusters/<file>` (~4 KB) — all members with grade, tensions, supports, source counts. Use to traverse a family.
3b. **Lineage** `kb/lineage.md` (~25 KB; read one `##` card) — 15 art & design movements: dates, figures, original intent, what the style signals today, how it reached digital, what got lost, linked principles. Principle files name their movements in a `Lineage` line.
4. **Theory** `kb/frameworks.md` (~55 KB; read only the relevant `## n.` section) — dual-process, Codex/B.I.A.S./Psych, Fogg/Hook/Skinner, Prospect Theory, Cialdini, Gestalt, Norman, Cognitive Load Theory, Nielsen/Jakob/Laws of UX, Kano/JTBD/peak-end, SDT, dark-pattern ethics & regulation, replication caveats, empirical aesthetics (§14).
5. **Sources** (large: search, never load whole) — `kb/sources/growth-design-case-studies.md` (47+10 case studies, tactics, Product Psychology course outline, C.L.E.A.R. UI course), `uxtools-articles.md` (69 posts), `uxtools-challenges-tools.md` (18 practice challenges + tutorials, 9 tool categories), `uxtools-survey.md` (Design Tools Survey 2024, State of Prototyping 2026 data), `uxtools-episodes.md` (11 transcript summaries + index of 47 episodes).
6. **Web research** only for freshness, gaps or primary-source verification.

Where the KB lives: the `kb/` folder next to this file (this repository). If the skill is installed without the folder, read the same paths from the GitHub repository (raw files) or fall back to web research. `kb/CHANGELOG.md` lists evidence updates; `kb/UPDATE_PROTOCOL.md` explains how to extend the KB.

## Modes
**SUPPORT** (suggest) → identify context(s) + journey moment → start from the context playbook → walk F-I-A-R so picks aren't all from one step → choose 3–7 (Hick's Law applies to advice too) → for each: why here · design move · metric/test · grade. Check ⟂ tensions among picks and state the resolution. Load p-files only for the picks you'll go deep on.

**VALIDATE** (audit; input can be a screenshot, Figma frame, flow description, URL or file) → describe the flow step by step → per step ask: F is the key info noticed? I does it match the mental model / build trust? A is the action easy, default sane, feedback clear? R will the ending/peak be remembered, can users resume? → for visual, brand or marketing surfaces add a **style-signal check**: what does the style signal, to whom, and does that fit the product's job and audience? Which movement does it inherit (lineage card)? Are aesthetic claims graded (golden ratio and rule of thirds are Contested)? Experts and users differ (Symmetry, Curvature, Visual Complexity Preference) — test with users, not the team → ethics gate → scorecard `Step | Principle | ✅/⚠️/❌ | Evidence in design | Fix | H/M/L` → top 3 fixes by impact÷effort + what to test.

**DEEP RESEARCH** → p-file → its `Explained by frameworks` → frameworks.md section → its linked sources → web for primary papers (and uxtools.co as a practitioner reference). Report: mechanism → evidence & grade (say if contested) → when it applies/doesn't → design implications → examples → citations. Offer to save the note alongside the project's design docs.

**STYLE & LINEAGE** (visual direction, brand, "make it feel X") → describe the visual choice formally → match it to a movement card in `kb/lineage.md` → original intent → what it signals today → what got lost on the way to digital → the C11 principles that keep it alive or contradict it, with grades → recommendation in one line ("Use X because it signals Y, which these users need for Z"); mark interpretation as interpretation. For deep history, drills and reading, hand off to the companion **designer-growth-foundations** skill (Module H) when installed.

**Reasoning over the network**: explain *why* via `mechanism-of` chains, predict side effects via `tension` and Second-Order Effect, justify to stakeholders with S/M evidence first, P as practice, C only with caveats. Name designer-side biases (C10) when critiquing research or roadmaps. Name principles exactly as in the index so they stay searchable; always say which principles you used and why.

## Ethics gate (always in VALIDATE)
❌ fake scarcity/urgency/social proof/anchors · trapping defaults, tiny or hidden cancel, roach-motel offboarding · confirmshaming / guilt copy · variable rewards or triggers with no user benefit and no exit points · framing that hides cost · cashless obfuscation. Tests: *Would the user thank us if they understood exactly how this works?* (Regret test) and nudge vs sludge. Note regulation (FTC 2022 dark-patterns report, EU DSA Art. 25) in frameworks §12.

## Enterprise & complex products
For enterprise, industrial and safety-critical software, weight trust, clarity and error prevention — Mental Model, Signifiers, Feedforward, Feedback Loop, Recognition Over Recall, Cognitive Load, Visual Hierarchy, Default Bias, Authority Bias — above growth tactics (Scarcity, Variable Reward). Each principle file has an Enterprise/B2B note.

## Context playbooks (ranked by evidence, then source depth)
- **onboarding**: Default Bias, Cognitive Load, Familiarity Bias, Reciprocity, Social Proof, Peak-End Rule, Hick's Law, Authority Bias, Goal Gradient Effect
- **settings**: Default Bias, Cognitive Load, Familiarity Bias, Social Proof, Hick's Law, Authority Bias, Reactance, Recognition Over Recall, Anchoring Bias
- **content/copy**: Cognitive Load, Familiarity Bias, Reciprocity, Social Proof, Framing, Authority Bias, Confirmation Bias, Survey Bias, Reactance
- **research**: Peak-End Rule, Authority Bias, Confirmation Bias, Survey Bias, Survivorship Bias, Availability Heuristic, Anchoring Bias, Halo Effect, Negativity Bias
- **retention**: Reciprocity, Loss Aversion, Peak-End Rule, Survey Bias, Survivorship Bias, Goal Gradient Effect, Sunk Cost Effect, Variable Reward, Negativity Bias
- **dashboards**: Cognitive Load, Confirmation Bias, Survivorship Bias, Availability Heuristic, Recognition Over Recall, Anchoring Bias, Law of Similarity, Von Restorff Effect, Fitts's Law
- **pricing**: Default Bias, Reciprocity, Social Proof, Loss Aversion, Framing, Hick's Law, Authority Bias, Reactance, Anchoring Bias
- **notifications**: Default Bias, Loss Aversion, Hick's Law, Reactance, Variable Reward, Von Restorff Effect, Negativity Bias, Banner Blindness, Selective Attention
- **checkout**: Default Bias, Social Proof, Loss Aversion, Peak-End Rule, Framing, Authority Bias, Goal Gradient Effect, Anchoring Bias, Fitts's Law
- **forms**: Default Bias, Cognitive Load, Hick's Law, Goal Gradient Effect, Recognition Over Recall, Anchoring Bias, Law of Similarity, Chunking, Fitts's Law
- **navigation**: Familiarity Bias, Hick's Law, Availability Heuristic, Recognition Over Recall, Law of Similarity, Chunking, Von Restorff Effect, Serial Position Effect, Fitts's Law
- **stakeholder-communication**: Framing, Confirmation Bias, Survey Bias, Survivorship Bias, Availability Heuristic, Sunk Cost Effect, Halo Effect, Serial Position Effect, False Consensus Effect
- **errors**: Cognitive Load, Loss Aversion, Peak-End Rule, Von Restorff Effect, Negativity Bias, Fitts's Law, Banner Blindness, Affect Heuristic, Self-Serving Bias
- **data-viz**: Cognitive Load, Framing, Confirmation Bias, Availability Heuristic, Picture Superiority Effect, Law of Similarity, Chunking, Von Restorff Effect, Selective Attention
- **branding**: Visual Style Connotation, Familiarity Bias, Processing Fluency, MAYA Principle, Colour–Emotion Associations, Social Proof, Authority Bias, Halo Effect, Picture Superiority Effect
- **visual-design**: Processing Fluency, Fifty-Millisecond Impression, Visual Complexity Preference, Prototypicality, Visual Balance, Unity-in-Variety, Symmetry Preference, Curvature Preference, Aesthetic-Usability Effect
- **gamification**: Goal Gradient Effect, Sunk Cost Effect, Variable Reward, Self-Serving Bias, Hyperbolic Discounting, Shaping, Spacing Effect, Feedback Loop, Curiosity Gap
- **offboarding**: Reciprocity, Loss Aversion, Peak-End Rule, Framing, Survey Bias, Survivorship Bias, Reactance, Sunk Cost Effect, Negativity Bias
- **empty-states**: Banner Blindness, Shaping, Discoverability, Curiosity Gap, Progressive Disclosure, Curse of Knowledge, Pseudo-Set Framing, Delighters, Spark Effect
- **loading/waits**: Peak-End Rule, Goal Gradient Effect, Chronoception, Planning Fallacy, Feedback Loop, Labor Illusion, Sensory Appeal, Expectations Bias, Delighters
- **search**: Confirmation Bias, Availability Heuristic, Recognition Over Recall, Picture Superiority Effect, Discoverability, Method of Loci, Bandwagon Effect, Labor Illusion, Pareto Principle

## Key tensions (resolve explicitly)
- Von Restorff Effect ⟂ Law of Similarity: consistency everywhere, distinctiveness for one primary action per view; if everything is highlighted, nothing is.
- Progressive Disclosure ⟂ Discoverability: hide by *frequency of use*, not by importance; keep a visible signifier (overflow, "Advanced") and test findability of hidden items.
- Aesthetic-Usability Effect ⟂ Signifiers: minimal styling must still show what is clickable; beauty may mask usability problems in tests, so measure task success, not just ratings.
- Familiarity Bias / Jakob's Law ⟂ Delighters: be conventional in structure and navigation, novel in moments of value; innovate where it changes the outcome, not the chrome.
- Default Bias / Nudge ⟂ Reactance: defaults should be what most users would pick if informed, visibly changeable, with a reason given; hidden or self-serving defaults trigger reactance and regulatory risk.
- Scarcity ⟂ Reactance: use only real, verifiable limits; explicit pressure ("only 2 left — hurry!") on low-stakes items reads as manipulation.
- Loss Aversion ⟂ Noble Edge Effect: loss framing for genuine risks (data loss, security); avoid confirmshaming, which costs warmth and brand trust.
- Variable Reward ⟂ Flow State / SDT autonomy: unpredictability in discovery and content is fine; core workflows need predictable, informational feedback.
- Investment Loops / Sunk Cost Effect ⟂ Provide Exit Points: make data export and cancellation as easy as onboarding; retention earned through value, not lock-in.
- Hick's Law (fewer choices) ⟂ Pareto Principle / expert flexibility: reduce options for novices via defaults and grouping; give experts shortcuts and saved views rather than removing capability (Chernev's moderators decide).
- Cognitive Load ⟂ Tesler's Law: remove extraneous load ruthlessly, but don't push irreducible complexity onto users by oversimplifying; the system should absorb it.
- Curiosity Gap / Zeigarnik Effect ⟂ Cognitive Load: open loops motivate in moderation; too many unfinished items (badges, checklists) become stress and noise.
- Labor Illusion ⟂ Chronoception / Doherty-style speed: show work only when a wait is unavoidable; never add artificial delay to fast operations beyond what aids trust.
- Social Proof / Bandwagon Effect ⟂ Singularity Effect: aggregate numbers build legitimacy, a single identifiable story builds emotion; use one named case next to the count.
- Peak-End Rule ⟂ Negativity Bias / Hyperbolic Discounting: protect the end of flows and eliminate negative peaks first; don't sacrifice the experiencing self (ongoing friction) for a memorable finale.

- Processing Fluency / Prototypicality ⟂ Von Restorff Effect / Aesthetic Aha: fluent and typical wins first impressions, but distinct and slightly challenging builds memory and delight — MAYA Principle: typical structure, one advanced element; test familiarity and novelty separately.
- Symmetry, Curvature and Visual Complexity Preference ⟂ designer taste: lay users prefer simpler, symmetric, curved forms more than experts do (Curse of Knowledge, False Consensus Effect) — validate visual direction with target users, not the design team.
- Golden Ratio / Rule of Thirds ⟂ evidence: fine as modular or compositional habits, but never claim them as perceptual laws in rationale; justify proportions by content, grid maths and tests.
- Visual Style Connotation ⟂ Familiarity Bias / trends: a borrowed style imports its original signal (Swiss = neutral authority, Arts & Crafts = handmade, Constructivism = revolution); check the signal fits before following a trend, and credit non-European sources instead of using them as decoration.

## Mechanism chains (why principles co-occur)
- Limited working memory (~4 chunks) → Cognitive Load → Hick's Law, Chunking, Miller's Law (as misnomer), Recognition Over Recall, Progressive Disclosure, Decision Fatigue (contested), Serial Position Effect (recency).
- Pre-attentive perceptual grouping → Gestalt laws (Proximity, Similarity, Prägnanz) → Visual Hierarchy, Chunking (visual), Juxtaposition, Banner Blindness (ad-shaped regions grouped and filtered).
- Salience / bottom-up attention capture → Selective Attention & Attentional Bias → Von Restorff Effect, Contrast, Visual Anchors, Centre-Stage Effect, Picture Superiority Effect, Sensory Appeal.
- Motor control (speed–accuracy trade-off) → Fitts's Law → target sizing, edge/corner placement, thumb zones; interacts with Hick's Law in menu design.
- Reference-dependent valuation (prospect theory) → Loss Aversion & diminishing sensitivity → Endowment Effect, Sunk Cost Effect, Framing, Anchoring Bias, Decoy Effect, Default Bias, Pseudo-Set Framing, Weber's Law (just-noticeable price/feature differences), Cashless Effect.
- Present bias / time preference → Hyperbolic Discounting → Temptation Bundling, Planning Fallacy, Fresh Start Effect, Goal Gradient Effect, trial/subscription design.
- System 1 shortcut reliance (bounded rationality) → Heuristics (availability, affect, representativeness) → Availability Heuristic, Affect Heuristic, Halo Effect, Aesthetic-Usability Effect, Authority Bias, Social Proof, Barnum-Forer Effect.
- Socially learned compliance rules → Cialdini principles → Social Proof → Bandwagon Effect; Commitment & Consistency → Investment Loops → Sunk Cost Effect; Reciprocity → free-value-first onboarding.
- Operant reinforcement → Prompt + Ability + Motivation (B=MAP) → Hook loop → External Trigger → Internal Trigger; Variable Reward; Shaping → Aha! Moment → Investment Loops → habit/retention.
- Goal tension / open loops → Zeigarnik Effect & Goal Gradient Effect → progress bars, checklists, Curiosity Gap, endowed progress.
- Basic psychological needs (SDT) → autonomy threatened → Reactance → Streisand Effect, Backfire Effect (contested); competence satisfied → IKEA Effect, Flow State, Aha! Moment; relatedness → Group Attractiveness Effect, Social Proof.
- Consistency drive / dissonance reduction → Cognitive Dissonance → Confirmation Bias, Commitment & Consistency, Self-Serving Bias, post-purchase rationalisation (Sunk Cost Effect).
- Memory encoding & retrieval dynamics → Serial Position Effect, Spacing Effect, Method of Loci, Picture Superiority Effect, Storytelling Effect → Peak-End Rule (remembering self) → Delighters, Negativity Bias, Availability Heuristic → return/recommend decisions.
- Mental models & conceptual mapping → Familiarity Bias / Jakob's Law → Skeuomorphism, Signifiers, Feedforward, Feedback Loop → gulfs of execution/evaluation closed → Discoverability, error recovery (Provide Exit Points).
- Time perception → Chronoception (duration judged by attention & uncertainty) → Labor Illusion, Parkinson's Law, Peak-End duration neglect → loading/waiting design.
- Egocentric projection (designer side) → Curse of Knowledge & Empathy Gap & False Consensus Effect → Law of the Instrument, Planning Fallacy, Survivorship Bias, Survey Bias, Observer-Expectancy / Hawthorne Effects → biased research → Second-Order Effects shipped unnoticed.

- Ease of perceptual processing (fluency) → positive affect misattributed to the object → Processing Fluency → Prototypicality, Symmetry Preference, Visual Balance, Fractal Fluency, Fifty-Millisecond Impression → Aesthetic-Usability Effect & Halo Effect → trust and perceived usability; balanced by novelty and insight (MAYA Principle, Aesthetic Aha, Unity-in-Variety).
- Learned cultural association → Visual Style Connotation & Colour–Emotion Associations → brand personality and expectations → Familiarity Bias / Mental Model; movements in `kb/lineage.md` explain where each association came from.

## Principle index — (cycle·grade) tagline ⟂ main tensions

**C1 Perceptual organisation & attention** · C1-perceptual-organisation-attention.md
- Law of Proximity (F·S) Near things seem related
- Law of Similarity (I·S) Similar-looking = related ⟂ Von Restorff Effect
- Law of Prägnanz (I·S) Ambiguity is read in the simplest form
- Visual Hierarchy (F·P) Order in which things are perceived
- Visual Anchors (F·P) Elements that guide the eye ⟂ Banner Blindness
- Contrast (F·S) Heavier visual weight draws attention ⟂ Aesthetic-Usability Effect
- Von Restorff Effect (F·S) The odd one out gets noticed ⟂ Banner Blindness, Selective Attention
- Juxtaposition (F·M) Close + similar = one unit
- Centre-Stage Effect (F·M) People pick the middle option ⟂ Serial Position Effect
- Banner Blindness (F·S) Users ignore what looks like ads ⟂ Von Restorff Effect, Visual Anchors
- Selective Attention (F·S) Focus filters out the environment ⟂ Von Restorff Effect, Flow State
- Attentional Bias (F·M) Current thoughts filter what users notice ⟂ Decision Fatigue
- Aesthetic-Usability Effect (F·C) Beautiful feels easier ⟂ Contrast, Occam's Razor
- Sensory Appeal (R·M) Multi-sensory experiences engage more ⟂ Cognitive Load
- Picture Superiority Effect (R·S) Images beat words for recall ⟂ Banner Blindness
- Weber's Law (A·S) Small changes go unnoticed ⟂ Anchoring Bias, Von Restorff Effect

**C2 Cognitive load & complexity management** · C2-cognitive-load-complexity-management.md
- Cognitive Load (F·S) Mental effort needed to complete a task ⟂ Fitts's Law, Curiosity Gap
- Hick's Law (F·S) More choices → slower, harder decisions ⟂ Discoverability, Decoy Effect
- Miller's Law (I·C) Working memory holds ~4 chunks, not 7 ⟂ Hick's Law
- Chunking (R·S) Grouped info is easier to remember
- Progressive Disclosure (F·M) Reveal complexity gradually ⟂ Discoverability, Recognition Over Recall
- Tesler's Law (F·P) Complexity can't vanish — only move ⟂ Law of the Instrument, Cognitive Load
- Occam's Razor (I·P) Prefer the simplest adequate solution ⟂ Signifiers, Aesthetic-Usability Effect
- Pareto Principle (A·P) ~80% of effects from ~20% of causes ⟂ Second-Order Effect, Survivorship Bias
- Decision Fatigue (A·C) Many decisions degrade decision quality ⟂ Attentional Bias, Reactance
- Recognition Over Recall (R·S) Recognising beats remembering ⟂ Progressive Disclosure
- Fitts's Law (F·S) Bigger, closer targets are faster to hit ⟂ Cognitive Load

**C3 Interaction clarity & mental models** · C3-interaction-clarity-mental-models.md
- Mental Model (I·M) Users bring beliefs about how things work ⟂ Curse of Knowledge, Law of the Instrument
- Signifiers (F·P) Cues that communicate what an element does ⟂ Occam's Razor, Aesthetic-Usability Effect
- Feedforward (I·P) Know the result before acting
- Feedback Loop (F·M) Actions need visible results ⟂ Variable Reward, Cashless Effect
- Discoverability (A·S) Users can find features by looking ⟂ Hick's Law, Progressive Disclosure
- Familiarity Bias (I·S) People prefer what they know ⟂ Delighters, Curse of Knowledge
- Skeuomorphism (I·M) Real-world resemblance eases adoption ⟂ Occam's Razor, Cognitive Load
- Provide Exit Points (R·P) Let users leave at the right moment ⟂ Investment Loops, Sunk Cost Effect

**C4 Value, reference points & choice architecture** · C4-value-reference-points-choice-architectu.md
- Anchoring Bias (F·S) The first number/info seen sets the reference ⟂ Weber's Law
- Framing (F·S) Presentation changes decisions more than facts do ⟂ Reactance, Backfire Effect
- Decoy Effect (F·M) A worse third option makes the target look better (numeric side-by-side only) ⟂ Hick's Law
- Loss Aversion (A·S) Losses hurt more than equal gains please ⟂ Cashless Effect, Noble Edge Effect
- Endowment Effect (R·C) Owning it makes it worth more ⟂ Reactance
- Sunk Cost Effect (A·S) Prior investment keeps people going ⟂ Provide Exit Points
- Pseudo-Set Framing (I·M) Grouped tasks beg completion ⟂ Reactance
- Unit Bias (I·M) One unit feels like the right amount
- Cashless Effect (A·M) Invisible money is spent more freely ⟂ Loss Aversion, Feedback Loop
- Default Bias (A·S) People stick with the preset ⟂ Reactance
- Nudge (F·M) Small cues steer choices without forcing (expect ~1–2 pp lifts) ⟂ Reactance, Second-Order Effect
- Hyperbolic Discounting (A·S) Now beats later ⟂ Empathy Gap, Planning Fallacy
- Temptation Bundling (A·M) Pair a 'should' with a 'want' ⟂ Second-Order Effect
- Scarcity (I·M) Limited supply raises perceived value ⟂ Reactance, Streisand Effect

**C5 Social influence & trust** · C5-social-influence-trust.md
- Social Proof (I·S) People copy what others do ⟂ Reactance, Survey Bias
- Authority Bias (I·S) Experts' opinions weigh more ⟂ Reactance, Backfire Effect
- Reciprocity (I·S) Give value first, users give back ⟂ Reactance
- Commitment & Consistency (A·M) Small yeses lead to bigger ones ⟂ Reactance
- Bandwagon Effect (A·M) Adoption grows with adoption ⟂ Familiarity Bias, Singularity Effect
- Group Attractiveness Effect (I·M) Items look better in a group ⟂ Von Restorff Effect
- Halo Effect (I·S) One trait colours the whole judgment ⟂ Negativity Bias
- Noble Edge Effect (I·M) Users favour caring, responsible brands ⟂ Reactance, Loss Aversion
- Singularity Effect (I·M) One person moves us more than a crowd (narrow single-victim version contested) ⟂ Survivorship Bias, Social Proof
- Spotlight Effect (I·M) We think others notice us more than they do ⟂ Hawthorne Effect
- False Consensus Effect (A·S) We think others agree with us ⟂ Survey Bias, Empathy Gap

**C6 Triggers, rewards & habit loops** · C6-triggers-rewards-habit-loops.md
- External Trigger (F·P) The prompt contains the next step ⟂ Internal Trigger, Banner Blindness
- Internal Trigger (R·P) Memory/emotion prompts action ⟂ External Trigger
- Self-Initiated Triggers (I·M) Users respond to prompts they set
- Variable Reward (I·S) Unpredictable rewards drive repeat behaviour ⟂ Feedback Loop, Expectations Bias
- Investment Loops (A·P) Invested users come back ⟂ Provide Exit Points
- Shaping (R·S) Reinforce steps toward a target behaviour
- Goal Gradient Effect (I·S) Motivation rises near the finish
- Zeigarnik Effect (R·C) Unfinished tasks stick in mind ⟂ Fresh Start Effect, Provide Exit Points
- Spark Effect (F·P) Small effort → more action ⟂ IKEA Effect
- Fresh Start Effect (I·M) New beginnings spark action ⟂ Zeigarnik Effect
- Curiosity Gap (I·M) Missing information creates a pull to fill it ⟂ Cognitive Load, Streisand Effect

**C7 Autonomy, competence & ownership** · C7-autonomy-competence-ownership.md
- Reactance (A·S) Forcing creates resistance ⟂ Nudge, Framing
- IKEA Effect (A·M) Self-made things feel more valuable ⟂ Spark Effect
- Flow State (I·C) Full immersion in a task ⟂ Selective Attention, Variable Reward
- Aha! Moment (I·P) When users first get the value
- Delighters (R·P) Unexpected small pleasures are remembered ⟂ Familiarity Bias
- Streisand Effect (I·P) Censoring spreads the info ⟂ Curiosity Gap, Scarcity

**C8 Memory, time & experience over time** · C8-memory-time-experience-over-time.md
- Peak-End Rule (R·S) Experiences are judged by peaks and the ending ⟂ Expectations Bias, Chronoception
- Serial Position Effect (R·S) First and last are remembered ⟂ Centre-Stage Effect
- Spacing Effect (R·S) Spaced repetition beats cramming ⟂ Cognitive Load
- Method of Loci (R·S) Location aids memory ⟂ Familiarity Bias
- Storytelling Effect (R·M) Stories beat facts for memory ⟂ Availability Heuristic
- Negativity Bias (R·S) Bad sticks more than good ⟂ Halo Effect, Affect Heuristic
- Availability Heuristic (R·S) Recent/easy-to-recall wins ⟂ Planning Fallacy, Storytelling Effect
- Labor Illusion (A·M) Visible effort increases perceived value ⟂ Parkinson's Law, Chronoception
- Chronoception (A·S) Time perception is subjective ⟂ Parkinson's Law, Peak-End Rule
- Parkinson's Law (A·P) Work expands to fill the time ⟂ Labor Illusion, Planning Fallacy

**C9 Belief, judgment & self-perception biases (user side)** · C9-belief-judgment-self-perception-biases-u.md
- Confirmation Bias (F·S) People seek evidence for what they already believe
- Priming (F·C) Earlier stimuli shape later responses ⟂ Observer-Expectancy Effect
- Expectations Bias (F·M) Expectations shape perception ⟂ Peak-End Rule, Variable Reward
- Affect Heuristic (A·S) Current emotion steers judgment ⟂ Negativity Bias
- Backfire Effect (A·C) Challenges harden beliefs ⟂ Authority Bias, Framing
- Cognitive Dissonance (I·C) Holding conflicting ideas is uncomfortable
- Barnum-Forer Effect (A·S) Generic descriptions feel personal ⟂ Curse of Knowledge
- Self-Serving Bias (A·S) Credit for wins, blame for losses ⟂ Hindsight Bias
- Dunning-Kruger Effect (A·C) Low skill → overconfidence ⟂ Curse of Knowledge

**C10 Designer, research & systems-thinking biases (team side)** · C10-designer-research-systems-thinking-biase.md
- Empathy Gap (F·M) We underestimate emotion's pull on behaviour ⟂ Hyperbolic Discounting, False Consensus Effect
- Curse of Knowledge (I·M) Experts forget what novices don't know ⟂ Mental Model, Familiarity Bias
- Survivorship Bias (F·S) Ignoring what didn't make it through ⟂ Survey Bias, Singularity Effect
- Hawthorne Effect (I·C) Being observed changes behaviour ⟂ Spotlight Effect
- Observer-Expectancy Effect (A·M) Researcher bias leaks into participants ⟂ Priming
- Survey Bias (I·S) Answers skew to the socially acceptable ⟂ Survivorship Bias, Social Proof
- Hindsight Bias (I·S) 'I knew it all along' ⟂ Planning Fallacy, Self-Serving Bias
- Law of the Instrument (A·P) With a hammer, everything's a nail ⟂ Tesler's Law, Mental Model
- Planning Fallacy (A·S) Tasks take longer than planned ⟂ Hindsight Bias, Parkinson's Law
- Second-Order Effect (A·P) Consequences of consequences ⟂ Temptation Bundling, Nudge

**C11 Aesthetics & visual culture** · C11-aesthetics-visual-culture.md
- Processing Fluency (I·S) Easy to process feels good and true ⟂ Aesthetic Aha
- Prototypicality (I·M) Typical-looking designs are liked faster ⟂ Von Restorff Effect
- MAYA Principle (I·M) Most advanced, yet acceptable — novel but recognisable
- Unity-in-Variety (I·M) Coherence plus richness beats either alone
- Fifty-Millisecond Impression (F·M) Visual appeal is judged almost instantly
- Visual Complexity Preference (F·M) Simpler screens usually win first impressions
- Symmetry Preference (F·M) Symmetry pleases most people, not experts ⟂ Von Restorff Effect
- Curvature Preference (I·M) Curves preferred over sharp angles, modestly
- Visual Balance (F·M) Weighted elements feel settled around the centre
- Colour–Emotion Associations (I·M) Colours carry shared, partly universal feelings
- Fractal Fluency (F·M) Nature-like mid-complexity patterns are easy and calming
- Aesthetic Aha (I·M) Pleasure spikes when hidden order clicks
- Visual Style Connotation (I·M) How it looks says what it is
- Complexity–Arousal Curve (F·C) Medium complexity liked most — on average ⟂ Processing Fluency
- Golden Ratio (I·C) 1.618 is folklore more than a law
- Rule of Thirds (F·C) A useful habit, not a perceptual law ⟂ Centre-Stage Effect
- Peak Shift Effect (I·C) Exaggerated defining features can beat the original ⟂ Prototypicality

## Recommended reading
Cognitive Biases Codex (Buster Benson) · Super Thinking (Weinberg & McCann) · Hooked (Nir Eyal) · Influence & Pre-Suasion (Cialdini) · Predictably Irrational (Ariely) · Thinking, Fast and Slow (Kahneman) · The Design of Everyday Things (Norman) · Laws of UX (Yablonski) · Tiny Habits (Fogg) · Art and Visual Perception (Arnheim) · Interaction of Color (Albers) · A History of Graphic Design (Meggs) · Ways of Seeing (Berger) · Reber, Schwarz & Winkielman 2004 (processing fluency) · Smarthistory (free).