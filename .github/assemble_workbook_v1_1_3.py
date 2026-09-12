from __future__ import annotations

import hashlib
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "downloads/paper-writing-agent-v1.1.3.zip"
TARGET = ROOT / "paper-writing-agent/skills/journal-if-lookup/data/2025IF.xlsx"
MEMBER = "paper-writing-agent/skills/journal-if-lookup/data/2025IF.xlsx"
EXPECTED_SIZE = 9_785_182
EXPECTED_SHA = "a1283b9f4fceb8afc51d05b8001aee35322a45ba657dfd0ec9fdd69fa16cd3ec"


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            hasher.update(block)
    return hasher.hexdigest()


with zipfile.ZipFile(ARCHIVE) as archive:
    data = archive.read(MEMBER)
temporary = TARGET.with_name(TARGET.name + ".tmp")
temporary.write_bytes(data)
actual_sha = digest(temporary)
if len(data) != EXPECTED_SIZE or actual_sha != EXPECTED_SHA:
    temporary.unlink(missing_ok=True)
    raise RuntimeError(
        f"Workbook verification failed: expected {EXPECTED_SIZE} bytes/{EXPECTED_SHA}, "
        f"got {len(data)} bytes/{actual_sha}"
    )
temporary.replace(TARGET)

workflow = ROOT / ".github/workflows/assemble-workbook-v1.1.3.yml"
helper = ROOT / ".github/assemble_workbook_v1_1_3.py"
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
