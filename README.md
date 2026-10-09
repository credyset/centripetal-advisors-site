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
