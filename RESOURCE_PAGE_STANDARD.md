# Centripetal resources — reference-page plan and emerging standard

Updated October 9, 2026. The combined Guides & Tools subsection is implemented. The cash-flow guide and Board Deck Builder are the first reference designs, ready for human review. Page templates, visual treatments, and interaction patterns remain provisional until that review and actual narrow-width verification. Live Framer is outside this work. Existing detail URLs remain unchanged.

## The distinction

A guide helps a reader understand and apply a framework to a decision. A tool accepts inputs or choices and produces a useful result: an outline, calculation, assessment, or prioritized review list. Checking items alone does not require a separate tool page.

These are resource formats, not competing topic hierarchies. A guide may contain a tool. The distinction should describe what a reader can do, not force two destinations for the same resource.

A Blog article continues to answer one narrower question and remains a separate top-level section, per the user’s direction. A service page describes the firm’s work, responsibilities, and possible outputs.

## Agreed library direction

Resources → Guides & Tools / LinkedIn Posts / Media. Blog stays separate.

Keep the Resources hub organized first by founder question, then by format. Consolidate the two parallel Guides and Tools collection destinations into one primary library for the eight current resources. The combined library is implemented at `guides/index.html`; `resources/tools.html` is an entry link to that library rather than a second catalog. Cards have clear format labels: Guide, Guide with checklist/worksheet, Assessment, or Builder. Start with simple labels; filtering is a later usability choice, not a prerequisite.

Retain existing resource detail URLs and one primary page per resource. Existing collection URLs can continue as useful entry paths to the combined library; plan eventual redirects separately. Do not change paths simply to make the format label match the folder name. No automatic SEO or citation advantage is claimed for combining menu labels.

## Consolidation map

| Resource | Primary role | Recommended treatment |
|---|---|---|
| Do I Need a Fractional CFO? | Guide | One staffing/work-ownership framework; absorb any useful CFO Fit Calculator prompts after review |
| Series A Diligence Readiness | Guide with checklist | Keep the evidence checklist within the guide; absorb Fundraise Readiness rather than publish a second checklist |
| Venture Debt Readiness | Guide with checklist | Keep the lender evidence review within the guide |
| Cash-Flow Mistakes & Forecast Review | Guide with worksheet | Keep the review list within the guide; it does not calculate runway |
| Treasury Hygiene | Guide | One controls/ownership framework, with a review aid if it serves that framework |
| First 90 Days After Your Raise | Guide | One operating-cadence framework |
| SaaS Finance Scorecard | Assessment | A tool-focused page with clear scoring explanation and supporting context; absorb the duplicate Finance Diagnostic concept |
| Board Deck Structure Builder | Builder | A tool-focused page producing a preparation outline, with supporting evidence guidance on the same page |
| Cash Runway Scenario Modeler (unpromoted) | Potential standalone tool | Separate only if validated calculation inputs, outputs, and interpretation add a distinct job beyond the cash worksheet |

A separate tool page is justified when readers can use it directly, its inputs change a meaningful output, and the output serves a distinct task. Separate pages may be appropriate for a future validated model or a substantial reusable builder. They should link to the related explanation rather than reproduce an entire guide. Preserve prototype sources until consolidation is actually reviewed and implemented.

## Two reference pages before reusable templates

Develop the cash-flow guide and Board Deck Builder as the two reference pages before freezing these variants. Both share Home-derived typography, colors, navigation, breadcrumbs, source/review conventions, and topic-aware next steps. Their composition can differ because their primary jobs differ. A guide with an embedded exercise uses the guide variant; it does not require a third template. The module sequences below are starting hypotheses to test on real pages, not mandatory blocks for every resource.

### Guide variant

1. Hero: decision-focused title, topic/format label, one-sentence purpose.
2. Opening answer: who it helps, what question it resolves, and what the reader will leave with.
3. Contents for longer pages.
4. Framework: a coherent sequence; evidence, interpretation, and decision connected in each section.
5. Worked example where it makes a trade-off clearer; label invented illustrations.
6. Optional embedded checklist or worksheet at the point where the reader can use it. Explain what selections mean and what they do not establish.
7. Interpretation and unresolved questions, without repeating the entire framework.
8. Related article/resource and relevant service or conversation.
9. Sources and content ownership/review information established by evidence. Do not invent personal authorship or publication dates.

### Tool variant

