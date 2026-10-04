# uxtools.co Design Tools Survey 2024 + State of Prototyping 2026

# Batch D — uxtools.co Design Tools Survey (2024 report) + State of Prototyping Spring 2026

## Batch overview
- Sources: the 2024 Design Tools Survey (n=2,220, Nov 2024–Jan 2025, 9 tool categories, segmented by "Shapes of Work") and the open-data State of Prototyping Spring 2026 (n=1,478, Mar–Apr 2026, CC BY 4.0).
- Theme 1, consolidation versus satisfaction: Figma dominates UI design (82.3%, 46:1 against Sketch), basic prototyping (71.4%), design systems (59.2%) and, through FigJam, whiteboarding (48.8%). Niche specialists still score higher on satisfaction (ProtoPie 4.55–4.88, Origami 4.75, Balsamiq 5.00, Sketchboard 4.50). On average specialists rate +0.37 higher than market leaders. Adoption is driven by ecosystem lock-in and defaults, and these surveys show little sign that it reflects how good each tool is.
- Theme 2, lock-in: 86.7% say switching tools is hard because of their design system, rising to 74.2% "difficult" at 1000+ employees. 86.8% of Figma UI users also prototype in Figma. These are textbook **Default Bias**, **Sunk Cost Effect**, **Investment Loops** and **Familiarity Bias** in designers' own tool choice.
- Theme 3, context drives choice: tool use varies by work shape (corporate, growth, startup, agency, independent, educator, student) and by IC versus leader. Leaders adopt AI and Miro more often. Agencies keep legacy tools for client compatibility. Students lag industry Figma use by 17–23 points.
- Theme 4, the research tooling gap: research tools are fragmented (no tool above 13%). Only 13.7% use recruiting tools and 23.6% use a repository. 82.3% of independents do research with no budget.
- Theme 5, the AI shift (2026): 5 of the top 10 weekly tools are AI. Claude is #2 (50.8%) and Claude Code #4 (38.4%). Vibe coding has split the field into thirds: 37.7% none, 43.8% use it for more than half their building. Design engineers sit at 80.9% and IC designers at 35%. The top blockers are time to learn (55.7%), too many tools (53%) and output quality (52.2%). Workflow satisfaction rises roughly linearly with vibe coding, from 5.93 to 7.39 out of 10.
- Strongest psychology links: **Default Bias**, **Sunk Cost Effect**, **Investment Loops**, **Familiarity Bias**, **Bandwagon Effect** and **Social Proof** (tool consolidation). **Decision Fatigue**, **Hick's Law** and **Cognitive Load** (too many AI tools). **Survivorship Bias** and **Survey Bias** (self-selected UX Tools audience). **Law of the Instrument** (one tool for everything). **Dunning-Kruger Effect** and **Affect Heuristic** (AI trust and role anxiety). **Loss Aversion** (researchers feel less secure).

---

## Introduction — About This Report
- URL: https://uxtools.co/survey/introduction/about-this-report
- Type: survey
- Date/author (if known): 2024 Design Tools Survey (data Nov 2024–Jan 2025), UX Tools
- Summary:
  - UX Tools has surveyed more than 22,000 designers since 2017. The 2024 edition had 2,220 respondents.
  - Headline framing: unprecedented consolidation, plus specialised tools emerging, plus organisational context shaping tool choice.
  - The report is free because sponsors (Maze, Framer, UserTesting, Dovetail, Mobbin) fund it. UX Tools says sponsors had no editorial influence.
  - Response volume varies by category, with interface design the largest and portfolio/research categories smaller.
- Actionable takeaways for a designer:
  - Several sponsors appear as category winners (Dovetail, Framer, Maze). Read those results with that in mind, even with the stated independence.
  - Use the category-level numbers as directional benchmarks when justifying tool choices to stakeholders.
- Psychology links:
  - Authority Bias — survey reports carry authority; check sample and sponsorship before citing them as fact.
  - Survey Bias — results depend on who is willing to answer, and the respondents here are a self-selected audience.
  - Halo Effect — sponsor brands sit next to independent data, which can lend them credibility.
- References & resources: Maze — https://maze.co/ ; Framer — https://framer.com ; UserTesting — https://www.usertesting.com/ ; Dovetail — https://dovetail.com/ ; Mobbin — https://mobbin.com/

## Introduction — Demographic Summary
- URL: https://uxtools.co/survey/introduction/demographic-summary
- Type: survey
- Summary:
  - Work shapes are fairly evenly split: corporate (~529, ~23.8%), agency 456, growth 449, startup 426, educators 184, students 184, uncategorised 12.
  - Roles: 1,162 ICs (52.3%), 698 leaders, 449 other.
  - Product Designer plus UI/UX Designer make up 60.8% of roles, a sign that job titles are converging.
  - Geography: US + Canada 29.3%, Europe ~20.8%. The top countries also include India, Germany, the UK, China, France, Brazil, South Korea and Spain.
- Actionable takeaways for a designer:
  - The sample is global and product-heavy, which makes it reasonably representative for a Canadian product designer's benchmarks.
  - Researchers and engineers are underrepresented, so weight research-tool numbers lightly.
- Psychology links:
  - Survivorship Bias — only people engaged with UX Tools are counted, and disengaged or non-English designers are missing.
  - False Consensus Effect — it is tempting to assume "everyone uses X" when the sample mirrors your own community.

## Introduction — Methodology
- URL: https://uxtools.co/survey/introduction/methodology
- Type: survey
- Summary:
  - 2,220 responses collected Nov 2024–Jan 2025 across 9 categories: UI design, basic prototyping, advanced prototyping, whiteboarding, design systems management, user testing, research recruiting, research repositories, portfolio building.
  - Recruited from UX Tools' own audience (1M+ social followers, 95K newsletter subscribers, 450K annual site visitors). No compensation.
  - Responses more than 80% incomplete or clearly low-effort were removed. Tool names were normalised with a dictionary, and only tools with ≥0.1% usage are shown.
  - Seven Shapes of Work segments by company size: corporate 1000+, growth 101–1000, startup 2–100, agency, independent/solo, educators/researchers, students.
- Actionable takeaways for a designer:
  - Reuse the "Shapes of Work" segmentation idea, context over job title, when running your own internal tool or onboarding surveys.
  - Copy the data-hygiene practice for your own surveys: exclude low-effort responses and normalise free-text answers.
