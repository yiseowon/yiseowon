import json
import re

with open("todo/todo.json") as f:
    items = json.load(f)

if items:
    lines = [f"- [{'x' if item['done'] else ' '}] {item['text']}" for item in items]
else:
    lines = ["_nothing on the list right now_"]

block = "\n".join(lines)

with open("README.md") as f:
    readme = f.read()

updated = re.sub(
    r"<!-- TODO:START -->.*<!-- TODO:END -->",
    f"<!-- TODO:START -->\n{block}\n<!-- TODO:END -->",
    readme,
    flags=re.DOTALL,
)

with open("README.md", "w") as f:
    f.write(updated)
