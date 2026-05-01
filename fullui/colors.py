"""
colors.py

ANSI color system, background colors, styles, helpers and utilities
for terminal UI applications.

v0.3.0 ADDITIONS:
- Random colors
- Gradients that accept both RGB and ANSI colors as start/end points
- New gradient presets "G"
"""

# =========================================================
# IMPORTS
# =========================================================

import random
import re

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
    wine   = "\033[38;2;120;0;40m"

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
    return f"\033[38;2;{r};{g};{b}m"


def bg_rgb(r, g, b):
    return f"\033[48;2;{r};{g};{b}m"


# =========================================================
# BOX UTILITIES
# =========================================================

def box1(text, color=C.w):
    line = "─" * (len(text) + 2)
    return f"{color}┌{line}┐\n{color}│ {text} │\n{color}└{line}┘"


def box2(text, color=C.w):
    line = "═" * (len(text) + 2)
    return f"{color}╔{line}╗\n{color}║ {text} ║\n{color}╚{line}╝"


def box3(text, color=C.w):
    line = "─" * (len(text) + 2)
    return f"{color}╭{line}╮\n{color}│ {text} │\n{color}╰{line}╯"


def box4(text, color=C.w):
    line = "█" * (len(text) + 4)
    return f"{color}{line}\n{color}█ {text} █\n{color}{line}"


def box5(text, color=C.w):
    line = "·" * (len(text) + 2)
    return f"{color}.{line}.\n{color}: {text} :\n{color}'{line}'"


def box6(text, color=C.w):
    line = "■" * (len(text) + 4)
    return f"{color}{line}\n{color}■ {text} ■\n{color}{line}"


def customBox(text, box, color):
    line = box * (len(text) + 4)
    return f"{color}{line}\n{color}{box} {text} {box}\n{color}{line}"


# =========================================================
# GRADIENT EFFECTS
# =========================================================

def rainbow(text):
    colors = [C.r, C.y, C.g, C.c, C.b, C.m]
    return "".join(colors[i % len(colors)] + ch for i, ch in enumerate(text)) + S.rs


def blueGra(text):
    colors = [C.b, C.c, C.lb]
    return "".join(colors[i % len(colors)] + ch for i, ch in enumerate(text)) + S.rs


def redGra(text):
    colors = [C.r, C.o, C.y]
    return "".join(colors[i % len(colors)] + ch for i, ch in enumerate(text)) + S.rs


def customGra(text, *colors):
    if not colors:
        colors = (C.w,)
    return "".join(colors[i % len(colors)] + ch for i, ch in enumerate(text)) + S.rs


# =========================================================
# GRADIENT CORE
# =========================================================

def _to_rgb(color):

    if isinstance(color, tuple):
        return color

    if not isinstance(color, str):
        return (255, 255, 255)

    # ANSI RGB
    match = re.search(r'38;2;(\d+);(\d+);(\d+)', color)
    if match:
        return tuple(map(int, match.groups()))

    # ANSI 5-bit (extendido)
    match2 = re.search(r'38;5;(\d+)', color)
    if match2:
        val = int(match2.group(1))
        return (val * 5 % 255, val * 3 % 255, val * 7 % 255)

    # ANSI básico
    match_basic = re.search(r'\033\[(\d+)m', color)
    if match_basic:
        basic_map = {
            "30": (0,0,0), "31": (255,0,0), "32": (0,255,0),
            "33": (255,255,0), "34": (0,0,255),
            "35": (255,0,255), "36": (0,255,255), "37": (255,255,255),
        }
        return basic_map.get(match_basic.group(1), (255,255,255))

    return (255,255,255)


def gradientSmooth(text, start_color, end_color):

    start_rgb = _to_rgb(start_color)
    end_rgb   = _to_rgb(end_color)

    length = len(text)

    if length <= 1:
        return rgb(*start_rgb) + text + S.rs

    out = ""

    for i, ch in enumerate(text):
        r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * i / (length - 1))
        g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * i / (length - 1))
        b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * i / (length - 1))

        out += rgb(r, g, b) + ch

    return out + S.rs


# =========================================================
# RANDOM COLORS
# =========================================================

# =============== RANDOM COLORS SIMPLE ===============

def randomColor(include_basic=True, include_extended=True):

    colors = []

    if include_basic:
        colors += [C.k, C.r, C.g, C.y, C.b, C.m, C.c, C.w]

    if include_extended:
        colors += [
            C.o, C.p, C.wn,
            C.gd, C.ln, C.ng, C.eb, C.np,
            C.fo, C.sb, C.bc, C.dp, C.sg,
            C.gr, C.dg, C.lb, C.dr, C.dc, C.pu, C.br
        ]

    return random.choice(colors)

# =============== RANDOM COLORS RGB ===============

