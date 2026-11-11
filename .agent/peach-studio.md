# Peach Studio design system

The selected theme is a calm butter-and-sky pastel theme for technical education. Keep the content legible and calm: light backgrounds, substantial whitespace, clear diagrams, dark readable text, and a small number of butter-yellow and pastel-blue accents.

## Color tokens

These values describe the current presentation and are the starting point for future work:

| Role | Color | Hex | Use |
| --- | --- | --- | --- |
| Background | Cloud | `#F8F7F2` | Main slide or page background |
| Surface | Soft white | `#FFFFFC` | Cards, diagram nodes, notes, controls |
| Primary pastel | Butter yellow | `#F2E1AD` | Highlights, selected states, key diagram nodes |
| Secondary pastel | Sky blue | `#CEDFEA` | Illustrations, secondary diagram nodes |
| Main text | Deep slate | `#353344` | Headings, body, important labels |
| Muted text | Muted gray | `#767387` | Supporting labels and metadata; check contrast |
| Border | Soft line | `#DDDCD2` | Subtle dividers and card outlines |
| Soft panel | Pale yellow | `#F2E1AD` | Gentle background emphasis |
| Emphasis text | Muted olive-brown | `#62572F` | Sparse headline emphasis; check contrast |

The user requested pastel colors for the visual palette. Use dark neutral text where needed for readable contrast; avoid placing small pastel-colored text on a light pastel background. Test actual text and interactive-state contrast, particularly muted text and the olive-brown accent, and darken a color when necessary.

```css
:root {
  --bg: #F8F7F2;
  --surface: #FFFFFC;
  --accent: #F2E1AD;
  --sage: #CEDFEA;
  --ink: #353344;
  --muted: #f3db04;
  --line: #DDDCD2;
  --light: #F2E1AD;
}
```

## Typography

- **Display:** Libre Baskerville, with Georgia or another readable serif as fallback. Use selectively for opening titles and takeaways.
- **Body and UI:** Inter, with Arial or another sans-serif fallback. Use for most slide headings, explanations, buttons, and diagrams. The font selections approximate the user's visual references; the original font names are unknown.
- **Technical labels:** DM Mono, with a monospace fallback. Use sparingly for navigation, identifiers, or metadata.
- On a 1600 × 900 reference slide, the current deck uses roughly 105 px for the opening title, 65 px for slide titles, 25–27 px for body text, and 13–16 px for metadata. Treat these as reference sizes, not fixed screen CSS on every device; adjust for responsiveness and ensure readability.

## Visual principles

- Use one main idea per screen. Establish a clear visual order: title, main diagram or explanation, supporting detail.
- Keep backgrounds mostly cloud white, with soft white surfaces. Reserve butter yellow and sky blue for meaningful emphasis.
- Give components consistent roles: butter yellow for the current or important item, sky blue for a secondary concept, neutral surfaces for the rest. Pair color with labels or shape so color is not the only signal.
- Use a soft butter-yellow and blue glow near the edges of the otherwise light background, with a very subtle dot texture when it suits the slide. Prefer centered headings and spacious white cards for key ideas, following the user's image references.
- Use simple illustrations, flows, or diagrams when they explain the content. Avoid decorative charts that imply measurements.
- Prefer subtle borders and modest corner radii. Keep spacing generous and avoid visual clutter.
- Provide visible keyboard focus, responsive layouts, and reduced-motion support.
