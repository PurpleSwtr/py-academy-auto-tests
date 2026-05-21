import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
UTILS = ROOT / "utils"


def pytest_terminal_summary(terminalreporter, exitstatus):
    all_reports = (
        terminalreporter.stats.get("passed", [])
        + terminalreporter.stats.get("failed", [])
        + terminalreporter.stats.get("skipped", [])
    )

    test_files = {
        str(report.fspath) for report in all_reports if hasattr(report, "fspath")
    }

    passed_tests = len(terminalreporter.stats.get("passed", []))
    failed_tests = len(terminalreporter.stats.get("failed", []))

    if (
        passed_tests > 0
        and failed_tests == 0
        and exitstatus == 0
        and "tests/tests_one.py" in test_files
    ):
        result = subprocess.run([sys.executable, str(UTILS / "check_complete.py")])
        is_test_complete = result.returncode == 0
        if not is_test_complete:
            print("\nВсе тесты прошли успешно! Файл прогресса обновлён")
            subprocess.run([sys.executable, str(UTILS / "complete.py")])
