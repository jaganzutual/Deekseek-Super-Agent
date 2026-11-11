# Full-screen presentation guide

## Intended output

Create a self-contained technical lesson that works as a full-screen slideshow and can also be read at the user's own pace. The content must be accurate for the current project; use original explanations and attribute sources. Do not add company biographies, promotions, courses, or unrelated demo links unless requested.

The reference for pacing and layout is [the compact Super Agent deck](https://superagent-webinar-compact.vercel.app/#2). Use it for the presentation format and information hierarchy; adapt content and visuals to the current project and Peach Studio rather than copying unrelated branding.

## Composition

- Design a 16:9 presentation with a large title, a large visual or concise explanation, a small section label, and a slide number.
- Present one main idea per slide. Use different layouts where useful: opening slide, simple columns, diagrams, comparison rows, and key takeaways.
- Keep copy short enough to explain aloud. Put extra context in speaker notes instead of overcrowding slides.
- Prefer slide-specific diagrams and original illustrations. The current deck uses simple CSS shapes in butter yellow, pastel blue, and soft white; imagery should support the topic rather than decorate it.
- Include a source link where the lesson makes article-based claims. Clearly separate source claims, illustrative examples, and implemented behavior.

## Interaction

- Offer Previous and Next controls and keyboard navigation with left/right arrows. Provide visible progress or slide numbers.
- Support a slide overview, speaker notes, and full-screen mode when appropriate. Make direct slide links work via the URL hash.
- Progressive reveals may show one idea at a time. Clearly indicate how to advance; support going back through reveals.
- Use native buttons, accessible labels, visible focus, and reduced motion. Do not let shortcuts interfere with form fields or focused controls.
- On narrow screens, reflow content, keep controls usable, and allow scrolling when a slide exceeds the viewport. Do not assume a scaled desktop canvas is readable on a phone.

## Implementation and verification

The existing Peach Studio prototype is a static HTML, CSS, and JavaScript presentation at `peach-superagent-deck/dist/index.html` in this workspace. It has 25 slides, hash navigation, section navigation, notes, overview, and progressive reveals. It was published separately as a private Sites preview; its browser layout was not visually verified because browser access was unavailable.

Use a static build when that is sufficient; use the destination project's existing framework and package manager if already established. Avoid adding dependencies only to reproduce the theme.

Before delivery, verify the actual project build, every slide and direct link, first/last navigation boundaries, reveal order, notes, keyboard controls, focus states, and full-screen behavior. Check a desktop presentation size and narrow screens, and confirm no text clips or overlaps. If browser testing is unavailable, report that limitation rather than claiming visual verification.
