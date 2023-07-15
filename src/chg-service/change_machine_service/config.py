import os
from typing import Any


def get_config(env: dict[str, Any] | None = None) -> dict[str, Any]:
    env = env or dict(os.environ)
    return {
        "CHG_ALGORITHM": env.get("CHG_ALGORITHM", "greedy"),
    }
