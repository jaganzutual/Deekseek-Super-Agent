"""Generate the site's walkthrough from the same code as the CLI demo."""
import json
from pathlib import Path
from agent import run

_, trace = run()
target = Path(__file__).parents[1] / "public" / "trace.json"
target.write_text(json.dumps(trace, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"Wrote {target}")
