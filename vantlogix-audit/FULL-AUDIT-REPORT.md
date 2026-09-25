# Vantlogix website: SEO audit

Project: Framer project "Indigo Bookings" (Vantlogix site), 12 pages
Audit date: 25 September 2026
Method: project-level audit read from the Framer project through the Framer agent API

## Scope and limits

The site has never been published. Framer reports every page as "added", and the production URL is empty. That means there is no live URL to crawl, so this audit reads the project itself: page metadata, headings, copy, links, images, CMS, redirects and custom code.

These checks need a live site and are **not** covered here:

- robots.txt, XML sitemap, canonical tags and HTTP status codes. Framer generates these automatically on publish, so check them after launch.
- Core Web Vitals (LCP, INP, CLS) and page speed.
- Security headers, redirects between www and non-www, HTTPS.
- Rendered-HTML checks, backlinks, and Google Search Console data.

Because performance could not be measured, it is left out of the score and the other weights are rescaled.

## Executive summary

**SEO Health Score: 36 / 100**

**Business type:** B2B technology and services company for venue and event operators. It sells a platform (SPOVIX) and four professional services, with offices in Dubai, San Jose and Kochi.

The copy is specific and credible, with a named founder, real offices, a named client (Yas Marina Circuit), and SOC 2 Type 1. The problems are almost all in setup that search engines rely on: no page titles or descriptions, no mobile layouts, no structured data, a duplicate homepage, and news items that have no pages of their own.

| Category | Weight | Score |
|---|---|---|
| Technical SEO | 22% | 40 |
| Content quality | 23% | 55 |
| On-page SEO | 20% | 30 |
| Schema / structured data | 10% | 0 |
| Performance (Core Web Vitals) | 10% | not measured (site unpublished) |
| AI search readiness | 10% | 40 |
| Images | 5% | 25 |

### Top 5 critical issues

1. **No page titles or meta descriptions anywhere.** The site title is Framer's default "My Framer Site" and the description is "Made with Framer". All 12 pages inherit these, so every search result would show the same wrong title.
2. **No mobile or tablet layouts.** Every page and the shared layout template have only a Desktop breakpoint. Google indexes the mobile version of a page first, so this affects rankings on every page.
3. **Duplicate homepage.** `/home` repeats `/` almost word for word (479 vs 523 words, same headings). Two URLs competing for the same query weaken both.
4. **Two H1 headings on the homepage.** The hero contains two copies of "We build technology for complex venues and live events" (Hero Panel → Hero Text, text nodes `bvdxQfF4A` and `pE44kUZ06`).
5. **Internal notes and placeholder copy in live page text.** Examples: "Confirm investor naming", "Confirm a press kit exists before this ships", "Address and direct phone line to be confirmed before launch", "this slot shows the pattern without inventing content". Visitors and crawlers would read these once the site is published.

### Top 5 quick wins

1. Set a site title and description on the Root, then a unique title and description on each page (drafts are in the action plan).
2. Delete `/home`, or redirect it to `/`.
3. Remove the duplicate homepage H1.
4. Add alt text to the five images that lack it.
5. Add Organization structured data (JSON-LD) in Site Settings → Custom Code.

## Technical SEO (40 / 100)

**What works**

- Clean, readable URL structure: `/services/data-analytics`, `/industries`, `/careers`. Service detail pages nest under `/services`.
- One shared layout template ("Corporate Layout") gives every page the same header and navigation.
- No broken redirect chains; the project has no redirects yet.

**Findings**

