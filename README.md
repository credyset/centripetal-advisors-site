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

All 40 HTML pages remain `noindex, follow` with concept canonicals. The sitemap inventories 19 promoted pages; it is not evidence of indexing. A future production migration must replace staging canonicals and intentionally remove noindex. Production Google/LinkedIn analytics and Framer events are absent. Preview contact forms stop before the copied form handler sends any request and show an inline explanation. External Calendly and LinkedIn links remain the original destinations.

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

## October 9, 2026 trust and authorship refinement

This pass addresses May audit category 12 (entity trust and E-E-A-T) and strengthens category 8 (internal linking). The dedicated About page now follows the public Home founder story, founding year, role, and co-pilot positioning. It replaces the historical draft's unconfirmed pricing comparisons and conflicting 2–4 versus 3:1 client-load claims. It uses the original public Charles portrait, explains operating principles, and links to the reviewed services, Scorecard, Series A resource, and preserved Home testimonials. It is included in the concept sitemap, now 19 pages. No original Home section, captured module, or navigation geometry changed.

AboutPage, Organization, and Person data connect the visible Charles Solomon profile to the firm. No education, career history, review endorsement, new performance claim, or rating is invented. All six promoted guides show a linked corporate byline and a visible concept update date near their opening; Article author URLs and dates match that visible attribution. All promoted native page footers reach About, and service sidebars now point there. A double-escaped ampersand in the board-reporting link label was also corrected.

