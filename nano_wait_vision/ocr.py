import pytesseract


def extract_text(image) -> str:
    if image is None:
        return ""

    try:
        return pytesseract.image_to_string(image)
    except Exception:
        return ""


def text_confidence(haystack: str, needle: str) -> float:
    """
    Deterministic heuristic for screen automation (not NLP).

    Rules:
    - If needle is present → confidence > 0
    - Otherwise → 0.0
    """
    if not haystack or not needle:
        return 0.0

    haystack_l = haystack.lower()
    needle_l = needle.lower()

    if needle_l in haystack_l:
        return min(1.0, len(needle_l) / max(1, len(haystack_l)))

    return 0.0
