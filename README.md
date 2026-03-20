#  Virtual Mouse — Hand Gesture Control

Control your computer's mouse cursor using just your hand and a webcam. Built with **OpenCV**, **MediaPipe**, and **PyAutoGUI**.

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?logo=opencv)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

##  Features

| Gesture | Action |
|---|---|
|  **Index finger up** (only) | Move cursor |
|  **Index + Middle fingers up** | Left click |
|  **Fist / other gestures** | No action (idle) |

- **Real-time hand tracking** using MediaPipe's 21-point hand landmark model
- **Smooth cursor movement** with configurable smoothening factor
- **Adjustable sensitivity** — separate horizontal and vertical gain
- **Mirror-corrected** — cursor moves in the natural direction
- **Live preview window** with hand skeleton overlay
- Press **`Q`** to quit

---

##  How It Works

1. Webcam captures live video feed
2. MediaPipe detects hand landmarks (21 key points)
3. Finger positions are analyzed to determine which fingers are raised
4. Based on the gesture:
   - **Index only** → cursor follows fingertip position
   - **Index + Middle** → triggers a left click
5. Hand skeleton is drawn on the preview window for visual feedback

---

##  Setup

### Prerequisites

- Python 3.8 or higher
- A working webcam

### Installation

```bash
# Clone the repo
git clone https://github.com/<your-username>/virtual-mouse.git
cd virtual-mouse

# Create virtual environment
python -m venv venv

# Activate it
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Run

```bash
python cv.py
```

A window titled **"Virtual Mouse"** will open showing your webcam feed with hand tracking overlay. Use the gestures above to control your mouse.

---

##  Configuration

You can tweak these values at the top of `cv.py`:

| Parameter | Default | Description |
|---|---|---|
| `smoothening` | `4` | Higher = smoother cursor, Lower = faster response |
| `movement_gain_x` | `0.6` | Horizontal sensitivity multiplier |
| `movement_gain_y` | `1.0` | Vertical sensitivity multiplier |

---

##  Tech Stack

- **[OpenCV](https://opencv.org/)** — webcam capture and video display
- **[MediaPipe](https://mediapipe.dev/)** — real-time hand landmark detection
- **[PyAutoGUI](https://pyautogui.readthedocs.io/)** — programmatic mouse control
- **[NumPy](https://numpy.org/)** — numerical operations (MediaPipe dependency)

---

##  Project Structure

```
virtual-mouse/
├── cv.py               # Main application script
├── requirements.txt    # Python dependencies
├── .gitignore          # Git ignore rules
├── LICENSE             # MIT License
└── README.md           # This file
```

---

##  Notes

- Works best in **well-lit environments** with a clear background
- Only tracks **one hand** at a time (configurable in code)
- `pyautogui.FAILSAFE` is disabled — the cursor won't freeze at screen corners
- On first run, MediaPipe will download its hand tracking model (~10 MB)

---

##  License

This project is licensed under the [MIT License](LICENSE).
