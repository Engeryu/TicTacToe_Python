# ❌⭕ Python TicTacToe 🐍

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Code of Conduct](https://img.shields.io/badge/Code%20of%20Conduct-Contributor%20Covenant-ff69b4.svg)](CODE_OF_CONDUCT.md)

An interactive two-player TicTacToe game in Python. The board updates after each turn for a clear and engaging user experience.

## 🚀 Features

* **Two-player game:** Challenge a friend directly in your terminal.
* **Interactive board:** Clear visualization of the game state.
* **Real-time updates:** The board is redrawn after each move.
* **Rule checking:** Automatic detection of wins and draws.
* **Simple text-based interface:** Easy to launch and play without a complex graphical interface.

## ⚙️ Installation

1. **Clone the repository:**

```bash
git clone <YOUR_REPOSITORY_URL>
cd <YOUR_REPOSITORY_NAME>
```

2. **Ensure you have Python installed** (version 3.7 or higher). You can check your version with:

```bash
python --version
```

3. **No external dependencies are required.** The game uses only standard Python features.

---

## ▶️ How to Play

1. **Run the main script:**

   ```bash
   python TicTacToe.py
   ```
2. **Follow the on-screen instructions:** The game will ask for player names and prompt you to enter the coordinates of the square where you want to place your symbol ('X' or 'O').
3. **Take turns playing** until one player aligns three of their symbols or the board is full (draw).

---

## 📂 Project Structure

```bash
.
├── CODE_OF_CONDUCT.md
├── LICENSE
├── README.md
├── SECURITY.md
├── src
│   ├── board.py         # Manages the game board logic and display
│   ├── game_rule.py     # Contains functions to check game rules (win, draw)
│   ├── player.py        # Defines the Player class to manage player information
│   ├── __pycache__      # Compiled Python files
│   │   ├── board.cpython-311.pyc
│   │   ├── game_rule.cpython-311.pyc
│   │   ├── player.cpython-311.pyc
│   │   └── text.cpython-311.pyc
│   └── text.py          # Manages text display and user interactions
└── TicTacToe.py       # Main script to launch the game

```

---

🛡️ Security
-------------

Please refer to the SECURITY.md file for security guidelines.

---

📜 License
----------

This project is licensed under the MIT license. See the LICENSE file for more details.

---

🤝 Contributing
---------------

Contributions are welcome! Please review the CODE_OF_CONDUCT.md file for contribution guidelines.

---

**Have fun playing TicTacToe!** 🎉
