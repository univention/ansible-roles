#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README_PATH = ROOT / "README.md"
README_IN_PATH = ROOT / "README.in"
ROLES_DIR = ROOT / "roles"


def find_role_readmes():
    return sorted(ROLES_DIR.glob("*/README.md"))


def has_content(path):
    """Check if the README has content beyond a headline."""
    with open(path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines()]
    return any(line for line in lines if line and not line.startswith("#"))


def generate_anchor(path):
    """Generate GitHub/GitLab-compatible anchor from filename path."""
    rel_path = path.relative_to(ROOT)
    anchor = str(rel_path).replace("/", "").replace(".", "").lower()
    return f"- [{path.parent.name}]({rel_path.as_posix()}#{anchor})"


def read_head(path) -> str:
    """Read a specific path and return ist contents"""
    content = ""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    return content


def combine_readmes():
    role_readmes = find_role_readmes()
    with open(README_PATH, "w", encoding="utf-8") as out:
        out.write(read_head(README_IN_PATH))
        out.write("\n## Modules\n")
        # Table of modules
        for path in role_readmes:
            if has_content(path):
                out.write(generate_anchor(path) + "\n")

        # Full content
        for path in role_readmes:
            if has_content(path):
                out.write("\n---\n\n")
                out.write(f"### {path.parent.name}\n")
                with open(path, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    # Skip the first line if it's a heading
                    if lines and lines[0].lstrip().startswith("#"):
                        lines = lines[1:]
                    out.writelines(lines)


if __name__ == "__main__":
    combine_readmes()
