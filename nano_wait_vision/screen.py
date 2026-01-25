import cv2
import numpy as np
import pyautogui

try:
    import mss
except ImportError:
    mss = None
    print("Warning: 'mss' library not found. Multi-monitor may be slower.")

def capture_screen(gray: bool = False, screen_index: int = 0):
    """
    Captura a tela especificada (multi-monitor) e retorna como numpy array.
    
    Parameters:
        gray: retorna imagem em grayscale
        screen_index: índice do monitor (0 = principal)
    """
    if mss:
        with mss.mss() as sct:
            monitors = sct.monitors[1:]  # mss monitora a tela 1..N
            if screen_index >= len(monitors):
                raise ValueError(f"screen_index {screen_index} fora do range (0-{len(monitors)-1})")
            monitor = monitors[screen_index]
            screenshot = np.array(sct.grab(monitor))
            frame = cv2.cvtColor(screenshot[..., :3], cv2.COLOR_RGB2BGR)
    else:
        # fallback para pyautogui (captura só a principal)
        screenshot = pyautogui.screenshot()
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    if gray:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    return frame