- Psychology links:
  - Survey Bias — an uncompensated, audience-recruited sample skews toward enthusiasts.
  - Observer-Expectancy Effect — the publisher (a tools newsletter) has an incentive to find "tool trends".
  - Survivorship Bias — filtering out incomplete responses removes less-engaged voices.
- New concepts: Shapes of Work — segmenting designers by organisational context (size, client versus product, IC versus lead) instead of by title.

## Introduction — Shapes of Work
- URL: https://uxtools.co/survey/introduction/shapes-of-work
- Type: survey
- Summary:
  - Job titles no longer explain tool choice. Context does: company size, team structure, client versus product focus, and leadership responsibility.
  - Each shape is split into IC (hands-on) and Lead (direction).
  - Corporate means layered teams, legacy systems and strong process. Growth is scaling fast with evolving systems. Startups wear many hats and iterate fast. Agencies do project-based client work. Independents have high autonomy. Educators work in academic settings. Students are building portfolios.
- Actionable takeaways for a designer:
  - When building personas for internal tools (for example ops dashboards), segment by work context and decision authority, not by title.
  - Expect leaders and ICs in the same org to need different tools and messaging.
- Psychology links:
  - Mental Model — each shape has a different mental model of "what design work is", which shapes tool expectations.
  - Empathy Gap — leaders and ICs underestimate each other's constraints, as the AI and Miro gaps later show.
- New concepts: IC/Lead split — the axis between individual contributor and leader that consistently predicts adoption differences.

## Interface Design — Overview
- URL: https://uxtools.co/survey/interface-design/overview
- Type: survey
- Summary:
  - Top 10 UI tools: Figma, Sketch, Adobe XD, Illustrator, Framer, Proto.io, Photoshop, Penpot, Affinity Designer, UXPin.
  - Figma to Sketch is 46:1, which the report calls the most complete tool collapse in modern design history.
  - Figma's takeover came from multiplayer collaboration, cross-platform access (Sketch is Mac-only) and big ecosystem bets.
  - Adobe XD was sunset in 2023 and retired in 2024, but 1.4% still report using it.
- Actionable takeaways for a designer:
  - Collaboration and cross-platform reach beat feature depth. Weigh "who else can open it" heavily in tool decisions.
  - Plan exit paths for legacy files, because sunset tools linger.
- Psychology links:
  - Bandwagon Effect — once teams standardised on Figma, adoption cascaded.
  - Social Proof — multiplayer files make tool use visible and shared, which reinforces adoption.
  - Default Bias — the 1.4% still on XD after retirement show inertia.
  - Investment Loops — every shared file and collaborator raises the cost of leaving (network-effect lock-in; see New concepts).
- New concepts: Network effects — a product becomes more valuable as more collaborators use it, and this drove Figma's category collapse.

## Interface Design — Shapes of Work
- URL: https://uxtools.co/survey/interface-design/shapes-of-work
- Type: survey
- Summary:
  - Corporate ICs: Figma 93.1% (4.59/5), XD 1.7%, Sketch 1.4%. Corporate leaders: Figma 86.6%.
  - Startup ICs: Figma 77.5% (4.62), Framer appears (4.73). Figma to Sketch is 111:1 among startup ICs, the highest of any segment.
  - Agency leaders use legacy tools such as Sketch 2.5× more than their ICs, because clients require compatibility.
  - Solo in-house designers keep Sketch at 4.3%, the highest retention of any shape.
  - Educators: Figma 77.5%. Students: Figma 65.3%, plus Illustrator 5.6% and XD 4.2%. That is a 17-point gap against industry (82.3%).
- Actionable takeaways for a designer:
  - Expect new grads or juniors to need Figma ramp-up. Pair them up and share component libraries.
  - In client-facing work, match the client's toolchain. Compatibility outweighs preference.
- Psychology links:
  - Familiarity Bias — solo designers and agency leaders stick with what they know (Sketch).
  - Default Bias — corporate standardisation (93%) is often a mandate, not a personal choice.
  - Commitment & Consistency — client agreements lock agencies into legacy formats.

## Interface Design — Trends
- URL: https://uxtools.co/survey/interface-design/trends
- Type: survey
- Summary:
  - Top-rated: Figma 82.3% share at 4.57/5. Framer 0.6% at 4.50. Proto.io 0.4% at 4.43. Penpot 0.3% at 4.14. Balsamiq 0.04% at a perfect 5.00.
  - Corporate is the most standardised (93.1%) and education the most divergent (students 65.3%).
  - Niche tools beat the incumbent on satisfaction in specific use cases.
- Actionable takeaways for a designer:
  - Satisfaction ratings from tiny user bases (Balsamiq at 0.04%) are unreliable. Check n before citing.
  - Low-fi tools like Balsamiq still delight a niche. Low fidelity is a deliberate choice for early ideation.
- Psychology links:
  - Survivorship Bias — niche tools' remaining users self-selected because they love them, which inflates satisfaction.
  - Cognitive Dissonance — users who chose an unusual tool may rate it higher to justify that choice.
  - IKEA Effect — users invested in mastering a niche tool value it more.

## Prototyping — Basic Prototyping
- URL: https://uxtools.co/survey/prototyping/basic-prototyping
- Type: survey
- Summary:
  - Top tools: Figma, ProtoPie, Adobe XD, HTML/CSS/JS, Sketch, Framer, Balsamiq, Penpot, UXPin, Flinto, Proto.io.
  - 86.8% of Figma UI designers also prototype in Figma, which the report calls the strongest lock-in in the survey.
  - ProtoPie scores 4.77 against Figma's 4.21 for basic prototyping, a +0.56 gap.
  - Loyalty from UI tool to prototyping tool: Figma 86.8%, Sketch 57.5%, XD 100%.
- Actionable takeaways for a designer:
  - The default prototyping tool is the one you design in, not necessarily the best one. Evaluate deliberately when fidelity matters.
- Psychology links:
  - Default Bias — the prototyping tool is chosen by convenience, not fit.
  - Law of the Instrument — "everything is a Figma prototype" even when another tool fits better.
  - Investment Loops — existing files and components make staying put the cheapest option.

