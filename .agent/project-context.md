# Current project: DeepSeek Super Agent

## Purpose

Learn and explain the architecture in DeepSeek Harness's [“Exploring Super-agent Design: Towards a More Autonomous Agent System”](https://x.com/DeepSeekHarness/status/2116857257245987236). The local `DeepSeek-Super-Agent.pdf` is a machine translation of the original Chinese article. This is an independent learning project, not an official DeepSeek product.

The user wants content focused on the DeepSeek Super Agent itself. Do not include the reference presentation's company biography, marketing, courses, or unrelated demo links.

## Architecture to teach

- A long-lived router coordinates interaction and dispatches work to isolated workers.
- Incoming events can be filtered with deterministic rules and semantic judgment. Subscribed thread follow-ups can pass directly to workers; the router can still observe events for global continuity.
- Inline and spill manage limited context, while Chain of Recall follows related object references to retrieve information.
- Asynchronous operations permit new input while long work runs. Persistent state, separate execution environments, and an independent watchdog support recovery.
- The paper identifies security, privacy, scaling, long-term memory, and user interaction as open problems. Its preliminary benchmarks use synthetic workloads and do not establish real coding quality.

Treat these as the article's design ideas, not as features implemented in this repository. Verify any implementation against its code before describing behavior.

## Repository and deployment

- GitHub repository: `https://github.com/jaganzutual/Deekseek-Super-Agent`
- Default branch observed in this workspace: `master`; verify before relying on it later.
- Preferred publication: GitHub Pages.
- GitHub Pages URL: `https://jaganzutual.github.io/Deekseek-Super-Agent/`. The deck is published there via the repository workflow; verify the current deployment before reporting it as live.
- Current Peach Studio deck is in `peach-superagent-deck/dist/index.html` and was deployed separately as a private Sites preview: `https://peach-superagent-deck-jagan.jagansivam.chatgpt.site`.
- The workspace contains staged deletions from the requested reset and untracked site directories. Preserve the user's work and inspect Git status before making or committing changes.

When reusing this folder in another project, replace this file's project-specific details and verify the target repository and deployment settings.
