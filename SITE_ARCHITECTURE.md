# Centripetal concept — content architecture

Updated October 9, 2026. GitHub concept only. No live Framer changes.

## Agreed structure and page roles

Blog remains a separate top-level section, as requested. The agreed Resources structure is Guides & Tools, LinkedIn Posts, and Media. The combined library is implemented at `guides/index.html`; the old tools entry links to it without repeating the catalog. The table records current routes and their roles. About and Contact are distinct destinations. Their placement alone is not a measured search or AI-citation benefit.

| Section | Job | Concept destination |
|---|---|---|
| Home | Position the firm and direct the next step | `index.html` |
| Services | Explain responsibilities, scope, possible outputs, and relevant situations | `services.html` and six service pages |
| Resources | Connect founder questions to resources and formats | `resources/index.html` |
| Guides & Tools | Eight distinct frameworks, embedded reviews, assessments, and a builder, with format labels | `guides/index.html`; original detail URLs remain stable |
| Legacy tools entry | Direct existing links to the combined library | `resources/tools.html`; no second resource catalog |
| LinkedIn Posts | A feed-style selection of Charles's published public posts | `resources/linkedin-posts.html` |
| Media | Charles's confirmed podcast appearances | `resources/media.html` |
| Blog | Focused explanatory articles supporting related guides/services | `blogs.html`; six topics and fifteen existing article concepts |
| About | Firm identity, people, operating approach, approved experience | `about.html` |
| Contact | Topic-aware conversation entry | `contact.html` |

The current captured Home menu keeps its layout and original sections. Its added Resources link now reaches the proper hub. About remains reachable through the existing founder/footer paths; a full primary-navigation layout review can consider its prominence. This batch does not claim the complete target navigation has been redesigned.

## Topics and reader paths

Topics describe the founder's question; formats describe the experience. The hub presents topics first and formats second. One asset can support several topics without being copied into multiple URLs.

| Topic | Available guides/exercises | Service relationship |
|---|---|---|
| Finance leadership | Finance Scorecard; Do I Need a Fractional CFO? | Fractional CFO for SaaS |
| Fundraising readiness | Series A diligence; First 90 Days | Fundraising readiness |
| Cash & runway | Cash-Flow Mistakes review; First 90 Days | Cash-flow & runway planning |
| Board & investor reporting | Board Deck Structure Builder; related article concept remains pending content review | Board & investor reporting |
| Venture debt | Venture Debt Readiness checklist | Venture debt readiness |
| Treasury & finance operations | Treasury Hygiene; related cash review | Treasury & finance operations |

A typical path is article or public post → relevant guide/exercise → specific service or conversation. Readers may also enter directly at a service, guide, or podcast page. Links should support these different starting points rather than force a funnel.

## Asset inventory and overlap

`tools/content-architecture.csv` inventories the 45 current HTML pages by section, topic, role, and review state. It is a routing/content inventory, not a factual sign-off on legacy drafts.

- Seven curated guides retain their original destinations and distinct framework roles.
- The combined library lists eight resources once, distinguishing guides, embedded checklists/worksheets, assessment, and builder. Four older calculator/tool prototypes remain unpromoted.
- The Finance Diagnostic overlaps the Scorecard; Fundraise Readiness overlaps Series A diligence; CFO Fit Calculator overlaps the CFO decision guide. Decide whether each has a distinct job before promoting it.
- Runway Modeler requires assumption, formula, boundary, and interpretation review. Board Deck Builder now has a distinct board-meeting preparation role: decision, recommendation, evidence, assumptions, ownership, and follow-up. Its wording remains a concept for firm review.
- Fifteen existing article concepts now have one catalog at `blogs.html`, grouped under the same six topics as Resources. The Scorecard is represented as a guide/tool rather than a Blog listing. `blog/index.html` is a legacy entry path linking to the canonical catalog, without a second article list. All existing detail URLs remain stable.
- CFO timing, CFO-versus-VP, and bookkeeper/controller/CFO articles overlap the decision guide. Assign a narrow question to each or consolidate. Cash forecast articles overlap the cash guide; separate explanation from the working review. The board-reporting article links to the refined Board Deck Builder; the investor-pitch article continues to link to Series A diligence.

## Agreed library direction and reference-page plan

