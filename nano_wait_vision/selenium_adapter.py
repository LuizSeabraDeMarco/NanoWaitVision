from .vision import VisionMode
from .vision_state import VisionState

class VisionWait:
    """
    Selenium-like visual wait adapter (sem Selenium, apenas GUI-agnóstico).

    Exemplo de uso:
        wait = VisionWait(timeout=15)
        wait.until_text("Dashboard")
    """

    def __init__(self, timeout: float = 10.0, verbose: bool = False):
        self.timeout = timeout
        self.vision = VisionMode(verbose=verbose)

    def until_text(self, text: str) -> VisionState:
        return self.vision.wait_text(text, timeout=self.timeout)

    def until_icon(self, icon_path: str, threshold: float = 0.8) -> VisionState:
        return self.vision.wait_icon(
            icon_path=icon_path,
            threshold=threshold,
            timeout=self.timeout
        )
