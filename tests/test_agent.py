import importlib.util
import unittest
from unittest.mock import patch
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "learn/examples/agent.py"
spec = importlib.util.spec_from_file_location("agent", path)
agent = importlib.util.module_from_spec(spec)
spec.loader.exec_module(agent)


class AgentTest(unittest.TestCase):
    def test_tool_result_reaches_second_model_call(self):
        with patch.object(agent, "read_project_note", return_value="A different note."):
            answer, trace = agent.run()
        self.assertEqual(answer, "Summary: A different note.")
        self.assertEqual(trace[3]["output"], "A different note.")
        self.assertEqual(trace[4]["input"], trace[3]["output"])
        self.assertIn("tool result", trace[5]["input"])

    def test_rejects_unknown_tool(self):
        with self.assertRaises(ValueError):
            agent.dispatch_tool("write_file")


if __name__ == "__main__":
    unittest.main()
