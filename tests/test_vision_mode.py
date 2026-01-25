import pytest
from nano_wait.vision import VisionMode
from nano_wait.selenium_adapter import VisionWait
from nano_wait.vision_state import VisionState

def test_observe_returns_state(vision, mock_capture_screen, mock_extract_text):
    state = vision.observe()
    assert isinstance(state, VisionState)
    assert state.detected is True
    assert state.text == "Hello World"

def test_wait_text_success(vision, mock_capture_screen, mock_extract_text):
    state = vision.wait_text("Hello World", timeout=1.0)
    assert state.detected is True
    assert state.confidence > 0.5
    assert "success" in [phase["result"] for phase in state.diagnostics["phases"]]

def test_wait_text_timeout(vision, mock_capture_screen):
    # Simula OCR retornando texto errado → timeout
    from unittest.mock import patch
    with patch("nano_wait.ocr.extract_text", return_value="wrong"):
        state = vision.wait_text("Hello World", timeout=0.5)
        assert state.detected is False
        assert state.reason == "timeout"

def test_wait_icon_success(vision, mock_capture_screen):
    import numpy as np
    import cv2

    # Mock de icon com mesma forma da tela
    dummy_icon = np.zeros((10, 10), dtype=np.uint8)
    cv2.imwrite("/tmp/dummy_icon.png", dummy_icon)

    state = vision.wait_icon("/tmp/dummy_icon.png", timeout=1.0, threshold=0.0)
    assert state.detected is True
    assert state.confidence >= 0.0

def test_vision_wait_adapter(wait, mock_capture_screen, mock_extract_text):
    state = wait.until_text("Hello World")
    assert state.detected is True