## Prototyping — Advanced Prototyping
- URL: https://uxtools.co/survey/prototyping/advanced-prototyping
- Type: survey
- Summary:
  - In 2024 "advanced" was self-reported. From 2025 it will be defined by multimodality, cross-device interaction, real-device testing, realistic behaviours or physical controls.
  - Top tools: Figma, ProtoPie, Swift/SwiftUI, Framer, Axure RP, Webflow, Proto.io, Origami Studio, UXPin, Flinto.
  - 20.2% of Figma users switch to another tool for advanced prototyping.
  - Satisfaction: specialised tools 4.54, code-based 4.51, Figma 4.08, a +0.46 gap.
- Actionable takeaways for a designer:
  - For hardware or hardware-control UIs needing realistic behaviour (sensors, physical controls), ProtoPie or native code beats Figma.
  - Use the 2025 definition as a checklist for when a prototype needs to "go advanced".
- Psychology links:
  - Law of the Instrument — the minority who break from Figma report higher satisfaction.
  - Aesthetic-Usability Effect — high-fidelity, realistic prototypes get more forgiving and realistic test feedback.
  - Mental Model — realistic behaviours test users' actual expectations of device interaction.
- New concepts: Advanced prototype criteria — multimodal, cross-device, on real device, realistic behaviour, physical controls.

## Prototyping — Shapes of Work
- URL: https://uxtools.co/survey/prototyping/shapes-of-work
- Type: survey
- Summary:
  - Figma's share of basic prototyping: corporate ICs 78.9%, growth ICs 81.2%, startup ICs 73.1%, agency ICs 77%, solo 81%, independents 68.7%, educators 61.4%, students 48.6%.
  - ProtoPie earns its top ratings from leaders: corporate leaders 4.88, startup leaders 4.86, agency leaders 4.83.
  - 16.2% of corporate leaders use ProtoPie for advanced prototyping, over 5× their basic rate. Growth leaders use it most (18.4%). Agency leaders: 15.5%, 4.2× their basic use.
  - 16.1% of startup leaders use Swift/SwiftUI, the highest native-code prototyping rate in the survey.
  - 10.8% of independents use HTML/CSS/JS for advanced prototyping.
  - Students lag the industry average on Figma prototyping by 22.8 points (48.6% against 71.4%).
- Actionable takeaways for a designer:
  - Leaders reach for specialised tools when they need to sell a vision. Use high-fidelity prototypes for stakeholder buy-in.
  - Code prototyping (SwiftUI, HTML) is a differentiator at startups and for freelancers.
- Psychology links:
  - Storytelling Effect — leaders use rich prototypes to tell a convincing product story.
  - Authority Bias — polished, realistic prototypes carry more weight in decision meetings.
  - Picture Superiority Effect — interactive, visual demos are remembered better than specs.

## Prototyping — Trends
- URL: https://uxtools.co/survey/prototyping/trends
- Type: survey
- Summary:
  - 17.7% of advanced prototypers use code-based tools (Swift/SwiftUI, HTML/CSS/JS, React, Flutter), so prototyping and development are converging.
  - Three patterns: a two-tool workflow (Figma plus a specialist), code convergence, and a satisfaction inversion where smaller specialist tools are rated higher.
- Actionable takeaways for a designer:
  - Budget learning time for one code-adjacent prototyping skill.
  - Normalise two-tool workflows instead of forcing one tool to do everything.
- Psychology links:
  - Law of the Instrument — the two-tool pattern pushes back against one-tool thinking.
  - Pareto Principle — Figma covers about 80% of prototyping needs, and specialists handle the remaining high-value 20%.

## Digital Whiteboarding — Overview
- URL: https://uxtools.co/survey/digital-whiteboarding/overview
- Type: survey
- Summary:
  - Top 10: FigJam, Miro, Mural, Whimsical, Lucidspark, Milanote, Sketchboard, Adobe XD, Illustrator, Canva.
  - FigJam holds 48.8% share. Launched in 2021, it used Figma's 82.3% base to take the category quickly. The report calls this "The FigJam Effect".
  - Sketchboard (4.50) and Milanote (4.44) outscore the leaders despite minimal share.
- Actionable takeaways for a designer:
  - Adjacent-product launches inside an existing ecosystem can win categories quickly. The same applies to extending an existing product platform.
- Psychology links:
  - Familiarity Bias — FigJam feels like Figma, so adopting it costs almost nothing.
  - Default Bias — it is already in the workspace and the default choice.
  - Halo Effect — Figma's reputation transferred to FigJam.
- New concepts: The FigJam Effect — capturing a new category by leveraging an existing ecosystem's installed base.

## Digital Whiteboarding — Shapes of Work
- URL: https://uxtools.co/survey/digital-whiteboarding/shapes-of-work
- Type: survey
- Summary:
  - Corporate ICs: FigJam 54.6% (4.40), Miro 21.4% (4.25), Mural 2%. Corporate leaders: FigJam 46.4%, Miro 27.9%.
  - Startups: FigJam about 55–56% (4.45), Miro about 13.6%, the lowest of any professional shape. Whimsical rates 4.35–4.40.
  - Growth companies prefer FigJam more strongly than corporates because they have fewer legacy constraints.
  - Agency leaders use Miro more than their ICs because clients use it.
  - Independents: FigJam 38.1%, Miro 24.5%. 37.4% use other tools, the most diverse group.
  - Educators are the only shape where Miro (38.6%) beats FigJam (31.8%).
- Actionable takeaways for a designer:
  - For cross-functional workshops with non-designers, Miro may lower friction. For design-team work, FigJam integrates better.
- Psychology links:
  - Familiarity Bias — Miro persists where cross-functional partners already know it.
  - Default Bias — legacy installs keep Miro alive in corporates and academia.
  - Social Proof — clients' tools set the agency's tool.

## Digital Whiteboarding — Trends
- URL: https://uxtools.co/survey/digital-whiteboarding/trends
- Type: survey
- Summary:
  - Leaders use Miro at 27.1% against 19.9% for ICs, driven by cross-functional collaboration needs.
  - Consolidation follows the UI-tool pattern: Figma ecosystem across UI (82.3%), basic prototyping (71.4%) and whiteboarding (48.8%).
  - Three patterns: ecosystem integration, a leader–IC divide, and higher satisfaction for niche tools.
- Actionable takeaways for a designer:
  - Pick the whiteboard by who attends: execs and product people versus designers.
