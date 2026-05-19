import json
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / "progress.json"

state = json.loads(STATE.read_text())
task = state["current"]

state["log"][str(task)] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
state["current"] += 1

# Не очень полезная функция
# (ROOT / "src" / f"{state['current']}.py").touch()

STATE.write_text(json.dumps(state, indent=2, ensure_ascii=False))
