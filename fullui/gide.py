"""
gide.py

FULLUI GIDE (GUI + IDE) - Developer Tools and Registry System

v0.3.1 ADDITIONS:
- Added "Registry Inspector" to view registered themes, colors, and animations.
- Added "System Info" panel to display current theme and version.
"""

# =========================================================
# IMPORTS
# =========================================================

from .colors import C, S
from .themes import getTheme, setTheme, FIRE_STORM
from .ui import *

# =========================================================
# VERSION
# =========================================================

version = "0.3.1"

# =========================================================
# REGISTRY SYSTEM (v0.2.0)
# =========================================================

# =============== INTERNAL REGISTRY ===============

_THEME_REGISTRY = {}
_COLOR_REGISTRY = {}
_ANIMATION_REGISTRY = {}

# =============== REGISTRATION FUNCTIONS ===============

def registerTheme(name, theme):
    _THEME_REGISTRY[name] = theme

def registerColor(name, value):
    _COLOR_REGISTRY[name] = value

def registerAnim(name, func):
    _ANIMATION_REGISTRY[name] = func

# =============== INSPECTION FUNCTIONS ===============

def registrInspector():
    clear()
    title("REGISTRY INSPECTOR")

    print(C.c + "Themes:" + S.rs, len(_THEME_REGISTRY))
    print(C.c + "Colors:" + S.rs, len(_COLOR_REGISTRY))
    print(C.c + "Animations:" + S.rs, len(_ANIMATION_REGISTRY))

    pause()

# =========================================================
# SYSTEM PANEL (DEV TOOL)
# =========================================================

# =============== SYSTEM INFO ===============

def infoSystem():
    clear()
    title("SYSTEM INFO")

    print(C.c + "Theme:" + S.rs, getTheme().name)
    print(C.c + "Version:" + S.rs, version)

    pause()

# =============== UI SYSTEM ===============

def uiSystem():
    def show_info_class():
        attrs = {
            k: v for k, v in INFO.__dict__.items()
            if not k.startswith("_") and isinstance(v, str)
        }

        lines = []
        for k, v in attrs.items():
            lines.append(f"{k}  ->  {v}")

        return "\n".join(lines)

    while True:
        choice = menu(
            t="UI FUNCTIONS",
            st="FULLUI Dev Inspector",
            op=[
                "Title",
                "Subtitle",
                "Options",
                "Break Option",
                "Input",
                "Status Messages",
                "Message Box",
                "Mini Title",
                "Book Viewer",
                "Quiz System",
                "Print (p)",
                "Pause()",
                "Clear()",
                "INFO Class (aliases)"
            ],
            bt="Back",
            bs="X"
        )

        if choice is None:
            return

        # TITLE
        if choice == 1:
            title("FULLUI TITLE DEMO")

        # SUBTITLE
        elif choice == 2:
            subtitle("This is a subtitle demo")

        # OPTIONS
        elif choice == 3:
            for i in range(1, 6):
                option(f"Option {i}", num=i)

        # BREAK OPTION
        elif choice == 4:
            opbreak("Exit Demo")

        # INPUT
        elif choice == 5:
            val = uinput(prompt="Type something: ")
            p("You typed:", val)

        # STATUS MESSAGES
        elif choice == 6:
            success("Operation successful")
            error("Something failed")
            warning("This is a warning")
            info("System info message")

        # MESSAGE BOX
        elif choice == 7:
            message(
                "This is a long message rendered inside FULLUI.",
                line="=",
                width=50
            )

        # MINI TITLE
        elif choice == 8:
            miniTitle("Mini Title Example")

        # BOOK VIEWER
        elif choice == 9:
            book([
                "Page 1\nHello from FULLUI",
                "Page 2\nThis is interactive",
                "Page 3\nUse A / D / X"
            ])

        # QUIZ SYSTEM
        elif choice == 10:
            quiz(
                t="FULLUI QUIZ DEMO",
                qs=[
                    {
                        "question": "¿Qué lenguaje usa FULLUI?",
                        "options": ["Java", "Python", "C++"],
                        "correct": 2
                    },
                    {
                        "question": "¿Qué función limpia la consola?",
                        "options": ["pause()", "clear()", "p()"],
                        "correct": 2
                    },
                    {
                        "question": "¿Qué función imprime texto en FULLUI?",
                        "options": ["ConsoleLog()", "write()", "p()"],
                        "correct": 3
                    }
                ],
                twin="Perfecto",
                tf="Fallaste todo",
                tmid="Vas bien"
            )
        
        # PRINT (P)
        elif choice == 11:
            p("This is using p() like print()", 123, {"key": "value"})

        # PAUSE
        elif choice == 12:
            p("Before pause...")
            pause("👉 Press Enter to continue (this is pause)")
            p("After pause")

        # CLEAR
        elif choice == 13:
            p("This will clear in 2 seconds...")
            import time
            time.sleep(2)
            clear()
            p("Screen cleared ✔")

        # INFO CLASS
        elif choice == 14:
            menu(
                t="INFO CLASS",
                st=show_info_class(),
                op=["Back"],
                sB=False
            )

        pause()
    