- Psychology links:
  - Bandwagon Effect — ecosystem consolidation compounds.
  - Empathy Gap — leaders' and ICs' tools diverge because their jobs do.

## Design Systems — Overview
- URL: https://uxtools.co/survey/design-systems/overview
- Type: survey
- Summary:
  - Top tools: Figma, Storybook, Zeroheight, Adobe XD, Sketch, Supernova, Notion, Zeplin, Confluence, UXPin. Figma to Storybook is 25:1.
  - Satisfaction: Figma 59.2% share at 4.19. Zeroheight 1.6% at 4.06. Supernova 0.7% at 3.87. Storybook 2.4% at 3.69. Productboard 0.3% at 4.20.
  - Storybook users report 33% better developer collaboration.
  - 86.7% say design systems make switching tools difficult or very difficult. By company size: 74.2% at 1000+, 58.9% at 101–1000, 37.4% at 11–100, 21.5% at 1–10.
  - Handoff gap: 13.7 weeks on average from spec to implemented component. Designer satisfaction is 4.19 against developer 3.42, a 0.77 gap. 67% cite design–code sync as a significant challenge. 46.3% report significant inconsistencies between spec and code.
- Actionable takeaways for a designer:
  - For a design system, add a code-side documentation layer (Storybook or Zeroheight) to close the gap between Figma and code.
  - Track time from spec to component and the rate of inconsistencies as design-system health KPIs.
  - Measure developer satisfaction separately, because designers overrate their own system.
- Psychology links:
  - Sunk Cost Effect — accumulated libraries make migration feel wasteful even when a better tool exists.
  - Investment Loops — every component added deepens lock-in.
  - Endowment Effect — teams overvalue the systems they built.
  - IKEA Effect — designers rate their own system (4.19) higher than developers who consume it (3.42).
  - Empathy Gap — the satisfaction gap between designers and developers.
  - Loss Aversion — fear of losing system work blocks tool migration.
- New concepts: Switching costs / vendor lock-in — accumulated assets make change prohibitively expensive, and this grows with org size.

## Design Systems — Shapes of Work
- URL: https://uxtools.co/survey/design-systems/shapes-of-work
- Type: survey
- Summary:
  - Corporate ICs: Figma 62.6% (4.15), Zeroheight 2.9%, Storybook 2.6%. Leaders: Figma 61.5%, Storybook 3.9%, Zeroheight 3.4%.
  - 63.7% of corporate designers run systems across 5+ product lines.
  - 76.2% of growth designers built a system while already supporting multiple products.
  - Startups: Figma 48–53%, Notion and Storybook small. 42.7% have no formal system, just "a collection of reusable components".
  - 58.9% of agency designers maintain systems for 3+ clients at once.
  - Independents: 37.4% keep personal component libraries adapted per client. Solo in-house: Figma 63.6% (4.25).
  - Students' Figma design-system use (36.1%) trails industry (59.2%) by 23.1 points.
- Actionable takeaways for a designer:
  - In a multi-product org, plan for multi-brand tokens early, as with multi-product lines.
  - "Reusable component collection" is a legitimate first stage. Formalise it when the number of products grows.
- Psychology links:
  - Chunking — design systems chunk UI into reusable units, which cuts designer cognitive load.
  - Cognitive Load — scale (5+ products) multiplies governance load.
  - Law of Similarity — consistency across product lines is what the system protects.

## Design Systems — Trends
- URL: https://uxtools.co/survey/design-systems/trends
- Type: survey
- Summary:
  - Figma's dominance extends across categories: UI 82.3%, basic prototyping 71.4%, design systems 59.2%.
  - Three patterns: ecosystem lock-in, a development divide (Storybook and Zeroheight survive on handoff value), and a scale spectrum from enterprise governance to startup MVP libraries.
  - Prediction: by 2026, hybrid design–development tools will disrupt handoff. This is based on the 46.3% inconsistency rate and 37% higher satisfaction for integrated approaches.
- Actionable takeaways for a designer:
  - Invest in tokens and code-connected components (for example Figma Code Connect) now.
- Psychology links:
  - Second-Order Effect — consolidating on one ecosystem has knock-on effects on handoff quality and developer satisfaction.
  - Default Bias — the system becomes the default tool choice for the whole org.

## Portfolio Builders — Overview
- URL: https://uxtools.co/survey/portfolio-builders/overview
- Type: survey
- Summary:
  - Healthy diversity: no tool exceeds 13% share, and this category has the highest satisfaction in the survey (4.17/5).
  - Top 10: Framer, code (HTML/CSS/JS), Webflow, Adobe Portfolio, Squarespace, Wix, Notion, Semplice, UXFolio, Medium.
  - 44.7% of designers maintain a portfolio with a dedicated tool.
- Actionable takeaways for a designer:
  - Pick the portfolio tool for expressiveness, because nothing is locked in. Framer and code score best.
- Psychology links:
  - Default Bias — with no dominant default here, designers choose by fit, which may explain the higher satisfaction.
  - Spotlight Effect — portfolios are personal-brand displays where designers feel observed.

## Portfolio Builders — Shapes of Work
- URL: https://uxtools.co/survey/portfolio-builders/shapes-of-work
- Type: survey
- Summary:
  - Corporate has the lowest portfolio adoption (ICs 30.5%, leaders 37.4%). Framer leads with 13.7% (4.63).
  - Growth: 39.9% of ICs and 42.4% of leaders. Startups: 51.7% and 57.4%, with Framer about 16% (leaders 4.64).
  - Agencies: ICs 61.1%, leaders 66.7%.
  - Independents: 70.5%, with Framer 18.5% (4.65), code 15.2% (4.58), Webflow 10.8%. Solo in-house: 40.2%.
  - Students use Adobe Portfolio 2.8× more than average (12.5% against 4.4%).
- Actionable takeaways for a designer:
  - Portfolio upkeep tracks job insecurity. Keep it current even in a stable corporate role.
- Psychology links:
  - Loss Aversion — volatile contexts (startups, freelancers) drive more portfolio upkeep as insurance.
  - Hyperbolic Discounting — secure corporate designers defer portfolio work until they need it.
  - Default Bias — students default to Adobe Portfolio through Creative Cloud bundles.

