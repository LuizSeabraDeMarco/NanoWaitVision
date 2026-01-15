from .vision import VisionMode


class VisionWait:
    """
    Selenium-like visual wait adapter.

    Example:
        wait = VisionWait(timeout=15)
        wait.until_text("Dashboard")
    """

    def __init__(self, timeout: float = 10.0, verbose: bool = False):
        self.timeout = timeout
        self.vision = VisionMode(verbose=verbose)

    def until_text(self, text: str):
        state = self.vision.wait_text(text, timeout=self.timeout)
        if not state.detected:
            raise TimeoutError(f"Text not found on screen: '{text}'")
        return state

    def until_icon(self, icon_path: str, threshold: float = 0.8):
        state = self.vision.wait_icon(
            icon_path=icon_path,
            timeout=self.timeout,
            threshold=threshold,
        )
        if not state.detected:
            raise TimeoutError(f"Icon not found on screen: {icon_path}")
        return state
