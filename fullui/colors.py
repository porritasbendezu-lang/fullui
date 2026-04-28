# ===== COLORES DE TEXTO =====

class C:
    black   = "\033[30m"
    red     = "\033[31m"
    green   = "\033[32m"
    yellow  = "\033[33m"
    blue    = "\033[38;2;0;0;255m"
    magenta = "\033[35m"
    cyan    = "\033[36m"
    white   = "\033[37m"
    orange = "\033[38;5;208m"
    pink = "\033[38;5;213m"
    gray = "\033[90m"
    dark_green = "\033[38;2;0;100;0m"
    light_blue = "\033[38;2;173;216;230m"
    dark_red = "\033[38;2;128;0;32m"
    dark_cyan = "\033[38;2;0;139;139m"
    purple = "\033[38;2;128;0;128m"
    brown = "\033[38;2;139;69;19m"

    # alias cortos
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


# ===== COLORES DE FONDO =====

class BG:
    black   = "\033[40m"
    red     = "\033[41m"
    green   = "\033[42m"
    yellow  = "\033[43m"
    blue    = "\033[44m"
    magenta = "\033[45m"
    cyan    = "\033[46m"
    white   = "\033[47m"
    orange = "\033[38;5;208m"
    pink = "\033[38;5;213m"
    gray = "\033[90m"
    dark_green = "\033[38;2;0;100;0m"
    light_blue = "\033[38;2;173;216;230m"
    dark_red = "\033[38;2;128;0;32m"
    dark_cyan = "\033[38;2;0;139;139m"
    purple = "\033[38;2;128;0;128m"
    brown = "\033[38;2;139;69;19m"

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


# ===== ESTILOS =====

class S:
    bold      = "\033[1m"
    dim       = "\033[2m"
    italic    = "\033[3m"
    underline = "\033[4m"
    blink     = "\033[5m"
    reverse   = "\033[7m"
    reset     = "\033[0m"

    bd = bold
    it = italic
    ul = underline
    bl = blink
    rv = reverse
    rs = reset


# ===== FUNCIONES RGB =====

def rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"


def bg_rgb(r, g, b):
    return f"\033[48;2;{r};{g};{b}m"


# ===== HELPERS =====

def success(text):
    return f"{C.g}{text}{S.rs}"


def error(text):
    return f"{C.r}{S.bd}{text}{S.rs}"


def warning(text):
    return f"{C.y}{text}{S.rs}"


def info(text):
    return f"{C.c}{text}{S.rs}"


def miniTitle(text):
    return f"{S.bd}{C.b}=== {text} ==={S.rs}"


# ===== CAJAS =====

def box1(text, color = C.w):
    line = "─" * (len(text)+2)
    return (
        f"{color}┌{line}┐\n"
        f"{color}│ {text} │\n"
        f"{color}└{line}┘"
    )

def box2(text, color = C.w):
    line = "═" * (len(text)+2)
    return (
        f"{color}╔{line}╗\n"
        f"{color}║ {text} ║\n"
        f"{color}╚{line}╝"
    )

def box3(text, color = C.w):
    line = "─" * (len(text)+2)
    return (
        f"{color}╭{line}╮\n"
        f"{color}│ {text} │\n"
        f"{color}╰{line}╯"
    )

def box4(text, color = C.w):
    line = "█" * (len(text)+4)
    return (
        f"{color}{line}\n"
        f"{color}█ {text} █\n"
        f"{color}{line}"
    )

def box5(text, color = C.w):
    line = "·" * (len(text)+2)
    return (
        f"{color}.{line}.\n"
        f"{color}: {text} :\n"
        f"{color}'{line}'"
    )

def box6(text, color = C.w):
    line = "■" * (len(text)+4)
    return (
        f"{color}{line}\n"
        f"{color}■ {text} ■\n"
        f"{color}{line}"
    )

def customBox(text, box, color):
    line = box * (len(text)+4)
    return (
        f"{color}{line}\n"
        f"{color}{box} {text} {box}\n"
        f"{color}{line}"
    )

# ===== TEXTOS ESPECIALES =====

def rainbow(text):
    colors = [
        C.r, C.y, C.g,
        C.c, C.b, C.m
    ]

    out = ""

    for i, ch in enumerate(text):
        out += colors[i % len(colors)] + ch

    return out + S.rs

def blueGra(text):
    colors = [
        C.b, C.c, C.lb,
    ]

    out = ""

    for i, ch in enumerate(text):
        out += colors[i % len(colors)] + ch

    return out + S.rs

def redGra(text):
    colors = [
        C.r, C.o, C.y,
    ]

    out = ""

    for i, ch in enumerate(text):
        out += colors[i % len(colors)] + ch

    return out + S.rs

def customGra(text, col1 = C.w, col2 = C.w, col3 = C.w):
    colors = [
        col1, col2, col3,
    ]

    out = ""

    for i, ch in enumerate(text):
        out += colors[i % len(colors)] + ch

    return out + S.rs