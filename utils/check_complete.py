import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UTILS = ROOT / "utils"
STATE = ROOT / "progress.json"


def check_complete() -> bool:
    state = json.loads(STATE.read_text())
    tasks = state["log"]

    current_task = str(state["current"])

    if current_task in tasks:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    check_complete()
