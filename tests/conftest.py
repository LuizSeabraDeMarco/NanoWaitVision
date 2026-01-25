import pytest
from unittest.mock import patch, MagicMock
from nano_wait.vision import VisionMode
from nano_wait.selenium_adapter import VisionWait

@pytest.fixture
def vision():
    """Instância VisionMode para testes de GUI."""
    return VisionMode(verbose=True, diagnostic=True)

@pytest.fixture
def wait():
    """Instância VisionWait plug-and-play (Selenium-free)."""
    return VisionWait(timeout=2, verbose=True)

@pytest.fixture
def mock_capture_screen():
    """Mock para captura de tela."""
    with patch("nano_wait.screen.capture_screen") as mock:
        # Retorna uma imagem dummy (np array preto)
        import numpy as np
        mock.return_value = np.zeros((100, 100, 3), dtype=np.uint8)
        yield mock

@pytest.fixture
def mock_extract_text():
    """Mock para OCR."""
    with patch("nano_wait.ocr.extract_text") as mock:
        # Retorna texto fixo
        mock.return_value = "Hello World"
        yield mock
