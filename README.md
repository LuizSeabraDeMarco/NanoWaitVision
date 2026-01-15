# Nano-Wait-Vision — Visual Execution Extension

[![PyPI version](https://img.shields.io/pypi/v/nano-wait-vision.svg)](https://pypi.org/project/nano-wait-vision/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**nano-wait-vision** is the official computer vision extension for [nano-wait](https://pypi.org/project/nano-wait/). It integrates visual awareness (OCR, icon detection, screen states) into the adaptive waiting engine, enabling deterministic, screen-driven automations.

> [!IMPORTANT]
> **Critical Dependency:** This package **DEPENDS** on `nano-wait`. It does not replace `nano-wait` — it extends it.

---

## 🧠 What is Nano-Wait-Vision?

Nano-Wait-Vision is a deterministic vision engine for Python automation. Instead of waiting blindly with `sleep()`, it allows your code to wait for real visual conditions:

*   **Text** appearing on screen
*   **Icons** becoming visible
*   **UI states** changing

It is designed to work in strict cooperation with `nano-wait`:

| Component | Responsibility |
| :--- | :--- |
| ⏱️ **nano-wait** | When to check (adaptive pacing & CPU-aware waiting) |
| 👁️ **nano-wait-vision** | What to check (screen, OCR, icons) |

---

## 🧩 Key Features

nano-wait-vision extends nano-wait with:

*   **👁️ OCR (Optical Character Recognition):** Read real text directly from the screen.
*   **🖼️ Icon Detection:** Template matching via OpenCV.
*   **🧠 Explicit Visual States:** Each operation returns a structured `VisionState`.
*   **📚 Persistent & Explainable Diagnostics:** No black-box ML models.
*   **🖥️ Screen-Based Automation:** Ideal for RPA and GUI testing.
*   **⚡ Selenium / Pytest Adapters:** Immediate adoption in corporate or academic QA workflows.

> [!TIP]
> All waiting logic is delegated to `nano-wait.wait()` — never `time.sleep()`.

---

## 🚀 Quick Start

### Installation

```bash
pip install nano-wait
pip install nano-wait-vision
```

### Simple Visual Observation

```python
from nano_wait_vision import VisionMode

vision = VisionMode()
state = vision.observe()

print(f"Detected: {state.detected}")
print(f"Text: {state.text}")
```

### Wait for Text to Appear

```python
from nano_wait_vision import VisionMode

vision = VisionMode(verbose=True)

# Wait up to 10 seconds for the word "Welcome"
state = vision.wait_text("Welcome", timeout=10)

if state.detected:
    print("Text detected!")
```

### Wait for an Icon

```python
from nano_wait_vision import VisionMode

vision = VisionMode()

# Wait up to 10 seconds for an icon image
state = vision.wait_icon("ok.png", timeout=10)

if state.detected:
    print("Icon found on screen.")
```

---

## ⚠️ Installation & Dependencies

This library interacts directly with your operating system screen and OCR engine.

### Python Dependencies (auto-installed)
*   `opencv-python`
*   `pytesseract`
*   `pyautogui`
*   `numpy`

### 🧠 Mandatory External Dependency — Tesseract OCR

OCR will not work unless **Tesseract** is installed and available in your PATH.

| OS | Command / Action |
| :--- | :--- |
| **macOS** | `brew install tesseract` |
| **Ubuntu / Debian** | `sudo apt install tesseract-ocr` |
| **Windows** | Download from the official Tesseract repo and add to PATH |

> [!WARNING]
> If Tesseract is missing, OCR calls will silently fail or return empty text.

---

## 🧠 Mental Model — How It Works

Nano-Wait-Vision follows this loop: **observe → evaluate → wait → observe**.

Two engines cooperate:

| 👁️ Vision Engine | ⏱️ nano-wait |
| :--- | :--- |
| OCR / Icons | Adaptive timing |
| Screen capture | CPU-aware waits |
| Visual states | Smart pacing |

Vision never sleeps. All delays are handled by `nano-wait`.

---

## 📦 VisionState — Return Object

Every visual operation returns a `VisionState` object:

```python
VisionState(
    name: str,
    detected: bool,
    confidence: float,
    attempts: int,
    elapsed: float,
    text: Optional[str],
    icon: Optional[str],
    diagnostics: dict
)
```

*Always check `detected` before acting on the result.*

---

## 🧪 Diagnostics & Debugging

Nano-Wait-Vision supports verbose diagnostics:

```python
vision = VisionMode(verbose=True)
state = vision.wait_text("Terminal")
```

Diagnostics include:
*   Attempts per phase
*   Confidence scores
*   Elapsed time
*   Reason for failure

A full macOS diagnostic test is provided in `test_screen.py`, generating debug screenshots for inspection.

---

## 🖥️ Platform Notes

### macOS (Important)
*   Screen capture requires **Screen Recording permission**.
*   OCR requires RGB images (internally handled by Nano-Wait-Vision).
*   Fully tested on macOS Retina displays.

### Windows & Linux
*   Works out of the box.
*   Ensure correct DPI scaling on Windows for accurate coordinate mapping.

---

## 🧪 Ideal Use Cases

Use Nano-Wait-Vision when dealing with:
*   **RPA** (Robotic Process Automation)
*   **GUI automation** and testing
*   **OCR-driven** workflows
*   **Visual regression** tests
*   Applications **without APIs**
*   Screen-based alternatives to Selenium

---

## 🧩 Design Philosophy

*   **Deterministic:** Predictable behavior based on visual truth.
*   **Explainable:** Clear diagnostics for every action.
*   **No opaque ML:** Uses reliable computer vision techniques.
*   **System-aware:** Respects system resources via `nano-wait`.
*   **Debuggable by design:** Built-in tools for troubleshooting.

---

## 🧪 Selenium / Pytest Integration

### Selenium-style Visual Waits
```python
from nano_wait_vision.selenium import VisionWait

wait = VisionWait(timeout=15)
wait.until_text("Dashboard")
wait.until_icon("ok.png")
```

### Pytest Fixture
```python
def test_homepage(vision):
    assert vision.wait_text("Welcome")
```
*Pytest fixture is available via `nano_wait_vision.pytest_fixture.vision`*

---

## 📄 License

This project is licensed under the MIT License.
