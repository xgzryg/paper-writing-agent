from __future__ import annotations

import hashlib
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ASSETS = [
    (
        ROOT / "paper-writing-agent/skills/journal-if-lookup/data/journals_index.json",
        ROOT / ".release-parts/v1.1.3/journals_index",
        30_531_585,
        "bf53e64ff4835a8742a75a8057c87b5b4967dd0158400a43e7b302a0cd705788",
    ),
    (
        ROOT / "downloads/paper-writing-agent-v1.1.3.zip",
        ROOT / ".release-parts/v1.1.3/zip",
        24_562_133,
        "065bbe16996853eccd82886f9f9943a7ed4a27521d4a2d617cca257e86cb9b33",
    ),
]


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            hasher.update(block)
    return hasher.hexdigest()


def assemble(target: Path, part_dir: Path, expected_size: int, expected_sha: str) -> None:
    parts = sorted(part_dir.glob("part-*"))
    if not parts:
        raise RuntimeError(f"No release parts found in {part_dir}")
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary = target.with_name(target.name + ".tmp")
    with temporary.open("wb") as output:
        for part in parts:
            with part.open("rb") as source:
                shutil.copyfileobj(source, output, 1024 * 1024)
    actual_size = temporary.stat().st_size
    actual_sha = digest(temporary)
    if actual_size != expected_size or actual_sha != expected_sha:
        temporary.unlink(missing_ok=True)
        raise RuntimeError(
            f"{target}: expected {expected_size} bytes/{expected_sha}, "
            f"got {actual_size} bytes/{actual_sha}"
        )
    temporary.replace(target)


for target, part_dir, expected_size, expected_sha in ASSETS:
    assemble(target, part_dir, expected_size, expected_sha)

shutil.rmtree(ROOT / ".release-parts")
workflow = ROOT / ".github/workflows/assemble-v1.1.3.yml"
helper = ROOT / ".github/assemble_v1_1_3.py"
workflow.unlink(missing_ok=True)
helper.unlink(missing_ok=True)
try:
    workflow.parent.rmdir()
except OSError:
    pass
try:
    helper.parent.rmdir()
except OSError:
    pass
