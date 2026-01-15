from .vision import VisionMode
from .vision_state import VisionState

# Default global instance (plug-and-play)
vision = VisionMode()

# High-level QA-friendly aliases
wait_text = vision.wait_text
wait_icon = vision.wait_icon
observe = vision.observe

__all__ = [
    "VisionMode",
    "VisionState",
    "vision",
    "wait_text",
    "wait_icon",
    "observe",
]
