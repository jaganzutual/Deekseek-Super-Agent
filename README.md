# Deekseek Super Agent

A forkable learning project exploring the ideas in DeepSeek Harness’s [“Exploring Super-agent Design”](https://x.com/DeepSeekHarness/status/2116857257245987236). Start with one small, deterministic agent loop, then explore how the paper extends agent systems to concurrent workers and event-driven operation.

- **Start learning:** [Open the GitHub Pages lesson](https://jaganzutual.github.io/Deekseek-Super-Agent/) (available once Pages deployment succeeds).
- **Run the demo:** [Set up and run the Python example](#run-the-demo).
- **Fork and remix:** [Publish your own learning site](#fork-and-publish).

This is an independent educational project, not an official DeepSeek product. The paper describes architectural ideas; the code here implements only a small teaching example, not the paper’s full super-agent.

## Run the demo

Requirements: Python 3.9 or newer. No API key or Python packages are needed.

```bash
python3 learn/examples/agent.py
```

The scripted model asks the dispatcher to read a fixed local note. The agent loop adds the returned text to its in-memory history and calls the model again. The model then returns a final answer. It simply prefixes the note with `Summary:`; it does not perform real language-model summarization.

Example final output:

```text
Summary: The project explores how an agent can use tools to answer questions.
```

Run the focused checks with `python3 -m unittest discover -s tests -v`. To experiment, edit `learn/examples/project_note.txt`, predict what the model will receive, and rerun the demo.

## Preview and edit the lessons

Requirements: Node.js 22 and npm, plus Python 3.9 or newer.

```bash
npm ci
npm run trace
npm run dev
```

Open the address printed by Slidev. The deck has three screens; arrow keys navigate between screens, and the walkthrough has its own buttons. Speaker notes are included in the Markdown. Build the static site with:

```bash
npm run build
```

- Edit lesson content and speaker notes in [`learn/slides.md`](learn/slides.md).
- Edit the interactive walkthrough in [`learn/components/Walkthrough.vue`](learn/components/Walkthrough.vue), the component diagram in [`learn/components/Boundaries.vue`](learn/components/Boundaries.vue), and visual styles in [`learn/style.css`](learn/style.css).
- Change the demo in [`learn/examples/agent.py`](learn/examples/agent.py) and its note in [`learn/examples/project_note.txt`](learn/examples/project_note.txt).
- `npm run trace` regenerates [`learn/public/trace.json`](learn/public/trace.json) from the Python run. The production build regenerates it automatically. Commit updated trace data when changing the demo or note.
- Read [`ARCHITECTURE.md`](ARCHITECTURE.md) for the larger proposed system. It is a design discussion, not a list of implemented features.

## Fork and publish

1. Fork this repository on GitHub.
2. Enable Actions in the fork if GitHub prompts you.
3. In the fork, open **Settings → Pages** and choose **GitHub Actions** as the source.
4. Run **Deploy learning site** from the Actions tab, or push to your fork’s default branch.
5. Open the Pages URL reported by the deployment. A project site normally uses `https://<owner>.github.io/<repository>/`.
6. Edit a lesson or the project note, rerun the demo and `npm run trace`, and push to update your site.

The workflow derives the Pages base path from the deployment configuration and source links from the repository running the workflow. A fork deploys to its own Pages site and links to its own code. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for how to contribute changes.

## Source and attribution

The architecture is inspired by DeepSeek Harness, [“Exploring Super-agent Design: Towards a More Autonomous Agent System”](https://x.com/DeepSeekHarness/status/2116857257245987236), particularly sections 2–4. The included [`DeepSeek-Super-Agent.pdf`](DeepSeek-Super-Agent.pdf) is a machine translation of the original Chinese article. The article’s router, concurrent workers, event subscriptions, persistent state, and watchdog are broader than the single local loop demonstrated here.

This repository currently has **no license**. MIT is a reasonable choice for original project code and learning materials, subject to the owner’s decision. The article and third-party dependencies retain their own rights and licenses.
