import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UTILS = ROOT / "utils"
RAW_TESTS = UTILS / "raw_test_cases"
SRC_DIR = ROOT / "src"


def add_task_tests(task: int, raw_data: str):
    file_path = RAW_TESTS / f"{task}.json"

    if isinstance(raw_data, str):
        data = json.loads(raw_data)
    else:
        data = raw_data

    file_path.write_text(
        json.dumps(data, indent=4, ensure_ascii=False), encoding="utf-8"
    )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    try:
        name = int(sys.argv[1].strip())
    except Exception as e:
        raise ValueError(
            f"Вы не можете создавать задачи с не целочисленными значениями! {e}"
        )
    add_task_tests(name, sys.argv[2].strip())
    subprocess.run([sys.executable, UTILS / "json_to_tests.py"])
    subprocess.run([sys.executable, UTILS / "switch_task.py", str(name), sys.argv[3]])
