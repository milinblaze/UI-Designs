# Vantlogix — brag plan

## Planning rubric

1. **What is it?** Vantlogix: the company behind SPOVIX, a venue and event management platform, plus four consulting and engineering services for complex venues.
2. **Who is it for?** Operators of stadiums, motorsport circuits, racecourses, arenas, and conference and multi-sport venues.
3. **What's the one-line claim?** "We build technology for complex venues and live events." (site H1)
4. **What makes it specific?** Built close to motorsport, not adapted for it. Race-weekend demand spikes, accreditation, and ancillary services are the conditions it was built inside.
5. **Best proof?** Yas Marina Circuit runs SPOVIX across race weekends. SOC 2 Type 1. Offices in Dubai, San Jose and Kochi.
6. **What visuals exist?** Race-weekend operations photo; the site's motorsport section; the site's four-service card grid.
7. **Tone?** Calm corporate: measured narration, soft ambient music, smooth eases, dark navy with one accent blue.
8. **Format?** Landscape 1920×1080, 25.8 s, 30 fps.
9. **Hook?** A race-weekend clock ticking toward lights-out, with the site's own list of pressures stacking up.

## Creative angle

Race weekend is the stress test. Open inside that pressure, then reveal the company built for it.
All on-screen copy comes from the live site. No invented numbers.

## Storyboard (25.8 s)

| # | Time | Scene | On-screen text | Motion / transition |
|---|------|-------|----------------|---------------------|
| 1 | 0.0–3.4 | **Hook**: navy field, race-control grid lines, a big timing readout "RACE WEEKEND" | "Race weekend." then three stacked pressure chips: "Demand spikes" / "Accreditation" / "Ancillary services" | Title slams in, chips stagger from the right, hairline rule sweeps across. Hard cut out. |
| 2 | 3.4–8.2 | **Reveal**: race-ops photo, slow push-in, navy gradient on left | "Vantlogix" wordmark, then H1 "We build technology for complex venues and live events" | Photo scales 1.12 to 1.0; wordmark rises, H1 lines mask up. |
| 3 | 8.2–12.4 | **Highlight 1, the platform**: SPOVIX lockup plus venue-type ticker | "SPOVIX", "A modular venue and event management system", ticker: Stadiums · Motorsport venues · Racecourses · Arenas · Conference & exhibition centres · Multi-sport complexes | Lockup scales in; ticker scrolls continuously under it. |
| 4 | 12.4–17.1 | **Highlight 2, show the thing**: the site's service grid floating in perspective | "Four services, each standalone" (from the UI itself) plus side label "Consulting · Development · Data · Cloud" | UI panel flies up with slight tilt, settles flat; label wipes in. |
| 5 | 17.1–21.4 | **Highlight 3, proof**: the site's motorsport section with the race photo in place | "Built close to motorsport, not adapted for it" (from the UI), proof strip: "Yas Marina Circuit · SOC 2 Type 1 · UAE · India · Middle East · US" | UI slides in from right; proof chips count in one by one. |
| 6 | 21.4–25.8 | **Outro**: navy, big wordmark | "Ready to see what Vantlogix can do for your venue?" plus a "Talk to our team" button | Question fades up, button pops, accent glow breathes. Holds to end. |

## Audio

All audio is pre-mixed into `composition/assets/audio/mix.wav` (−14 LUFS).

**Voiceover:** ElevenLabs `eleven_multilingual_v2`, preset voice Alice (`Xb7hH8MSUJpSbSDYk0k2`, British female), stability 0.6, similarity 0.8, style 0.15, natural speed. Each line starts 0.3 s into its scene. The API key is read from `ELEVENLABS_API_KEY` and is never stored in this repo.

| Scene | Line |
|---|---|
| 1 | On race weekend, every system is tested. |
| 2 | Vantlogix builds technology for complex venues and live events. (sent to TTS as "Vantlogics" so it is said like "logics"; starts at 3.6 s) |
| 3 | Including SPOVIX, our venue and event management platform. |
| 4 | Alongside consulting, engineering, data and cloud services. |
| 5 | Built close to motorsport, and proven at Yas Marina Circuit. |
| 6 | Talk to our team about your venue. |

**Music:** original ambient bed synthesised by `assets/audio/make_music.py`: 90 BPM, C major (Fmaj7–C/E–Am7–G), soft pads, gentle plucked arpeggio, sub bass, no drums. Ducked gently under the voice.

**SFX:** one soft chime as the outro lands.