- **Critical: no mobile or tablet breakpoints.** All 12 pages and the layout template use a single Desktop breakpoint. Add Tablet (810 px) and Phone (390 px) breakpoints and check each section at those sizes.
- **High: duplicate page `/home`.** Remove it or set up a redirect `/home` → `/`.
- **High: site not published.** Nothing can be indexed until it is. Connect the custom domain before launch so Google indexes the final URLs, not a `framer.app` or `framer.website` address.
- **Info: server-side checks pending.** After publishing, confirm that `robots.txt` allows crawling, that `sitemap.xml` lists all 11 intended pages (and excludes `/home` if it's kept), and that canonical tags point to the custom domain.

## Content quality (55 / 100)

**What works**

- Specific, non-generic copy. It names real series (MotoGP, Formula 1), real problems (accreditation, ancillary-service requisitioning), and real proof (Yas Marina Circuit, SOC 2 Type 1).
- Strong E-E-A-T signals: a named founder (Sanjeev), 20+ years of combined technology and motorsport experience, three named offices with a street address in San Jose, a client quote with a named person and title, and a milestone timeline.
- Each service has its own page with a clear "who this is for" section.

**Findings**

- **High: internal notes and placeholder text in page copy** (the Newsroom, Contact, Careers and About pages). Remove them or move them into Framer comments.
- **Medium: thin pages.** The four service detail pages have 128–150 words each, Contact has 123 and Careers has 184. Aim for at least 300–500 words on each service page, covering typical projects, deliverables, venue examples and FAQs.
- **Medium: news has no article pages.** The News collection has 2 items (SOC 2 Type 1, SPOVIX launch) but no detail page such as `/newsroom/:slug`. "Read the announcement" links back to `/newsroom`. Each announcement should have its own indexable page.
- **Low: "Future entry" placeholder card** on `/newsroom` ("The grid is built for more than two items…"). Hide it until there is real content.

## On-page SEO (30 / 100)

**What works**

- Every page has a single, descriptive H1 except the homepage. The heading order (H1 → H2 → H3) is logical.
- Service pages link back to `/services` and to `/contact`.

**Findings**

- **Critical: no titles or meta descriptions** (see the action plan for drafts).
- **High: two H1s on the homepage.**
- **Medium: H1s without search terms.** "Talk to Vantlogix" (/contact), "Complex venues, high-profile events" (/industries) and "Join the team behind SPOVIX" (/careers) don't say what the page is about. People search for "venue management software", "stadium management software", "event management software", and similar. The copy uses "platform" and "system" but almost never "software".
- **Medium: generic H2** "Our Flagship Platform" on the homepage. Something like "SPOVIX: venue and event management software" would carry the search term.
- **Medium: weak internal linking.**
  - `/industries` links only to `/contact`. Link the Yas Marina case study and each venue type to the relevant services.
  - `/careers` has no internal links in the page body.
  - The homepage H3 about Yas Marina should link to the case study on `/industries`.
- **Low: long H3** on the homepage (the Yas Marina sentence is 22 words). Headings work better short, with the sentence as body text.

## Schema / structured data (0 / 100)

No structured data exists: the custom code slots (head and body) are all empty, and Framer adds none by default.

**Add:**

- `Organization` on every page: name, logo, URL, `sameAs` (LinkedIn), and the three offices as `address` / `location`.
- `WebSite` on the homepage.
- `Service` on each of the four service pages.
- `NewsArticle` on each news page, once news detail pages exist.
- `BreadcrumbList` on the service detail pages.

## Images (25 / 100)

Six content images were found; only one has alt text (the race-weekend photo on `/industries`).

| Page | Image | Alt text |
|---|---|---|
| / and /home | ScrollShrinkImage, image 1 | missing |
| / and /home | ScrollShrinkImage, image 2 | missing |
| / and /home | "Screen" frame | missing |
| / and /home | "Image" frame | missing |
| /industries | "Image" frame (hero area) | missing |
| /industries | Race-weekend photo | present |

Framer serves images through its CDN in modern formats, so file format is less of a concern. Alt text is the fix.

## AI search readiness (40 / 100)

**What works:** clear factual statements that AI answers can quote. Examples: "Vantlogix is the company behind SPOVIX", "SOC 2 Type 1 compliance attained, Mar 2024", "offices in Dubai, San Jose and Kochi". Named entities are consistent across pages.

**Findings**

- The default title and description ("My Framer Site / Made with Framer") would be what AI tools see first.
- No Organization schema linking Vantlogix, SPOVIX and the offices.
- No `llms.txt`. Framer can't host arbitrary root files; add one later if the site moves hosting or Framer adds support. It is a low priority.
- No dates on most content apart from the timeline and news. A "last updated" date helps freshness.

## Performance (not measured)

The site isn't published, so there are no field or lab measurements. After publishing, run PageSpeed Insights on `/`, `/services` and `/industries`. Watch the homepage's large hero and scroll-animated images, which usually decide LCP.
