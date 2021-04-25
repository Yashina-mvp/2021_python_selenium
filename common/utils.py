"""Common utils for the proyect."""
from pathlib import Path


def get_project_root() -> Path:
    """Get project root path."""
    # Path: /Users/yashg/2021_python_selenium/common/utils.py
    return Path(__file__).parent.parent
