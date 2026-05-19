import subprocess
import sys
from pathlib import Path

import pytest

from utils.parse_tasks import INPUT_MAP, OUTPUT_MAP, SCRIPTS

ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT / "src"


def run_task(task_id: int, input_text: str) -> str:
    script_path = SRC_DIR / f"{task_id}.py"
    if not script_path.exists():
        raise FileNotFoundError(f"файл {script_path} не найден")

    result = subprocess.run(
        [sys.executable, str(script_path)],
        input=input_text,
        text=True,
        capture_output=True,
        timeout=10,
    )

    if result.returncode != 0:
        raise RuntimeError(f"задача {task_id} упала:\n{result.stderr}")

    return result.stdout.strip()


test_tasks = []
for task_id in SCRIPTS:
    if task_id in INPUT_MAP:
        for case_id in INPUT_MAP[task_id]:
            if case_id in OUTPUT_MAP.get(task_id, {}):
                test_tasks.append(
                    (
                        task_id,
                        INPUT_MAP[task_id][case_id],
                        OUTPUT_MAP[task_id][case_id],
                    )
                )


@pytest.mark.parametrize("task_id, input_data, expected", test_tasks)
def test_all(task_id, input_data, expected):
    assert run_task(task_id, input_data) == expected
