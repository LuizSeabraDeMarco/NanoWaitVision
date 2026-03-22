from .vision import VisionMode
from .vision_state import VisionState
from .selenium_adapter import VisionWait

# Instância global
vision = VisionMode()

# Aliases simples (🔥 UX)
wait_text = vision.wait_text
wait_icon = vision.wait_icon
observe = vision.observe

def wait_for(target, timeout=10):
    if target.endswith(".png"):
        return vision.wait_icon(target, timeout=timeout)
    return vision.wait_text(target, timeout=timeout)

__all__ = [
    "VisionMode",
    "VisionState",
    "VisionWait",
    "vision",
    "wait_text",
    "wait_icon",
    "observe",
    "wait_for"
]