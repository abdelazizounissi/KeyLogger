# ⌨️ Simple Python Keyboard Monitor (Keylogger)

A minimalist and robust keyboard input monitor written in Python using the `pynput` library.  
This tool captures and logs keystrokes to a local text file — useful for learning about input handling and event listeners.

---

## ⚠️ Ethical & Legal Warning

**THIS SCRIPT IS FOR EDUCATIONAL AND PERSONAL USE ONLY.**

- Do **NOT** run this script on any computer you do not own or on which you do not have explicit permission.  
- Unauthorized keylogging is **illegal and unethical**.  
- The author and maintainers are **not responsible** for any misuse.

---

## ✨ Features

- Reliable logging of characters, punctuation, Numpad numbers, and decimal points.  
- Writes keystrokes into a readable `simple_log.txt` file.  
- Press `Esc` to stop monitoring gracefully.  
- Easy to convert to a standalone `.exe` with PyInstaller.

---

## 📋 Requirements

- Python 3.x
- `pynput` library

---

## 🚀 Installation & Usage

### Option 1 — Run from source

1. Clone the repository:
```bash
git clone https://github.com/abdelazizounissi/KeyLogger.git
cd KeyLogger
```

2. Install dependencies:
```bash
pip install pynput
```

3. Run the program:
```bash
python KeyLogger.py
```

### Option 2 — Download pre-built application

- **[KeyLogger_App.zip](KeyLogger_App.zip)** - Standalone executable application (no Python installation required)

Simply download, extract, and run the application!

⚠️ Note: Because this program monitors keyboard activity, antivirus software may flag the executable. You may need to manually allow or whitelist it.

---

## 🎯 How to use

- Start the application (either the `.py` file or the `.exe`).
- The program begins monitoring keystrokes immediately.
- Keystrokes are printed to the console (if running the script) and appended to `simple_log.txt`.
- Press `Esc` to stop monitoring and exit the program.

---


## 🛠️ Build a standalone executable (optional)

To build a single-file Windows executable with PyInstaller:

1. Install PyInstaller:
```bash
pip install pyinstaller
```

2. Build (example):
```bash
pyinstaller --onefile KeyLogger.py
```

- The resulting executable will be in the `dist/` directory.
- You can add `--noconsole` if you don't want a console window to appear (may affect logging visibility).

---

## 📝 License

This project is open source and available for personal and educational use.

---

## 👤 Author

**Abdelaziz Ounissi**

© 2025 Abdelaziz Ounissi

---

## 🤝 Contributing

Feel free to fork the repository and submit pull requests with improvements, fixes, or documentation updates.

---

## 📧 Support

If you have issues or suggestions, please open a GitHub Issue in this repository.
