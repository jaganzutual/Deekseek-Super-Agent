# Contributing

Corrections to the lessons, small runnable examples, and pull requests are welcome.

1. Fork the repository and create a branch.
2. For a lesson correction, edit `learn/slides.md` or the relevant component. Keep claims about the article separate from behavior implemented here.
3. For a demo change, keep the example deterministic, local, and runnable without credentials. Update the trace with `npm run trace` and ensure the lesson matches the actual output.
4. Run `python3 -m unittest discover -s tests -v` and `npm ci && npm run build`. Preview the lesson with `npm run dev` when possible.
5. Open a pull request describing the change and how you verified it.

Please retain article attribution and do not add third-party content without checking its license.
