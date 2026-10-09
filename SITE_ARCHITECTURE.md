# Centripetal concept — content architecture

Updated October 9, 2026. GitHub concept only. No live Framer changes.

## Agreed structure and page roles

Blog remains a separate top-level section, as requested. Resources contains Guides, Tools & Assessments, LinkedIn Posts, and Media. About and Contact are distinct destinations. Their placement alone is not a measured search or AI-citation benefit.

| Section | Job | Concept destination |
|---|---|---|
| Home | Position the firm and direct the next step | `index.html` |
| Services | Explain responsibilities, scope, possible outputs, and relevant situations | `services.html` and six service pages |
| Resources | Connect founder questions to resources and formats | `resources/index.html` |
| Guides | Substantial frameworks with evidence, decisions, and next steps | `guides/index.html` and seven existing guide URLs |
| Tools & Assessments | Interactive work within reviewed guide concepts | `resources/tools.html`; original exercises retain their URLs |
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
| Board & investor reporting | Existing article/tool drafts require review; hub currently links to service | Board & investor reporting |
| Venture debt | Venture Debt Readiness checklist | Venture debt readiness |
| Treasury & finance operations | Treasury Hygiene; related cash review | Treasury & finance operations |

A typical path is article or public post → relevant guide/exercise → specific service or conversation. Readers may also enter directly at a service, guide, or podcast page. Links should support these different starting points rather than force a funnel.

## Asset inventory and overlap

`tools/content-architecture.csv` inventories the 45 current HTML pages by section, topic, role, and review state. It is a routing/content inventory, not a factual sign-off on legacy drafts.

- Seven curated guides retain their original destinations and distinct framework roles.
- The tool collection links to four existing experiences: Scorecard, Series A checklist, venture-debt checklist, and cash-review worksheet. It does not promote five older calculator/tool prototypes.
- The Finance Diagnostic overlaps the Scorecard; Fundraise Readiness overlaps Series A diligence; CFO Fit Calculator overlaps the CFO decision guide. Decide whether each has a distinct job before promoting it.
- Runway Modeler requires assumption, formula, boundary, and interpretation review. Board Deck Builder requires its sharper investor-question angle and content review.
- Fifteen existing article concepts now have one catalog at `blogs.html`, grouped under the same six topics as Resources. The Scorecard is represented as a guide/tool rather than a Blog listing. `blog/index.html` is a legacy entry path linking to the canonical catalog, without a second article list. All existing detail URLs remain stable.
- CFO timing, CFO-versus-VP, and bookkeeper/controller/CFO articles overlap the decision guide. Assign a narrow question to each or consolidate. Cash forecast articles overlap the cash guide; separate explanation from the working review. Board articles should support the future Board Deck Builder, rather than duplicate it.

## Tool role decisions

| Existing prototype | Architecture decision | Reason / remaining review |
|---|---|---|
| Finance Readiness Diagnostic | Consolidate into the existing Finance Scorecard; do not add a second diagnostic destination | Same broad finance self-assessment job; preserve the reviewed Scorecard’s existing scoring model |
| Fundraise Readiness Checklist | Consolidate into Series A Diligence Readiness | Same evidence/readiness task; refine one checklist rather than introduce competing readiness labels |
| CFO Fit Calculator | Consolidate into the CFO decision guide | Staffing fit depends on work and ownership; an unverified score would duplicate or oversimplify that decision |
| Cash Runway Scenario Modeler | Keep as a distinct unpromoted model concept | A calculation/scenario model has a different job from the cash evidence-review worksheet; formulas, assumptions and boundaries need review before use |
| Board Deck Structure Builder | Keep as a distinct unpromoted preparation concept | Organize evidence around board decisions and anticipated questions; distinguish recurring board reporting from a fundraising pitch and its diligence |

No prototype is newly exposed through Tools & Assessments in this portion. Existing prototype URLs remain available for reference; consolidation describes the future editorial/product direction and does not delete source material. The Board Deck Builder is the next guide/tool architecture review.

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
| Board Reporting for Seed and Series A Companies | Which decision should the board package support at this meeting? | `guides/saas-finance-scorecard.html` | `services/board-investor-reporting.html` |
| The Cash-Flow Signals Lenders Probe That a 13-Week Model Can Hide | Which obligations and receipt assumptions should accompany a lender cash model? | `guides/venture-debt-readiness.html` | `services/venture-debt-readiness.html` |
| Treasury Controls Every SaaS Founder Should Have Before the Next Board Meeting | Can the team demonstrate who can move cash and how exceptions are checked? | `guides/treasury-hygiene.html` | `services/treasury-finance-operations.html` |
| CARR vs ARR: When the Definition Matters | Which definition and contract timing explain the gap between contracted and live recurring revenue? | `guides/series-a-diligence-readiness.html` | `services/fundraising-readiness.html` |
| Customer Concentration: The Board Question You Should Answer First | What operating decision changes if a material customer renews late or leaves? | `guides/saas-cash-flow-mistakes.html` | `services/cash-flow-runway-planning.html` |
| The Vertical SaaS Advantage Has a Half-Life | How does the acquisition plan change as growth moves beyond founder-led distribution? | `guides/saas-finance-scorecard.html` | `services/fractional-cfo-for-saas.html` |

