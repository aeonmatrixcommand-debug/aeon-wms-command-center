from dataclasses import dataclass
from typing import Any

@dataclass
class Event:
    name: str
    source: str
    payload: Any
