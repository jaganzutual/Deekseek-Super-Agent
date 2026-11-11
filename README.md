# DeepSeek Super Agent

Interactive slides explaining the architecture in DeepSeek Harness's “Exploring Super-agent Design: Towards a More Autonomous Agent System.”

**Open the slides:** https://jaganzutual.github.io/Deekseek-Super-Agent/

## Structure

- `public/index.html` — the deck shell: styles, navigation, notes, and overview.
- `public/slides/` — one HTML file per slide, named `topic-NN.html`. The order is listed in `slideFiles` inside `index.html`.
- `.github/workflows/pages.yml` — publishes `public/` to GitHub Pages on every push to `master`.

Each slide file is a fragment: a `.slide-data` section holding the kicker, title, body markup, and speaker notes. The shell fetches the files and renders the active one.

## Preview locally

The slides are fetched at runtime, so open them over HTTP rather than double-clicking the file:

```bash
cd public
python3 -m http.server 8000
```

Then visit `http://localhost:8000/`.

This is an independent learning project, not an official DeepSeek product.
