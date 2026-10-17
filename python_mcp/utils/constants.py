"""
#######################################################
python_mcp
constants

Contains constants to be used in python_mcp project.
#######################################################
"""

from pathlib import Path

# Fixed project folder
# Change this to your own project folder name
PROJECT_ROOT = Path("python-cli-chatbot").resolve()
# Folders that are not useful for the AI coding agent
# These can be huge, noisy, or unnecessary
IGNORED_FOLDERS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    "node_modules",
    "dist",
    "build",
}
# Files I never want the AI coding agent to read
# These may contain API keys, passwords, or private data
BLOCKED_FILES = {".env", "secrets.json", "credentials.json"}
