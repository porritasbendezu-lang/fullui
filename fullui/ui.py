"""
ui.py

Core interface system for FULLUI.

Provides:
- Console menus
- Titles and subtitles
- Options rendering
- Input handling
- Improved CLI flow utilities (validation + loop)

🔥 v0.2.0 ADDITIONS:
- System Panel (Developer Tools)
- Theme / Color / Animation Inspectors
- Registry System (extensibility)
- System Info Panel
"""

# =========================================================
# IMPORTS
# =========================================================

from .colors import C, S, BG
from .themes import apply_theme, get_theme, set_theme
import os
import time

# =========================================================
# INTERNAL REGISTRY (v0.2.0)
# =========================================================

_THEME_REGISTRY = {}
_COLOR_REGISTRY = {}
_ANIMATION_REGISTRY = {}

# =========================================================
# IDENTIFIERS (ALIAS SYSTEM)
# =========================================================

class I:
    """
    Alias registry for menu parameters.
    """

    t = "titleText"
    titleText = "titleText"

    st = "subtitleText"
    subtitleText = "subtitleText"

    op = "options"
    options = "options"

    sT = "showTitle"
    showTitle = "showTitle"

    sST = "showSubtitle"
    showSubtitle = "showSubtitle"

    tm = "titleMargins"
    titleMargins = "titleMargins"

    tw = "titleWidth"
    titleWidth = "titleWidth"

    tcm = "titleColorMargins"
    titleColorMargins = "titleColorMargins"

    tct = "titleColorText"
    titleColorText = "titleColorText"

    ts = "titleStyle"
    titleStyle = "titleStyle"

    sl = "subtitleLines"
    subtitleLines = "subtitleLines"

    sw = "subtitleWidth"
    subtitleWidth = "subtitleWidth"

    sc = "subtitleColor"
    subtitleColor = "subtitleColor"

    ss = "subtitleStyle"
    subtitleStyle = "subtitleStyle"

    k1 = "key1"
    key1 = "key1"

    k2 = "key2"
    key2 = "key2"

    oct = "optionsColorText"
    optionsColorText = "optionsColorText"

    ock = "optionsColorKeys"
    optionsColorKeys = "optionsColorKeys"

    os = "optionsStyle"
    optionsStyle = "optionsStyle"

    sB = "showBreak"
    showBreak = "showBreak"

    bt = "breakText"
    breakText = "breakText"

    # 🔥 FIX: typo corregido
    bs = "breakSymbol"
    breakSymbol = "breakSymbol"

    bct = "breakColorText"
    breakColorText = "breakColorText"

    bck = "breakColorKeys"
    breakColorKeys = "breakColorKeys"

    bst = "breakStyle"
    breakStyle = "breakStyle"

    ic = "inputColor"
    inputColor = "inputColor"

    isty = "inputStyle"
    inputStyle = "inputStyle"

    p = "prompt"
    prompt = "prompt"

# =========================================================
# UTILITIES
# =========================================================

