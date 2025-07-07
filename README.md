# virtual_calculator.py
# ✋🧮 Gesture-Controlled Virtual Calculator

A touchless virtual calculator that takes input from **hand gestures** using a webcam — no mouse or keyboard needed!  
Built with **Python**, **OpenCV**, and **MediaPipe** for real-time hand tracking and gesture recognition.

---

## 📌 **Features**

✅ Detects hand landmarks using MediaPipe  
✅ Recognizes pinch gestures (thumb + index finger) to click virtual buttons  
✅ Solves mathematical expressions in real-time  
✅ Works entirely hands-free — ideal for experimenting with touchless HCI  
✅ Simple and beginner-friendly computer vision project

---

## 🚀 **How It Works**

- Uses your webcam feed to detect your hand.
- Tracks **21 hand landmarks**.
- Checks if thumb tip and index finger tip are close enough — if yes, it simulates a **button click**.
- Draws a virtual calculator with clickable buttons on the webcam feed.
- Updates and solves the expression when you press `=`!

---

## 🛠️ **Tech Stack**

- **Python**
- **OpenCV** for video capture and drawing the UI
- **MediaPipe** for real-time hand tracking
- **NumPy** for simple distance calculation

---

## ▶️ **Getting Started**

**1️⃣ Clone this repository**

```bash
git clone https://github.com/yourusername/gesture-calculator.git
cd gesture-calculator
