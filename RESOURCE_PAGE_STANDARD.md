# Centripetal resources — proposed page and library standard

For discussion, October 9, 2026. This is a recommendation, not an agreed navigation change. Live Framer is outside this work. Existing URLs remain unchanged.

## The distinction

A guide helps a reader understand and apply a framework to a decision. A tool accepts inputs or choices and produces a useful result: an outline, calculation, assessment, or prioritized review list. Checking items alone does not require a separate tool page.

These are resource formats, not competing topic hierarchies. A guide may contain a tool. The distinction should describe what a reader can do, not force two destinations for the same resource.

A Blog article continues to answer one narrower question and remains a separate top-level section, per the user’s direction. A service page describes the firm’s work, responsibilities, and possible outputs.

## Recommended library structure

Resources → Guides & Tools / LinkedIn Posts / Media. Blog stays separate.

Keep the Resources hub organized first by founder question, then by format. Replace the two parallel Guides and Tools collection destinations with one primary library for the eight current resources. Cards have clear format labels: Guide, Guide with checklist/worksheet, Assessment, or Builder. Start with simple labels; filtering is a later usability choice, not a prerequisite.

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

## One shared shell, two page variants

Both variants share Home-derived typography, colors, navigation, breadcrumbs, page grid, headings, source/review conventions, and topic-aware next steps. Their module order differs because their primary jobs differ. A guide with an embedded exercise uses the guide variant; it does not require a third template.

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

## Alignment and layout contract

- Use one outer content grid aligned with the hero and neighboring sections (currently max 1160px in the shared native shell).
- Keep prose readable at approximately 760px inside that grid, anchored to its left edge. Do not center a narrow section independently between wider sections.
- Interactive work can use the wider grid for inputs and results. Define a deliberate mobile sequence and a direct way to reach the result when it follows the inputs.
- Share spacing, headings, evidence blocks, source treatment, and next-step patterns. Preserve the Home-derived Lora/Roboto and pine/stone/sage system.
- Test visible alignment and input/result accessibility at actual narrow and wide viewports. A failed resize request is not a mobile pass.

The Board Builder alignment correction is applied independently of this proposal: its narrow sections now sit inside the same outer grid as its hero and working area. This does not change the Home page or other resource templates.

## Order of work

1. Settle the library label and the guide/tool distinction.
2. Confirm the consolidation map and which resources have a genuinely separate interactive job.
3. Establish the shared shell and two variants using one guide and one tool as examples.
4. Apply the approved patterns to the existing resource pages, keeping URLs and reviewing actual content as each page is migrated.
5. Resume tool-specific questions, copies, and outputs. Further visual treatments and new interactions follow the structure/content work.

The Board Builder is an implementation candidate for the tool variant. Its current mixture of long reading sections and repeated review prompts should be assessed against this standard before further feature work. No library navigation consolidation is implemented by this document.

## Basis and limits

The local SEO/AI surfaceability overview recommends a focused resource system organized around founder triggers and distinct jobs, while treating the Scorecard as a dedicated interactive experience. The recommendation above adapts that direction to the eight resources currently exposed in the concept; the combined library label and two variants are editorial/UX judgments for discussion.

[Google’s SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) supports logical organization, descriptive links, and avoiding duplicate destinations for the same content. [Google’s AI-feature guidance](https://developers.google.com/search/docs/appearance/ai-features) supports accessible text, useful content, and ordinary SEO practices. Neither establishes a benefit from a particular “Guides” versus “Tools” menu label. Citation and conversion outcomes remain unmeasured.