# =============== ANIMATION SYSTEM ===============
    
def animationSystem():
    from . import animations as anim

    animations_list = {
        "spinner": lambda: anim.spinner("Loading", 2),
        "dot_ripple": lambda: anim.dot_ripple("Loading", 2),
        "bounce": lambda: anim.bounce("UI"),
        "matrix": lambda: anim.matrix("FULLUI"),
        "fade_in": lambda: anim.fade_in("Hello"),
        "pulse_bar": lambda: anim.pulse_bar("Loading"),
        "type_shuffle": lambda: anim.type_shuffle("FULLUI"),
        "wave": lambda: anim.wave("FULLUI"),
        "blink": lambda: anim.blink("READY"),
        "energy_pulse": lambda: anim.energy_pulse("SYSTEM"),
        "scanline": lambda: anim.scanline("Scanning"),
        "glitch": lambda: anim.glitch("ERROR"),
        "loading_dots": lambda: anim.loading_dots("Loading"),
        "progress_fill": lambda: anim.progress_fill(),
        "typing": lambda: anim.typing("Loading"),
        "countdown": lambda: anim.countdown(5),
        "success_check": lambda: anim.success_check("Success"),
        "loading_bar_wave": lambda: anim.loading_bar_wave(),
        "spinner_dots": lambda: anim.spinner_dots("Loading"),
        "spinner_bar": lambda: anim.spinner_bar("Loading"),
        "loading_blocks": lambda: anim.loading_blocks(),
        "pulse_text": lambda: anim.pulse_text("Loading"),
        "scanner": lambda: anim.scanner(),
        "reverse_type": lambda: anim.reverse_type("Loading"),
        "icon_spin": lambda: anim.icon_spin(),
        "glitch_heavy": lambda: anim.glitch_heavy("Loading"),
        "bar_wave_color": lambda: anim.bar_wave_color(),
        "shake": lambda: anim.shake("Loading"),
        "fire_text": lambda: anim.fire_text("Loading"),
        "progress_ping": lambda: anim.progress_ping(),
        "dot_matrix": lambda: anim.dot_matrix(),
        "spiral": lambda: anim.spiral("Loading"),
        "success_burst": lambda: anim.success_burst("Loading"),
    }

    animations_list.update(_ANIMATION_REGISTRY)

    names = list(animations_list.keys())

    while True:
        choice = menu(
            t="ANIMATIONS SYSTEM",
            st="Select an animation to preview",
            op=names,
            bt="Back",
            bs="X"
        )

        if choice is None:
            return

        name = names[choice - 1]

        menu(
            t="RUNNING ANIMATION",
            st=f"{name}\n\nPress ENTER to start",
            op=["Start"],
            sB=False
        )

        clear()
        title(f"RUNNING: {name}")

        try:
            animations_list[name]()
        except Exception as e:
            print(C.r + f"Error: {e}" + S.rs)

        menu(
            t="ANIMATION FINISHED",
            st=f"{name} completed",
            op=["Continue"],
            sB=False
        )

# =============== ICONS SYSTEM ===============