line_break = "\n"
lb = line_break

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[H", end="")

def pause():
    input(C.b + S.bd + "Press Enter..." + S.rs)

# =========================================================
# UI COMPONENTS
# =========================================================

def title(text="", margins="=", width=30, colorMargins=C.r, colorText=C.w, style=S.bd):
    line = margins * width
    print(f"{colorMargins}{style}{line}{S.rs}")
    print(f"{colorText}{style}{text.center(width)}{S.rs}")
    print(f"{colorMargins}{style}{line}{S.rs}")

def subtitle(text="", lines="-", numLines=10, width=30, color=C.w, style=S.it):
    print(color + style + ((lines)*numLines + " " + text + " " + (lines)*numLines).center(width) + S.rs)

def option(text="", key1="[", key2="]", num=1, colorText=C.w, colorKeys=C.g, style=S.bd):
    print(f"{colorKeys}{style}{key1}{num}{key2}{S.rs} {colorText}{text}{S.rs}")

def opbreak(text="Salir", key1="[", key2="]", symbol="X", colorText=C.w, colorKeys=C.r, style=S.bd):
    print(f"{colorKeys}{style}{key1}{symbol}{key2}{S.rs} {colorText}{text}{S.rs}")

# =========================================================
# REGISTRY SYSTEM (v0.2.0)
# =========================================================

def register_theme(name, theme):
    _THEME_REGISTRY[name] = theme

def register_color(name, value):
    _COLOR_REGISTRY[name] = value

def register_animation(name, func):
    _ANIMATION_REGISTRY[name] = func

# =========================================================
# SYSTEM PANEL (DEV TOOL - PRO)
# =========================================================

def system_panel():
    """
    FULLUI Developer Panel
    """

    while True:
        choice = menu(
            t="FULLUI SYSTEM PANEL",
            st="Developer Tools",
            op=[
                "Themes Manager",
                "Colors Inspector",
                "Animations Preview",
                "System Info",
                "Registry Inspector"
            ],
            bt="Exit Debug",
            bs="X"
        )

        if choice == 1:
            themes_manager()
        elif choice == 2:
            show_colors()
        elif choice == 3:
            animations_preview()
        elif choice == 4:
            system_info()
        elif choice == 5:
            registry_inspector()
        elif choice is None:
            break

# =========================================================
# THEMES MANAGER
# =========================================================

def themes_manager():
    from .themes import (
        DEFAULT, DARK, NEON, FIRE, ICE,
        HACKER, VOID, ELECTRIC, NIGHT,
        ALERT, FROST, NATURE, DEV, GAMER, BRUTAL
    )

    themes = [
        DEFAULT, DARK, NEON, FIRE, ICE,
        HACKER, VOID, ELECTRIC, NIGHT,
        ALERT, FROST, NATURE, DEV, GAMER, BRUTAL
    ] + list(_THEME_REGISTRY.values())

    while True:
        clear()
        title("THEMES MANAGER")

        print(C.c + "Active Theme:" + S.rs, C.y + get_theme().name + S.rs)
        print()

        for i, t in enumerate(themes, 1):
            print(f"{C.g}[{i}]{S.rs} {C.w}{t.name}{S.rs}")

        print("\n" + C.r + "[X] Back" + S.rs)

        choice = input("\n> ")

        if choice.lower() == "x":
            return

        if choice.isdigit():
            n = int(choice)

            if 1 <= n <= len(themes):
                selected = themes[n - 1]

                clear()
                title("THEME PREVIEW")

                print(selected.titleColor + selected.titleStyle + "Title Example" + S.rs)
                print(selected.subtitleColor + selected.subtitleStyle + "Subtitle Example" + S.rs)
                print(selected.optionKeyColor + "[1]" + S.rs, selected.optionColor + "Option Example" + S.rs)

                print("\n" + C.y + "Apply this theme? (y/n)" + S.rs)

                if input("> ").lower() == "y":
                    set_theme(selected)
                    print(C.g + "Theme applied!" + S.rs)
                    time.sleep(1)

# =========================================================
# ANIMATIONS PREVIEW
# =========================================================

def animations_preview():
    from . import animations as anim

    animations_list = {
        "spinner": lambda: anim.spinner("Loading", 2),
        "dot_ripple": lambda: anim.dot_ripple("Loading", 2),
        "bounce": lambda: anim.bounce("UI"),
        "matrix": lambda: anim.matrix("FULLUI"),
        "fade_in": lambda: anim.fade_in("Hello"),
        "pulse_bar": lambda: anim.pulse_bar(50),
        "type_shuffle": lambda: anim.type_shuffle("FULLUI"),
        "wave": lambda: anim.wave("FULLUI"),
        "blink": lambda: anim.blink("READY"),
        "energy_pulse": lambda: anim.energy_pulse("SYSTEM"),
        "scanline": lambda: anim.scanline("Scanning"),
        "glitch": lambda: anim.glitch("ERROR")
    }

    animations_list.update(_ANIMATION_REGISTRY)

    while True:
        clear()
        title("ANIMATIONS PREVIEW")

        for i, name in enumerate(animations_list.keys(), 1):
            print(f"{C.c}[{i}]{S.rs} {name}")

        print("\n" + C.r + "[X] Back" + S.rs)

        choice = input("\n> ")

        if choice.lower() == "x":
            return

        if choice.isdigit():
            n = int(choice)

            if 1 <= n <= len(animations_list):
                clear()
                name = list(animations_list.keys())[n - 1]

                title(f"RUNNING: {name}")

                try:
                    animations_list[name]()
                except Exception as e:
                    print(C.r + f"Error: {e}" + S.rs)

                pause()

# =========================================================
# COLORS INSPECTOR
# =========================================================

def show_colors():
    clear()
    title("COLOR INSPECTOR")

    for k, v in C.__dict__.items():
        if not k.startswith("_"):
            print(v + k + S.rs)

    for k, v in _COLOR_REGISTRY.items():
        print(v + k + S.rs)

    pause()

# =========================================================
# REGISTRY INSPECTOR
# =========================================================

def registry_inspector():
    clear()
    title("REGISTRY INSPECTOR")

    print(C.c + "Themes:" + S.rs, len(_THEME_REGISTRY))
    print(C.c + "Colors:" + S.rs, len(_COLOR_REGISTRY))
    print(C.c + "Animations:" + S.rs, len(_ANIMATION_REGISTRY))

    pause()

# =========================================================
# SYSTEM INFO
# =========================================================

def system_info():
    clear()
    title("SYSTEM INFO")

    print(C.c + "Theme:" + S.rs, get_theme().name)
    print(C.c + "Version:" + S.rs, "0.2.0")

    pause()

# =========================================================
# MAIN MENU
# =========================================================

def menu(**kwargs):

    alias_map = {
        "t": "titleText",
        "st": "subtitleText",
        "op": "options",
        "sT": "showTitle",
        "sST": "showSubtitle",
        "tm": "titleMargins",
        "tw": "titleWidth",
        "tcm": "titleColorMargins",
        "tct": "titleColorText",
        "ts": "titleStyle",
        "sl": "subtitleLines",
        "snl": "subtitleNumberLines",
        "sw": "subtitleWidth",
        "sc": "subtitleColor",
        "ss": "subtitleStyle",
        "k1": "key1",
        "k2": "key2",
        "oct": "optionsColorText",
        "ock": "optionsColorKeys",
        "os": "optionsStyle",
        "sB": "showBreak",
        "bt": "breakText",
        "bs": "breakSymbol",
        "bct": "breakColorText",
        "bck": "breakColorKeys",
        "bst": "breakStyle",
        "ic": "inputColor",
        "isty": "inputStyle",
        "p": "prompt"
    }

    normalized = {alias_map.get(k, k): v for k, v in kwargs.items()}
    normalized = apply_theme(normalized)

    while True:
        clear()

        options = normalized.get("options", [])
        breakSymbol = normalized.get("breakSymbol", "X")

        # =====================================================
        # TITLE (🔥 FIXED)
        # =====================================================

        if normalized.get("showTitle", True):
            title(
                normalized.get("titleText", ""),
                normalized.get("titleMargins", "="),
                normalized.get("titleWidth", 30),
                normalized.get("titleColorMargins", C.r),  # ✅ FIX
                normalized.get("titleColorText", C.w),
                normalized.get("titleStyle", S.bd)
            )

        # =====================================================
        # SUBTITLE
        # =====================================================

        if normalized.get("showSubtitle", True) and normalized.get("subtitleText"):
            subtitle(
                normalized.get("subtitleText", ""),
                normalized.get("subtitleLines", "-"),
                normalized.get("subtitleNumberLines", 5),
                normalized.get("subtitleWidth", 30),
                normalized.get("subtitleColor", C.w),
                normalized.get("subtitleStyle", S.it)
            )

        print()

        # =====================================================
        # OPTIONS
        # =====================================================

        for i, opt in enumerate(options, 1):
            option(
                opt,
                normalized.get("key1", "["),
                normalized.get("key2", "]"),
                i,
                normalized.get("optionsColorText", C.w),
                normalized.get("optionsColorKeys", C.g),
                normalized.get("optionsStyle", S.bd)
            )

        # =====================================================
        # BREAK (🔥 YA SOPORTA THEME)
        # =====================================================

        if normalized.get("showBreak", True):
            print()
            opbreak(
                normalized.get("breakText", "Salir"),
                normalized.get("key1", "["),
                normalized.get("key2", "]"),
                breakSymbol,
                normalized.get("breakColorText", C.w),
                normalized.get("breakColorKeys", C.r),
                normalized.get("breakStyle", S.bd)
            )

        # =====================================================
        # INPUT
        # =====================================================

        choice = input(
            f"{normalized.get('inputColor', C.c)}"
            f"{normalized.get('inputStyle', S.bd)}\n"
            f"{normalized.get('prompt', '> ')}{S.rs}"
        )

        if normalized.get("showBreak", True) and choice.lower() == breakSymbol.lower():
            return None

        if choice.isdigit():
            n = int(choice)
            if 1 <= n <= len(options):
                return n

        print(C.r + "Invalid option" + S.rs)
        time.sleep(1)