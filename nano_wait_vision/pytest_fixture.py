import pytest
from .vision import VisionMode


@pytest.fixture
def vision():
    """
    Pytest fixture for vision-based GUI waits.

    Usage:
        def test_app(vision):
            assert vision.wait_text("Welcome")
    """
    return VisionMode()
