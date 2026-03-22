import pytesseract
import cv2
import numpy as np

def preprocess_image(image, method: str = "default") -> np.ndarray:
    """
    Pré-processa a imagem para OCR mais confiável.
    
    method:
        - "default": grayscale + threshold simples
        - "adaptive": adaptive threshold
        - "blur": blur leve para reduzir ruído
    """
    if image is None:
        return None

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    if method == "adaptive":
        # Adaptive threshold para telas com variação de luz
        gray = cv2.adaptiveThreshold(
            gray, 255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            11, 2
        )
    elif method == "blur":
        # Suaviza ruídos pequenos
        gray = cv2.medianBlur(gray, 3)
        _, gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    else:
        # Threshold simples
        _, gray = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    return gray

def extract_text(image, method: str = "default") -> str:
    """
    Extrai texto de uma imagem usando pytesseract com pré-processamento.
    """
    if image is None:
        return ""

    try:
        preprocessed = preprocess_image(image, method)
        return pytesseract.image_to_string(preprocessed)
    except Exception:
        return ""

def text_confidence(haystack: str, needle: str) -> float:
    """
    Heurística determinística para automação.
    """
    if not haystack or not needle:
        return 0.0

    haystack_l = haystack.lower()
    needle_l = needle.lower()

    if needle_l in haystack_l:
        return min(1.0, len(needle_l) / max(1, len(haystack_l)))

    return 0.0
