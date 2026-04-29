"""
colors.py

ANSI color system, background colors, styles, helpers and utilities
for terminal UI applications.
"""


# =========================================================
# TEXT COLORS
# =========================================================

class C:
    """
    Foreground (text) ANSI colors.
    """

    black   = "\033[30m"
    red     = "\033[31m"
    green   = "\033[32m"
    yellow  = "\033[33m"
    blue    = "\033[38;2;0;0;255m"
    magenta = "\033[35m"
    cyan    = "\033[36m"
    white   = "\033[37m"

    orange = "\033[38;5;208m"
    pink   = "\033[38;5;213m"

    gray       = "\033[90m"
    dark_green = "\033[38;2;0;100;0m"
    light_blue = "\033[38;2;173;216;230m"
    dark_red   = "\033[38;2;128;0;32m"
    dark_cyan  = "\033[38;2;0;139;139m"
    purple     = "\033[38;2;128;0;128m"
    brown      = "\033[38;2;139;69;19m"

    # aliases (shortcuts)
    k = black
    r = red
    g = green
    y = yellow
    b = blue
    m = magenta
    c = cyan
    w = white
    o = orange
    p = pink

    gr = gray
    dg = dark_green
    lb = light_blue
    dr = dark_red
    dc = dark_cyan
    pu = purple
    br = brown


# =========================================================
# BACKGROUND COLORS
# =========================================================

class BG:
    """
    Background ANSI colors.
    """

    black   = "\033[40m"
    red     = "\033[41m"
    green   = "\033[42m"
    yellow  = "\033[43m"
    blue    = "\033[44m"
    magenta = "\033[45m"
    cyan    = "\033[46m"
    white   = "\033[47m"

    # NOTE:
    # Extended colors must use 48;2 for background (not 38;2)

    orange = "\033[48;5;208m"
    pink   = "\033[48;5;213m"

    gray       = "\033[48;5;240m"
    dark_green = "\033[48;2;0;100;0m"
    light_blue = "\033[48;2;173;216;230m"
    dark_red   = "\033[48;2;128;0;32m"
    dark_cyan  = "\033[48;2;0;139;139m"
    purple     = "\033[48;2;128;0;128m"
    brown      = "\033[48;2;139;69;19m"

    # aliases
    k = black
    r = red
    g = green
    y = yellow
    b = blue
    m = magenta
    c = cyan
    w = white
    o = orange
    p = pink

    gr = gray
    dg = dark_green
    lb = light_blue
    dr = dark_red
    dc = dark_cyan
    pu = purple
    br = brown


# =========================================================
# TEXT STYLES
# =========================================================

class S:
    """
    Text styles (formatting).
    """

    bold      = "\033[1m"
    dim       = "\033[2m"
    italic    = "\033[3m"
    underline = "\033[4m"
    blink     = "\033[5m"
    reverse   = "\033[7m"

    reset = "\033[0m"

    bd = bold
    it = italic
    ul = underline
    bl = blink
    rv = reverse
    rs = reset


# =========================================================
# RGB UTILITIES
# =========================================================

def rgb(r, g, b):
    """
    Foreground RGB color.

    Args:
        r (int): red (0-255)
        g (int): green (0-255)
        b (int): blue (0-255)
    """
    return f"\033[38;2;{r};{g};{b}m"


def bg_rgb(r, g, b):
    """
    Background RGB color.

    Args:
        r (int): red (0-255)
        g (int): green (0-255)
        b (int): blue (0-255)
    """
    return f"\033[48;2;{r};{g};{b}m"


# =========================================================
# HELPERS
# =========================================================

def success(text):
    """
    Success message style (green).
    """
    return f"{C.g}{text}{S.rs}"


def error(text):
    """
    Error message style (red bold).
    """
    return f"{C.r}{S.bd}{text}{S.rs}"


def warning(text):
    """
    Warning message style (yellow).
    """
    return f"{C.y}{text}{S.rs}"


def info(text):
    """
    Info message style (cyan).
    """
    return f"{C.c}{text}{S.rs}"


def miniTitle(text):
    """
    Small styled title header.
    """
    return f"{S.bd}{C.b}=== {text} ==={S.rs}"


# =========================================================
# BOX UTILITIES
# =========================================================

def box1(text, color=C.w):
    """
    Simple ASCII box using ┌ ┐ └ ┘.
    """
    line = "─" * (len(text) + 2)
    return (
        f"{color}┌{line}┐\n"
        f"{color}│ {text} │\n"
        f"{color}└{line}┘"
    )


def box2(text, color=C.w):
    """
    Double-line box style.
    """
    line = "═" * (len(text) + 2)
    return (
        f"{color}╔{line}╗\n"
        f"{color}║ {text} ║\n"
        f"{color}╚{line}╝"
    )


def box3(text, color=C.w):
    """
    Rounded box style.
    """
    line = "─" * (len(text) + 2)
    return (
        f"{color}╭{line}╮\n"
        f"{color}│ {text} │\n"
        f"{color}╰{line}╯"
    )


def box4(text, color=C.w):
    """
    Thick block style box.
    """
    line = "█" * (len(text) + 4)
    return (
        f"{color}{line}\n"
        f"{color}█ {text} █\n"
        f"{color}{line}"
    )


def box5(text, color=C.w):
    """
    Dotted decorative box.
    """
    line = "·" * (len(text) + 2)
    return (
        f"{color}.{line}.\n"
        f"{color}: {text} :\n"
        f"{color}'{line}'"
    )


def box6(text, color=C.w):
    """
    Solid block decorative box.
    """
    line = "■" * (len(text) + 4)
    return (
        f"{color}{line}\n"
        f"{color}■ {text} ■\n"
        f"{color}{line}"
    )


def customBox(text, box, color):
    """
    Custom box using any character.

    Args:
        text (str): content
        box (str): border character
        color: ANSI color
    """
    line = box * (len(text) + 4)
    return (
        f"{color}{line}\n"
        f"{color}{box} {text} {box}\n"
        f"{color}{line}"
    )


# =========================================================
# GRADIENT TEXT EFFECTS
# =========================================================

def rainbow(text):
    """
    Rainbow color effect per character.
    """
    colors = [C.r, C.y, C.g, C.c, C.b, C.m]
    out = ""

    for i, ch in enumerate(text):
        out += colors[i % len(colors)] + ch

    return out + S.rs


def blueGra(text):
    """
    Blue gradient text effect.
    """
    colors = [C.b, C.c, C.lb]
    out = ""

    for i, ch in enumerate(text):
        out += colors[i % len(colors)] + ch

    return out + S.rs


def redGra(text):
    """
    Red gradient text effect.
    """
    colors = [C.r, C.o, C.y]
    out = ""

    for i, ch in enumerate(text):
        out += colors[i % len(colors)] + ch

    return out + S.rs


def customGra(text, col1=C.w, col2=C.w, col3=C.w):
    """
    Custom 3-color gradient text.

    Args:
        col1, col2, col3: ANSI colors
    """
    colors = [col1, col2, col3]
    out = ""

    for i, ch in enumerate(text):
        out += colors[i % len(colors)] + ch

    return out + S.rs