`tools/build_blog.py` uses the shared Home-derived native shell for the catalog and article pages. Reading content is inside one main landmark, the primary navigation precedes it, one H1 is exposed, and contents links identify section targets. Existing URLs, clean canonicals, breadcrumbs, and the separate top-level Blog destination are preserved. No search/filter feature, calculator, automatic feed, or new branding system is introduced.

The role map is a working editorial contract, not evidence that the retained article copy already fulfills it. Review priorities: CARR/ARR definitions and accounting distinctions; CFO role/scope and historical pricing/threshold claims; treasury coverage and timing promises; lender and investor behavior generalizations; absolute AI capability claims; then sophistication and repetition across the remaining drafts. Article-specific review notes are recorded alongside each source body.

## LinkedIn Posts and Media

The initial LinkedIn subsection is a curated feed with three independently verified public post URLs, editorial summaries identified as summaries, and links to the originals. It is not an automatically synchronized feed. Exact publication dates are omitted where the retrieved public page did not establish them. No private call transcripts, unpublished drafts, comments, contact exports, or engagement counts are republished. The local post corpus informed discovery; the private draft content library was excluded.

Media initially contained two public episode listings: Unstuck Pod (September 17, 2026, 20 minutes) and Bee Formless (May 20, 2026, 31 minutes). Dates, durations, titles, and descriptions come from publisher-supplied platform listings. The Bee Formless Apple page was directly readable; the Unstuck Amazon episode was available through public search but its direct fetch failed. Player functionality was not tested. The podcast-target/transcript prospect corpus is not an appearances list and was excluded.

The supplied Recorded Podcasts CSV adds four linked appearances: Insure the Horizon, The Capital Multiplier, Founder Wisdom Podcast (called VC Wisdom in the supplied list), and Analytics and Automation Solutions. Publisher titles and publication dates were checked directly in YouTube/Spotify browser pages; appointment dates from the CSV are not used as release dates. Public summaries paraphrase publisher descriptions. Belinda Murray’s YouTube link was matched to Bee Formless using the publisher’s public post and added to the existing episode. Jamie Schneiderman’s appearance matches the existing Unstuck entry and is not duplicated.

Six linked appearances are now available. Per the user’s follow-up, Media contains only live linked episodes: the More conversations section and its four awaiting-link listings were removed. Missing episode URLs can be supplied later; those shows are not displayed as live appearances. What We Need to Grow sits beneath “To Be Recorded” in the source list and is held out of completed appearances until confirmed. Private contact details and tracking notes are excluded from the repository and public page.

No automatic scraping, third-party feed subscription, embedded trackers, player requests, or authentication was added. Source records and summaries live in `tools/resource-library.json`; `tools/build_resources.py` rebuilds the collections. The update method for the eventual LinkedIn feed remains a human preference to resolve; the curated concept is independently usable.

## Route and template rules

- Resources has its own hub; `guides/index.html` now means the guide collection.
- Guide and article detail URLs are preserved. Blog is not moved under Resources.
- Resource navigation, descriptive links, CollectionPage/ItemList data, and breadcrumbs connect the collections.
- Native global Resources links, captured-page enhancement links, and Resources breadcrumbs point to the new hub. Original frozen capture modules stay unchanged.
- Keep public summaries as text on the site, with a source link. A third-party embed alone would not give the library a dependable reading experience.
- Concept pages remain noindex. Changes to canonical routes and production redirects belong to a separately planned production migration.

## Next manageable portions

Work in the user’s agreed sequence:

1. **Architecture and strategy:** live-only Media, the separate Blog catalog, article/guide roles, topic relationships, and prototype consolidation decisions are now recorded. Next, review the Board Deck Builder’s question/evidence structure without launching a new calculator or changing the visual system.
2. **Content, copy, and messaging:** review legacy article evidence, refine guide drafts and service language, complete missing appearance URLs, and review the Board Deck Builder’s content and assumptions.
3. **Further visual design and interactivity:** assess navigation prominence, feed updates, filtering, search, and tool presentation after the structure and content are settled. Preserve live Home-derived Lora/Roboto typography and pine/stone/sage branding throughout. Add topic landing pages only when enough distinct resources justify useful synthesis.

The live-only Media cleanup and Blog structure repair are complete for this portion. Further visual design and interactivity remain deferred.

## Basis and measurement

The May audit's architecture and internal-linking recommendations and the August overview's separate `/blog/` publishing model provide the starting point. This user's direction supersedes the earlier recommendation to nest Blog in Resources navigation. The reports' Framer publishing directions are source material, not authorization to alter the live project.

[Google SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) supports logical organization and descriptive internal links. [Google AI-feature guidance](https://developers.google.com/search/docs/appearance/ai-features) emphasizes discoverability, accessible text, and content quality; it does not establish an advantage for a particular Blog menu position. Search, conversion, citation, and field-performance outcomes remain unmeasured.
