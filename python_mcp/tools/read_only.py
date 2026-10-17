"""
#######################################################
python_mcp
read_only

Contains read-only tools to be used by agent.
#######################################################
"""

from pathlib import Path
from python_mcp.utils.constants import BLOCKED_FILES, IGNORED_FOLDERS, PROJECT_ROOT


def is_safe_path(file_path: Path) -> bool:
    """
    Make sure the file is inside the project folder.
    This is the most important safety check.
    Without this, an AI agent may try to read files outside the project.
    """
    try:
        file_path.resolve().relative_to(PROJECT_ROOT)
        return True
    except ValueError:
        return False


def list_project_files() -> str:
    """
    List all useful files in the project.
    The AI coding agent can use this before making suggestions,
    so it does not guess the folder structure.
    """
    files = []
    for path in PROJECT_ROOT.rglob("*"):
        # Skip ignored folders
        if any(folder in path.parts for folder in IGNORED_FOLDERS):
            continue
        # Only include files
        if path.is_file():
            files.append(str(path.relative_to(PROJECT_ROOT)))
    if not files:
        return "No project files found."
    return "\n".join(files)


def read_project_file(relative_file_path: str) -> str:
    """
    Read a safe text file from the project.
    Example input:
    app/main.py
    The AI coding agent cannot read files outside the project folder.
    """
    file_path = (PROJECT_ROOT / relative_file_path).resolve()
    if not is_safe_path(file_path):
        return "Blocked: file is outside the project folder."
    if file_path.name in BLOCKED_FILES:
        return "Blocked: this file may contain private data."
    if not file_path.exists():
        return "File not found."
    if not file_path.is_file():
        return "This path is not a file."
    try:
        return file_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return "This file cannot be read as normal text."


def search_notes(keyword: str) -> str:
    """
    Search my project notes.
    I keep important decisions, TODOs, and reminders in notes.md.
    This helps the AI coding agent understand why something was done.
    """
    notes_file = PROJECT_ROOT / "notes.md"
    if not notes_file.exists():
        return "notes.md not found."
    notes_text = notes_file.read_text(encoding="utf-8")
    results = []
    for line_number, line in enumerate(notes_text.splitlines(), start=1):
        if keyword.lower() in line.lower():
            results.append(f"Line {line_number}: {line}")
    if not results:
        return f"No notes found for: {keyword}"
    return "\n".join(results)