The user agrees to one Guides & Tools subsection within Resources. Its navigation is implemented. The first guide and tool reference designs are ready for human review: Cash-Flow Mistakes & Forecast Review and Board Deck Builder. [RESOURCE_PAGE_STANDARD.md](RESOURCE_PAGE_STANDARD.md) now maps audit recommendations to both pages and separates content/SEO requirements, brand/layout foundations, component/interaction patterns, and page composition. Template sequences and visual rules remain provisional until these examples are refined and reviewed. The cash guide now has a direct answer, reading index, continuous framework and example, then optional worksheet. The builder places the working outline first, with optional review and a compact supporting method. Desktop interaction checks pass; actual narrow-width verification remains open because browser viewport requests do not change the rendered 1280px width. Broad page migration waits for that verification and batched human review.

## Tool role decisions

| Existing prototype | Architecture decision | Reason / remaining review |
|---|---|---|
| Finance Readiness Diagnostic | Consolidate into the existing Finance Scorecard; do not add a second diagnostic destination | Same broad finance self-assessment job; preserve the reviewed Scorecard’s existing scoring model |
| Fundraise Readiness Checklist | Consolidate into Series A Diligence Readiness | Same evidence/readiness task; refine one checklist rather than introduce competing readiness labels |
| CFO Fit Calculator | Consolidate into the CFO decision guide | Staffing fit depends on work and ownership; an unverified score would duplicate or oversimplify that decision |
| Cash Runway Scenario Modeler | Keep as a distinct unpromoted model concept | A calculation/scenario model has a different job from the cash evidence-review worksheet; formulas, assumptions and boundaries need review before use |
| Board Deck Structure Builder | Expose as a distinct preparation concept in Guides & Tools | Meeting focus and request type shape an outline; six evidence areas track follow-ups. No stage mandates, readiness rating, or automatic slide creation. Distinct from fundraising diligence |

The refined Board Deck Builder is now exposed through Guides & Tools and the Board topic in Resources. Four remaining prototype URLs remain available for reference; consolidation describes the future editorial/product direction. The builder retains its stable URL, uses the shared Home-derived shell, and links to board-reporting support and a topic-aware conversation. Only the fixed topic/source identifiers reach Contact; selections remain in memory.

`tools/board-builder-content.json` holds six core evidence sections and five focus modules (operating plan, cash commitment, revenue/customer dependence, financing, material miss). `tools/build_board_builder.py` builds static readable content, metadata, and the default outline; `assets/board-builder.js` changes the outline and transient follow-up list. Input versus decision-request framing does not determine governance approvals. Completing the review does not certify readiness. Stripe’s linked recurring-revenue explanation supports the metric distinctions; the preparation sequence is concept editorial judgment, not a validated board prediction. The local operator-reality guidance informed the focus on concise reporting, company-level evidence, and leader ownership. No fabricated client results, service delivery promises, or personal Charles authorship is included.

## Article-versus-guide contract

An article addresses one narrow founder question. A guide owns the broader framework, evidence review, checklist, or exercise. A service explains the responsibilities and working support. Articles have a named related guide and service; the catalog does not duplicate the Scorecard as an article. Blog remains separate from Resources.

The fifteen entries below are existing **concept drafts**, visibly marked as pending content/factual review. They are available for architecture review in the noindex concept, not represented as approved public thought leadership. Unexplained 2024 dates and publication claims were removed. No personal Charles authorship or Article publication metadata is asserted. They remain outside the curated sitemap until editorial review. Existing draft bodies are retained in `tools/blog-content.json`; repetitive appended checklist boilerplate and generic CTA blocks are removed so the article’s narrow role and related framework are clear.