## Portfolio Builders — Trends
- URL: https://uxtools.co/survey/portfolio-builders/trends
- Type: survey
- Summary:
  - Independents have the highest adoption (70.5%), and portfolio adoption tracks career volatility and business need.
  - Three patterns: tool diversity (no tool above 13%), correlation with work shape, and the highest satisfaction of any category (4.17).
- Actionable takeaways for a designer:
  - Treat the portfolio as a product. Framer and code give the most control and satisfaction.
- Psychology links:
  - Self-Serving Bias — designers curate portfolios to frame their own success.
  - Peak-End Rule — reviewers remember the strongest case study and the closing impression.

## User Research — User Testing Overview
- URL: https://uxtools.co/survey/user-research/user-testing-overview
- Type: survey
- Summary:
  - Top 10: Maze, Google Meet/Zoom, UserTesting, Figma prototypes with video calls, Dovetail, Lookback, Optimal Workshop, Userlytics, Marvel, Loop11.
  - The top 3 testing tools together hold 30.3% share, against Figma's 82.3% in UI design. The category is fragmented.
  - Reasons for fragmentation: different methods (moderated versus unmoderated), contexts (web, mobile, physical) and users (research teams versus hybrid ICs).
  - Satisfaction ranges from Marvel at 4.33 to Figma prototypes on calls at 3.43, a 0.72 spread.
- Actionable takeaways for a designer:
  - Plain video calls with a Figma prototype are common but the lowest-rated. Use a dedicated tool when testing at scale.
  - Testing physical or hardware UIs may need context-specific methods beyond web tools.
- Psychology links:
  - Hawthorne Effect — moderated sessions change participant behaviour, so method choice matters.
  - Observer-Expectancy Effect — the moderator's framing can bias results.
  - Default Bias — Zoom is used because it is already there, not because it fits.

## User Research — Research Recruiting Overview
- URL: https://uxtools.co/survey/user-research/research-recruiting-overview
- Type: survey
- Summary:
  - Top 10: UserTesting, Maze, User Interviews, SurveyMonkey, Respondent, TestingTime, Optimal Workshop, PlaybookUX, Userlytics, Ethnio.
  - Only 13.7% use dedicated recruiting tools, the lowest of any research category.
  - Optimal Workshop rates 4.67 against UserTesting's 3.65, a gap of 1.02 between the best-rated and the most popular.
  - Challenges: low adoption, panel quality (47.2% struggle to find qualified participants), and a cost–quality trade-off.
- Actionable takeaways for a designer:
  - For niche B2B audiences (public-safety or field operators), build your own participant panel rather than relying on generic panels.
- Psychology links:
  - Survivorship Bias — convenient participants are not representative users.
  - Survey Bias — unqualified panelists produce misleading data.
  - Bandwagon Effect — the most popular recruiting tool (UserTesting) is not the highest rated.

## User Research — Research Repository Overview
- URL: https://uxtools.co/survey/user-research/research-repository-overview
- Type: survey
- Summary:
  - Top 10: Dovetail, Notion, Confluence, SharePoint, Maze, Airtable, Miro, UserTesting, Productboard, Whimsical.
  - Only 23.6% use any repository tool, the biggest growth opportunity.
  - Satisfaction: Productboard 4.20 is the highest and SharePoint 3.05 the lowest, a gap of 1.15.
  - Three approaches: specialist (Dovetail, 9.0%, 3.99), general platform (Notion, 5.9%, 3.94), enterprise (SharePoint, 2.1%, 3.05).
- Actionable takeaways for a designer:
  - Even a Notion-based insight repository beats none. Insights that are not stored are forgotten and research gets repeated.
- Psychology links:
  - Availability Heuristic — without a repository, teams rely on whichever recent insight comes to mind.
  - Confirmation Bias — a searchable evidence base helps counter cherry-picking.
  - Recognition Over Recall — tagged repositories let teams recognise past findings instead of recalling them.

## User Research — Shapes of Work
- URL: https://uxtools.co/survey/user-research/shapes-of-work
- Type: survey
- Summary:
  - Corporate ICs test with Maze (14.3%, 4.17), Zoom (13.7%) and UserTesting (10.9%). Corporate leaders lead with UserTesting (16.2%). Leaders adopt UserTesting 48.6% more than ICs because they hold budget authority.
  - Corporate repositories: Dovetail is used by 14.3% of ICs and 18.4% of leaders. Confluence is around 7–8% at low satisfaction (about 3.4).
  - Growth ICs use Maze most (17.6%) of any segment.
  - Startup ICs use Zoom most (14.8%). Their repository of choice is Notion (7–9%).
  - Agencies use UserTesting 26% more than average.
  - 82.3% of independents do research with no dedicated budget.
  - Only 31.9% of educators teach research tools as a module, against 83.7% who teach design tools.
- Actionable takeaways for a designer:
  - Make the research-tool budget case to leaders, since they control adoption. Use ROI framing.
  - Without a budget, pair Zoom with a Notion repository as a minimum viable research stack.
- Psychology links:
  - Authority Bias — budget holders (leaders) decide the stack.
  - Default Bias — free and existing tools (Zoom, Notion) win when budget is absent.
  - Curse of Knowledge — education under-teaches research, so juniors start with gaps.

## User Research — Trends
- URL: https://uxtools.co/survey/user-research/trends
- Type: survey
- Summary:
  - Persistent fragmentation: no research tool exceeds 13% adoption.
  - Specialist tools (Optimal Workshop, Dovetail) beat popular ones on satisfaction.
  - Corporates adopt research tools at 2× the rate of independents.
  - Prediction: by 2027, research tools will consolidate toward UI-tool levels. Corporates will lead this, with 42.1% already using repositories.
- Actionable takeaways for a designer:
  - Pick research tools that integrate (testing, recruiting, repository) to reduce workflow friction.
- Psychology links:
  - Cognitive Load — fragmented, disconnected research systems add switching costs.
  - Second-Order Effect — consolidation will reshape which insights get surfaced.

## AI Adoption — Overview
- URL: https://uxtools.co/survey/ai-adoption/overview
- Type: survey
- Summary:
  - General AI use (ChatGPT, Notion AI) by shape: agency leaders 88.7%, agency ICs 81.1%. Startup 88.4% and 77.1%. Growth 85.6% and 77.2%. Corporate 78.2% and 74.9%. Average: leaders 85.2%, ICs 77.6%.
  - 75.2% of AI use inside design tools is for text (copy, documentation, content), not visuals.
  - Uses ranked: text/copy, documentation, content generation, design variations, layout help, research insights, mockups, editing, visual assets, component creation.