1. Hero and concise purpose: task, intended reader, actual output.
2. Working area early on the page: necessary inputs, visible labels, defaults, and result.
3. Result interpretation: assumptions, meaning, next action, and unresolved evidence. No unexplained scores or implied validation.
4. Supporting method/framework as readable text. Keep contextual prompts near the relevant input; avoid repeating them in full below.
5. A short worked example when useful.
6. Related guide/service and topic-aware conversation.
7. Sources and review status.

For both variants, substantive explanations and examples remain readable independently of the interactive result. Do not hide the important answer behind an email gate or rely on generated output alone to communicate the resource’s purpose. Saving, downloading, and presentation-file generation need separate product decisions; they are not implied by the label “builder.”

## Audit requirements applied to both reference pages

The [May technical audit](../../content/seo_audit/Centripetal_SEO_Audit_2026-05-19.md), [May action plan](../../content/seo_audit/Centripetal_SEO_Action_Plan_2026-05-19.md), [August SEO/AI surfaceability overview](../../content/seo_audit/Centripetal_SEO_AI_Surfaceability_GTM_Overview_2026-08-13.md), and [seomachine AEO/GEO patterns](../../tools/seomachine/.claude/skills/seo-audit/references/aeo-geo-patterns.md) are the basis. The earlier standard incorporated some of these requirements but did not make their application and verification sufficiently explicit. The table below is a work plan, not a statement that every requirement has already passed.

| Audit recommendation / finding | Guide reference: Cash-Flow Mistakes & Forecast Review | Tool reference: Board Deck Structure Builder | How we assess the result |
|---|---|---|---|
| One founder trigger, search intent, and decision prompt | Review whether collection, payment, and customer assumptions support the next cash commitment | Prepare a board meeting around management’s recommendation and its evidence; keep fundraising pitch/diligence distinct | Each page brief names one primary task and candidate query; queries are hypotheses, not verified search volume |
| A direct answer near the top | Concise answer describing how to trace dated assumptions to commitments, with deeper review below | Define the preparation outline, what it produces, and how it helps the next meeting before asking for inputs | The opening answers the page’s question without requiring scrolling through a form; factual qualifications stay with the answer |
| Descriptive headings and reusable answer structures | Sections answer specific forecast-review questions; evidence/decision links and a worked example | Short readable method, discussion prompts, and a visible default/example outline | One H1, descriptive H2/H3 hierarchy, coherent steps or tables where appropriate; no forced FAQ or universal word-count formula |
| Specific expertise and attributable evidence | Primary references support accounting mechanics; approved firm insight explains the operating judgment | Primary references support metric distinctions; owners, dependencies, and known versus unresolved evidence distinguish the preparation task | Review substantive claims, sources, examples, and firm attribution; retain concept review status until wording is reviewed; no invented Charles quote or client outcome |
| Intent-matched depth rather than generic volume | Make the dated receipt/commitment trade-off concrete; avoid an introductory finance textbook | Connect each selected focus to a different recommendation/evidence prompt; remove duplication between field help and long prose | A reader can explain what decision the resource helps them make and what remains unresolved |
| Contextual internal links and one primary next step | Related cash service, relevant operating/treasury guide, supporting article, and cash-topic conversation | Board-reporting service, cash/diligence frameworks when relevant, supporting article, and board-topic conversation | Descriptive working links; logical discovery and return paths; use relevant links rather than mechanically adding a quota |
| Unique metadata, canonical, heading and schema hygiene | Retain unique metadata, clean URL, and breadcrumb/firm identity; review Article attribution against actual editorial status | Unique metadata, clean URL, breadcrumb/firm identity, and truthful WebPage representation | Existing static checks plus page-specific review; structured data must describe the visible content and real attribution |
| Accessible text and image descriptions | Full framework and example readable on the page; meaningful visuals have explanatory text and alt treatment | The task, method, assumptions, and example remain readable outside the generated result | Inspect rendered text and structured data; meaningful alt text, decorative empty alt, labels and keyboard access |
| Performance and accessible experience | Deliberate reading rhythm, useful navigation, responsive evidence/example blocks | Minimal necessary inputs, legible result, accessible updates and deliberate mobile ordering | Actual narrow/wide viewport checks, keyboard checks, and a page-specific performance baseline; record failures rather than infer a pass |
| Measure outcomes | Reading/exercise use and movement to the relevant next step | Start, useful result, abandonment, and relevant next step | Define future events without collecting private financial input; concept usability checks precede any production search/citation measurement |