def iconSystem():
    from .icons import I

    categories = {
        "CHECK / STATUS": [
            "check", "error", "warning", "info", "plus", "minus"
        ],
        "ARROWS": [
            "arrow", "right", "left", "up", "down",
            "r2", "l2", "u2", "d2", "loop", "back", "curve", "swap", "sync"
        ],
        "SHAPES": [
            "square", "square_empty", "square_small", "square_small_empty",
            "circle", "circle_empty", "circle_dot", "circle_half",
            "triangle_up", "triangle_down", "triangle_right", "triangle_left",
            "diamond", "diamond_empty"
        ],
        "STARS": [
            "star", "star_empty", "star_small", "star_big", "sparkle"
        ],
        "BOX": [
            "h", "v", "hd", "vd",
            "tl", "trc", "bl", "br",
            "tee_u", "tee_d", "tee_l", "tee_r", "cross"
        ],
        "BLOCKS": [
            "block", "dark", "mid", "light"
        ],
        "TEXT": [
            "bullet", "bullet2", "dot", "dash", "ellipsis"
        ],
        "NUMBERS": [f"n{i}" for i in range(0, 21)],
        "MATH": [
            "eq", "neq", "approx", "gt", "lt_", "gte", "lte",
            "infy", "sum", "prod", "root"
        ],
        "SYSTEM": [
            "gear", "power", "reload", "sync2", "link", "unlink"
        ],
        "TIME": [
            "clock", "timer", "hourglass"
        ],
        "MEDIA": [
            "play", "pause", "stop", "record", "next", "prev"
        ],
        "EXTRA": [
            "flag", "anchor", "scissors", "pencil",
            "check2", "cross2",
            "heart", "spade", "club", "diamond_card",
            "music", "music2",
            "sun", "cloud", "umbrella", "snow",
            "phone", "peace", "yin"
        ],
        "ASCII": [
            "ack", "acr", "aar"
        ]
    }

    def render_category(name, keys):
        lines = []

        row = []
        for i, k in enumerate(keys, 1):
            icon = getattr(I, k)
            row.append(f"{icon} {k}")

            if i % 4 == 0:
                lines.append("   ".join(row))
                row = []

        if row:
            lines.append("   ".join(row))

        return "\n".join(lines)

    while True:
        choice = menu(
            t="ICONS SYSTEM",
            st="Browse icon categories",
            op=list(categories.keys()),
            bt="Exit",
            bs="X"
        )

        if choice is None:
            return

        cat_name = list(categories.keys())[choice - 1]
        keys = categories[cat_name]

        preview = render_category(cat_name, keys)

        menu(
            t=cat_name,
            st=preview,
            op=["Back"],
            sB=False
        )

# =============== LAYOUT SYSTEM ===============

def layoutSystem():
    clear()
    from .layouts import useLayout, _LAYOUT_PRESETS

    layouts = list(_LAYOUT_PRESETS.keys())

    print("\n=== FULLUI LAYOUTS DEMO ===")
    print("Press ENTER to continue...\n")

    for i, name in enumerate(layouts, 1):
        print(f"\n--- [{i}/{len(layouts)}] {name.upper()} ---\n")

        if name == "sidebar":
            useLayout(
                "sidebar",
                "• Home\n• Settings\n• Exit",
                "Welcome to FULLUI\nSidebar layout demo"
            )

        elif name == "dashboard":
            useLayout(
                "dashboard",
                [("CPU", "32%"), ("RAM", "64%"), ("DISK", "80%")]
            )

        elif name == "split":
            useLayout(
                "split",
                "Left content\nHello world",
                "Right content\nFULLUI Layouts"
            )

        elif name == "stack":
            useLayout(
                "stack",
                "First block",
                "Second block",
                "Third block"
            )

        elif name == "hero":
            useLayout(
                "hero",
                "FULLUI",
                "Beautiful terminal UI"
            )

        else:
            print(f"(No preview for {name})")

        input("\nPress ENTER for next layout...")

    print("\n✔ End of layouts demo\n")

# =============== THEME SYSTEM ===============

