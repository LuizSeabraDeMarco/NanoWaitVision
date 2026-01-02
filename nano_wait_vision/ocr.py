import pytesseract


def extract_text(image) -> str:
    """
    Extract text from an image using Tesseract OCR.
    """
    if image is None:
        return ""

    try:
        return pytesseract.image_to_string(image)
    except Exception:
        return ""
