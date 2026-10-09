# Centripetal Advisors concept — audit foundations

The concept is published only at https://credyset.github.io/centripetal-advisors-site/. The live Framer project is unchanged.

## October 8, 2026 pass

This iteration applies the May SEO/AI surfaceability audit’s high-confidence recommendations while keeping the restored public Home design. It adds a founder-resource section before Why Centripetal, a curated resource hub, six focused service pages, and expanded Services explanations and visible FAQs. The original eight-category SaaS Finance Scorecard remains the lead interactive resource. Series A readiness adds 14 questions, 24 diligence items, a progress count, and reset. Four further guides cover CFO fit, venture debt, treasury, and the first 90 days after a raise.

The six promoted guides were reviewed for unsupported benchmarks, stale figures, legal assumptions, and claims that exceed the available evidence. Authorship is corporate; no expert review or endorsement is fabricated. Historical articles and five experimental tools remain available on disk but are not newly promoted from the Home, Services, or curated hub. Their full factual review remains outside this pass.

Page-specific titles/descriptions, concept canonicals, structured data, internal paths, image dimensions, meaningful alt text, and heading semantics are implemented. Home Vimeo players initialize only near their viewport; the production editor iframe is disabled. These are implementation changes, not measured ranking or AI-citation gains. Field performance, search-demand evidence, attribution, proof-figure reconciliation, and the completed AI-citation baseline remain future work.

## Preserved baseline and architecture

The published public output was captured on October 8, 2026, not exported from the editable Framer project. Home retains the original navigation, hero animation, statistics, complete co-pilot section and diagram, logo bands, About section, four-video testimonial carousel, Why Centripetal, Munger quote, form, and footer. Baseline commit: `fc6b82f`. The earlier redesigned proposal on `concept/home-and-seo-foundations` / draft PR #1 is not this Home.

`assets/baseline/runtime/`, its source manifest, and historical six-viewport geometry remain immutable. Current pages use a separate `assets/runtime-foundations/` copy. Seven modules differ: Home and core page heading semantics; primary navigation accessibility and a post-commit signal; deferred Vimeo setup; Contact heading variants; and disabled editor bootstrap. Fonts, public images, and Vimeo media still depend on their original public hosts.

`assets/home-baseline.v3.js` preserves preview metadata/routes/forms and places native additions after the copied renderer commits, avoiding hydration conflicts. Home and Services additions are static siblings outside the React root before enhancement, so they remain readable without JavaScript. The `.inc` snippets are authoring references; updating them alone does not rebuild page HTML. Native pages use `assets/foundations.js` and scoped styles; no tool selections are submitted or saved.

## Preview boundaries

All 40 HTML pages remain `noindex, follow` with concept canonicals. The sitemap inventories 18 promoted pages; it is not evidence of indexing. A future production migration must replace staging canonicals and intentionally remove noindex. Production Google/LinkedIn analytics and Framer events are absent. Preview contact forms stop before the copied form handler sends any request and show an inline explanation. External Calendly and LinkedIn links remain the original destinations.

## Verification

```sh
python3 tools/check_site.py
python3 tools/check_baseline.py
python3 tools/check_foundations.py
node --check assets/home-baseline.v3.js
node --check assets/foundations.js
```

Static validation covers 40 pages, 1,392 URLs, unique metadata, local anchors/assets, explicit image dimensions, JSON-LD, and staging noindex. Captured source includes hidden responsive variants; exposed Home H1 and overflow were separately checked at 390, 900, 1024, 1280, 1440, and 1920 pixels. Recorded measurements in `tools/foundations-layout-qa.json` show unchanged original section geometry before the added resource section, and the expected height shift afterward. Eight Scorecard boundary cases pass; partial completion does not show a final band. Browser checks also cover both mobile menus and Escape, Series A count/reset, Services ordering/FAQ, contact isolation, and deferred video/carousel loading.

For local review, serve this directory on port 8765. Do not rerun `capture_live_baseline.py` or `freeze_render_modules.py` in this working copy: the capture scripts intentionally overwrite core HTML and would remove the foundation changes. Refresh a public baseline in a separate checkout and compare it explicitly.

Retrospective: preserved source geometry before editing; used the existing Scorecard rather than inventing a scoring model; caught a checklist initialization selector and phone flex-order issue during final interaction checks. Performance and citation outcomes still require measurement on the eventual production implementation.

## October 9, 2026 reader refinement

Six curated guides and six service pages now include static, crawlable contents links. Heading targets accept keyboard focus and allow clearance for sticky navigation. Service sidebars identify their related service by name, and duplicate contact links were removed from the final CTA.

The Scorecard retains the original 8–40 total and four bands. On completing all categories, it lists the three lowest scores in stable category order, links to relevant existing resources, and shows all eight scores in a table. Equal scores are not independently ranked; the visible explanation makes the tie behavior explicit. Reset clears scores, commentary, progress, results, and priorities. Keyboard radio controls and completion announcements remain available. Phone choices are 60-pixel rows rather than cramped five-column labels.

Series A and venture-debt checklists now both have live counts and reset. Guides and service pages have print controls and print styles; disclosures open for printing and restore afterward. A browser print request opened a modal that paused embedded-browser automation; navigation canceled it. Browser-specific PDF pagination and real assistive-technology testing remain unverified. No downloadable PDF, tracking, submission, or persistent storage is added.

The native navigation conflict between 1001 and 1100 pixels is fixed. Dark-page eyebrow and role text use higher-contrast existing palette colors. Measured static color ratios: sage on white 6.77:1; stone on pine 9.51:1; light role text on pine 7.97:1. Focus outlines measure 4.07:1 against pine and 3.32:1 against white. This is a focused review, not a full WCAG conformance claim.

Native pages request one shared font stylesheet directly from the document, with preconnect hints; the redundant stylesheet import and overlapping font links were removed. This reduces duplicate declarations and the nested stylesheet request, without asserting a measured Core Web Vitals improvement. Captured Home typography, rendering modules, original sections, and layout are unchanged by this pass.

Verification: eight scoring boundaries, partial-result suppression, deterministic priority ties, complete reset, keyboard arrow/Space input, Escape menu dismissal, keyboard anchor focus, checklist count/reset, seven Scorecard widths from 320 to 1440 pixels, and representative guide/service layouts at 320 and 1024 pixels. Browser measurements are recorded in `tools/reader-paths-qa.json`; static validation checks all local anchors, metadata, and assets.

### Batched human review queue

- Confirm current proof figures and reconcile the preserved responsive network-count variants before a production migration.
- Review the financial wording and Scorecard category interpretations with the firm; no Charles review or approval is represented.
- Identify client evidence that can support more distinctive service explanations, with permitted wording and attribution.
- Use the audit supplement and Search Console/lead data to refine priorities; historical articles and experimental calculators still need their separate factual/model review.

Implementation references: [MDN printing documentation](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Printing) and the design plugin accessibility-review skill. The current concept remains noindex and the live Framer project is untouched.
