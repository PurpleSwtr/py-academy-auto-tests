import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE_FILE = ROOT / "progress.json"
SRC_DIR = ROOT / "src"


def load_state() -> dict:
    if not STATE_FILE.exists():
        return {"current": None, "log": {}}

    with open(STATE_FILE, "r", encoding="utf-8") as f:
        state = json.load(f)

    return {k.strip(): v for k, v in state.items()}


def save_state(state: dict):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)


def switch_task(task_id: str):
    state = load_state()
    try:
        state["current"] = int(task_id)
        save_state(state)
    except Exception as e:
        raise ValueError(
            f"Вы не можете создавать задачи с не целочисленными значениями! {e}"
        )
    script_path = SRC_DIR / f"{task_id}.py"

    if not script_path.exists():
        script_path.touch()

    print(f"Текущая задача: {task_id}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    switch_task(sys.argv[1].strip())
