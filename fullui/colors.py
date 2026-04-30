"""
colors.py

ANSI color system, background colors, styles, helpers and utilities
for terminal UI applications.

v0.2.3 ADDITIONS:
- Remove funtions and pass to ui.py functions
- Custom gradients with multiple colors
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
    wine = "\033[38;2;120;0;40m"

    gray       = "\033[90m"
    dark_green = "\033[38;2;0;100;0m"
    light_blue = "\033[38;2;173;216;230m"
    dark_red   = "\033[38;2;128;0;32m"
    dark_cyan  = "\033[38;2;0;139;139m"
    purple     = "\033[38;2;128;0;128m"
    brown      = "\033[38;2;139;69;19m"

    # =============== NEW COLORS (v2.0.0) ===============

    gold          = "\033[38;2;212;175;55m"
    lime          = "\033[38;2;50;255;80m"
    neon_green    = "\033[38;2;0;255;120m"
    electric_blue = "\033[38;2;0;180;255m"
    neon_purple   = "\033[38;2;180;0;255m"
    fire_orange   = "\033[38;2;255;120;0m"
    soft_black    = "\033[38;2;20;20;20m"
    bright_cyan   = "\033[38;2;0;255;255m"
    deep_pink     = "\033[38;2;255;20;147m"
    steel_gray    = "\033[38;2;100;100;110m"

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
    wn = wine

    gd = gold
    ln = lime
    ng = neon_green
    eb = electric_blue
    np = neon_purple
    fo = fire_orange
    sb = soft_black
    bc = bright_cyan
    dp = deep_pink
    sg = steel_gray

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

    orange = "\033[48;5;208m"
    pink   = "\033[48;5;213m"

    gray       = "\033[48;5;240m"
    dark_green = "\033[48;2;0;100;0m"
    light_blue = "\033[48;2;173;216;230m"
    dark_red   = "\033[48;2;128;0;32m"
    dark_cyan  = "\033[48;2;0;139;139m"
    purple     = "\033[48;2;128;0;128m"
    brown      = "\033[48;2;139;69;19m"

    # =============== NEW BACKGROWNDS COLORS (v0.2.0) ===============

    gold          = "\033[48;2;212;175;55m"
    lime          = "\033[48;2;50;255;80m"
    neon_green    = "\033[48;2;0;255;120m"
    electric_blue = "\033[48;2;0;180;255m"
    neon_purple   = "\033[48;2;180;0;255m"
    fire_orange   = "\033[48;2;255;120;0m"
    soft_black    = "\033[48;2;20;20;20m"
    bright_cyan   = "\033[48;2;0;255;255m"
    deep_pink     = "\033[48;2;255;20;147m"
    steel_gray    = "\033[48;2;100;100;110m"

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


def customGra(text, *colors):
    """
    Custom gradient text with unlimited colors.

    Args:
        *colors: any number of ANSI colors
    """

    if not colors:
        colors = (C.w,)

    out = ""

    for i, ch in enumerate(text):
        out += colors[i % len(colors)] + ch

    return out + S.rs