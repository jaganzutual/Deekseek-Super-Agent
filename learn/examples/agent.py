"""A deterministic teaching agent: one scripted model and one read-only tool."""
from pathlib import Path

NOTE = Path(__file__).with_name("project_note.txt")
TASK = "Read this local project note and summarize it."


def read_project_note():
    """Read only the bundled note, not an arbitrary path supplied by a model."""
    return NOTE.read_text(encoding="utf-8").strip()


def dispatch_tool(name):
    if name != "read_project_note":
        raise ValueError(f"Unknown tool: {name}")
    return read_project_note()


def scripted_model(history):
    """Request a tool first; then summarize the tool result without an LLM."""
    if history[-1]["role"] == "user":
        return {"type": "tool_call", "name": "read_project_note"}
    if history[-1]["role"] == "tool":
        return {"type": "final", "content": "Summary: " + history[-1]["content"]}
    raise ValueError("Unexpected conversation state")


def run():
    """Return the answer and the actual trace. The loop owns message history."""
    history = [{"role": "user", "content": TASK}]
    trace = []

    def record(title, active, input_text, output_text, change, code):
        trace.append({"title": title, "active": active, "input": input_text,
                      "output": output_text, "state": change, "code": code})

    record("The user submits a task", "user", TASK, "A user message", "History: user message", "run")
    record("The loop sends context to the model", "loop", "History: user message", "Model receives 1 message", "History unchanged", "run")
    for _ in range(4):
        response = scripted_model(history)
        if response["type"] == "tool_call":
            history.append({"role": "assistant", "content": "Call " + response["name"]})
            record("The model requests a tool", "model", "User message", "Call read_project_note", "History: user + assistant request", "scripted_model")
            result = dispatch_tool(response["name"])
            record("The dispatcher reads the note", "tool", "read_project_note", result, "History unchanged; result returned to loop", "dispatch_tool")
            history.append({"role": "tool", "content": result})
            record("The loop records the result", "loop", result, "Tool message added", "History: user + assistant request + tool result", "run")
        elif response["type"] == "final":
            history.append({"role": "assistant", "content": response["content"]})
            record("The model answers with updated context", "model", "History including tool result", response["content"], "History: 4 messages; run ends on final answer", "scripted_model")
            return response["content"], trace
        else:
            raise ValueError("Unknown model response")
    raise RuntimeError("Model did not finish within 4 steps")


if __name__ == "__main__":
    answer, events = run()
    for index, event in enumerate(events, 1):
        print(f"{index}. {event['title']}: {event['output']}")
    print("\n" + answer)
