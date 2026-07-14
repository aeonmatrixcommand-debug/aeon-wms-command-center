from pathlib import Path

PROMPT_DIR = Path("prompts")

def load_prompt(name: str):
    path = PROMPT_DIR / f"{name}.prompt.yml"
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")
