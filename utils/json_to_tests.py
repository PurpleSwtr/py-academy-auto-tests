import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def json_to_test_files(json_path: str):
    json_file = Path(json_path)
    if not json_file.exists():
        raise FileNotFoundError(f"файл {json_path} не найден.")

    with open(json_file, "r", encoding="utf-8") as f:
        tests = json.load(f)

    task_id = json_file.stem

    input_dir = ROOT / "src" / "input" / task_id
    output_dir = ROOT / "src" / "output" / task_id

    input_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)

    for i, test in enumerate(tests, start=1):
        expected_text = test.get("expected") or test.get("output", "")
        input_text = test.get("input", "")

        (input_dir / f"{i}.txt").write_text(input_text, encoding="utf-8")
        (output_dir / f"{i}.txt").write_text(expected_text, encoding="utf-8")


if __name__ == "__main__":
    raw_folder = Path(__file__).parent / "raw_test_cases"
    for jf in raw_folder.glob("*.json"):
        try:
            json_to_test_files(str(jf))
        except Exception as e:
            print(f"{e}")
    print("новые тесты добавлены")
