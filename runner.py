import subprocess
from pathlib import Path

folder = Path(__file__).parent

for file in sorted(folder.glob("*.py")):
    if file.name == "runner.py":
        continue

    print(f"\n{folder}>python {file.name}")
    subprocess.run(["python", str(file)])