Source scope: the [current public Home](https://centripetaladvisors.com/) About Us and co-pilot copy, the May audit's trust-asset recommendations, and the existing Centripetal context. Expanded Charles credentials, Alex's public bio, and detailed named case studies remain in the batched review queue. The new page's operating-principle copy is concept wording for firm review. Public numeric proof stays on the preserved Home pending reconciliation. This closes part of the trust gap; it is not a claim that the entire audit or E-E-A-T assessment is complete.

Verification: all 40 pages and 1,483 URLs pass static checks; original baseline and module checks pass. Browser checks cover About at 320, 390, 768, 1024, and 1440 pixels; all six guide bylines at 320 and 1024; and the author-to-About path. Founder anchor focus, image loading, and structured identity/author/date relationships were checked. Recorded checks are in `tools/trust-authorship-qa.json`. The concept remains noindex; search performance and AI-citation impact have not been measured.

## October 9, 2026 service specificity and conversation paths

This pass addresses May audit category 4 (Services specificity), category 8 (internal linking), and category 11 (topic-aware conversion paths). Each of the six native service pages now explains a distinct trigger, four areas of work, three possible working outputs, a clearly illustrative decision, a tailored beginning sequence, and four FAQs. The Services overview connects those areas within the embedded finance role and acknowledges the wider accounting, capital-process, RevOps, tax coordination, and back-office scope. Outputs and cadence are agreed around the engagement; no fees, fixed timelines, results, lender eligibility, or fabricated client proof are promised. The preserved Home sections remain intact.

All six services and six curated guides lead to Contact with fixed topic and source slugs. Contact offers a topic selector, three relevant prompts, an optional Add prompts button, and a return link to the source. The Scorecard link carries no scores. Names, email addresses, and messages stay in page memory only, survive topic and responsive-layout changes, and are never put in URLs or persistent storage by the new feature. Preview message displays an explicit no-send notice. The current Contact renderer's production form action props were removed; the capture guard remains in place. These are concept flows, not a production lead-capture deployment.

The copied Contact heading variants now match static HTML and the client renderer: one exposed H1 at phone/tablet widths and a form H2 beneath the desktop Contact H1. The contextual panel is inserted only after the renderer commits. Core preview canonicals discard topic, source, revision, and hash parameters. Frozen source modules remain untouched.

Authoring: `tools/service-content.json` and `tools/refine_services.py` rebuild services, the overview, and guide conclusion CTAs. `assets/conversation-context.inc` is the panel reference, embedded in Contact HTML; `assets/conversation.js` controls the context and transient draft. The service builder is idempotent.

Verification: all six service pages at 320 and 1024 pixels; all six guide CTAs; twelve topic/source destinations; Contact at 320, 390, 768, 900, 1024, 1280, and 1440 pixels. Checks cover one exposed H1, one context panel/form anchor, no horizontal overflow, correct return destinations, clean canonicals, safe unknown-parameter fallback, prompt deduplication, draft preservation, cleared-draft preservation, and the no-send notice. Latest Contact renderer/enhancement logs show no warnings or errors. Recorded browser checks: `tools/service-conversation-qa.json`. Static checks cover 40 pages, 1,494 URLs, and 19 sitemap entries; original baseline integrity and current runtime imports pass. Historical Home geometry and Scorecard checks remain historical evidence.

Batched firm review: confirm whether any service areas are offered as standalone projects; refine the responsibilities Centripetal owns directly versus coordinates with specialists; confirm whether the proposed working outputs reflect actual engagements; provide approved client evidence where available. Search, conversion, field-performance, and AI-citation gains have not been measured. The GitHub concept remains noindex, and the live Framer site is untouched.

Contact follow-up verification: a published screenshot exposed fixed captured frame heights that clipped the expanded context panel and fields. Context-bearing form ancestors now size to their content, scoped exclusively to Contact. Expanded prompts and the Preview button remain within every clipping ancestor at all seven Contact widths, with no horizontal overflow. The additional containment measurements are included in `tools/service-conversation-qa.json`.

## October 9, 2026 cash-flow guide — first guide batch

Adapted the existing Cash Flow Mistakes concept into a native, crawlable guide using the concept's shared Lora/Roboto typography, pine/stone/sage palette, navigation, section rhythm, byline, contents, disclosures, and print support. The source originals remain unchanged: `Centripetal/content/guides/guide_01_cash_flow_mistakes/src/guide_v1.md`, its Charles-review package copy, the older web edition, and `Centripetal/website-v3-local/guides/saas-cash-flow-mistakes.html`. No Charles review or approval is represented.

The May audit's content depth, internal linking, answer extraction, and topic-specific conversion recommendations guide this batch. The audit overview left Cash Flow Mistakes' sophistication angle pending. This edition focuses on second-order forecast dependencies: invoice approval and acceptance timing, weekly receipt concentration versus ARR concentration, dated commitments versus monthly averages, and assumptions tied to decision owners. Each section identifies evidence to bring and a decision to revisit. These are editorial priorities, not verified keyword-volume or conversion findings.

Older unsupported valuation-loss percentages, universal customer-concentration cutoffs, absolute forecast claims, and categorical revenue-recognition examples were excluded. SEC, Xero, and QuickBooks primary references support the cash/accounting mechanics. A qualitative hiring/invoice example is expressly illustrative and contains no claimed client outcomes. Company-specific recognition policy and forecast assumptions require the firm's review.

The worksheet is a transient review list with five areas, native radio controls, live counts, follow-up-first ordering, links back to the evidence, and reset. It does not calculate runway or assign a readiness rating. It requests no financial inputs, stores no selections, and sends no worksheet selections to Contact. The new source slug selects the existing cash-and-runway conversation path and returns to this guide. Resources, the cash-flow service, Treasury Hygiene, and First 90 Days link to the new guide; it is in the concept sitemap.

Verification: all 41 pages, local links, metadata, structured data, sitemap entries, baseline integrity, current module imports, and changed-script syntax are checked. Browser checks at the confirmed 1280×720 viewport cover default/mixed/complete/reset states, keyboard arrow/Space input, anchor focus, disclosure, contact context, return destination, and no-send preview. `tools/cash-guide-qa.json` records the results. The viewport override did not take effect; attempted phone/tablet sizes all remained 1280×720 and are explicitly excluded from responsive evidence. New-guide phone/tablet visual checks, printed pagination, full accessibility evaluation, and measured search/citation effects remain outstanding. Original Home sections and frozen capture modules remain unchanged.

Batched firm feedback: review the guide's decision framing and proposed evidence; identify actual recurring collection/forecast situations we can describe with approved attribution. The next manageable guide/tool candidate is the existing Board Deck Structure Builder, after this guide's responsive visual review. The concept remains noindex; no live Framer edits were made.

## October 9, 2026 architecture and resource hierarchy — first portion

`SITE_ARCHITECTURE.md` records the agreed hierarchy, page jobs, topic relationships, routing rules, overlap, and next portions. `tools/content-architecture.csv` inventories 45 HTML pages. Blog stays a separate section per the user's instruction; no menu-position citation advantage is claimed. The captured Blogs page and legacy article index need a separate catalog repair before promoting 15 older article drafts. Five old tool prototypes remain unpromoted pending their own review.

Resources now has a dedicated hub at `resources/index.html`, with six founder topics and four formats. `guides/index.html` is the seven-guide collection. Tools & Assessments links to four existing interactive experiences, with no duplicate exercise URLs. LinkedIn Posts contains three selected public posts, summarized as summaries and linked to originals; it is a curated feed, not automatic synchronization. Media contains two episode listings featuring Charles: Unstuck Pod and Bee Formless. Sources, dates/durations, and limitations are documented in the architecture file and `tools/resource-library.json`. Only public post and publisher-supplied episode material is published; the private content library and podcast-prospect corpus are excluded. No trackers, authentication, remote players, or feed vendor were added.

`tools/build_resources.py` builds the collections, source ItemLists, breadcrumbs, footer/subsection navigation, and new-hub Resources links. Existing guide and Blog destinations remain stable. The captured Home enhancement changes its Resources destination only; original Home sections and frozen modules remain intact. The native menu icon is fixed: flex shrink and excess margins had collapsed the three bars to zero height at phone widths. Native pages request the updated scoped foundation stylesheet.

Verification: 45 pages, local anchors/assets, metadata, structured data, staging noindex, baseline integrity, imports, and script syntax pass. Six surfaces (four new resource pages, guide collection, and cash-flow guide) have confirmed layouts at 320, 390, 768, 1024, and 1440 pixels with one exposed H1 and no horizontal overflow. Phone screenshots and menu/Escape checks confirm visible menu bars; Home's phone Resources link reaches the new hub. Subsection navigation and Tools → cash worksheet anchor focus work. The previous cash-guide responsive limitation is resolved; its QA file now points to this follow-up. Recorded browser evidence: `tools/resource-layout-qa.json`. This is not a full accessibility/performance audit, and search, conversion, or citation effects remain unmeasured. Podcast playback, automatic LinkedIn updates, and printed pagination remain outside the checks.

Next architecture portion: repair the separate Blog catalog, narrow the article/guide roles, and review evidence before promoting legacy drafts. Automatic LinkedIn updates and additional appearance/post URLs remain batched human feedback items. The live Framer project is untouched.