def randomRGB():
    return rgb(
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )


class _DynamicColor:
    def __init__(self, func):
        self.func = func

    def __str__(self):
        return self.func()

    def __add__(self, other):
        return str(self) + other

    def __radd__(self, other):
        return other + str(self)

    def __repr__(self):
        return self.func()


C.random = _DynamicColor(randomColor)
C.ran = C.random
C.randomRGB = _DynamicColor(randomRGB)
C.rrgb = C.randomRGB


# =========================================================
# GRADIENT PRESETS SYSTEM
# =========================================================

class _Gradient:
    def __init__(self, func):
        self.func = func

    def __add__(self, text):
        return self.func(text)

    def __radd__(self, text):
        return self.func(text)

    def __call__(self, text):
        return self.func(text)

    def __str__(self):
        return ""

    def __format__(self, format_spec):
        return ""


def _make_gradient(c1, c2):
    return _Gradient(lambda text: gradientSmooth(text, c1, c2))


class _G:
    pass


G = _G()

# presets
G.rb = _make_gradient(C.r, C.b)
G.br = _make_gradient(C.b, C.r)
G.rg = _make_gradient(C.r, C.g)
G.gb = _make_gradient(C.g, C.b)

G.fire = _make_gradient(C.r, C.y)
G.ice = _make_gradient(C.c, C.lb)
G.neon = _make_gradient(C.np, C.bc)
G.forest = _make_gradient(C.dg, C.g)
G.sunset = _make_gradient(C.o, C.r)
G.ocean = _make_gradient(C.b, C.c)
G.gold = _make_gradient(C.gd, C.y)
G.purple = _make_gradient(C.pu, C.np)

# =============== MORE PRESETS ANSI COLORS (v0.3.0) ===============

G.pinkfire   = _make_gradient(C.dp, C.fo)
G.cyber      = _make_gradient(C.eb, C.np)
G.limefire   = _make_gradient(C.ln, C.fo)
G.blood      = _make_gradient(C.dr, C.r)
G.sky        = _make_gradient(C.lb, C.c)
G.toxic      = _make_gradient(C.ng, C.ln)
G.steel      = _make_gradient(C.sg, C.gr)
G.royal      = _make_gradient(C.pu, C.gd)
G.sun        = _make_gradient(C.y, C.o)
G.deepsea    = _make_gradient(C.dc, C.b)

# =============== RGB GRADIENT PRESETS (v0.3.0) ===============

G.rgb1  = _make_gradient((255, 0, 0), (255, 255, 0))       # rojo → amarillo
G.rgb2  = _make_gradient((0, 255, 0), (0, 255, 255))       # verde → cyan
G.rgb3  = _make_gradient((0, 0, 255), (255, 0, 255))       # azul → magenta
G.rgb4  = _make_gradient((255, 0, 255), (255, 105, 180))   # magenta → rosa
G.rgb5  = _make_gradient((255, 140, 0), (255, 0, 0))       # naranja → rojo

G.rgb6  = _make_gradient((0, 255, 255), (0, 0, 255))       # cyan → azul
G.rgb7  = _make_gradient((50, 255, 80), (0, 100, 0))       # verde lima → verde oscuro
G.rgb8  = _make_gradient((255, 255, 255), (100, 100, 100)) # blanco → gris
G.rgb9  = _make_gradient((255, 20, 147), (128, 0, 128))    # rosa fuerte → morado
G.rgb10 = _make_gradient((255, 255, 0), (255, 120, 0))     # amarillo → naranja

G.rgb11 = _make_gradient((0, 0, 0), (255, 255, 255))       # negro → blanco
G.rgb12 = _make_gradient((120, 0, 40), (255, 0, 0))        # vino → rojo
G.rgb13 = _make_gradient((0, 180, 255), (0, 255, 120))     # azul eléctrico → verde neón
G.rgb14 = _make_gradient((255, 0, 120), (255, 255, 255))   # rosa → blanco
G.rgb15 = _make_gradient((0, 255, 120), (180, 0, 255))     # verde neón → púrpura

G.rgb16 = _make_gradient((255, 200, 0), (255, 50, 50))     # dorado → rojo suave
G.rgb17 = _make_gradient((0, 50, 100), (0, 255, 255))      # azul oscuro → cyan brillante
G.rgb18 = _make_gradient((30, 30, 30), (200, 200, 200))    # gris oscuro → claro
G.rgb19 = _make_gradient((255, 100, 0), (255, 0, 255))     # naranja → magenta
G.rgb20 = _make_gradient((0, 255, 200), (0, 0, 100))       # aqua → azul profundo

def randomGradient(text):
    return gradientSmooth(text, randomRGB(), randomRGB())


G.random = _Gradient(randomGradient)
G.ran = G.random