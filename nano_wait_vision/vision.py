import time
import json
from pathlib import Path
from typing import Optional

import cv2

from nano_wait import wait
from .vision_state import VisionState
from .ocr import extract_text
from .screen import capture_screen


VISION_DIR = Path.home() / ".nano-wait"
PATTERNS_FILE = VISION_DIR / "vision_patterns.json"


class VisionMode:
    def __init__(self, mode: str = "observe", verbose: bool = False):
        self.mode = mode
        self.verbose = verbose
        self.patterns = self._load_patterns()

    # ==========================
    # Public API
    # ==========================

    def observe(self) -> VisionState:
        frame = capture_screen()
        text = extract_text(frame).strip()

        return VisionState(
            name="observe",
            detected=bool(text),
            confidence=1.0 if text else 0.0,
            text=text,
        )

    def wait_text(self, text: str, timeout: float = 10.0) -> VisionState:
        start = time.time()

        while time.time() - start < timeout:
            frame = capture_screen()
            detected_text = extract_text(frame)

            if text.lower() in detected_text.lower():
                return VisionState(
                    name=text,
                    detected=True,
                    confidence=1.0,
                    text=detected_text,
                )

            wait(0.2, smart=True)

        return VisionState(name=text, detected=False)

    def wait_icon(
        self,
        icon_path: str,
        timeout: float = 10.0,
        threshold: float = 0.8,
    ) -> VisionState:
        icon = cv2.imread(icon_path, cv2.IMREAD_GRAYSCALE)
        if icon is None:
            raise FileNotFoundError(f"Icon not found: {icon_path}")

        start = time.time()

        while time.time() - start < timeout:
            screen = capture_screen(gray=True)
            result = cv2.matchTemplate(screen, icon, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, _ = cv2.minMaxLoc(result)

            if max_val >= threshold:
                return VisionState(
                    name=icon_path,
                    detected=True,
                    confidence=float(max_val),
                    icon=icon_path,
                )

            wait(0.2, smart=True)

        return VisionState(
            name=icon_path,
            detected=False,
            confidence=0.0,
            icon=icon_path,
        )

    def learn(self, name: str, text: str):
        self.patterns[name] = {"type": "text", "value": text}
        self._save_patterns()

    def learn_icon(self, name: str, icon_path: str):
        self.patterns[name] = {"type": "icon", "value": icon_path}
        self._save_patterns()

    # ==========================
    # Persistence
    # ==========================

    def _load_patterns(self):
        if not PATTERNS_FILE.exists():
            return {}

        with open(PATTERNS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    def _save_patterns(self):
        VISION_DIR.mkdir(parents=True, exist_ok=True)
        with open(PATTERNS_FILE, "w", encoding="utf-8") as f:
            json.dump(self.patterns, f, indent=2)
