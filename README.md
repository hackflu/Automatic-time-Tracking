# ⏱️ Automatic Time Tracking System for Windows

This is a Python-based **Automatic Time Tracking** tool designed to monitor how much time you spend on each software application on your Windows system.

It automatically tracks the **start time**, **end time**, and **duration** for every app you open and logs this data into a JSON file (`activities.json`) — useful for self-productivity, time auditing, or digital habit tracking.

---

## 📌 Features

- 🪟 Detects active (foreground) application using native Windows APIs
- 🕓 Logs:
  - Start time
  - End time
  - Total time spent (in seconds)
  - Time breakdown (hours, minutes, seconds)
- 💾 Saves data to `activities.json`
- 🧠 Works entirely in the background
- 🧩 Lightweight and no internet required

---

## 🛠️ Technologies Used

| Library         | Description                                       |
|-----------------|---------------------------------------------------|
| `win32gui`      | Gets the title of the active window               |
| `uiautomation`  | Monitors and interacts with UI elements           |
| `datetime`      | Handles time tracking and formatting              |
| `sys`           | Accesses system-level information and arguments   |
| `json`          | Saves structured tracking data locally            |

---

## 🚀 How to Set Up and Run

### 1. ✅ Install Python

If you haven’t already:
- Download and install Python: https://www.python.org/downloads/
- During installation, **make sure you check** ✅ “Add Python to PATH”

---

### 2. 📦 Install Required Libraries

Open a terminal (or PyCharm terminal) and run:

```bash
pip install pywin32 uiautomation