| Article | Narrow question / job | Related guide | Related service |
|---|---|---|---|
| When to Hire a Fractional CFO | What changed in the company that creates a need for senior finance ownership? | `guides/do-i-need-a-fractional-cfo.html` | `services/fractional-cfo-for-saas.html` |
| Bookkeeper, Controller, CFO: What Your Stage Actually Needs | Which finance responsibilities are uncovered by the current team? | `guides/do-i-need-a-fractional-cfo.html` | `services/fractional-cfo-for-saas.html` |
| Fractional CFO or VP Finance? The Decision Is Complexity, Not ARR | When does daily operating ownership change the finance leadership model? | `guides/do-i-need-a-fractional-cfo.html` | `services/fractional-cfo-for-saas.html` |
| What AI Cannot Replace in Founder Finance | Who checks and owns the decision supported by an AI finance output? | `guides/saas-finance-scorecard.html` | `services/fractional-cfo-for-saas.html` |
| The Series A Data Room: What Goes In and What Gets Opened | Can an investor trace a reported number back to its evidence? | `guides/series-a-diligence-readiness.html` | `services/fundraising-readiness.html` |
| What Investors Probe After Slide 12 | Which links between the pitch story and supporting evidence need explanation? | `guides/series-a-diligence-readiness.html` | `services/fundraising-readiness.html` |
| After the Raise, Capital Structure Becomes an Operating Decision | How would another financing obligation change the post-raise operating plan? | `guides/first-90-days-after-raise.html` | `services/venture-debt-readiness.html` |
| The 13-Week Cash Flow Forecast: What It Shows and What It Hides | What can a weekly cash view answer, and what depends on the longer-range plan? | `guides/saas-cash-flow-mistakes.html` | `services/cash-flow-runway-planning.html` |
| Why Investors Don't Trust Your Forecast | Can a reader follow an assumption change through the forecast to a decision? | `guides/saas-cash-flow-mistakes.html` | `services/cash-flow-runway-planning.html` |
| Board Reporting for Seed and Series A Companies | Which decision should the board package support at this meeting? | `guides/tools/board-deck-builder.html` | `services/board-investor-reporting.html` |
| The Cash-Flow Signals Lenders Probe That a 13-Week Model Can Hide | Which obligations and receipt assumptions should accompany a lender cash model? | `guides/venture-debt-readiness.html` | `services/venture-debt-readiness.html` |
| Treasury Controls Every SaaS Founder Should Have Before the Next Board Meeting | Can the team demonstrate who can move cash and how exceptions are checked? | `guides/treasury-hygiene.html` | `services/treasury-finance-operations.html` |
| CARR vs ARR: When the Definition Matters | Which definition and contract timing explain the gap between contracted and live recurring revenue? | `guides/series-a-diligence-readiness.html` | `services/fundraising-readiness.html` |
| Customer Concentration: The Board Question You Should Answer First | What operating decision changes if a material customer renews late or leaves? | `guides/saas-cash-flow-mistakes.html` | `services/cash-flow-runway-planning.html` |
| The Vertical SaaS Advantage Has a Half-Life | How does the acquisition plan change as growth moves beyond founder-led distribution? | `guides/saas-finance-scorecard.html` | `services/fractional-cfo-for-saas.html` |

`tools/build_blog.py` uses the shared Home-derived native shell for the catalog and article pages. Reading content is inside one main landmark, the primary navigation precedes it, one H1 is exposed, and contents links identify section targets. Existing URLs, clean canonicals, breadcrumbs, and the separate top-level Blog destination are preserved. No search/filter feature, calculator, automatic feed, or new branding system is introduced.

The role map is a working editorial contract, not evidence that the retained article copy already fulfills it. Review priorities: CARR/ARR definitions and accounting distinctions; CFO role/scope and historical pricing/threshold claims; treasury coverage and timing promises; lender and investor behavior generalizations; absolute AI capability claims; then sophistication and repetition across the remaining drafts. Article-specific review notes are recorded alongside each source body.

## LinkedIn Posts and Media

The LinkedIn subsection now uses a hybrid curated feed: seven recent user-supplied posts as timeline entries with editorial introductions, verified original activity links, and always-visible native LinkedIn previews with browser-native lazy loading. The earlier-selections section is removed from the displayed feed; those source records remain stored for future curation. The secondary feed introduction and repeated author/platform/format labels are also removed per the user’s cleanup request. Three recent article-share cards also link to the corresponding LinkedIn article. The preview headings are editorial summaries, not claimed original titles. Chris Ellis retains attribution inside Charles’s repost/commentary preview.

All seven supplied embed URLs were inspected directly and rendered within the local concept. Original activity URLs were taken from the embeds’ own links, rather than assuming the supplied share/ugcPost identifier equals the activity identifier. Only relative ages were available, so absolute publication dates and persistent relative timestamps are omitted. The supplied order is retained. Reactions and comments are shown only by LinkedIn itself, not copied into native cards.

`assets/linkedin-feed.css` isolates the timeline layout, Home-derived typography/palette, author rail, and narrow-width topic navigation to this page. Each preview is a static iframe directly below its editorial introduction, without an outer card border, padding, or disclosure control. Each iframe has a unique descriptive title, the supplied height, a responsive width, and `loading="lazy"` so the browser can defer off-screen frames. Previews no longer need page JavaScript; original-post and article links remain available if LinkedIn cannot render. LinkedIn controls the appearance and any “more” interaction inside its own frame. No automatic synchronization, scraping, subscription service, copied external imagery, unpublished post corpus, or account authentication was added. The static source is `tools/resource-library.json`.

