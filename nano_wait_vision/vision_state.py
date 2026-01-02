from dataclasses import dataclass
from typing import Optional


@dataclass
class VisionState:
    name: str
    detected: bool
    confidence: float = 0.0
    text: Optional[str] = None
    icon: Optional[str] = None

    def __bool__(self):
        return self.detected
