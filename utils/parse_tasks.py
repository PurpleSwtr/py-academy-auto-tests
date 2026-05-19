from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SRC_DIR = ROOT / "src"
INPUT_DIR = SRC_DIR / "input"
OUTPUT_DIR = SRC_DIR / "output"

_INPUT_DATA = []
_OUTPUT_DATA = []
SCRIPTS = ()


def get_files_from_dir(path: Path) -> list:
    res = []
    for dir_path in path.iterdir():
        for file_path in dir_path.iterdir():
            if file_path.is_file():
                try:
                    with open(file_path, "r", encoding="utf-8") as file:
                        content = file.read()
                        res.append((dir_path.name, file_path.stem, content))
                except Exception as e:
                    print(e)
    return res


def group_by_task(raw_data: list) -> dict:
    result = {}
    for task_id, case_id, content in raw_data:
        result.setdefault(task_id, {})[case_id] = content.strip()
    return result


_INPUT_DATA = get_files_from_dir(INPUT_DIR)
_OUTPUT_DATA = get_files_from_dir(OUTPUT_DIR)
SCRIPTS = list(
    file_path.stem
    for file_path in SRC_DIR.iterdir()
    if file_path.suffix == ".py" and file_path.stem != "__init__"
)
INPUT_MAP = group_by_task(_INPUT_DATA)
OUTPUT_MAP = group_by_task(_OUTPUT_DATA)
