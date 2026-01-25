from .vision import VisionMode
from .vision_state import VisionState
from .selenium_adapter import VisionWait  # Adapter sem Selenium

# Instância global pronta para uso (plug-and-play)
vision = VisionMode()

# Aliases de alto nível (QA-friendly)
wait_text = vision.wait_text
wait_icon = vision.wait_icon
observe = vision.observe

__all__ = [
    "VisionMode",
    "VisionState",
    "VisionWait",  # Adapter plug-and-play sem Selenium
    "vision",
    "wait_text",
    "wait_icon",
    "observe",
]
