# 🖐️ Human Computer Interaction – Gesture Controlled Mouse

A Python project to control your computer mouse using hand gestures. Built using **MediaPipe**, **OpenCV**, and **ctypes**, this script enables real-time control of cursor movement and basic mouse operations like **left click**, **right click**, and **dragging** using finger gestures.

---

## 📊 Features

* 👉 Move cursor using index finger
* 🧿 Left click: Thumb + Index pinch
* ✌️ Right click: Index + Middle pinch
* 📌 Drag: Pinch and hold (Thumb + Index)
* 📺 Real-time webcam input and gesture visualization

---

## ⚖️ Requirements

* Python 3.8 or later
* Windows OS
* Libraries:

  * opencv-python
  * mediapipe
  * numpy

Install dependencies :

```bash
pip install opencv-python mediapipe numpy
```

---

## ▶️ How to Run

1. Clone the repository
2. Go inside the directory
3. Run the main script :

```bash
python main.py
```

3. Use gestures in front of your webcam to control the mouse
4. Press **Q** to quit the application

---

## 🔧 How It Works

* Uses **MediaPipe Hands** to detect 21 hand landmarks
* Tracks finger positions and calculates distances between key fingers
* Maps hand movement to screen coordinates with smoothing
* Performs mouse actions using `ctypes.windll.user32`

---

## 🔹 Gestures Summary

| Gesture              | Action      |
| -------------------- | ----------- |
| Index finger move    | Move Cursor |
| Thumb + Index pinch  | Left Click  |
| Index + Middle pinch | Right Click |
| Hold Thumb + Index   | Drag & Drop |

---

## 📄 License

This project is open source and free to use for educational and personal projects.