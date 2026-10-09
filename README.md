# Centripetal Advisors — Website Concept

A separate, reviewable concept for [centripetaladvisors.com](https://centripetaladvisors.com), maintained only in `credyset/centripetal-advisors-site`. Framer is a read-only design reference. This repository does not publish changes to Framer.

## October 8 foundation pass

The May 19 SEO audit is the working technical baseline, as confirmed by Christian. The August 13 SEO / AI surfaceability overview supplies the later resource priorities and content architecture.

- Restored the published Home design foundation: centered mark, original hero messaging, green/stone background, Lora/Roboto, rounded consultation CTA, co-pilot diagram, founder section, and existing client testimony.
- Added six focused service pages under `services/`, each with an explicit answer, founder context, work and deliverables, FAQs, supporting resources, and a relevant next step. The Services overview retains the published headline and the broad finance scope.
- Connected Home → Resources → guides/articles → relevant service → contact. Resources is now in primary navigation. The six existing guides remain central; the working scorecard stays interactive. The draft board-deck builder remains on disk but is omitted from the hub and sitemap.
- Removed the repeated generic “Put this into practice” paragraphs from articles. Added visible firm attribution without claiming Charles approved or authored the concept drafts.
- Consolidated font requests; optimized source assets; deferred Vimeo and Calendly loading until selected; added accessible menu state/Escape behavior, skip links, breadcrumbs, reduced-motion support, and scorecard keyboard grouping.
- Added unique canonical/social metadata, truthful Organization / WebSite / WebPage / Service / Article / CreativeWork / Breadcrumb structures, and a sitemap. Removed unverified publication dates and replaced outdated explicit BOI filing references with general responsibility language.

## Content status

This remains a concept. New service copy is proposed language based on existing firm capabilities; it is not a newly approved publication by Charles. Existing articles and tool interpretations still need final editorial and benchmark review. No new financial outcome claims, approved case studies, or measured search improvements are asserted.

The live site's inconsistent numerical proof variants have not been promoted into new Home claims. Existing client quote excerpts and video links come from the published Home page; the quote wording was retained. Public brand assets were optimized locally for the concept.

## Preview and validation

Serve the repository root with a static server, for example:

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

Open `http://127.0.0.1:8765/`. No build dependencies are needed.

```sh
python3 tools/check_site.py
node --check assets/concept.js
```

The structural check covers unique metadata, one H1 and main landmark per page, local URLs and fragments, explicit image dimensions and alt attributes, valid JSON-LD, sitemap uniqueness, and staging `noindex`.

Canonical and sitemap URLs currently use the existing GitHub Pages concept origin, `https://credyset.github.io/centripetal-advisors-site/`. All 38 pages remain `noindex, follow`; search engines can read the safeguard. The 37 sitemap entries omit the deferred board-deck tool. Sitemap presence does not make a `noindex` concept eligible for indexing.

## Measurement sequence

Finish and review the concept foundation first. Then reassess the AI citation study using the reports' founder-intent clusters, recording brand mentions, cited sources, competitors, and answer accuracy. A live baseline measures Centripetal's publicly available presence; it cannot attribute an improvement to unpublished or `noindex` concept pages. Production search and citation changes are a later measurement stage after an approved indexable release.
