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
-   📝 Layout System
-   🎮 Flexible alias-based system
-   ⚡ Terminal animations
-   🎭 Plug & Play Theme Engine
-   🛠 Developer Tools Panel
-   📦 Modular architecture
-   ✅ 100% editable interfaces 

------------------------------------------------------------------------

# 🆕 New in v0.2.2

## Improvements & Refinements

-   Fixed some problems
-   Functions arranged in scripts
-   More flexible custom color gradients
-   Internal optimizations
-   Functions implemented to create books and quizzes

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

# 🧠 Book Behavior

-   Pages interactive for commands
-   Long texts
-   Layout system

``` python
choice = book(
    pages = [
        "TEXT1"
        "TEXT2"
        "TEXT3"
    ]
    width= 60 
)
```

------------------------------------------------------------------------

# 🧠 Quiz Behavior

-   Multiples uestions
-   Correct answer system
-   Result layout

``` python
quiz(
    t="QUIZ",
    
    qs=[
        {
            "question": "¿...?",
            "options": ["A", "B", "C"],
            "correct": 2
        },
        {
            "question": "¿?",
            "options": ["1", "2", "3"],
            "correct": 2
        },
        {
            "question": "¿?",
            "options": ["@", "#", "&"],
            "correct": 1
        }
    ],

    twn="¡Wonderfull!",
    tf="Fail",
    tmid="no bad"
)
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

# 📝 Layout System

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
line_break # is "\n"
lb = line_break

p() #Print
clear() #Clear Console
pause() #Input pause
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
