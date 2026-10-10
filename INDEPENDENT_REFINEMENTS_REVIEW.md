# Centripetal concept — deeper QC closeout

October 10, 2026. GitHub concept only. The May audit and August overview remain the strategic basis. The previous review checkpoint was premature: it had not reconciled the actual diagnostic workbook or resolved the legacy public tool destinations.

## Independently resolved in this pass

| Finding | Correction |
|---|---|
| Diagnostic provenance treated as unknown | Reviewed the client-provided 2024 workbook. It has the same eight categories, 1–5 category scores, cumulative total, and more than 100 detailed prompt rows. The public page now identifies this basis and distinguishes its simplified descriptions from the full diagnostic. |
| Four aggregate score classifications had no source support | Removed them. Kept the category breakdown and cumulative total; included all ties at the third-lowest cutoff. High-score selections receive verification prompts. |
| Four reachable legacy tools retained duplicate or unvalidated behavior | Converted them to entry pages for the CFO guide, Scorecard, Series A guide, and cash review. Earlier prototypes remain in repository history and the local research archive; no raw client source workbook was uploaded. |
| Venture Debt lacked a working open-item list | Added the list, completion state and print action. Corrected an investor/lender wording error and supplied valid item anchors. |
| Checklist reset could run without updating the follow-up list | Replaced initialization-order-dependent button wiring with a reset signal. Verified cleared selections and restored open items. |
| Checkbox controls polluted accessible heading names | Moved the controls beside headings with explicit labels on both diligence guides. |
| Treasury and post-raise guides described outputs without enough help producing them | Added an offline treasury review brief and a post-raise decision log framework, including dependencies and clearly labeled illustrations. |
| Two articles needed a sharper decision distinction | Added facility-versus-spendable-cash and founder-led-versus-next-channel exercises. Neither is represented as an approved client example. |
| Old SVB citation redirected to a homepage | Replaced it with the current First Citizens Innovation Banking article. Other primary references were rechecked; FDIC blocked direct crawler access but search evidence confirmed the cited guidance. |
| Small contrast and navigation issues | Corrected Scorecard result/footer contrast, whole-option radio focus indication, and native footer heading levels. Copied mobile menus support Enter/Space and Escape with focus return; logo/social links have accessible names. |
| Historical QA output sounded like current scoring validation | The foundations check now explicitly labels historical Home geometry and no longer reports obsolete score-band checks as current. |

## Evidence

`tools/deeper-qc-20261010.json` records current browser observations. All 41 native pages were checked at actual widths of 320, 800 and 1280 pixels: 123 layout observations. No outer overflow, duplicate IDs, missing loaded first-party images, multiple main H1s, or invalid generated diligence anchors were observed. Changed expanded states were checked separately.

Browser checks cover Scorecard ties, all-low/all-high outcomes and reset; Venture Debt partial/completed/reset behavior; Series A reset; contact-topic prompts, draft preservation through responsive changes and preview-only submission; copied mobile keyboard navigation. The existing ten builder combinations and successful browser Copy check remain recorded in the earlier QA file. `tools/test_board_clipboard.mjs` runs the actual Copy handler against denied, unavailable and successful clipboard APIs in an isolated DOM fixture. This is failure-path evidence, not a browser permission-denial test.

Treasury print preview rendered all content across five pages with navigation and controls omitted. Print spacing was refined to keep brief labels with their descriptions. No physical printing was performed. The frozen Home visual modules remain intact; accessibility enhancements are in the separate concept helper.

The local client diagnostic is the source for categories and cumulative scoring, not a validated statistical model or a statement that all dated legal prompts still apply. Its sample percentage is inconsistent with its numeric total and is not reused. Public descriptions remain an editorial adaptation. Client-specific confidential conversations and unapproved personal quotes have not been added to the website.

## Judgment that remains

- Charles’s preferred language, distinctive examples, and approval for personal attribution or client stories.
- Which founder questions and service priorities should lead the final experience.
- Current engagement commitments, availability and delivery promises, if the final copy should include them.
- Reader usefulness and brand fit before freezing the two provisional reference patterns.

These are editorial and business choices. The existence of the diagnostic, its categories, the legacy consolidation, and the reset behavior no longer need user clarification.

## Measurement limits

The concept remains noindex. No ranking, citation or conversion improvement is claimed. Fresh Lighthouse/field performance, a full screen-reader audit and playback of every third-party embed at every width have not been measured. The saved asset inventory is a source-size inventory, not network transfer or Core Web Vitals. Production migration, analytics and the live AI-citation baseline remain separate work with their own scope. Historical May results have not been relabeled as current concept measurements.
