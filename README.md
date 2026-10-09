# Centripetal Advisors — Published Site Baseline

This repository now establishes the published Home page as the visual baseline for the concept. It is served separately at [the GitHub concept site](https://credyset.github.io/centripetal-advisors-site/). Framer is unchanged.

## Baseline scope

Captured from `https://centripetaladvisors.com/` on October 8, 2026. The Home markup, styles, responsive variants, public media references, and original rendering behavior are retained. This is a capture of the public published output, not an export of the editable Framer project.

Home includes the original navigation; animated hero; statistics; complete financial co-pilot section and diagram; Clients and Trusted By logo bands; original About Us section; video/quote testimonial carousel; Why Centripetal; Charlie Munger quote and contact form; and original footer.

The public Services, Contact, Blogs, and Privacy Policy pages are captured too so the Home navigation has matching core destinations. Older guides and articles remain on disk for later iteration. The previous SEO enhancement proposal is preserved on `concept/home-and-seo-foundations` and draft PR #1; it is not the starting Home baseline.

Public generated rendering modules are frozen locally under `assets/baseline/runtime/`. Original fonts, images, and Vimeo media remain referenced at their public URLs. Module and source hashes are recorded in `assets/baseline/source-manifest.json`.

## Preview boundaries

The visual content and behavior are preserved. Only nonvisual preview boundaries differ:

- Navigation between the captured core pages stays in this GitHub concept.
- Contact forms cannot send a production message. Selecting Submit explains that no message was sent.
- Production Google/LinkedIn analytics, the Framer events script, and the editor bootstrap are omitted.
- Captured pages use concept canonical URLs and `noindex, follow`.

The existing published responsive behavior, heading duplication, proof figures, and presentation are intentionally retained for this baseline. SEO and experience changes come after visual parity, in separately reviewable iterations.

## Verification

`assets/baseline/layout-comparison.json` records matching Home section geometry and overall page heights at 390, 900, 1024, 1280, 1440, and 1920 pixels. The Home sections were also reviewed visually after their reveal animations. Animated logo orientation, ticker position, count-up progress, and carousel state can differ between two pages opened at different times.

```sh
python3 -m http.server 8765 --bind 127.0.0.1
node --check assets/home-baseline.js
python3 tools/check_baseline.py
```

To intentionally refresh the public-source baseline later:

```sh
python3 tools/capture_live_baseline.py
python3 tools/freeze_render_modules.py
```

These read public published URLs. They do not access a Framer account or publish to Framer. Preserve this baseline commit and compare each later section revision against it.
