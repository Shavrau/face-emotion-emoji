# 🎭 Real-Time Emoji Mirror

An interactive **Computer Vision** and **Deep Learning** application that detects facial expressions in real time via webcam and overlays matching emojis over the user's face or on a sleek HUD dashboard.

---

## ✨ Features

- **7 Facial Emotion Classifications**: Happy 😄, Sad 😢, Angry 😡, Surprise 😲, Fear 😨, Disgust 🤢, and Neutral 😐.
- **3 Interactive Display Modes**:
  - 🎭 **Face Mask**: Scales and centers the emoji over the detected face (Instagram/Snapchat filter style).
  - 📊 **HUD Card**: Displays a modern semi-transparent telemetry card in the top-right corner with emotion name and confidence percentage.
  - 🌟 **Both**: Combines face mask overlay and HUD card simultaneously.
- **Natural Mirror Effect**: Horizontal reflection (`cv2.flip`) mimicking physical mirror behavior.
- **Alpha Blending**: Mathematical pixel-by-pixel compositing with boundary clipping to avoid black box artifacts or edge overflow errors.
- **Optimized Performance (30+ FPS)**: Frame-skipping neural inference coupled with temporal persistence to eliminate flickering.
- **Built-in Asset Generator**: Procedural emoji generation script using Pillow with supersampling anti-aliasing.

---

## 🛠️ Tech Stack

| Technology | Role |
| :--- | :--- |
| **Python 3.12** | Core programming language |
| **OpenCV (`opencv-python`)** | Video stream acquisition, affine transformations, HighGUI, and rendering |
| **FER (*Facial Emotion Recognition*)** | Haar Cascade face detection and emotion classification |
| **TensorFlow Lite** | Neural network runtime for expression inference |
| **NumPy** | Matrix operations and alpha blending vector math |
| **Pillow (PIL)** | Procedural emoji asset rendering and manipulation |

---

## 📁 Project Structure

```text
visao_computacional/
├── assets/
│   └── emojis/              # 256x256 transparent PNG emoji assets
├── scripts/
│   └── generate_emojis.py   # Procedural asset generator script
├── src/
│   ├── __init__.py          # Package initialization
│   ├── config.py            # Global settings, emotion maps, and labels
│   ├── detector.py          # EmotionDetector class (FER wrapper)
│   └── overlay.py           # EmojiOverlay class (alpha blending & HUD)
├── .gitignore               # Git ignored patterns (venv, pycache, etc.)
├── main.py                  # Real-time application entry point
├── README.md                # Project documentation
└── requirements.txt         # Pinned dependency requirements
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

### 2. Create and Activate Virtual Environment

- **Windows (PowerShell)**:
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```

- **Linux / macOS**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python main.py
```

---

## 🎮 Keyboard Controls

With the video window active:

| Key | Description |
| :---: | :--- |
| **`m`** | Cycle display modes (**Mask + HUD** ➔ **Face Mask** ➔ **HUD Card**) |
| **`f`** | Toggle mirror reflection (horizontal flip) |
| **`q`** | Quit application safely |

---

## ⚙️ Configuration

Custom parameters can be tuned in [src/config.py](src/config.py):
- `FRAME_SKIP`: Number of frames between neural inferences (default: `2`).
- `CAMERA_INDEX`: Device camera index (default: `0`).
- `MIRROR_EFFECT`: Default mirror reflection state (`True` or `False`).

---

## 📄 License

This project is licensed under the MIT License.
