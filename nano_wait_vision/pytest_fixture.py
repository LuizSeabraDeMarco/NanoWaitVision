import pytest
from .vision import VisionMode
from .selenium_adapter import VisionWait

@pytest.fixture
def vision():
    """Instância VisionMode para testes de GUI."""
    return VisionMode()

@pytest.fixture
def wait():
    """Instância VisionWait plug-and-play (Selenium-free)."""
    return VisionWait(timeout=10)
