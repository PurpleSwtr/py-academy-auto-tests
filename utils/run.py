import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / "progress.json"
INPUT = ROOT / "input.txt"

state = json.loads(STATE.read_text())

task = state["current"]
script = ROOT / "src" / f"{task}.py"

if not script.exists():
    raise FileNotFoundError(f"нет файла {task}.py")

input_text = INPUT.read_text(encoding="utf-8") if INPUT.exists() else ""
subprocess.run([sys.executable, str(script)], input=input_text, text=True)
