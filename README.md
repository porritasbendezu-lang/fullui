# 🎨 FULLUI --- Console UI System

> Build beautiful, interactive terminal apps --- fast.

FULLUI is a powerful and lightweight **console UI framework for
Python**, designed to transform boring CLI programs into visually rich
experiences.

------------------------------------------------------------------------

# ✨ Features

-   🎨 ANSI + RGB color system
-   🌈 Advanced gradients
-   ✨ Text styling system
-   🧱 Decorative boxes
-   🪟 Layout System
-   🎮 Flexible alias-based menu system
-   ⚡ Terminal animations
-   🎭 Plug & Play Theme Engine
-   🛠 Developer Tools Panel
-   📦 Modular architecture

------------------------------------------------------------------------

# 🆕 New in v0.2.2

## Improvements & Refinements

-   Improved UI rendering performance
-   Better theme handling
-   Cleaner module structure
-   Internal optimizations
-   Preparation for future widgets system

------------------------------------------------------------------------

# 🎯 Perfect For

-   Console games
-   CLI tools
-   Interactive terminal apps
-   UI prototyping
-   Terminal dashboards

------------------------------------------------------------------------

# 📦 Installation

``` bash
pip install fullui
```

------------------------------------------------------------------------

## ✨ Verify Installation

``` bash
python -c "import fullui; fullui.banner()"
```

------------------------------------------------------------------------

# 🚀 Quick Start

``` python
from fullui import *

banner()

menu(
    t="Main Menu",
    op=[
        "Play",
        "Settings"
    ]
)
```

------------------------------------------------------------------------

# 🧩 Recommended Import Style

``` python
from fullui.colors import C,S
from fullui.ui import menu
from fullui.layouts import panel

panel(
   "Profile",
   "Level 12"
)

choice = menu(
   t="Menu",
   op=["Start","Exit"]
)
```

------------------------------------------------------------------------

# 🧠 Menu Behavior

-   Loops until valid input
-   Returns int
-   Invalid input handled automatically
-   Returns None on exit

``` python
choice = menu(
    t="Game",
    op=["Play","Settings"]
)

if choice == 1:
    print("Play")
elif choice is None:
    print("Exit")
```

------------------------------------------------------------------------

# 🎨 Themes

``` python
from fullui import *

set_theme(NEON)

menu(
 t="Styled Menu",
 op=["Option A","Option B"]
)
```

Custom:

``` python
my_theme = create_theme(
    titleColor=C.r,
    inputColor=C.g
)

set_theme(my_theme)
```

------------------------------------------------------------------------

# 🪟 Layout System

## Panel

``` python
panel(
 "Player",
 "HP:100\nMana:50"
)
```

## Columns

``` python
columns(
 [
   "Inventory",
   "Map",
   "Stats"
 ]
)
```

## Dashboard

``` python
dashboard([
 "CPU 40%",
 "RAM 62%",
 "ONLINE"
])
```

------------------------------------------------------------------------

# 🎨 Colors

``` python
print(C.r+"Red"+S.rs)
print(S.bd+"Bold"+S.rs)
```

------------------------------------------------------------------------

# 🌈 Gradients

``` python
print(rainbow("FULLUI"))
```

------------------------------------------------------------------------

# 🎬 Animations

``` python
spinner()
glitch("ERROR")
progress_fill()
loading_dots()
```

------------------------------------------------------------------------

# 🖥 UI Alias System

``` python
menu(
 t="Menu",
 st="Info",
 op=["A","B"]
)
```

Aliases:

t, st, op, bs...

------------------------------------------------------------------------

# 🔧 Utilities

``` python
clear()
pause()
```

------------------------------------------------------------------------

# 🧩 Full Import

``` python
from fullui import *
```

Everything exposed through `__all__`.

------------------------------------------------------------------------

# 📄 License

MIT License

------------------------------------------------------------------------

# 👨‍💻 Author

**Leonardo Farid Porras Bendezú**\
aka **LeonardX007**
