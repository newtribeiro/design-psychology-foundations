# Theory backbone — 13 frameworks that explain the 106 principles

## 1. Dual-process theory, heuristics & biases, bounded rationality

**Definition.** Dual-process accounts split cognition into a fast, automatic, associative, low-effort mode (Type 1 / "System 1") and a slow, deliberate, working-memory-dependent mode (Type 2 / "System 2"). The heuristics-and-biases programme (Tversky & Kahneman) showed that people judge probability and value with a few shortcut rules (representativeness, availability, anchoring-and-adjustment) that are usually adequate but produce systematic, predictable errors. Bounded rationality (Simon) says real agents have limited information, time and computation, so they *satisfice* — pick the first option that clears an aspiration level — rather than optimise.

**Core model in words.** Picture two lanes feeding a decision. Lane 1 is always on: it pattern-matches, reacts to salience, emotion, familiarity and defaults, and hands Lane 2 a ready-made impression. Lane 2 is lazy and capacity-limited: it only intervenes when something feels wrong, stakes are high, or there is spare attention, and it is itself bounded by working memory. Heuristics are the rules Lane 1 uses; biases are the residue when the rule mismatches the environment. Simon's addition: the *environment* is half the scissors — a well-structured environment makes simple heuristics accurate ("ecological rationality", later Gigerenzer).

**Key sources.**
- Tversky & Kahneman (1974), "Judgment under Uncertainty: Heuristics and Biases", *Science* 185:1124–1131 — https://pubmed.ncbi.nlm.nih.gov/17835457/
- Simon (1955), "A Behavioral Model of Rational Choice", *Quarterly Journal of Economics* 69(1) — summary via The Decision Lab: https://thedecisionlab.com/thinkers/computer-science/herbert-simon
- Evans & Stanovich (2013), "Dual-process theories of higher cognition: advancing the debate", *Perspectives on Psychological Science* 8(3) — https://scottbarrykaufman.com///wp-content/uploads/2014/04/dual-process-theory-Evans_Stanovich_PoPS13.pdf
- Kahneman (2011), *Thinking, Fast and Slow* (popular synthesis; "System 1/2" labels popularised here; book, no URL).

**Evidence grade.** Strong for the existence of the classic heuristics (anchoring, availability, framing replicate well, e.g. Many Labs). Moderate for the strict two-system architecture — Evans & Stanovich themselves prefer "Type 1/Type 2 processes" and warn against treating the feature lists (fast/unconscious/emotional) as perfectly co-occurring.

**Principles explained / organised.**
- mechanism-of → Anchoring Bias, Availability Heuristic, Affect Heuristic, Framing, Confirmation Bias, Default Bias, Halo Effect, Priming, Expectations Bias, Familiarity Bias, Survivorship Bias, Barnum-Forer Effect, Hindsight Bias, Planning Fallacy, Dunning-Kruger Effect
- organises → Nudge (choice architecture = designing for Lane 1), Occam's Razor (simplest-sufficient explanation), Pareto Principle (satisficing on the vital few)
- supports → Recognition Over Recall, Cognitive Load (Type 2 is the scarce resource), Decision Fatigue (claimed depletion of Type 2 — see §13)
- tension → Cognitive Dissonance / Backfire Effect (System 2 is often used to *rationalise* System 1 conclusions rather than correct them)

**How a designer uses it.**
- Classify each screen moment as System-1 (glance, scroll, tap) or System-2 (compare plans, configure a complex workflow): design the former for recognition, salience and safe defaults; design the latter for comparison tables, undo and time.
- Assume users satisfice: the first plausible option wins, so order and default carry weight — make the first plausible option also the right one.
- Use "speed bumps" (confirmation, summary review) only where an error is costly — deliberately waking System 2 is a friction budget item.
- When auditing, ask "which heuristic is the user likely using here, and does our layout make that heuristic accurate or misleading?"

---

## 2. Cognitive Bias Codex (Benson) and growth.design's B.I.A.S. + Psych frameworks