The reference implementation now gives the cash guide a direct opening answer, continuous reading layout, contents index, standalone timing example, and optional evidence worksheet. The builder places its working area before the longer method, keeps evidence review optional, and groups the six supporting areas into one framework section. Both preserve Home-derived typography and colors, sourced financial mechanics, honest concept review status, stable URLs, and fixed topic-aware contact paths. Article schema was removed from the guide while personal editorial attribution and publication approval remain unestablished.

Desktop checks at an actual 1280×720 viewport passed: no horizontal overflow; guide mixed/all-reviewed/reset states and radio-keyboard behavior; all five builder focuses, both request types, mixed/all-reviewed/reset states, native disclosure keyboard behavior, and preserved core outline. The browser viewport control accepted a 390×844 request but the rendered page remained 1280×720. This is a tooling limitation, not a mobile pass. Responsive CSS is implemented; actual narrow-width verification is outstanding before broad template migration. `tools/reference-pages-qa.json` records checks and limits. Static payload sizes are recorded as a delivery baseline, not a Lighthouse score or measured Web Vitals.
### Applying the audit with current evidence

Keep useful question-and-answer content where readers have actual questions. Do not treat FAQPage or HowTo markup as an automatic visibility improvement: Google no longer shows FAQ rich results (May 2026) or How-to rich results (September 2023). This updates the reports’ broad schema recommendations; it does not require removing useful FAQs or imply these schema types cease to exist. See [Google’s FAQ update](https://developers.google.com/search/updates#removing-faq-rich-result) and [How-to update](https://developers.google.com/search/blog/2023/08/howto-faq-changes).

Google’s AI-feature guidance calls for useful accessible content, discoverable links, and structured data that matches the visible page; it does not require a special AI schema. This is evidence about Google’s AI Search features, not proof of identical behavior across ChatGPT, Perplexity, Gemini, or Claude. Readability and answer structures from the local seomachine patterns are useful editorial techniques; their illustrative statistics, citation-uplift percentages, fixed answer lengths, and ranking timelines are not accepted as verified Centripetal evidence.

The GitHub concept remains noindex. Resource design can be assessed for usefulness and technical quality here, but search visibility and live AI citations require the separate production measurement stage. The preserved May audit remains our starting point; no full rerun is required for this reference-page work.

## Design and interaction guidance: one system, four layers

Layout, visual design, and interaction belong to the same resource design system. Give them separate, connected specifications so a spacing rule does not have to describe result behavior. Establish them through the reference pages.

### 1. Content and SEO/AI requirements — apply now

Use the audit mapping above as the shared baseline. Content correctness, task clarity, readable answers, appropriate attribution, and relevant next steps constrain every layout choice. A reusable template cannot certify an unreviewed claim.

### 2. Brand and layout foundations — refine on the reference pages

- Preserve the live Home’s Lora/Roboto typography and pine/stone/sage identity. Extend the existing language rather than introduce a second brand system.
- Use a shared outer alignment grid. Prose, evidence, and interaction areas may have different widths within it, but transitions must be deliberate.
- The current 1160px outer and 760px prose widths are starting values from the concept, not rules to impose before testing. Assess line length, heading wraps, readable examples, and actual mobile space on both reference pages.
- Define heading scale, paragraph spacing, section rhythm, evidence emphasis, source treatment, and CTA hierarchy from the examples. Reduce repetitive full-width sections and competing callouts where a simpler composition works.
- Use visual hierarchy to make answer, evidence, example, result, and next action distinguishable. Choose tables/diagrams only when they explain a decision more clearly; do not add visual blocks to satisfy a template.
- Resolve mobile order, overflow, table behavior, and navigation at actual narrow and wide viewports. Document demonstrated behavior rather than inferred responsive CSS.

The Board Builder alignment correction remains applied: narrow sections sit inside the same outer grid as the working area. That correction does not establish the final design for all other resource pages.

### 3. Components and interaction patterns — test now where useful

| Pattern | User need | States/behavior to establish | Accessibility and evidence |
|---|---|---|---|
| Guide contents and section navigation | Find a relevant answer without reading everything | Clear section labels; predictable anchor landing; no unnecessary sticky control | Keyboard links, visible focus, headings clear of fixed navigation |
| Evidence and worked example | See why an assumption affects a decision | Distinguish source evidence from illustrative material; expand detail only when helpful | Readable text/table relationships; meaningful captions and alt treatment |
| Optional review worksheet | Keep unresolved work visible | Not reviewed, follow-up, reviewed, reset, and explicit meaning of completion | Labeled controls; review state separate from certification; useful print behavior |
| Builder inputs and outline | Make a small set of choices and understand the resulting plan | Clear defaults; meaningful result changes; preserve review choices when focus changes; deliberate empty/completed/reset states | Native groups and labels, keyboard order, concise update announcement, visible path to result on mobile |
| Assumptions/help | Understand what an input or result means | Short help near the control; longer method available separately | Essential explanation available without hover or animation |
| Primary next step | Continue with the relevant support or related resource | One clear primary action, descriptive secondary links, return path | Fixed topic context only; selections/private inputs excluded from contact URL |

Core interactivity is relevant now because it determines whether a tool is useful. Establish it alongside content and visual hierarchy. Decorative motion, richer hover effects, advanced filtering, downloads, saved progress, and presentation-file exports follow once there is a clear reader need. Avoid automatically treating “more interactivity” as a design improvement.

### 4. Page composition — derive after reviewing the two pages

Use the finished guide and tool to document module order, optional modules, narrow/wide behavior, and component variants. A universal standard should describe what is shared and where each format differs. It should not turn the successful first page into a rigid duplicate across the library.

## Reference-page development sequence

1. **Page brief and gap review:** identify founder task, candidate query, answer, evidence, output, primary next step, and current gaps. Confirm the combined library direction already agreed.
2. **Guide reference:** refine Cash-Flow Mistakes & Forecast Review’s opening, narrative, evidence/example presentation, optional worksheet, and related paths. Develop the visible design within the Home-derived brand and check reading/mobile usability.
3. **Tool reference:** refine Board Deck Builder’s concise introduction, early working area, input/result hierarchy, supporting explanation, and meaningful interaction states. Check that different choices produce a genuinely useful outline. Develop and test the visual/interaction design before extracting a template.
4. **Batched human review:** compare the two complete pages, concentrating on usefulness, sophistication, brand fit, clarity, and any firm-specific uncertainty. Refine them in manageable portions.
5. **Extract the proven patterns:** document common foundations, two page compositions, component variants/states, and accessibility/performance evidence. Mark remaining uncertainties explicitly.
6. **Apply selectively:** consolidate the library navigation and migrate the other pages according to their jobs. Preserve URLs, review copy/evidence, and avoid forcing a worksheet into every guide or a score into every tool.
7. **Measure later in production:** assess resource engagement, conversion, search discovery, and AI citations after separately authorized live deployment. This remains GitHub-concept work.

## Completion criteria for the reference pages

Before broad migration, each reference should demonstrate: one clear task; a direct readable answer; trustworthy and appropriately attributed evidence; useful explanation/output; distinct hierarchy for reading and doing; coherent Home-derived visual design; a relevant next step; and actual mobile/desktop and keyboard validation. Record a performance baseline and any limitations. Human feedback can be batched after each manageable reference-page portion; no complete-library redesign is needed first.

Neither reference is declared finished or a validated reusable template by this document. The current eight resources remain in place; only the library consolidation direction is agreed at this stage.

## Basis and limits

The local SEO/AI surfaceability overview recommends a focused resource system organized around founder triggers and distinct jobs, while treating the Scorecard as a dedicated interactive experience. The recommendation above adapts that direction to the eight resources currently exposed in the concept; the combined library label is agreed, while the two page compositions and design patterns are editorial/UX hypotheses to develop on the reference pages.

[Google’s SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) supports logical organization, descriptive links, and avoiding duplicate destinations for the same content. [Google’s AI-feature guidance](https://developers.google.com/search/docs/appearance/ai-features) supports accessible text, useful content, and ordinary SEO practices. Neither establishes a benefit from a particular “Guides” versus “Tools” menu label. Citation and conversion outcomes remain unmeasured.

## Reference review batch

Review the cash guide and Board Deck Builder together for (1) clarity of the founder task and result, (2) usefulness and accuracy of the evidence/prompt wording, and (3) fit with the Home design language. The approved combined library is implemented independently of the provisional page templates. Remaining guide copy, calculator formulas, and personal attribution still need their own review; the reference design does not approve them.
