"""
ui.py

Core interface system for FULLUI.

Provides:
- Console menus
- Titles and subtitles
- Options rendering
- Input handling
- Improved CLI flow utilities (validation + loop)
"""


# =========================================================
# IMPORTS
# =========================================================

from .colors import C, S, BG
from .themes import apply_theme  # 🔥 NEW: apply themes automatically
import os


# =========================================================
# IDENTIFIERS (ALIAS SYSTEM)
# =========================================================

class I:
    """
    Alias registry for menu parameters.
    Allows short or long keys interchangeably.
    """

    # TEXT
    t = "titleText"
    titleText = "titleText"

    st = "subtitleText"
    subtitleText = "subtitleText"

    op = "options"
    options = "options"

    # STRUCTURE
    sT = "showTitle"
    showTitle = "showTitle"

    sST = "showSubtitle"
    showSubtitle = "showSubtitle"

    # TITLE
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

    # SUBTITLE
    sl = "subtitleLines"
    subtitleLines = "subtitleLines"

    sw = "subtitleWidth"
    subtitleWidth = "subtitleWidth"

    sc = "subtitleColor"
    subtitleColor = "subtitleColor"

    ss = "subtitleStyle"
    subtitleStyle = "subtitleStyle"

    # OPTIONS
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

    # BREAK
    sB = "showBreak"
    showBreak = "showBreak"

    bt = "breakText"
    breakText = "breakText"

    bs = "breakSimbol"
    breakSimbol = "breakSimbol"

    bct = "breakColorText"
    breakColorText = "breakColorText"

    bck = "breakColorKeys"
    breakColorKeys = "breakColorKeys"

    bst = "breakStyle"
    breakStyle = "breakStyle"

    # INPUT
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
    """
    Clear terminal screen (cross-platform).
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def pause():
    """
    Pause execution until user presses Enter.
    """
    input(C.b + S.bd + "Press Enter..." + S.rs)


# =========================================================
# UI COMPONENTS
# =========================================================

def title(
    text="",
    margins="=",
    width=30,
    colorMargins=C.r,
    colorText=C.w,
    style=S.bd
):
    """
    Render a styled title header.

    🔥 FIX:
    Now uses real width for proper centering.
    """

    line = margins * width

    print(f"{colorMargins}{style}{line}{S.rs}")
    print(f"{colorText}{style}{text.center(width)}{S.rs}")
    print(f"{colorMargins}{style}{line}{S.rs}")


def subtitle(
    text="",
    lines="-",
    numLines=1,
    width=30,
    color=C.w,
    style=S.it
):
    """
    Render a subtitle line.
    """

    line = lines * numLines

    print(
        f"{color}{style}"
        f"{(line + ' ' + text + ' ' + line).center(width)}"
        f"{S.rs}"
    )


def option(
    text="",
    key1="[",
    key2="]",
    num=1,
    colorText=C.w,
    colorKeys=C.g,
    style=S.bd
):
    """
    Render a menu option line.
    """

    print(
        f"{colorKeys}{style}{key1}{num}{key2}{S.rs} "
        f"{colorText}{text}{S.rs}"
    )


def opbreak(
    text="Salir",
    key1="[",
    key2="]",
    simbol="X",
    colorText=C.w,
    colorKeys=C.r,
    style=S.bd
):
    """
    Render exit/break option.
    """

    print(
        f"{colorKeys}{style}{key1}{simbol}{key2}{S.rs} "
        f"{colorText}{text}{S.rs}"
    )


# =========================================================
# MAIN MENU SYSTEM
# =========================================================

def menu(**kwargs):
    """
    Main interactive menu system.

    🔥 IMPROVED:
    - Theme auto-application
    - Input validation
    - Loop until valid choice
    """

    # -----------------------------------------------------
    # ALIAS NORMALIZATION
    # -----------------------------------------------------

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
        "bs": "breakSimbol",
        "bct": "breakColorText",
        "bck": "breakColorKeys",
        "bst": "breakStyle",

        "ic": "inputColor",
        "isty": "inputStyle",
        "p": "prompt"
    }

    normalized = {
        alias_map.get(k, k): v
        for k, v in kwargs.items()
    }

    # 🔥 NEW: Apply theme automatically
    normalized = apply_theme(normalized)

    # -----------------------------------------------------
    # CONFIG VALUES
    # -----------------------------------------------------

    titleText = normalized.get("titleText", "")
    subtitleText = normalized.get("subtitleText", "")
    options = normalized.get("options", [])

    showTitle = normalized.get("showTitle", True)
    showSubtitle = normalized.get("showSubtitle", True)

    titleMargins = normalized.get("titleMargins", "=")
    titleWidth = normalized.get("titleWidth", 30)
    titleColorMargins = normalized.get("titleColorMargins", C.r)
    titleColorText = normalized.get("titleColorText", C.w)
    titleStyle = normalized.get("titleStyle", S.bd)

    subtitleLines = normalized.get("subtitleLines", "-")
    subtitleWidth = normalized.get("subtitleWidth", 30)
    subtitleColor = normalized.get("subtitleColor", C.w)
    subtitleStyle = normalized.get("subtitleStyle", S.it)

    key1 = normalized.get("key1", "[")
    key2 = normalized.get("key2", "]")

    optionsColorText = normalized.get("optionsColorText", C.w)
    optionsColorKeys = normalized.get("optionsColorKeys", C.g)
    optionsStyle = normalized.get("optionsStyle", S.bd)

    showBreak = normalized.get("showBreak", True)
    breakText = normalized.get("breakText", "Salir")
    breakSimbol = normalized.get("breakSimbol", "X")
    breakColorText = normalized.get("breakColorText", C.w)
    breakColorKeys = normalized.get("breakColorKeys", C.r)
    breakStyle = normalized.get("breakStyle", S.bd)

    inputColor = normalized.get("inputColor", C.c)
    inputStyle = normalized.get("inputStyle", S.bd)
    prompt = normalized.get("prompt", "> ")

    # -----------------------------------------------------
    # LOOP (🔥 NEW)
    # -----------------------------------------------------

    while True:

        clear()

        # RENDER UI
        if showTitle:
            title(
                titleText,
                titleMargins,
                titleWidth,
                titleColorMargins,
                titleColorText,
                titleStyle
            )

        if showSubtitle and subtitleText:
            subtitle(
                subtitleText,
                subtitleLines,
                3,
                subtitleWidth,
                subtitleColor,
                subtitleStyle
            )

        print()

        for i, opt in enumerate(options, 1):
            option(
                opt,
                key1,
                key2,
                i,
                optionsColorText,
                optionsColorKeys,
                optionsStyle
            )

        if showBreak:
            print()
            opbreak(
                breakText,
                key1,
                key2,
                breakSimbol,
                breakColorText,
                breakColorKeys,
                breakStyle
            )

        # -------------------------------------------------
        # INPUT
        # -------------------------------------------------

        choice = input(
            f"{inputColor}{inputStyle}\n{prompt}{S.rs}"
        )

        # -------------------------------------------------
        # VALIDATION (🔥 NEW)
        # -------------------------------------------------

        if showBreak and choice.lower() == breakSimbol.lower():
            return "break"

        if choice.isdigit():
            num = int(choice)
            if 1 <= num <= len(options):
                return num

        # Error feedback
        print(C.r + "Invalid option!" + S.rs)
        pause()