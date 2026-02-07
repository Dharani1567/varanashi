import json
from datetime import datetime
from pathlib import Path

MEMORY_FILE = Path("memory/refused_posts.json")


def save_refusal(content, reason, agent):
    """
    Save refused content into memory.
    """

    if not MEMORY_FILE.exists():
        MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)
        MEMORY_FILE.write_text("[]")

    with open(MEMORY_FILE, "r") as f:
        data = json.load(f)

    data.append({
        "content": content,
        "reason": reason,
        "agent": agent,
        "timestamp": datetime.utcnow().isoformat()
    })

    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)


def check_memory(content):
    """
    Check if similar content was refused before.
    """

    if not MEMORY_FILE.exists():
        return False, ""

    with open(MEMORY_FILE, "r") as f:
        data = json.load(f)

    content_lower = content.lower()

    for record in data:
        if record["content"].lower() in content_lower:
            return True, record["reason"]

    return False, ""

