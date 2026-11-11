# GitHub Pages deployment guide

GitHub Pages is the preferred deployment target for the current DeepSeek Super Agent project. Publishing requires authorization and repository access; do not claim a live deployment until the workflow and public URL have been checked.

## Static-site checklist

1. Keep source files and any required build configuration in the GitHub repository. Use the existing framework when present; a static HTML site may need no build step.
2. Generate a static output directory such as `dist/` containing `index.html` and all required assets. Do not assume a local preview proves production behavior.
3. Add a GitHub Actions workflow using `actions/configure-pages`, `actions/upload-pages-artifact`, and `actions/deploy-pages`, with the permissions required for Pages deployment.
4. Trigger the workflow for pushes to the repository's default branch and allow manual execution. Set the repository's **Settings → Pages → Source** to **GitHub Actions**.
5. Derive the base path from Pages configuration, and derive source links from the repository and default branch running the workflow. A project site generally lives under `/<repository-name>/`; a user or organization site can use `/`. Do not hardcode another project's owner or repository name into a reusable template.
6. Use hash-based slide links or configure an appropriate static-site fallback so direct slide links work on GitHub Pages.
7. Test a production build with the intended base path, then with a different owner and repository name. Verify index and assets, direct links, workflow status, and the live site after deployment.

For forks: fork the repo, enable Actions if prompted, select GitHub Actions as the Pages source, then run the deployment workflow or push to the fork's default branch. Use the Pages URL shown by that workflow. Each fork should publish to its own site and link to its own source.

The current repository serves the static deck from `public/` using `.github/workflows/pages.yml`. Keep the Pages workflow and the deck source in sync.
