# 🎨 FULLUI — Console UI System

> Build beautiful, interactive terminal apps — fast.

FULLUI is a powerful and lightweight **console UI framework for Python**, designed to transform boring CLI programs into visually rich experiences.

---

## ✨ Features

* 🎨 ANSI + RGB color system
* ✨ Text styling (bold, italic, underline, etc.)
* 🧱 Decorative boxes & layouts
* 🌈 Gradient text effects
* 🎮 Flexible menu system (alias-based)
* ⚡ Smooth CLI animations
* 🎭 Theme engine (plug & play)
* 🧠 Clean modular architecture

---

## 🎯 Perfect For

* 🎮 Console games
* 🧰 CLI tools
* 🖥️ Interactive terminal apps
* 🧪 UI prototyping

---

## 📦 Installation

```bash
pip install fullui
```

---

## 🚀 Quick Start

```python
from fullui import *

menu(
    t="Main Menu",
    op=["Play", "Exit"]
)
```

---

## 🧩 Recommended Import Style

```python
from fullui.colors import C, S
from fullui.ui import menu, clear, pause

clear()

choice = menu(
    t="Menu",
    st="Choose an option",
    op=["Start", "Exit"]
)

print(C.r + "You selected:" + S.rs, choice)
pause()
```

---

## 🧠 Menu Behavior (NEW)

Menus are now **interactive and validated by default**:

* 🔁 Loop until valid input
* 🔢 Returns selected option as `int`
* ❌ Handles invalid input automatically
* 🚪 Returns `"break"` if exit option is used

```python
choice = menu(
    t="Game",
    op=["Play", "Settings"]
)

if choice == 1:
    print("Start game")
elif choice == "break":
    print("Exit")
```

---

## 🎨 Themes (Improved)

Themes are now **automatically applied** — no extra work needed.

```python
from fullui import set_theme, NEON

set_theme(NEON)

menu(
    t="Styled Menu",
    op=["Option 1", "Option 2"]
)
```

### Custom Theme

```python
from fullui import create_theme, C, set_theme

my_theme = create_theme(
    titleColor=C.r,
    inputColor=C.g
)

set_theme(my_theme)
```

---

## 🎨 Colors & Styles

```python
from fullui import C, S

print(C.r + "Red Text" + S.rs)
print(S.bd + "Bold Text" + S.rs)
```

### RGB

```python
from fullui import rgb

print(rgb(255, 100, 0) + "Custom Color")
```

---

## 🧱 Boxes

```python
from fullui import box1, box4

print(box1("Hello"))
print(box4("Important"))
```

---

## 🌈 Gradients

```python
from fullui import rainbow, customGra, C

print(rainbow("FULLUI"))
print(customGra("Gradient", C.r, C.g, C.b))
```

---

## 🎬 Animations

```python
from fullui import spinner, glitch, pulse_bar

spinner("Loading", 3)
glitch("ERROR", 10)
pulse_bar(100)
```

---

## 🖥️ UI System

### Aliases

Short keys supported:

```python
menu(
    t="Menu",   # titleText
    st="Info",  # subtitleText
    op=["A","B"]
)
```

---

## 🔧 Utilities

```python
clear()   # Clear screen
pause()   # Wait for Enter
```

---

## 🧩 Full Import

```python
from fullui import *
```

Everything is exposed via `__all__`.

---

# 🆕 Patch Notes — v0.1.2

### 🔥 Improvements

* ✅ **Theme system fully integrated**

  * Themes now apply automatically inside `menu()`
  * No manual `apply_theme()` needed

* ✅ **Menu system upgraded**

  * Input validation added
  * Infinite loop until valid input
  * Clean return values (`int` or `"break"`)

* ✅ **UI alignment fix**

  * `title()` now uses proper width-based centering
  * More consistent layout rendering

* ✅ **Better UX**

  * Error feedback for invalid inputs
  * Pause system integrated in validation loop

---

### ⚠️ Behavior Changes

* `menu()` no longer returns raw input
* Now returns:

  * `int` → valid option
  * `"break"` → exit

---

### 🧠 Internal Improvements

* Cleaner rendering flow
* Theme injection system stabilized
* Better separation of concerns

---

# 🚀 Roadmap

* ⌨️ Keyboard navigation (arrow keys)
* 🧩 Layout system (panels, grids)
* 🎮 Interactive menus (real-time)
* 🎨 JSON theme support
* 🧠 State management system

---

# 📄 License

MIT License

---

# 👨‍💻 Author

**Leonardo Farid Porras Bendezú**
aka **LeonardX007**