- Actionable takeaways for a designer:
  - The quick AI wins are UX writing, documentation and content, such as icon-section copy for a design system.
- Psychology links:
  - Labor Illusion — AI-generated docs can look effortful, so review quality rather than volume.
  - Cognitive Load — offloading text tasks frees attention for visual decisions.

## AI Adoption — Shapes of Work
- URL: https://uxtools.co/survey/ai-adoption/shapes-of-work
- Type: survey
- Summary:
  - Adoption within design tools: corporate ICs 16.7% (documentation 36.2%) and leaders 21.8%, the smallest gap (5.1 points). Corporate concerns are security and compliance for ICs and ROI for leaders.
  - Growth: leaders 27.1%, ICs 19.2% (a 7.9-point gap, top-down).
  - Startup: leaders 33.3%, ICs 22.9%, the largest gap (10.4 points). Mainly content and text generation.
  - Agency leaders adopt most (33.9%) because of client-facing pressure.
  - Solo in-house: 24.7%, higher than any IC group in a structured org.
  - Educators adopt least (12.5%) and students 19%, which leaves a gap with industry.
- Actionable takeaways for a designer:
  - In enterprise settings, lead AI proposals with security and compliance. To leaders, frame them as ROI.
- Psychology links:
  - Authority Bias — top-down mandates drive leaders' adoption ahead of ICs.
  - Reactance — ICs may resist AI mandates that come without enablement.
  - Loss Aversion — compliance fears slow corporate IC uptake.

## AI Adoption — Trends
- URL: https://uxtools.co/survey/ai-adoption/trends
- Type: survey
- Summary:
  - "AI tools" ranked as the #3 future interest for 2025 (8.5%), after Figma and Framer. Then ProtoPie, AR tools, Webflow, Spline, Penpot, Maze, Dovetail and ChatGPT.
  - Leaders' AI adoption averages 32.2% (another figure given is 29.0%) against 19.9% for ICs.
  - Leaders' vision outruns implementation. ICs are expected to put AI into practice without enablement.
  - Hypothesis (not data): by 2026 the gap may reverse as AI shifts to practical text workflows. The 2026 data supports this partly: managers vibe-code at 46.6%, IC designers at 35%.
  - Patterns: a leader–IC divide, text-first use, and higher adoption among client-facing designers.
- Actionable takeaways for a designer:
  - Push for enablement time and training, not just tool licences.
- Psychology links:
  - Planning Fallacy — leaders underestimate the effort ICs need to adopt AI.
  - Empathy Gap — a disconnect between leaders and ICs.
  - Bandwagon Effect — AI interest is driven partly by hype.

## Top Tool Stacks — Overview
- URL: https://uxtools.co/survey/top-tool-stacks/overview
- Type: survey
- Summary:
  - #1 tool per category by shape, counting only tools with ≥5% adoption.
  - Corporate: Figma UI 90.9%, Figma basic prototyping 77.9%, Figma advanced 36.3%, FigJam 52%, Maze testing 16.3%, UserTesting recruiting 8.7%, Dovetail repository 12.3%, Framer portfolio 11%.
  - Growth: Figma 86.4%, 75.3% and 39%. FigJam 50.1%. Figma design systems 62.4%. Maze testing 16% and recruiting 6%. Dovetail 10.2%. Framer 15.1%.
  - Startup and agency: Figma plus FigJam, Zoom/Meet for testing, Notion as repository, Framer for portfolios.
  - Independent/solo: Figma 86.4%, 81% and 40.2%. FigJam 46.7%. Design systems 63.6%. Zoom testing 15.8%. Dovetail 6%. Code portfolio 14.7%.
  - Educators: Figma, FigJam, Maze, User Interviews, Dovetail, Notion portfolio. Students: Figma 65.3%, 48.6% and 22.2%. FigJam 44.4%. Design systems 36.1%. Zoom 15.3%. Code portfolio 9.7%.
- Actionable takeaways for a designer:
  - A corporate or growth stack benchmark: Figma, FigJam, Maze, Dovetail, Framer. Use it to justify a mid-size company's tool stack.
- Psychology links:
  - Social Proof — peers' stacks validate tool choices.
  - Bandwagon Effect — one stack has converged across most shapes.
  - Default Bias — the stack is often inherited, not chosen.

