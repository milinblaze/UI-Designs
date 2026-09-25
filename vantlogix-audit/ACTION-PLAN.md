# Vantlogix SEO action plan

Ordered by priority. Every item can be done in Framer without code, apart from the structured data, which is pasted into Site Settings → Custom Code.

## Critical (before launch)

1. **Set the site title and description** (Site Settings → General).
   - Title: `Vantlogix | Venue & Event Management Technology`
   - Description: `Vantlogix builds SPOVIX, venue and event management software for stadiums, motorsport circuits and arenas, plus consulting, development, data and cloud services.`
2. **Set a unique title and description on every page** (Page Settings → SEO). Drafts:

   | Page | Title | Description |
   |---|---|---|
   | / | Vantlogix: Technology for Complex Venues and Live Events | The company behind SPOVIX, venue and event management software for stadiums, circuits, racecourses and arenas, plus consulting, development, data and cloud services. |
   | /about | About Vantlogix: Built by People Who Run Live Events | Founded in the UAE by operators with 20+ years of technology and motorsport experience. Offices in Dubai, San Jose and Kochi. |
   | /services | Venue Technology Services: Consulting, Development, Data, Cloud | Four standalone services for venue and event operators: digital transformation consulting, application development, BI and data analytics, and cloud. |
   | /services/digital-transformation | Digital Transformation Consulting for Venues | Assess how your venue plans, sells and delivers events, and get a roadmap to modern, connected systems. |
   | /services/application-development | Custom Application Development for Venues | Bespoke ticketing, fan engagement and operations tools, plus integrations, built around your venue's workflows. |
   | /services/data-analytics | BI & Data Analytics for Venues and Events | Turn ticketing, retail, access and finance data into forecasts and reporting your teams can act on during live events. |
   | /services/cloud-solutions | Cloud Solutions for Venues and Live Events | Cloud strategy, migration and management built for event-day demand spikes, without paying for peak capacity all year. |
   | /industries | Industries & Clients: Stadiums, Motorsport, Arenas | Venue technology for stadiums, motorsport circuits, racecourses, arenas, and conference and multi-sport venues. See how Yas Marina Circuit uses SPOVIX. |
   | /newsroom | Vantlogix Newsroom: News and Case Studies | Company announcements and case studies from the venues and events Vantlogix works with. |
   | /careers | Careers at Vantlogix | Join a small team building SPOVIX and venue technology across Dubai, San Jose and Kochi. |
   | /contact | Contact Vantlogix | Talk to the Vantlogix team about services, partnerships or press. Offices in Dubai, San Jose and Kochi. |

3. **Add Tablet (810 px) and Phone (390 px) breakpoints** to the layout template and every page, then fix any section that breaks at those widths.
4. **Remove internal notes and placeholder copy** on About, Newsroom, Careers and Contact.
5. **Delete `/home`**, or add a redirect from `/home` to `/`.
6. **Remove the duplicate H1** in the homepage hero.

## High (first week after launch)

7. **Add Organization structured data** to Site Settings → Custom Code → End of `<head>`. Fill in the logo URL and LinkedIn URL:

   ```html
   <script type="application/ld+json">
   {
     "@context": "https://schema.org",
     "@type": "Organization",
     "name": "Vantlogix",
     "url": "https://YOUR-DOMAIN",
     "logo": "https://YOUR-DOMAIN/logo.png",
     "sameAs": ["https://www.linkedin.com/company/YOUR-PAGE"],
     "address": {
       "@type": "PostalAddress",
       "streetAddress": "2728 Orchard Pkwy",
       "addressLocality": "San Jose",
       "addressRegion": "CA",
       "postalCode": "95134",
       "addressCountry": "US"
     },
     "brand": { "@type": "Brand", "name": "SPOVIX" }
   }
   </script>
   ```

8. **Add alt text** to the four homepage images and the second image on `/industries`.
9. **Publish on the custom domain**, then check `robots.txt`, `sitemap.xml` and canonical tags.
10. **Submit the sitemap** in Google Search Console and request indexing for the homepage and service pages.
11. **Set a social share image and favicon** (Site Settings → General).

## Medium (within a month)

12. **Create news detail pages** (a CMS detail page at `/newsroom/:slug`) and point "Read the announcement" to them.
13. **Expand the four service pages** to 300–500 words each: typical projects, deliverables, venue examples, and a short FAQ.
14. **Rewrite weak H1s:**
    - /industries: "Venue technology for stadiums, circuits and arenas"
    - /contact: "Contact Vantlogix"
    - /careers: "Careers at Vantlogix"
15. **Use "software" where it fits.** Example: rename the homepage H2 "Our Flagship Platform" to "SPOVIX: venue and event management software".
16. **Add internal links:**
    - /industries: from each venue type to the relevant service, and to the Yas Marina story.
    - Homepage: from the Yas Marina H3 to the case study.
    - /careers: to /about.
17. **Add Service and BreadcrumbList structured data** on the four service pages.

## Low (backlog)

18. Shorten the long homepage H3 and move the sentence into body text.
19. Hide the "Future entry" newsroom card until there is a third item.
20. After launch, run PageSpeed Insights on `/`, `/services` and `/industries` and fix LCP issues from the hero and scroll images.
