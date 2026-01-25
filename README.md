# Nano-Wait-Vision — Visual Execution Extension

[![PyPI version](https://img.shields.io/pypi/v/nano-wait-vision.svg)](https://pypi.org/project/nano-wait-vision/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**nano-wait-vision** is the official computer vision extension for [nano-wait](https://pypi.org/project/nano-wait/). It integrates visual awareness (OCR, icon detection, screen states) into the adaptive waiting engine, enabling deterministic, screen-driven automations.

> [!IMPORTANT]
> **Critical Dependency:** This package **DEPENDS** on `nano-wait`. It does not replace `nano-wait` — it extends it.

---

## 🧠 What is Nano-Wait-Vision?

Nano-Wait-Vision is a deterministic vision engine for Python automation. Instead of waiting blindly with `sleep()`, it allows your code to wait for real visual conditions:

* **Text** appearing on screen
* **Icons** becoming visible
* **UI states** changing
* **Multi-Monitor Support:** now you can target specific screens for observation, text detection, and icon detection. Ideal for setups with multiple monitors.

It is designed to work in strict cooperation with `nano-wait`:

| Component                | Responsibility                                      |
| :----------------------- | :-------------------------------------------------- |
| ⏱️ **nano-wait**         | When to check (adaptive pacing & CPU-aware waiting) |
| 👁️ **nano-wait-vision** | What to check (screen, OCR, icons)                  |

---

## 🧩 Key Features

nano-wait-vision extends nano-wait with:

* **👁️ OCR (Optical Character Recognition):** Read real text directly from the screen.
* **🖼️ Icon Detection:** Template matching via OpenCV.
* **🖥️ Automatic HiDPI/Retina Support:** Icons and template matching are automatically scaled to work flawlessly on 4K, macOS Retina, and Windows HiDPI displays, requiring zero user configuration.
* **🖥️ Multi-Monitor Awareness:** Target any monitor by index; works seamlessly in multi-screen setups.
* **🧠 Explicit Visual States:** Each operation returns a structured `VisionState`.
* **📚 Persistent & Explainable Diagnostics:** No black-box ML models.
* **⚡ QA-Friendly & Plug-and-Play:** Zero dependency on web drivers (like Selenium), making corporate and academic adoption seamless.
* **🖥️ Screen-Based Automation:** Ideal for RPA and GUI testing.

> [!TIP]
> All waiting logic is delegated to `nano-wait.wait()` — never `time.sleep()`.

---

## 🚀 Quick Start

### Installation

```bash
pip install nano-wait
pip install nano-wait-vision
```

### Simple Visual Observation (Single or Multi-Monitor)

```python
from nano_wait_vision import VisionMode

# Observe the primary screen
vision_main = VisionMode(screen_index=0)
state_main = vision_main.observe()

# Observe a secondary screen (if available)
vision_second = VisionMode(screen_index=1)
state_second = vision_second.observe()

print(f"Primary screen text: {state_main.text}")
print(f"Secondary screen text: {state_second.text}")
```

### Wait for Text to Appear

```python
from nano_wait_vision import VisionMode

vision = VisionMode(verbose=True, screen_index=0)

# Wait up to 10 seconds for the word "Welcome" on the primary screen
state = vision.wait_text("Welcome", timeout=10)

if state.detected:
    print("Text detected!")
```

### Wait for an Icon

```python
from nano_wait_vision import VisionMode

vision = VisionMode(screen_index=1)  # target second monitor

# Wait up to 10 seconds for an icon image on the second monitor
state = vision.wait_icon("ok.png", timeout=10)

if state.detected:
    print("Icon found on screen.")
```

---

## ⚠️ Installation & Dependencies

This library interacts directly with your operating system screen and OCR engine.

### Python Dependencies (auto-installed)

* `opencv-python`
* `pytesseract`
* `pyautogui`
* `numpy`
* **Optional for Multi-Monitor:** `mss` (faster and full multi-monitor support)

### 🧠 Mandatory External Dependency — Tesseract OCR

OCR will not work unless **Tesseract** is installed and available in your PATH.

| OS                  | Command / Action                                          |
| :------------------ | :-------------------------------------------------------- |
| **macOS**           | `brew install tesseract`                                  |
| **Ubuntu / Debian** | `sudo apt install tesseract-ocr`                          |
| **Windows**         | Download from the official Tesseract repo and add to PATH |

> [!WARNING]
> If Tesseract is missing, OCR calls will silently fail or return empty text.

---

## 🧠 Mental Model — How It Works

Nano-Wait-Vision follows this loop: **observe → evaluate → wait → observe**.

Two engines cooperate:

| 👁️ Vision Engine                    | ⏱️ nano-wait    |
| :----------------------------------- | :-------------- |
| OCR / Icons                          | Adaptive timing |
| Screen capture (multi-monitor aware) | CPU-aware waits |
| Visual states                        | Smart pacing    |

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
vision = VisionMode(verbose=True, screen_index=0)
state = vision.wait_text("Terminal")
```

Diagnostics include:

* Attempts per phase
* Confidence scores
* Elapsed time
* Reason for failure

---

## 🖥️ Platform Notes

### Automatic HiDPI/Retina Support (New!)

The library now automatically detects the screen's scaling factor (DPI/Retina) and scales icon templates accordingly. This ensures template matching works reliably on all modern displays (macOS Retina, Windows HiDPI, 4K monitors) without any manual configuration.

### Multi-Monitor Support (New!)

* Target a specific monitor using the `screen_index` parameter.
* Supports setups with multiple monitors; automatically handles capturing and scaling per screen.
* Optional dependency: `mss` for faster and full multi-monitor screenshots.

### macOS (Important)

* Screen capture requires **Screen Recording permission**.
* OCR requires RGB images (internally handled by Nano-Wait-Vision).
* Fully tested on macOS Retina displays with automatic scaling.

### Windows & Linux

* Works out of the box.

---

## 🧪 Ideal Use Cases

Use Nano-Wait-Vision when dealing with:

* **RPA** (Robotic Process Automation)
* **GUI automation** and testing
* **OCR-driven** workflows
* **Visual regression** tests
* Applications **without APIs**
* Screen-based alternatives to traditional web drivers.

---

## 🧩 Design Philosophy

* **Deterministic:** Predictable behavior based on visual truth.
* **Explainable:** Clear diagnostics for every action.
* **No opaque ML:** Uses reliable computer vision techniques.
* **System-aware:** Respects system resources via `nano-wait`.
* **Debuggable by design:** Built-in tools for troubleshooting.

---

## 🧪 QA & Automation Adapters (Pytest & Generic Wait)

The library is now completely **driver-agnostic** and provides dedicated tools for QA and automation workflows.

### Generic Visual Waits (`VisionWait`)

The `VisionWait` class provides a "Selenium-like" adapter for visual waiting, but is now completely independent of Selenium or any web driver. It's a clean, plug-and-play way to integrate visual checks into any automation framework.

```python
from nano_wait_vision import VisionWait

wait = VisionWait(timeout=15) 
wait.until_text("Dashboard")
wait.until_icon("ok.png")
```

### Pytest Fixtures (Plug-and-Play)

For immediate adoption in QA projects, the library provides ready-to-use pytest fixtures.

```python
def test_homepage(vision, wait):
    # Use the global VisionMode instance
    assert vision.wait_text("Welcome") 
    
    # Use the VisionWait adapter
    wait.until_icon("login_button.png")
```

*Fixtures are available via `nano_wait_vision.pytest_fixture`.*

---

## 📄 License

This project is licensed under the MIT License.

---

Se você quiser, posso gerar também **uma seção visual de diagrama mostrando multi-monitor workflow** para o README, que deixa claro como o `screen_index` funciona em setups com 2 ou mais telas.

Quer que eu faça isso?
