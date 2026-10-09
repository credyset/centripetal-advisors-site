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
| Blog | Focused explanatory articles supporting related guides/services | Existing `blogs.html` destination; catalog repair is next |
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
- Fifteen local article concepts exist. The captured Blogs page contains Scorecard entries; `blog/index.html` also lacks a usable article catalog. Repairing the Blog index is the next architecture portion, followed by article-by-article evidence review.
- CFO timing, CFO-versus-VP, and bookkeeper/controller/CFO articles overlap the decision guide. Assign a narrow question to each or consolidate. Cash forecast articles overlap the cash guide; separate explanation from the working review. Board articles should support the future Board Deck Builder, rather than duplicate it.

## LinkedIn Posts and Media

The initial LinkedIn subsection is a curated feed with three independently verified public post URLs, editorial summaries identified as summaries, and links to the originals. It is not an automatically synchronized feed. Exact publication dates are omitted where the retrieved public page did not establish them. No private call transcripts, unpublished drafts, comments, contact exports, or engagement counts are republished. The local post corpus informed discovery; the private draft content library was excluded.

Media starts with two public episode listings: Unstuck Pod (September 17, 2026, 20 minutes) and Bee Formless (May 20, 2026, 31 minutes). Dates, durations, titles, and descriptions come from publisher-supplied platform listings. The Bee Formless Apple page was directly readable; the Unstuck Amazon episode was available through public search but its direct fetch failed. Player functionality was not tested. The podcast-target/transcript prospect corpus is not an appearances list and was excluded.

No automatic scraping, third-party feed subscription, embedded trackers, player requests, or authentication was added. Source records and summaries live in `tools/resource-library.json`; `tools/build_resources.py` rebuilds the collections. The update method for the eventual LinkedIn feed remains a human preference to resolve; the curated concept is independently usable.

## Route and template rules

- Resources has its own hub; `guides/index.html` now means the guide collection.
- Guide and article detail URLs are preserved. Blog is not moved under Resources.
- Resource navigation, descriptive links, CollectionPage/ItemList data, and breadcrumbs connect the collections.
- Native global Resources links, captured-page enhancement links, and Resources breadcrumbs point to the new hub. Original frozen capture modules stay unchanged.
- Keep public summaries as text on the site, with a source link. A third-party embed alone would not give the library a dependable reading experience.
- Concept pages remain noindex. Changes to canonical routes and production redirects belong to a separately planned production migration.

## Next manageable portions

1. Repair the separate Blog catalog and resolve article/guide overlap before promoting old drafts.
2. Expand/refresh the selected LinkedIn feed and Media inventory using public sources or supplied appearance/post links; decide on eventual automatic updates.
3. Review the Board Deck Builder and its supporting articles together.
4. Evaluate primary-navigation prominence, topic landing pages, filtering, and search as the reviewed library grows. Add a topic page only when it offers useful synthesis and sufficient distinct resources.

## Basis and measurement

The May audit's architecture and internal-linking recommendations and the August overview's separate `/blog/` publishing model provide the starting point. This user's direction supersedes the earlier recommendation to nest Blog in Resources navigation. The reports' Framer publishing directions are source material, not authorization to alter the live project.

[Google SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) supports logical organization and descriptive internal links. [Google AI-feature guidance](https://developers.google.com/search/docs/appearance/ai-features) emphasizes discoverability, accessible text, and content quality; it does not establish an advantage for a particular Blog menu position. Search, conversion, citation, and field-performance outcomes remain unmeasured.