## Design Tools Awards — Overview
- URL: https://uxtools.co/survey/design-tools-awards/overview
- Type: survey
- Summary:
  - These are the first annual awards (2024 survey). They are data-based, from 2,220 designers across 12 work profiles.
  - Specialised tools average +0.37 satisfaction over market leaders despite far smaller share.
  - Winners: Design Standard, Figma (82.3%). Satisfaction Leader, ProtoPie (corporate leaders 4.88). Ecosystem Champion, Figma + FigJam. Rising Star, Framer (18.5% of independents). Design Engineering, Storybook (33% better collaboration between design and development). Hidden Gem, Origami Studio (4.75 at 0.2% share). Research Excellence, Dovetail (9.0%). Career Catalyst, HTML/CSS/JS (15.2% of independents). Future of Design, Framer (#1 anticipated tool, 10%).
- Actionable takeaways for a designer:
  - Use the award list as a shortlist of specialists to evaluate beyond Figma.
- Psychology links:
  - Authority Bias — awards confer credibility. Note that two winners are sponsors (Framer, Dovetail).
  - Halo Effect — an "award-winning" label raises perceived quality.
  - Social Proof — data-driven awards act as aggregate peer endorsement.

## Award — Design Standard (Figma)
- URL: https://uxtools.co/survey/design-tools-awards/design-standard
- Type: survey
- Summary:
  - The benchmark UI tool: 82.3% share, 46:1 against the nearest competitor, 93.1% among corporate ICs. About 9 in 10 designers use it as their primary UI tool.
- Actionable takeaways for a designer:
  - Figma fluency is table stakes. Differentiate on other skills.
- Psychology links:
  - Default Bias — Figma is the industry default.
  - Bandwagon Effect — near-universal adoption self-reinforces.

## Award — Satisfaction Leader (ProtoPie)
- URL: https://uxtools.co/survey/design-tools-awards/satisfaction-leader
- Type: survey
- Summary:
  - ProtoPie: 4.55/5 overall, 11.1% share of advanced prototyping, 4.88 from corporate leaders, 18.4% adoption among growth leaders.
- Actionable takeaways for a designer:
  - Strong candidate for prototyping hardware, sensor or multi-device interactions, such as control-room UIs.
- Psychology links:
  - Delighters — high satisfaction comes from exceeding expectations on sophisticated interactions.
  - Flow State — tools that make complex interactions easy keep designers in flow.

## Award — Ecosystem Champion (Figma + FigJam)
- URL: https://uxtools.co/survey/design-tools-awards/ecosystem-champion
- Type: survey
- Summary:
  - Leads three markets: UI 82.3%, basic prototyping 71.4%, whiteboarding 48.8%. The report calls FigJam's takeover one of the fastest in its survey history.
- Actionable takeaways for a designer:
  - Integrated suites reduce context switching. Weigh that against niche quality.
- Psychology links:
  - Familiarity Bias — a shared UI language across products lowers adoption cost.
  - Investment Loops — cross-product assets deepen lock-in.

## Award — Rising Star (Framer)
- URL: https://uxtools.co/survey/design-tools-awards/rising-star
- Type: survey
- Summary:
  - Framer: 12.1% portfolio share, 10% want to try it in 2025, 4.57/5 satisfaction, 18.5% among independents.
- Actionable takeaways for a designer:
  - Framer is a strong option for a fast, expressive portfolio site.
- Psychology links:
  - Curiosity Gap — the highest "want to try" rate shows buzz-driven intent.
  - Bandwagon Effect — momentum among independents.

## Award — Design Engineering (Storybook)
- URL: https://uxtools.co/survey/design-tools-awards/design-engineering
- Type: survey
- Summary:
  - Storybook: 2.4% of the design-systems market, 23.9% adoption among corporate leaders, 34% among growth leaders. Teams report 33% better design–code sync.
- Actionable takeaways for a designer:
  - Propose Storybook alongside the Figma library to align with developers.
- Psychology links:
  - Feedback Loop — a live component catalogue gives designers and developers a shared feedback surface.
  - Mental Model — a shared source of truth aligns designers' and developers' models.

## Award — Hidden Gem (Origami Studio)
- URL: https://uxtools.co/survey/design-tools-awards/hidden-gem
- Type: survey
- Summary:
  - Origami Studio (Meta): 4.75/5 satisfaction at 0.2% share. #2 prototyping tool by satisfaction. High fidelity, niche, free.
- Actionable takeaways for a designer:
  - Worth evaluating for high-fidelity mobile interaction prototypes.
- Psychology links:
  - Survivorship Bias — a tiny, dedicated user base inflates ratings.
  - Von Restorff Effect — a niche standout is noticed for its difference.

## Award — Research Excellence (Dovetail)
- URL: https://uxtools.co/survey/design-tools-awards/research-excellence
- Type: survey
- Summary:
  - Dovetail: 9.0% repository share, 3.99/5, 18.4% adoption among corporate leaders. 42.1% of corporate leaders use some repository tool, building organisational memory.
- Actionable takeaways for a designer:
  - A repository turns one-off research (such as onboarding interviews) into reusable organisational memory.
- Psychology links:
  - Availability Heuristic — a repository counters reliance on recent or memorable anecdotes.
  - Spacing Effect — resurfacing insights over time keeps them alive in team memory.

## Award — Career Catalyst (HTML/CSS/JS)
- URL: https://uxtools.co/survey/design-tools-awards/career-catalyst
- Type: survey
- Summary:
  - Coding skills: 10.0% portfolio-tool share, 4.51/5, 15.2% among independents. Credited with giving designers creative control over implementation.
- Actionable takeaways for a designer:
  - Basic front-end skill increases career leverage. The 2026 data on design engineers (80.9% vibe-coding, 50% feel more valuable) reinforces this.
- Psychology links:
  - IKEA Effect — building your own site increases attachment and pride.
  - Dunning-Kruger Effect — partial coding knowledge can over- or under-estimate implementation effort, and more skill calibrates it.

## Award — Future of Design (Framer)
- URL: https://uxtools.co/survey/design-tools-awards/future-of-design
- Type: survey
- Summary:
  - Framer: 10.0% named it the #1 "tool to try" for 2025. 12.1% portfolio share, the largest in its category. 4.57/5, tied for the highest in the category. Praised for blending design and development into interactive output.
- Actionable takeaways for a designer:
  - Design-to-live-site tools are shortening the handoff. Prototype directly as the real artifact.
- Psychology links:
  - Curiosity Gap — anticipation-driven interest.
  - Aesthetic-Usability Effect — polished live output raises perceived quality.

## Conclusion — The Big Picture
- URL: https://uxtools.co/survey/conclusion/the-big-picture
- Type: survey
- Summary:
  - "Figma dominates, specialists thrive": 82.3% UI share, while ProtoPie (4.55) and other specialists lead satisfaction.
  - Work shape drives choice. Corporate prioritises ecosystem integration (93.1% Figma among corporate ICs). Independents favour flexibility. The page states 40.2% of independents maintain portfolios, but that figure is actually solo in-house; independents are 70.5%.
  - Education is about 17 points behind professional Figma adoption.
- Actionable takeaways for a designer:
  - Match tool strategy to organisational context rather than chasing popularity.
- Psychology links:
  - Bandwagon Effect — popularity does not mean best fit; specialists win on satisfaction.
  - Default Bias — corporate standardisation.

## Conclusion — Our Awards Reveal
- URL: https://uxtools.co/survey/conclusion/our-awards-reveal
- Type: survey
- Summary:
  - Excellence comes from delivering value in context, not just market dominance.
  - Three dynamics: ecosystem power (Figma + FigJam), specialised excellence (ProtoPie), future-focused innovation (Framer).
  - Ideation, collaboration and execution are converging.
- Actionable takeaways for a designer:
  - Assess tools on three axes: ecosystem fit, specialist depth and future trajectory.
- Psychology links:
  - Framing — the awards reframe "best" as context-dependent value rather than share.

## Conclusion — Tomorrow's Toolkit
- URL: https://uxtools.co/survey/conclusion/tomorrows-toolkit
- Type: survey
- Summary:
  - Future interest ranking: Figma, Framer, AI tools (8.5%, #3), ProtoPie, AR tools (#5), Webflow, Spline, Penpot, Maze, Dovetail, ChatGPT.
  - Four shifts: AI enters the workflow, the design–code gap narrows (46.3% see inconsistencies), spatial/AR design goes mainstream, research tools consolidate.
- Actionable takeaways for a designer:
  - Skills to invest in: AI workflows, tokens and code-connected systems, spatial or 3D (Spline), integrated research.
- Psychology links:
  - Bandwagon Effect — interest lists reflect hype cycles as much as need.
  - Hyperbolic Discounting — designers favour tools with immediate payoff over long-term systems work.

## Conclusion — Help Us Improve
- URL: https://uxtools.co/survey/conclusion/help-us-improve
- Type: survey
- Summary:
  - A feedback request: which insights were most valuable, what was missed, and what to explore next year. It also asks readers to share the report.
- Actionable takeaways for a designer:
  - A good template for a closing feedback prompt in your own research reports: three open questions plus a share ask.
- Psychology links:
  - Reciprocity — a free report followed by a request for feedback or a share.
  - Peak-End Rule — ending on an invitation shapes the final impression.

---

## State of Prototyping: Spring 2026
- URL: https://uxtools.co/survey/2026/state-of-prototyping
- Type: survey
- Date/author (if known): Spring 2026 (fielded Mar 14–Apr 6, 2026). Tommy Geoco and UX Tools. n=1,478 across 18 regions. Open data, CC BY 4.0.
- Summary:
  - Sample: startups 29.3%, independent 17.9%, enterprise 17.7%, mid-size 15.4%, agency 13.5%, students 6.2%. 61.4% are outside North America (Western Europe 16.2%, South Asia 8.1%).
  - Weekly tools: Figma 82.6%, Claude 50.8% (#2), ChatGPT 48.2%, Claude Code 38.4%, Figma Make 34.8%, FigJam 34%, Slack 32.7%, Gemini 32.3%, Meet 24.8%, Notion 24.5%. Five of the top 10 are AI, and an AI coding terminal outranks FigJam.
  - Vibe coding (AI-generated code the builder may not fully understand) as a share of building time: none 37.7%, occasionally 18.5%, about half 12.7%, most 17.5%, nearly all 13.6%. 43.8% use it for over half their building and 31.1% for most or all of it.
  - By role, share with 50%+ AI-generated code: design engineer 80.9%, lead/principal 56.8%, non-designer 50.9%, manager/director 46.6%, IC designer 35%, researcher 26.1% (n=23, directional only).
  - 59.1% built their own tool with AI in the last 6 months. 25.3% do so regularly, 30.5% want to, and only 10.4% have no plans.
  - Trust in AI output: first drafts heavily edited 34.2%, exploration only 29.2%, review before shipping 24.7%, ships with minor tweaks 8.1%, don't use AI output 2.4%, full trust 1.4%. About 32.8% trust it for production with review.
  - Blockers: time to learn 55.7%, too many tools 53%, output quality 52.2%, budget 34.2%, security 28.9%, engineering constraints 19.4%.
  - Change in 6 months: added AI 36.5%, AI now central 34.6% (startups 38.8% against enterprise 34.7%, only a 4.1-point gap; agencies 28.6%, students 21.7%), in flux 15.2%, mostly the same 9.9%, consolidated 3.8%.
  - Role outlook over 2 years ("more valuable" against "less secure"): design engineer 50% / 10.6%, lead 43.2% / 20%, manager 35.4% / 23.6%, IC designer 24.8% / 32.4%, researcher 17.4% / 39.1%.
  - Investment next 12 months (pick 3): AI coding 64%, agent workflows 46.3%, design systems and tokens 40.2%, canvas tools 21.3%, video/motion/3D 20.4%, simplifying the stack 17.5%, image generation 14.7%, no-code 13.7%, manual coding 9.5%.
  - Workflow satisfaction rises roughly linearly with vibe coding: 5.93 (none), 6.12, 6.83, 7.16, 7.39 (nearly all). Mean 6.49/10. The report notes this is correlation, not causation.
- Actionable takeaways for a designer:
  - Design systems and tokens are the "AI-proof" layer: 40.2% are investing there. Structured tokens make AI generation on-brand. This supports investing in design-system work.
  - For managers, the bottleneck is learning time, not more tools. Protect experimentation time and curate a small approved AI toolset.
  - Build small personal tools with AI (59% have). Low-risk builder practice closes the gap between IC designers and design engineers.
  - Treat AI output as a first draft with a review gate. Only 1.4% trust it unreviewed.
  - Cite this open dataset (CSV, API, MCP server) as evidence in internal AI-adoption proposals.
- Psychology links:
  - Decision Fatigue — "too many tools to evaluate" (53%) is a top blocker, and designers face choice overload themselves.
  - Hick's Law — more AI tool options slow adoption decisions, so curate a shortlist.
  - Bandwagon Effect — weekly AI use spreading fast across roles. Watch for hype-driven adoption.
  - Self-Serving Bias / Cognitive Dissonance — heavy adopters may rate their workflow satisfaction higher partly to justify their investment, a confound the report acknowledges.
  - Loss Aversion — researchers and IC designers feel less secure, which frames AI as a threat more than a gain.
  - IKEA Effect — the 59% building their own tools likely value those tools more than off-the-shelf ones.
- New concepts:
  - Vibe coding — building with AI-generated code you may not fully understand but that works.
  - Design engineer — a hybrid design-and-code role and the most AI-optimistic segment.
  - Agent workflows — chaining AI agents to perform multi-step design or build tasks.
  - Open data survey — publishing de-identified microdata (CC BY 4.0) with an API and MCP access for reanalysis.
- References & resources: Raw data download — https://survey.uxtools.co/download ; Open API — https://survey.uxtools.co/api ; MCP server for AI tools — https://survey.uxtools.co/agent ; Survey home / citation — https://survey.uxtools.co ; Tommy Geoco — https://linkedin.com/in/tommygeoco ; Sponsors/tools: Mobbin — https://mobbin.com/ ; Framer — https://framer.com/ ; MagicPath — https://magicpath.ai/ ; Dscout — https://dscout.com/ ; Magic Patterns — https://magicpatterns.com/ ; Dazl — https://dazl.dev/
