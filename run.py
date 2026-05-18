import os
import subprocess

TASK = os.getenv("TASK")

with open("input.txt", "r", encoding="utf-8") as file:
    task_input = file.read()

if __name__ == "__main__":
    subprocess.run(f"python {TASK}.py < {task_input}")