**Definition.** Buster Benson's 2016 "Cognitive bias cheat sheet" grouped ~175 Wikipedia-listed biases by the *problem* each one helps the brain solve: (1) too much information, (2) not enough meaning, (3) need to act fast, (4) what should we remember. John Manoogian III drew it as the circular "Cognitive Bias Codex". growth.design's 106-principle cheatsheet inherits that four-way split (its Information / Meaning / Time / Memory sections map directly to problems 1–4). growth.design's B.I.A.S. framework rewrites the four problems as a designer's sequence — **Block** (what users filter out), **Interpret** (how they make meaning), **Act** (what lets them act quickly), **Store** (what they will remember). The Psych framework (Darius Contractor, Dropbox, published on Andrew Chen's blog 2017) models a funnel as a running 0–100 "Psych" energy score: each element either adds motivation (+Psych) or costs friction (−Psych); users abandon when Psych hits zero. The task brief's shorthand "Psych = Motivation × Ability / net value = motivation − friction" is a growth.design teaching paraphrase (unverified exact wording); Contractor's original is additive gains and losses on a single scale.

**Core model in words.** Four gates in a row: incoming stimuli → filter (Block) → sense-making (Interpret) → action under time pressure (Act) → encoding for later (Store). Each bias is a side effect of one gate. Psych overlays a fuel gauge on the user journey: every screen is a ledger line of +/− energy; the design goal is to front-load +Psych (value, social proof, imagery) before −Psych (forms, payment).

**Key sources.**
- Benson (2016), "Cognitive bias cheat sheet" — discussed at RealKM: https://realkm.com/2016/10/28/just-how-rational-is-our-thinking-time-for-a-reality-check/ and simplified version https://realkm.com/2017/04/07/simplified-cognitive-bias-cheat-sheet/ ; Codex poster coverage: https://dailynous.com/?p=14025
- B.I.A.S. explainer: https://blog.logrocket.com/ux-design/bias-framework ; growth.design product psychology course and reference: https://growth.design/psychology , https://growth.design/courses/product-psychology/lesson-sample
- Contractor (2017), "Psych'd: A new user psychology framework for increasing funnel conversion": https://andrewchen.com/psychd-funnel-conversion/

**Evidence grade.** Practitioner. The Codex is a taxonomy, not a tested theory — it organises biases of very different evidential strength under one roof. Psych is a heuristic scoring device; its numbers are subjective team estimates, not measurements.

**Principles explained / organised.**
- organises → *all 106* via the four sections (Information = Block, Meaning = Interpret, Time = Act, Memory = Store).
- organises (Psych) → Social Proof, Aha! Moment, Spark Effect, Goal Gradient Effect, Labor Illusion, Curiosity Gap (+Psych); Cognitive Load, Decision Fatigue, Cashless Effect's inverse (pain of paying), Reactance (−Psych).
- supports → Progressive Disclosure (spend Psych only once it has been earned), Default Bias (zero-cost Psych).
- tension → Nudge ethics (Psych optimisation can drift into sludge/dark patterns; see §12).

**How a designer uses it.**
- Run a B.I.A.S. pass on a screen: what gets *blocked* (banner blindness), how is it *interpreted* (mental model, framing), what makes *acting* easy (defaults, Fitts), what is *stored* (peak-end, picture superiority).
- Draw a Psych line across an onboarding flow; move the steepest −Psych steps after the first +Psych "aha".
- Use the four problems as a coverage checklist when picking principles for a design so suggestions aren't all from one bucket.
- Do not cite Codex membership as evidence — check each principle's own evidence grade.

---

## 3. Fogg Behavior Model + Tiny Habits; Hook model; operant conditioning

**Definition.** Fogg Behavior Model: **B = MAP** — a behaviour happens when Motivation, Ability and a Prompt converge at the same moment. Tiny Habits (Fogg 2019): anchor a very small behaviour to an existing routine ("After I…, I will…") and celebrate immediately to wire in the habit. Hook model (Nir Eyal, *Hooked*, 2014): Trigger (external → internal) → Action (simplest behaviour in anticipation of reward) → Variable Reward (tribe, hunt, self) → Investment (user stores value that loads the next trigger). Operant conditioning (Skinner; Ferster & Skinner 1957 *Schedules of Reinforcement*): behaviour is shaped by its consequences; reinforcement schedules (fixed/variable × ratio/interval) differ in response rate and resistance to extinction, with variable-ratio producing high, persistent responding.

**Core model in words.** Fogg: a 2-D plot, motivation (y) vs ability (x), with a convex "action line"; prompts above the line succeed, below it fail. Raising ability (making it easier) is usually more reliable than raising motivation. Hook: a four-step loop whose investment step makes the next trigger more likely and the next action easier — a flywheel. Skinner supplies the reward physics inside the loop and the method of *shaping* (reinforcing successive approximations).

**Key sources.**
- Fogg Behavior Model site: https://behaviormodel.org/ ; Fogg (2009) "A behavior model for persuasive design", Persuasive '09 (conference paper; unverified page numbers).
- Fogg (2019), *Tiny Habits* (book).
- Eyal (2014), *Hooked: How to Build Habit-Forming Products* — summary: https://getstream.io/blog/hook-model/
- Reinforcement schedules overview: https://www.simplypsychology.org/schedules-of-reinforcement.html ; Ferster & Skinner (1957) catalogue record: https://search.worldcat.org/oclc/4596140

**Evidence grade.** Strong for operant conditioning and schedule effects (decades of lab work, though translation from animals to app users is looser). Practitioner/Moderate for Fogg (widely used, few independent tests of the model as a whole). Practitioner for Hook (framework from case studies, not experiments).

**Principles explained / organised.**
- organises → External Trigger, Internal Trigger, Self-Initiated Triggers (Prompt / Trigger), Variable Reward, Investment Loops, Shaping
- mechanism-of → Variable Reward (variable-ratio schedule), Shaping (successive approximation), Goal Gradient Effect (reinforcement proximity), Zeigarnik Effect (open loops as internal prompts), Spark Effect (ability ↑ via small effort)
- supports → Aha! Moment (first reward), Fresh Start Effect (motivation waves as prompt timing), Default Bias (ability ↑), Cognitive Load / Hick's Law (ability ↓ when high), IKEA Effect & Endowment Effect (investment)
- tension → Reactance (over-prompting), Provide Exit Points (habit loops resist exits), Flow State / SDT autonomy (controlled vs autonomous motivation)

**How a designer uses it.**
- Debug a "they don't do X" problem by asking, in order: is there a prompt at the right moment? is it easy enough (time, money, effort, cognitive load, routine fit)? only then — is motivation high enough?
- Shrink the first action (Tiny Habits / Spark Effect), then shape upward with progressive goals.
- Put the investment step *after* the reward (e.g. saving a filter/view after the first useful report) so it loads the next trigger.
- Use variable reward for content discovery, never for core task completion or money; pair with explicit exit points (§12).

---

## 4. Prospect Theory

**Definition.** Kahneman & Tversky (1979): people evaluate outcomes as gains or losses relative to a *reference point*, not as final wealth; the value function is concave for gains, convex for losses and steeper for losses (loss aversion, often estimated around 2:1); small probabilities are overweighted. Related: framing effects (Tversky & Kahneman 1981) and the endowment effect (Thaler 1980; Kahneman, Knetsch & Thaler 1990) — owning an item shifts the reference point so giving it up is coded as a loss.

**Core model in words.** An S-shaped curve crossing the origin at the reference point: steep below (losses hurt), flatter above (gains please less). Move the reference point (anchor, default, trial ownership) and the same outcome flips between "gain" and "loss". Diminishing sensitivity on both sides means the first $10 off matters more than the next $10.

**Key sources.**
- Kahneman & Tversky (1979), "Prospect Theory: An Analysis of Decision under Risk", *Econometrica* 47(2):263–291 — https://www.econometricsociety.org/publications/econometrica/1979/03/01/prospect-theory-analysis-decision-under-risk
- Tversky & Kahneman (1974) for anchoring — https://pubmed.ncbi.nlm.nih.gov/17835457/
- Kahneman, Knetsch & Thaler (1990), *Journal of Political Economy*, endowment experiments (mugs) — (book/journal; unverified URL).

**Evidence grade.** Strong overall; reference dependence and framing replicate robustly. Loss aversion's *magnitude* is debated (some studies find smaller or context-dependent asymmetry for small stakes) — treat "losses loom about twice as large" as a rule of thumb, not a constant.

**Principles explained / organised.**
- mechanism-of → Loss Aversion, Endowment Effect, Framing, Sunk Cost Effect, Default Bias (status quo as reference point), Anchoring Bias (anchor sets reference), Decoy Effect (reference-dependent comparison), Weber's Law (diminishing sensitivity, psychophysical analogue), Pseudo-Set Framing (incomplete set coded as loss), Cashless Effect (payment decoupling reduces loss salience), Scarcity (potential loss)
- supports → IKEA Effect, Zeigarnik Effect, Negativity Bias, Hyperbolic Discounting (separate time-preference theory but often co-applied)
- tension → Reactance (loss-framed pressure can backfire), Noble Edge Effect (heavy loss-framing undermines warmth)

**How a designer uses it.**
- Decide the reference point explicitly: trials, pre-filled carts and "your plan" pages make the current state feel owned.
- Frame consequences of inaction in loss terms only where the loss is real (security alerts, expiring data), gains elsewhere.
- Bundle losses (one price) and separate gains (itemise benefits) — diminishing sensitivity.
- Measure: conversion and *post-purchase* refund/churn; a loss frame that lifts conversion but raises refunds is manipulation, not clarity.

---

## 5. Cialdini's 7 principles of influence

**Definition.** Robert Cialdini's *Influence* (1984) distilled field and lab research on compliance into six "weapons of influence": **Reciprocity, Commitment & Consistency, Social Proof, Liking, Authority, Scarcity**. *Pre-Suasion* (2016) added a seventh, **Unity** — shared identity ("we") rather than mere similarity.

**Core model in words.** Each principle is a socially learned shortcut that usually yields good decisions with little thought ("experts are usually right", "if many do it, it's probably fine", "return favours"). Influence works by presenting a cue that activates the shortcut; because the response is semi-automatic (System 1), the cue can be exploited when it is fake. Pre-suasion adds a timing layer: what you put in attention *before* the ask changes how the ask is processed (privileged moments).

**Key sources.**
- Cialdini (1984/2021), *Influence* (book).
- Unity as 7th principle: ASU W. P. Carey explainer https://blogs.wpcarey.asu.edu/20250422-gentle-science-persuasion-part-seven-unity ; CXL summary https://conversionxl.com/cialdini-unity/
- Cialdini interview on Pre-Suasion: https://www.leadinglearning.com/episode-74-pre-suasion-robert-cialdini/

**Evidence grade.** Strong-to-Moderate. Social proof norms (e.g. hotel towel / energy-use descriptive norms), reciprocity and commitment have substantial field evidence; magnitudes vary and some flagship field results (e.g. towel reuse) replicate more weakly than first reported. Unity is newer and less tested. Scarcity's commercial effect is real but heavily abused (fake scarcity is a named dark pattern).

**Principles explained / organised.**
- organises → Reciprocity, Commitment & Consistency, Social Proof, Authority Bias, Scarcity, Bandwagon Effect (social proof variant), Group Attractiveness Effect & Halo Effect (Liking), Noble Edge Effect & Singularity Effect (Unity/identification, affect)
- mechanism-of → Bandwagon Effect, Investment Loops (commitment), Sunk Cost Effect (consistency pressure)
- supports → Priming (pre-suasion), Storytelling Effect, Spotlight Effect & False Consensus Effect (beliefs about what others notice/do)
- tension → Reactance (perceived pressure), Streisand Effect (suppression attracts attention — scarcity of information), Backfire Effect, ethics (§12: fake social proof, fake scarcity, confirmshaming)

**How a designer uses it.**
- Place genuine, *specific* social proof (counts, named peers in the same industry) at points of uncertainty, not everywhere.
- Ask for a small, public, user-authored commitment early (choose a goal, name a project) to leverage consistency later.
- Give first (free template, useful export) before asking for sign-up — reciprocity — and measure whether the gift is used.
- Treat every scarcity or urgency claim as a factual statement that must be true and auditable.

---

## 6. Gestalt principles of perception

**Definition.** Gestalt psychology (Wertheimer, Köhler, Koffka, 1910s–1930s) holds that perception organises input into wholes according to grouping laws: **proximity** (near = together), **similarity** (alike = together), **closure** (complete incomplete figures), **common region** (shared boundary = together; formalised by Palmer 1992), **continuity/good continuation** (smooth paths), **figure-ground** (segregating object from background), and the overarching **Prägnanz** (perceive the simplest, most stable organisation).

**Core model in words.** Before attention or meaning, the visual system partitions the scene into groups and figures. These groupings compete and combine: common region and uniform connectedness tend to override proximity, proximity tends to beat similarity, but strength depends on degree. Layout therefore *is* information architecture at the pre-attentive level — the eye "reads" relationships before the mind reads labels.

**Key sources.**
- Wagemans et al. (2012), "A century of Gestalt psychology in visual perception: I. Perceptual grouping and figure-ground organization", *Psychological Bulletin* 138(6) — https://pubmed.ncbi.nlm.nih.gov/22845751/ ; open copy https://pmc.ncbi.nlm.nih.gov/articles/PMC3728284
- Laws of UX entries (Proximity, Similarity, Common Region, Prägnanz, Uniform Connectedness): https://lawsofux.com/

**Evidence grade.** Strong — grouping effects are robust in psychophysics; the *relative ranking* of principles is context-dependent (Moderate).

**Principles explained / organised.**
- organises → Law of Proximity, Law of Similarity, Law of Prägnanz
- mechanism-of → Visual Hierarchy (figure-ground + grouping), Juxtaposition, Contrast (figure-ground segregation), Von Restorff Effect (breaking similarity), Chunking (visual grouping creates chunks), Banner Blindness (ad-shaped regions grouped and filtered)
- supports → Visual Anchors, Centre-Stage Effect, Aesthetic-Usability Effect (good gestalt reads as orderly), Signifiers, Cognitive Load (good grouping lowers extraneous load)
- tension → Von Restorff Effect vs Law of Similarity (consistency vs distinctiveness), Skeuomorphism (ornament can break Prägnanz)

**How a designer uses it.**
- Use spacing before lines or boxes; add a common region only when proximity alone is ambiguous (dense dashboards, forms).
- Make "same function = same look" a design-system rule (similarity), then reserve one visual exception per view for the primary action (isolation).
- Squint/blur test: the groups you see blurred should match the information architecture.
- Check form labels sit closer to their own field than to the next one — the commonest proximity bug.

---

## 7. Norman's design principles

**Definition.** Don Norman (*The Design of Everyday Things*, 1988; revised 2013) frames usability as communication between designer and user through the device: **affordances** (relationships between object and agent that make actions possible), **signifiers** (perceivable cues that indicate where/how to act — added explicitly in 2013 because "affordance" was being misused), **mapping** (spatial/conceptual correspondence between controls and effects), **feedback** (communicating results), **constraints** (physical, cultural, semantic, logical limits that guide action), and the **conceptual model** (the user's mental model of how it works, built from the "system image"). The **gulf of execution** is the gap between intention and available actions; the **gulf of evaluation** is the gap between system state and the user's ability to perceive/interpret it (Norman's seven stages of action, mid-1980s).

**Core model in words.** Designer's model → system image (the UI, docs, behaviour) → user's mental model. The user crosses two gulfs on every interaction loop: goal → plan → specify → *perform* (execution) and *perceive* → interpret → compare with goal (evaluation). Signifiers, mapping and constraints bridge execution; feedback and visible state bridge evaluation.

**Key sources.**
- Norman (2013), *The Design of Everyday Things*, revised edition (book).
- Gulfs explainer: https://blog.logrocket.com/ux-design/ux-gulf-of-execution-and-evaluation
- Nielsen's heuristics restate several Norman ideas (visibility of status, match with real world): https://www.nngroup.com/articles/ten-usability-heuristics/

**Evidence grade.** Practitioner-to-Moderate: an explanatory framework grounded in cognitive psychology and decades of usability practice, not a single experimental theory; individual parts (feedback latency, stimulus-response compatibility for mapping) have strong lab support.

**Principles explained / organised.**
- organises → Signifiers, Feedforward (execution-side signifier of outcome), Feedback Loop, Mental Model, Discoverability, Provide Exit Points (recoverability from slips/mistakes)
- mechanism-of → Skeuomorphism (borrowing a known mental model), Familiarity Bias (existing models lower the gulf), Recognition Over Recall (knowledge in the world vs in the head)
- supports → Fitts's Law (mapping/placement), Progressive Disclosure (constraints), Tesler's Law (who absorbs complexity), Curse of Knowledge (designer's model ≠ user's)
- tension → Aesthetic-Usability Effect / minimalism (flat design can strip signifiers), Banner Blindness (signifiers styled like ads get ignored)

**How a designer uses it.**
- For each primary task, write out both gulfs: "How does the user know what to do?" and "How do they know it worked?" — any blank is a defect.
- Prefer constraints and good defaults over error messages (make the wrong action impossible, not just warned).
- Use feedforward (preview, labelled outcomes "Delete 12 records") on destructive or irreversible actions.
- In expert software (e.g. fleet ops), map control layout to physical/spatial layout of the domain (map, equipment, timeline).

---

## 8. Cognitive Load Theory and working memory limits

**Definition.** Cognitive Load Theory (Sweller 1988; later Sweller, van Merriënboer & Paas) states that learning and problem solving are constrained by a small working memory; load comes from **intrinsic** (complexity inherent to the material, driven by element interactivity), **extraneous** (caused by poor presentation) and **germane** (effort devoted to building schemas — in recent formulations folded into intrinsic load). Working memory capacity: Miller (1956) observed limits around 7±2 items in absolute judgement and immediate memory span; Cowan (2001) argued that, once chunking and rehearsal are controlled, the true focus-of-attention capacity is about **3–5 chunks (~4)**.

**Core model in words.** A narrow funnel (working memory, ~4 chunks, seconds without rehearsal) between a firehose of input and a vast long-term memory. Schemas in long-term memory let many elements count as one chunk, which is why experts tolerate denser UIs. Design can't remove intrinsic load (Tesler), can reduce extraneous load, and can help schema formation.

**Key sources.**
- Sweller (1988), "Cognitive load during problem solving: effects on learning", *Cognitive Science* 12(2):257–285 — https://dc2.philarchive.org/rec/SWECLD
- Miller (1956), *Psychological Review* 63(2):81–97 — https://pubmed.ncbi.nlm.nih.gov/8022966/ (PubMed reprint record)
- Cowan (2001), "The magical number 4 in short-term memory", *Behavioral and Brain Sciences* 24(1) — https://pubmed.ncbi.nlm.nih.gov/11515286/
- Laws of UX: Cognitive Load, Working Memory, Chunking, Miller's Law — https://lawsofux.com/

**Evidence grade.** Strong for working-memory limits and chunking; Strong-to-Moderate for CLT's instructional effects (split-attention, redundancy, worked-example effects replicate, but "germane load" is poorly measurable and the three-way split has been revised). Miller's 7±2 as a UI rule (e.g. "max 7 menu items") is a misuse — see §13.

**Principles explained / organised.**
- mechanism-of → Cognitive Load, Miller's Law, Chunking, Hick's Law (more alternatives → more processing), Recognition Over Recall, Progressive Disclosure, Decision Fatigue (claimed), Serial Position Effect (primacy = rehearsal into LTM; recency = still in WM), Zeigarnik Effect (open goals occupy WM), Method of Loci & Spacing Effect (LTM encoding strategies that bypass WM limits), Picture Superiority Effect (dual coding)
- organises → Tesler's Law (intrinsic load is conserved), Occam's Razor (cut extraneous elements), Pareto Principle (expose the vital few)
- supports → Banner Blindness & Selective Attention (filtering protects WM), Default Bias (defaults remove decisions), Flow State (balanced load)
- tension → Aesthetic-Usability Effect / Sensory Appeal (decoration can add extraneous load), Curiosity Gap (deliberately creates an open loop)

**How a designer uses it.**
- Separate intrinsic from extraneous load in reviews: "Is this hard because the task is hard, or because we made it hard?"
- Keep what users must hold in mind ≤ ~4 chunks across steps; carry context forward (summaries, persistent selections) instead of relying on recall.
- Co-locate related info (avoid split attention between chart and legend, form and help).
- For expert tools, allow density but support schema formation: consistent patterns, saved views, keyboard shortcuts.

---

## 9. Nielsen's 10 usability heuristics, Jakob's Law, Laws of UX

**Definition.** Nielsen's heuristics (Nielsen & Molich 1990; refined 1994) are ten broad rules for interface evaluation: visibility of system status; match between system and real world; user control and freedom; consistency and standards; error prevention; recognition rather than recall; flexibility and efficiency of use; aesthetic and minimalist design; help users recognise, diagnose and recover from errors; help and documentation. **Jakob's Law**: users spend most of their time on *other* sites/apps, so they expect yours to work the same way. **Laws of UX** (Jon Yablonski, lawsofux.com, book 2020) is a curated catalogue of ~30 psychology-derived principles (Hick, Fitts, Miller, Jakob, Tesler, Doherty threshold, Postel, Peak-End, Gestalt laws, Zeigarnik, Goal-Gradient, etc.).

**Core model in words.** Heuristics are an *evaluation lens*, not a causal theory: each maps to underlying mechanisms (status visibility → gulf of evaluation; recognition → working memory; consistency → mental models/Jakob). Laws of UX is a *lookup table* linking mechanisms to design rules. Together they are the practitioner's interface layer onto §§1, 6, 7, 8.

**Key sources.**
- Nielsen (1994/updated), "10 Usability Heuristics for User Interface Design" — https://www.nngroup.com/articles/ten-usability-heuristics/
- Laws of UX catalogue — https://lawsofux.com/ (Jakob's Law at https://lawsofux.com/jakobs-law/)
- NN/g heuristic evaluation video — https://www.nngroup.com/videos/heuristic-evaluation/

**Evidence grade.** Practitioner (heuristics were derived by factor-analysing usability problems; heuristic evaluation reliably finds many but not all problems and needs several evaluators). Individual Laws of UX entries range from Strong (Fitts, Hick in their original domains) to Practitioner (Pareto, Parkinson, Occam as design maxims).

**Principles explained / organised.**
- organises → Feedback Loop (#1), Mental Model & Skeuomorphism (#2), Provide Exit Points (#3), Familiarity Bias (#4, Jakob), Recognition Over Recall (#6), Aesthetic-Usability Effect & Occam's Razor (#8), Discoverability (#10), Hick's Law, Fitts's Law, Miller's Law, Tesler's Law, Pareto Principle, Parkinson's Law, Peak-End Rule, Serial Position Effect, Von Restorff Effect, Zeigarnik Effect, Goal Gradient Effect, Chunking, Law of Proximity / Similarity / Prägnanz, Selective Attention, Cognitive Load, Flow State
- supports → Signifiers, Feedforward, Progressive Disclosure
- tension → Delighters/novelty vs Jakob's Law (innovation vs convention); Expert flexibility (#7) vs minimalism (#8)

**How a designer uses it.**
- Run a 3–5 evaluator heuristic review before usability testing; tag each finding with the heuristic *and* the underlying principle node so fixes are reasoned, not cosmetic.
- Default to platform/industry conventions (Jakob); spend novelty budget only where it creates a measurable advantage.
- Use Laws of UX as the vocabulary for stakeholder communication ("this is a Hick's Law issue") — then back it with data.
- Pair every "minimalist" change with a discoverability check (task success on hidden features).

---

## 10. Kano model; Jobs-to-be-Done + forces of progress; Peak-end & experienced vs remembered self

**Definition.**
- **Kano model** (Noriaki Kano et al., 1984): features relate non-linearly to satisfaction. **Must-be** (basic) features cause dissatisfaction when absent but no delight when present; **one-dimensional** (performance) features scale linearly; **attractive** features (delighters) delight when present but aren't missed when absent; plus indifferent and reverse categories. Delighters decay into must-bes over time.
- **Jobs-to-be-Done** (Christensen et al.; Ulwick; Moesta & Spiek): customers "hire" a product to make progress in a circumstance. **Forces of progress** (Moesta & Spiek): Push of the situation + Pull of the new solution must exceed Anxiety of the new solution + Habit of the present for a switch to happen.
- **Peak-end rule / two selves** (Kahneman et al. 1993; Redelmeier & Kahneman 1996): retrospective evaluations of an episode are dominated by its most intense moment and its end, with duration largely neglected. Kahneman distinguishes the *experiencing self* (moment-to-moment) from the *remembering self* (the story that drives future choices).

**Core model in words.** Kano: a 2-axis chart (feature fulfilment × satisfaction) with three curves — a floor (must-be), a diagonal (performance), an exponential (delighter). JTBD: a tug-of-war — two forces pulling toward switching, two holding back. Peak-end: an episode is compressed into a snapshot (peak + end) that the remembering self consults when deciding whether to return.

**Key sources.**
- Kano model overview: https://en.wikipedia.org/wiki/Kano_model (original: Kano, Seraku, Takahashi & Tsuji 1984, *Hinshitsu* / JSQC journal, Japanese).
- Four forces: https://jobstobedone.org/the-four-forces/
- Peak-end rule overview and citations: https://en.wikipedia.org/wiki/Peak%E2%80%93end_rule (Kahneman, Fredrickson, Schreiber & Redelmeier 1993, *Psychological Science*, cold-water study; Redelmeier & Kahneman 1996, *Pain*, colonoscopy).

**Evidence grade.** Kano: Practitioner/Moderate (widely used survey method; classification reliability critiqued — see https://www.quirks.com/articles/why-the-kano-model-wears-no-clothes). JTBD: Practitioner (interview methodology; little controlled testing). Peak-end: Strong-to-Moderate (robust in pain/affect studies; weaker or modified for long or goal-directed experiences, and the end effect is more reliable than the peak effect in some data).

**Principles explained / organised.**
- organises (Kano) → Delighters, Aha! Moment (attractive), Feedback Loop / Provide Exit Points / Recognition Over Recall (must-be hygiene)
- organises (JTBD forces) → Push ← Negativity Bias / Empathy Gap research; Pull ← Social Proof, Storytelling Effect, Aha! Moment; Anxiety ← Loss Aversion, Authority Bias (reassurance), Labor Illusion; Habit ← Default Bias, Familiarity Bias, Sunk Cost Effect, Endowment Effect
- mechanism-of (peak-end) → Peak-End Rule, Serial Position Effect (recency), Delighters, Negativity Bias (negative peaks dominate), Chronoception (duration neglect)
- supports → Second-Order Effect (delighters become baseline), Survivorship Bias (switchers interviewed ≠ non-switchers)
- tension → Hyperbolic Discounting/experiencing self vs remembering self; Delighters vs Jakob's Law/Familiarity Bias

**How a designer uses it.**
- Run a Kano survey (functional/dysfunctional question pairs) to separate must-bes from delighters before roadmapping; never ship a delighter while a must-be is broken.
- In switch interviews, map each of the four forces; design onboarding to reduce *anxiety* (trial, import, reversibility) and *habit* (migration tools), not just amplify pull.
- Engineer the end of key flows (success state, summary, celebration) and soften the worst moment (errors, waits) — measure with post-task satisfaction, not only time-on-task.
- Re-run Kano periodically: yesterday's delighter is today's baseline.

---

## 11. Self-Determination Theory (SDT)

**Definition.** Ryan & Deci (2000) propose three basic psychological needs — **autonomy** (volition, being the origin of one's actions), **competence** (effectiveness, mastery) and **relatedness** (connection to others). Satisfying them supports autonomous (intrinsic or well-internalised) motivation and wellbeing; controlling contexts (pressure, contingent rewards, surveillance) can undermine intrinsic motivation and push toward controlled motivation.

**Core model in words.** A continuum from amotivation → external regulation → introjected → identified → integrated → intrinsic motivation. Context moves people along it by supporting or thwarting the three needs. Links: **Reactance** (Brehm 1966) is the acute response to a threatened freedom — the autonomy need under attack. **IKEA Effect** (Norton, Mochon & Ariely 2012) — labour that ends in successful completion raises valuation, plausibly via competence (effect vanishes if the build fails). **Flow** (Csikszentmihalyi) — the optimal-challenge zone where competence and task demands balance.

**Key sources.**
- Ryan & Deci (2000), "Self-determination theory and the facilitation of intrinsic motivation, social development, and well-being", *American Psychologist* 55(1):68–78 — SDT topic page https://selfdeterminationtheory.org/topics/application-basic-psychological-needs/
- Reactance & SDT link (Pavey & Sparks 2009, *Motivation and Emotion*): https://selfdeterminationtheory.org/SDT/documents/2009_PaveySparks_MOEM.pdf ; reactance overview https://www.thedecisionlab.com/reference-guide/psychology/reactance-theory
- Norton, Mochon & Ariely (2012), IKEA effect, *Journal of Consumer Psychology* 22(3) — https://dash.harvard.edu/handle/1/12136084

**Evidence grade.** Strong for SDT's core need-satisfaction findings across many domains (large literature, meta-analyses); Moderate for the reward-undermining effect (real but moderated by reward type and framing). IKEA effect: Moderate (original studies; some later replications show smaller effects). Reactance: Strong as a phenomenon.

**Principles explained / organised.**
- organises → Reactance (autonomy threat), IKEA Effect (competence + ownership), Flow State (competence/challenge balance), Aha! Moment (competence spike), Streisand Effect (reactance to suppression)
- mechanism-of → Commitment & Consistency (self-chosen commitments internalise better), Shaping & Goal Gradient Effect (competence feedback), Social Proof / Group Attractiveness Effect (relatedness), Investment Loops (autonomous investment sticks)
- supports → Provide Exit Points (autonomy), Progressive Disclosure (competence-appropriate challenge), Delighters (non-contingent surprises don't undermine intrinsic motivation)
- tension → Variable Reward & gamified points (controlling rewards can crowd out intrinsic motivation), Nudge/Default Bias when experienced as manipulation, Hawthorne/Observer effects (feeling watched = controlling)

**How a designer uses it.**
- Audit each engagement mechanic: does it support autonomy (choice, rationale, opt-out), competence (clear progress, achievable challenge) and relatedness (meaningful connection) — or does it pressure?
- Give rationale for requests ("we ask for X because…") — reduces reactance and supports internalisation.
- Let users build/configure something early (IKEA) but guarantee they can finish successfully; failed builds destroy the effect.
- Tune difficulty adaptively (Flow); use informational feedback ("you mapped 3 sites faster than last week") rather than controlling feedback.

---

## 12. Ethics: dark-pattern taxonomies, regulation, regret test, nudge vs sludge

**Definition.**
- **Brignull** coined "dark patterns" (2010); the site is now **deceptive.design**, listing 18 types (sneaking, forced action, hard to cancel, preselection, obstruction, hidden subscription, hidden costs, trick wording, visual interference, fake social proof, fake urgency, nagging, fake scarcity, disguised ads, confirmshaming, comparison prevention, addictive design, currency confusion).
- **Gray et al. (2018, CHI)** analysed 118 practitioner-flagged examples into five strategies: nagging, obstruction, sneaking, interface interference, forced action.
- **Mathur et al. (2019, CSCW)** crawled ~11K shopping sites (~53K product pages), found 1,818 dark-pattern instances of 15 types in 7 categories on 183 sites, and 22 third parties selling them as turnkey plugins.
- **Regulation**: the EU **Digital Services Act** (Regulation (EU) 2022/2065) Art. 25 bars online platforms from designing interfaces that deceive, manipulate or materially distort users' free and informed decisions (with examples such as giving more prominence to some choices, repeated nagging, and making cancellation harder than sign-up). The **FTC** staff report *Bringing Dark Patterns to Light* (Sept 2022) catalogues disguised ads, difficult cancellation, buried terms/drip pricing, and tricking users into sharing data, and signals enforcement.
- **Regret test** (attributed to Nir Eyal's "manipulation matrix"/ethics discussions and to practitioner ethics checklists — unverified single origin): would the user regret the action if they fully understood what the design was doing?
- **Nudge vs sludge** (Thaler & Sunstein 2008; Thaler 2018 "Nudge, not sludge", *Science*): a nudge changes the choice architecture to help people by their own lights while preserving freedom; sludge is friction that makes beneficial actions harder (e.g. unsubscribe by letter) or nudges for the designer's benefit.

**Core model in words.** Every principle in the network has a *helping* use and an *exploiting* use; the same mechanism (loss aversion, defaults, social proof, scarcity) becomes a dark pattern when the cue is false, the friction is asymmetric, or the outcome works against the user's own goals. Tests: transparency (would it still work if disclosed?), symmetry (is opting out as easy as opting in?), truthfulness (is the claim real?), regret (would users endorse it in hindsight?).

**Key sources.**
- https://www.deceptive.design/types
- Gray et al. (2018): https://www.deceptive.design/articles/the-dark-patterns-side-of-ux-design ; PSU record https://pure.psu.edu/en/publications/the-dark-patterns-side-of-ux-design/
- Mathur et al. (2019): https://arxiv.org/abs/1907.07032v2
- FTC (2022): https://www.ftc.gov/system/files/ftc_gov/pdf/P214800%20Dark%20Patterns%20Report%209.14.2022%20-%20FINAL.pdf
- DSA Art. 25 text: https://www.springlex.eu/en/packages/dsa/dsa-regulation/article-25/
- Thaler on sludge: https://www.chicagobooth.edu/research/rustandy/blog/2019/nudging-for-good

**Evidence grade.** Strong as descriptive taxonomies (large-scale measurement, legal adoption). Effectiveness of dark patterns on behaviour is also well evidenced (e.g. experimental studies of obstruction and preselection). The regret test is Practitioner.

**Principles explained / organised.**
- counteracts / constrains → Scarcity (fake scarcity), Social Proof (fake social proof), Default Bias & Nudge (preselection, sneaking), Loss Aversion & Framing (confirmshaming, trick wording), Variable Reward & Investment Loops (addictive design), Sunk Cost Effect & Endowment Effect (hard to cancel), Cashless Effect (currency confusion), Banner Blindness exploitation (disguised ads), Decoy Effect & Anchoring Bias (comparison prevention, drip pricing), Hyperbolic Discounting (deferred-cost subscriptions)
- supports → Provide Exit Points, Noble Edge Effect (ethical behaviour as brand signal), Feedback Loop (transparent status), Reactance (users punish detected manipulation), Second-Order Effect (long-term trust costs)
- tension → short-term conversion metrics vs Peak-End Rule / retention

**How a designer uses it.**
- Run every persuasive pattern through four questions: true? symmetric? disclosed-proof? regret-free? Log the answers in design review.
- Make cancellation/opt-out paths equal-click to sign-up paths; DSA Art. 25 and FTC guidance treat asymmetry as a red flag.
- Track counter-metrics alongside conversion: refunds, chargebacks, support tickets, unsubscribes, complaint rate.
- Use the deceptive.design type list as a QA checklist before launch, especially for pricing, checkout, consent and offboarding.

---

## 13. Replication-crisis caveats for UX psychology

**Definition.** Since ~2011, large preregistered replication efforts showed that several famous social-psychology effects were much smaller than published or not reliably present. For UX, the lesson is to grade principles by evidence and to prefer mechanisms with robust support (perception, memory, reference dependence) over flashy single-study effects.

**Core model in words.** Effect sizes in the original literature were inflated by small samples, flexible analysis and publication bias; preregistered multi-lab studies estimate the true effect. Many UX "laws" are also *transplanted* from narrow lab tasks to interfaces — a second source of overclaiming.

**Key cases & sources.**
- **Ego depletion / decision fatigue**: Hagger et al. (2016) 23-lab preregistered replication, N≈2,141, d≈0.04 with CI spanning zero — https://nature.berkeley.edu/garbelottoat/wp-content/uploads/hagger-chatzisarantis-2016.pdf . The "hungry judges" parole study (Danziger et al. 2011) is disputed on case-ordering and magnitude grounds — https://dlab.sauder.ubc.ca/sjdm/journal/16/16823/jdm16823.html
- **Behavioural priming**: Doyen et al. (2012, PLOS ONE) failed to replicate elderly-prime slow walking except when experimenters expected it — https://pmc.ncbi.nlm.nih.gov/articles/PMC3261136 . (Semantic/repetition priming in perception is robust — keep the distinction.)
- **Power posing**: Ranehill et al. (2015) found no hormonal/behavioural effects in a larger sample — https://www.zne.uzh.ch/dam/jcr:e5fc4c3c-d50e-4aa9-96ab-4389e426d20d/Psychological%20Science-2015-Ranehill-0956797614553946.pdf ; Simmons & Simonsohn (2017) p-curve — https://faculty.wharton.upenn.edu/wp-content/uploads/2017/05/Simmons-Simonsohn-2017.pdf . Relevance: a warning against "body/pose" style claims in UX copy.
- **Choice overload**: Scheibehenne, Greifeneder & Todd (2010) meta-analysis of 50 experiments/63 conditions (N=5,036) found mean effect ≈ zero with high heterogeneity — https://edoc-vmtest.ub.unibas.ch/48789/1/20130423160206_5176945e2bba6.pdf ; Chernev, Böckenholt & Goodman (2015) (99 observations, N=7,202) found a reliable effect *when* moderators are present: choice-set complexity, task difficulty, preference uncertainty, effort-minimising goals — https://www.kellogg.northwestern.edu/faculty/research/detail/2015/when-product-assortment-leads-to-choice-overload-a-conceptual
- **Miller's 7±2 misuse**: Miller's paper concerned absolute judgement and memory span, not menu length; Cowan (2001) revises capacity to ~4 chunks; visible menus rely on recognition, not working memory — https://pubmed.ncbi.nlm.nih.gov/11515286/
- **Backfire effect**: Wood & Porter (2019) across many issues and >10K subjects rarely observed backfire; corrections usually move beliefs toward accuracy — https://papers.ssrn.com/abstract=2819073
- **Dunning-Kruger**: debated as partly a statistical artifact (regression to the mean, better-than-average effect) — https://frontiersin.org/articles/10.3389/fpsyg.2022.840180/full
- **Hawthorne effect**: Levitt & List's reanalysis of the original illumination data found little evidence for the classic effect — https://www.nber.org/papers/w15016

**Evidence grade (of the caveats themselves).** Strong — these are large preregistered or meta-analytic results.

**Principles to treat cautiously (tag as Contested or Moderate in the skill).**
- Contested: Decision Fatigue (ego depletion mechanism), Priming (behavioural/social priming; keep perceptual priming), Backfire Effect, Hawthorne Effect, Dunning-Kruger Effect (shape and cause), Miller's Law (as a UI item-count rule).
- Moderate/context-dependent: Hick's Law beyond simple RT tasks, choice overload claims inside Hick's/Decision Fatigue, Loss Aversion magnitude, IKEA Effect magnitude, Peak-End Rule for long goal-directed episodes, Fresh Start Effect, Spotlight Effect magnitude, Scarcity (field effects mixed with confounds), Barnum-Forer Effect (robust in lab, limited UI evidence), Unit Bias, Singularity Effect (identifiable victim effect smaller in meta-analysis), Noble Edge Effect, Spark Effect, Labor Illusion (strong original studies, fewer replications), Pseudo-Set Framing, Centre-Stage Effect, Weber's Law (strong in psychophysics; weak as a pricing/feature-change rule).
- Practitioner-only (no direct experimental basis as stated): Pareto Principle, Parkinson's Law, Occam's Razor, Law of the Instrument, Second-Order Effect, Tesler's Law, Provide Exit Points, Delighters, Discoverability, Feedforward, Visual Anchors, Juxtaposition.

**How a designer uses it.**
- Present principles to stakeholders with their evidence grade; never use a Contested principle as the sole justification for a decision.
- Convert principle claims into A/B or usability hypotheses with a pre-stated metric and minimum effect; expect smaller lifts than case studies report.
- For choice architecture, check Chernev's moderators (complexity, difficulty, preference uncertainty, goal) instead of cutting options by rule.
- Replace "7±2" with "minimise what users must *remember*; visible options can be many if well grouped".

---


## Mechanism chains
1. **Limited working memory (~4 chunks)** → Cognitive Load → Hick's Law, Chunking, Miller's Law (as misnomer), Recognition Over Recall, Progressive Disclosure, Decision Fatigue (contested), Serial Position Effect (recency).
2. **Pre-attentive perceptual grouping** → Gestalt laws (Proximity, Similarity, Prägnanz) → Visual Hierarchy, Chunking (visual), Juxtaposition, Banner Blindness (ad-shaped regions grouped and filtered).
3. **Salience / bottom-up attention capture** → Selective Attention & Attentional Bias → Von Restorff Effect, Contrast, Visual Anchors, Centre-Stage Effect, Picture Superiority Effect, Sensory Appeal.
4. **Motor control (speed–accuracy trade-off)** → Fitts's Law → target sizing, edge/corner placement, thumb zones; interacts with Hick's Law in menu design.
5. **Reference-dependent valuation (prospect theory)** → Loss Aversion & diminishing sensitivity → Endowment Effect, Sunk Cost Effect, Framing, Anchoring Bias, Decoy Effect, Default Bias, Pseudo-Set Framing, Weber's Law (just-noticeable price/feature differences), Cashless Effect.
6. **Present bias / time preference** → Hyperbolic Discounting → Temptation Bundling, Planning Fallacy, Fresh Start Effect, Goal Gradient Effect, trial/subscription design.
7. **System 1 shortcut reliance (bounded rationality)** → Heuristics (availability, affect, representativeness) → Availability Heuristic, Affect Heuristic, Halo Effect, Aesthetic-Usability Effect, Authority Bias, Social Proof, Barnum-Forer Effect.
8. **Socially learned compliance rules** → Cialdini principles → Social Proof → Bandwagon Effect; Commitment & Consistency → Investment Loops → Sunk Cost Effect; Reciprocity → free-value-first onboarding.
9. **Operant reinforcement** → Prompt + Ability + Motivation (B=MAP) → Hook loop → External Trigger → Internal Trigger; Variable Reward; Shaping → Aha! Moment → Investment Loops → habit/retention.
10. **Goal tension / open loops** → Zeigarnik Effect & Goal Gradient Effect → progress bars, checklists, Curiosity Gap, endowed progress.
11. **Basic psychological needs (SDT)** → autonomy threatened → Reactance → Streisand Effect, Backfire Effect (contested); competence satisfied → IKEA Effect, Flow State, Aha! Moment; relatedness → Group Attractiveness Effect, Social Proof.
12. **Consistency drive / dissonance reduction** → Cognitive Dissonance → Confirmation Bias, Commitment & Consistency, Self-Serving Bias, post-purchase rationalisation (Sunk Cost Effect).
13. **Memory encoding & retrieval dynamics** → Serial Position Effect, Spacing Effect, Method of Loci, Picture Superiority Effect, Storytelling Effect → Peak-End Rule (remembering self) → Delighters, Negativity Bias, Availability Heuristic → return/recommend decisions.
14. **Mental models & conceptual mapping** → Familiarity Bias / Jakob's Law → Skeuomorphism, Signifiers, Feedforward, Feedback Loop → gulfs of execution/evaluation closed → Discoverability, error recovery (Provide Exit Points).
15. **Time perception** → Chronoception (duration judged by attention & uncertainty) → Labor Illusion, Parkinson's Law, Peak-End duration neglect → loading/waiting design.
16. **Egocentric projection (designer side)** → Curse of Knowledge & Empathy Gap & False Consensus Effect → Law of the Instrument, Planning Fallacy, Survivorship Bias, Survey Bias, Observer-Expectancy / Hawthorne Effects → biased research → Second-Order Effects shipped unnoticed.

## Tension pairs
- **Von Restorff Effect ↔ Law of Similarity** — consistency everywhere, distinctiveness for one primary action per view; if everything is highlighted, nothing is.
- **Progressive Disclosure ↔ Discoverability** — hide by *frequency of use*, not by importance; keep a visible signifier (overflow, "Advanced") and test findability of hidden items.
- **Aesthetic-Usability Effect ↔ Signifiers** — minimal styling must still show what is clickable; beauty may mask usability problems in tests, so measure task success, not just ratings.
- **Familiarity Bias / Jakob's Law ↔ Delighters** — be conventional in structure and navigation, novel in moments of value; innovate where it changes the outcome, not the chrome.
- **Default Bias / Nudge ↔ Reactance** — defaults should be what most users would pick if informed, visibly changeable, with a reason given; hidden or self-serving defaults trigger reactance and regulatory risk.
- **Scarcity ↔ Reactance** — use only real, verifiable limits; explicit pressure ("only 2 left — hurry!") on low-stakes items reads as manipulation.
- **Loss Aversion ↔ Noble Edge Effect** — loss framing for genuine risks (data loss, security); avoid confirmshaming, which costs warmth and brand trust.
- **Variable Reward ↔ Flow State / SDT autonomy** — unpredictability in discovery and content is fine; core workflows need predictable, informational feedback.
- **Investment Loops / Sunk Cost Effect ↔ Provide Exit Points** — make data export and cancellation as easy as onboarding; retention earned through value, not lock-in.
- **Hick's Law (fewer choices) ↔ Pareto Principle / expert flexibility** — reduce options for novices via defaults and grouping; give experts shortcuts and saved views rather than removing capability (Chernev's moderators decide).
- **Cognitive Load ↔ Tesler's Law** — remove extraneous load ruthlessly, but don't push irreducible complexity onto users by oversimplifying; the system should absorb it.
- **Curiosity Gap / Zeigarnik Effect ↔ Cognitive Load** — open loops motivate in moderation; too many unfinished items (badges, checklists) become stress and noise.
- **Labor Illusion ↔ Chronoception / Doherty-style speed** — show work only when a wait is unavoidable; never add artificial delay to fast operations beyond what aids trust.
- **Social Proof / Bandwagon Effect ↔ Singularity Effect** — aggregate numbers build legitimacy, a single identifiable story builds emotion; use one named case next to the count.
- **Peak-End Rule ↔ Negativity Bias / Hyperbolic Discounting** — protect the end of flows and eliminate negative peaks first; don't sacrifice the experiencing self (ongoing friction) for a memorable finale.

---

## 14. Empirical aesthetics
**Definition.** The experimental study of why people find some things beautiful, pleasing or interesting, using measurement rather than philosophical argument; it links low-level visual features, cognitive processing, emotion and context to aesthetic judgements.
**Core model in words.** Fechner (1876) began measuring preferences "from below" (e.g. rectangles). Berlyne (1971) proposed that liking tracks arousal potential (complexity, novelty) in an inverted U. Later work showed the U is unreliable and shifted to processing fluency: what is easy to perceive (symmetric, prototypical, high-contrast) feels good. Leder et al. (2004) staged aesthetic experience from perceptual analysis through implicit memory, classification and cognitive mastering to aesthetic judgement and emotion; Leder & Nadal (2014) added context and the "aesthetic episode". Chatterjee & Vartanian (2014) frame it as a triad of sensory-motor, emotion-valuation and meaning-knowledge systems. Redies (2015) separates universal, perception-based beauty from culture- and knowledge-based appreciation. Preferences such as curvature and symmetry are fairly general among lay viewers, while experts and different cultures often prefer more complexity, novelty or asymmetry.
**Key sources.**
- Leder, Belke, Oeberst & Augustin (2004), British Journal of Psychology 95(4) — https://doi.org/10.1348/0007126042369811
- Leder & Nadal (2014), British Journal of Psychology 105(4) — https://doi.org/10.1111/bjop.12084
- Reber, Schwarz & Winkielman (2004), Personality and Social Psychology Review 8(4) — https://doi.org/10.1207/s15327957pspr0804_3
- Chatterjee & Vartanian (2014), Trends in Cognitive Sciences 18(7) — https://doi.org/10.1016/j.tics.2014.03.003
- Redies (2015), Frontiers in Human Neuroscience 9 — https://doi.org/10.3389/fnhum.2015.00218
- Leder et al. (2019), "Symmetry is not a universal law of beauty", Empirical Studies of the Arts 37(1) — https://doi.org/10.1177/0276237418777941
**Evidence grade.** Moderate — individual effects (fluency, curvature, symmetry, prototypicality) are well replicated, but stimuli are often abstract or static, effect sizes are moderate, and many findings shrink with expertise, culture or longer viewing.
**Principles explained / organised.**
- organises → Processing Fluency; Prototypicality; MAYA Principle; Unity-in-Variety; Complexity–Arousal Curve; Fifty-Millisecond Impression; Visual Complexity Preference; Symmetry Preference; Curvature Preference; Visual Balance; Golden Ratio; Rule of Thirds; Colour–Emotion Associations; Fractal Fluency; Peak Shift Effect; Aesthetic Aha; Visual Style Connotation
- mechanism-of → Aesthetic-Usability Effect; Halo Effect; Familiarity Bias; Sensory Appeal; Affect Heuristic
- tension → Occam's Razor (variety and expert preference for complexity push against pure minimalism)
**How a designer uses it.**
- Use fluency levers (contrast, symmetry, prototypical layout) to make first impressions positive, then add controlled novelty and variety for interest.
- Treat popular "laws" (golden ratio, rule of thirds, inverted U) as hypotheses and check their evidence grade before citing them.
- Segment aesthetic tests by audience: lay users, experts and cultures differ, so averaged preference can mislead.
- Measure aesthetics alongside task performance, since appeal colours perceived usability but does not replace it.