Media initially contained two public episode listings: Unstuck Pod (September 17, 2026, 20 minutes) and Bee Formless (May 20, 2026, 31 minutes). Dates, durations, titles, and descriptions come from publisher-supplied platform listings. The Bee Formless Apple page was directly readable; the Unstuck Amazon episode was available through public search but its direct fetch failed. Player functionality was not tested. The podcast-target/transcript prospect corpus is not an appearances list and was excluded.

The supplied Recorded Podcasts CSV adds four linked appearances: Insure the Horizon, The Capital Multiplier, Founder Wisdom Podcast (called VC Wisdom in the supplied list), and Analytics and Automation Solutions. Publisher titles and publication dates were checked directly in YouTube/Spotify browser pages; appointment dates from the CSV are not used as release dates. Public summaries paraphrase publisher descriptions. Belinda Murray’s YouTube link was matched to Bee Formless using the publisher’s public post and added to the existing episode. Jamie Schneiderman’s appearance matches the existing Unstuck entry and is not duplicated.

Six linked appearances are now available. Per the user’s follow-up, Media contains only live linked episodes: the More conversations section and its four awaiting-link listings were removed. Missing episode URLs can be supplied later; those shows are not displayed as live appearances. What We Need to Grow sits beneath “To Be Recorded” in the source list and is held out of completed appearances until confirmed. Private contact details and tracking notes are excluded from the repository and public page.

Media remains text and direct platform links, without embedded players. The LinkedIn feed contains seven always-visible iframes; the browser determines when their third-party requests load through native lazy loading. Source records and summaries live in `tools/resource-library.json`; `tools/build_resources.py` rebuilds the collections. Automatic LinkedIn ingestion remains a separate future decision.

## Route and template rules

- Resources has its own hub; `guides/index.html` is the combined Guides & Tools library; `resources/tools.html` links to it without a second catalog.
- Guide and article detail URLs are preserved. Blog is not moved under Resources.
- Resource navigation, descriptive links, CollectionPage/ItemList data, and breadcrumbs connect the collections.
- Native global Resources links, captured-page enhancement links, and Resources breadcrumbs point to the new hub. Original frozen capture modules stay unchanged.
- Keep public summaries as text on the site, with a source link. A third-party embed alone would not give the library a dependable reading experience.
- Concept pages remain noindex. Changes to canonical routes and production redirects belong to a separately planned production migration.

## Next manageable portions

The user has refined the next sequence: develop and review one guide and one tool before extracting standards to apply across the library.

1. **Reference guide:** Cash-Flow Mistakes & Forecast Review. Refine the founder prompt and direct answer, content/evidence, worked example, reading layout, and optional worksheet together.
2. **Reference tool:** Board Deck Builder. Refine the task, useful output, input/result relationship, supporting method, visual hierarchy, and core interaction states together.
3. **Review and extract:** batch human feedback on the two complete pages, then document demonstrated shared foundations and guide/tool differences. The agreed combined library is implemented; actual narrow-width verification remains required before page-template migration.
4. **Apply and extend:** adapt the reference patterns to the remaining resources according to their jobs and review each page’s copy/evidence. Revisit legacy articles, service wording, navigation prominence, and unpromoted model assumptions in manageable portions. Advanced filtering, feed automation, decorative motion, and new exports remain later product decisions.

The live-only Media cleanup, Blog structure repair, and initial Board Deck Builder refinement are complete. Useful visual hierarchy and core interaction design are part of the two reference-page exercises, while Home-derived branding and all live Framer boundaries remain intact. See the audit-to-page mapping, design layers, and completion criteria in RESOURCE_PAGE_STANDARD.md.

## Basis and measurement

The May audit's architecture and internal-linking recommendations and the August overview's separate `/blog/` publishing model provide the starting point. This user's direction supersedes the earlier recommendation to nest Blog in Resources navigation. The reports' Framer publishing directions are source material, not authorization to alter the live project.

[Google SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) supports logical organization and descriptive internal links. [Google AI-feature guidance](https://developers.google.com/search/docs/appearance/ai-features) emphasizes discoverability, accessible text, and content quality; it does not establish an advantage for a particular Blog menu position. Search, conversion, citation, and field-performance outcomes remain unmeasured.