def themeSystem():
    from .themes import (
        DEFAULT, DARK, NEON, FIRE, ICE,
        HACKER, VOID, ELECTRIC, NIGHT,
        ALERT, FROST, NATURE, DEV, GAMER, BRUTAL,
        SUNSET, OCEAN, FOREST, CYBERPUNK, LAVENDER,
        GOLD, ROSE, MIDNIGHT, EMBER, MINT, CRIMSON_GOLD,
        AQUA_LIME, PURPLE_PINK, BLUE_ORANGE, EMERALD_GOLD,
        RED_BLACK, SKY_PURPLE, MANGO_FIRE, TEAL_ROSE,
        INDIGO_CYAN,
        CHRISTMAS, HALLOWEEN, VALENTINE,
        EASTER, NEW_YEAR, BIRTHDAY, CARNIVAL, INDEPENDENCE,
        SPRING_FEST, WINTER_FEST, OKTOBERFEST, DIWALI,
        FIRE_STORM, ICE_NEON, CYBER_VOID, FOREST_LIGHT, COSMIC_GOLD,
        CYBER_NEON, TOXIC_WASTE, BLOOD_MOON, DEEP_OCEAN, SUNCORE,
        ROYAL_LUX, STEEL_CORE, PINK_VIBE, NIGHT_GLITCH, AURORA
    )

    themes = [
        DEFAULT, DARK, NEON, FIRE, ICE,
        HACKER, VOID, ELECTRIC, NIGHT,
        ALERT, FROST, NATURE, DEV, GAMER, BRUTAL,
        SUNSET, OCEAN, FOREST, CYBERPUNK, LAVENDER,
        GOLD, ROSE, MIDNIGHT, EMBER, MINT, CRIMSON_GOLD,
        AQUA_LIME, PURPLE_PINK, BLUE_ORANGE, EMERALD_GOLD,
        RED_BLACK, SKY_PURPLE, MANGO_FIRE, TEAL_ROSE,
        INDIGO_CYAN,
        CHRISTMAS, HALLOWEEN, VALENTINE,
        EASTER, NEW_YEAR, BIRTHDAY, CARNIVAL, INDEPENDENCE,
        SPRING_FEST, WINTER_FEST, OKTOBERFEST, DIWALI,
        FIRE_STORM, ICE_NEON, CYBER_VOID, FOREST_LIGHT, COSMIC_GOLD,
        CYBER_NEON, TOXIC_WASTE, BLOOD_MOON, DEEP_OCEAN, SUNCORE,
        ROYAL_LUX, STEEL_CORE, PINK_VIBE, NIGHT_GLITCH, AURORA
        ] + list(_THEME_REGISTRY.values())

    index = 0

    setTheme(themes[index])

    while True:
        current = themes[index]

        choice = menu(
            t="THEME CAROUSEL",
            st=f"{current.name} ({index + 1}/{len(themes)})",
            op=[
                "Next Theme",
                "Previous Theme",
                "Select Theme"
            ],
            bt="Exit",
            bs="X"
        )

        if choice is None:
            return

        if choice == 1:
            index = (index + 1) % len(themes)
            setTheme(themes[index])

        elif choice == 2:
            index = (index - 1) % len(themes)
            setTheme(themes[index])

        elif choice == 3:
            menu(
                t="THEME LOCKED",
                st=f"{current.name} selected",
                op=["Continue"],
                sB=False
            )

# =============== COLOR SYSTEM ===============

def colorSystem():
    clear()
    title("COLOR INSPECTOR")

    # Obtener atributos válidos
    colors = {k: v for k, v in C.__dict__.items() if not k.startswith("_")}

    # Agrupar por valor
    grouped = {}

    for name, value in colors.items():
        grouped.setdefault(value, []).append(name)

    # Mostrar agrupados
    for value, names in grouped.items():
        main = None
        alias = None

        # Elegir nombre largo como principal y corto como alias
        for n in names:
            if len(n) > 2:
                main = n
            else:
                alias = n

        if main and alias:
            print(value + f"{main} = {alias}" + S.rs)
        else:
            # fallback si no hay alias claro
            print(value + ", ".join(names) + S.rs)

    # Colores registrados manualmente
    for k, v in _COLOR_REGISTRY.items():
        print(v + f"{k} (custom)" + S.rs)
    p("")
    pause()

setTheme(FIRE_STORM)

# =============== SYSTEM VIEW ===============

def gideFULLUI():
    while True:
        choice = menu(
                t = "FULLUI SYSTEM PANEL".center(80),
                st = "Developer Tools",
                op = [
                    "Colors",
                    "Icons",
                    "Themes",
                    "Layouts",
                    "Animations",
                    "UI",
                    "Registry Inspector",
                    "System Info"
                ],
                tw = 80,
            )
        
        if choice == 1:
            colorSystem()
        elif choice == 2:
            iconSystem()
        elif choice == 3:
            themeSystem()
        elif choice == 4:
            layoutSystem()
        elif choice == 5:
            animationSystem()
        elif choice == 6:
            uiSystem()
        elif choice == 7:
            registrInspector()
        elif choice == 8:
            infoSystem()
        elif choice is None:
            break
