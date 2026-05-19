import json
from pathlib import Path

import pytest

from .tests_all import run_task, test_tasks

ROOT = Path(__file__).resolve().parent.parent
progress = json.loads((ROOT / "progress.json").read_text())

current_task = next(str(v) for k, v in progress.items() if k.strip() == "current")

current_tests = [t for t in test_tasks if str(t[0]) == current_task]


@pytest.mark.parametrize("task_id, input_data, expected", current_tests)
def test_current(task_id, input_data, expected):
    assert run_task(task_id, input_data) == expected
