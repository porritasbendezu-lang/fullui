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
-   🎯 Icons added
-   🧱 Decorative boxes
-   📝 Layout System
-   🎮 Flexible alias-based system
-   ⚡ Terminal animations
-   🎭 Plug & Play Theme Engine
-   🛠 Developer Tools Panel
-   📦 Modular architecture
-   ✅ 100% editable interfaces 

------------------------------------------------------------------------

# 🆕 New in v0.3.1

## Improved guide for FULLUI info

-   Gide system added from FULLUI
-   Fixed some problems
-   Themes for all UI styles
-   Icons more clean

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
pages = [
    "FullUI es un sistema de interfaz para terminal basado en estilos, temas y animaciones.",
    
    "El sistema book() permite navegar páginas usando teclado sin necesidad de frameworks externos.",

    "Cada página puede contener texto largo y el render se encarga del layout automáticamente.",

    "FullUI combina colores, layouts y animaciones para crear experiencias CLI más vivas."
]

book(
    pages=pages,
    width=60
)

success("Fin del libro")
pause()
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

setTheme(NEON)

menu(
 t="Styled Menu",
 op=["Option A","Option B"]
)
```

Custom:

``` python
my_theme = createTheme(
    titleColor=C.r,
    inputColor=C.g
)

setTheme(my_theme)
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

# 🎨 Colors and Styles

``` python
print(C.r+"Red"+S.rs)
print(S.bd+"Bold"+S.rs)
print(C.random+"Random Color"+S.rs)
print(BG.b+"Backgrownd")
```

------------------------------------------------------------------------

# 🌈 Gradients

``` python
print(rainbow("FULLUI"))
print(G.fire+"This it a gradient text")
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
