from .colors import C, S, BG
import os

# ===== EDITABLES =====

class I:
    # ===== TEXTOS =====
    t   = "titleText"
    titleText = "titleText"

    st  = "subtitleText"
    subtitleText = "subtitleText"

    op  = "options"
    options = "options"

    # ===== ESTRUCTURA =====
    sT  = "showTitle"
    showTitle = "showTitle"

    sST = "showSubtitle"
    showSubtitle = "showSubtitle"

    # ===== TITLE CONFIG =====
    tm  = "titleMargins"
    titleMargins = "titleMargins"

    tw  = "titleWidth"
    titleWidth = "titleWidth"

    tcm = "titleColorMargins"
    titleColorMargins = "titleColorMargins"

    tct = "titleColorText"
    titleColorText = "titleColorText"

    ts  = "titleStyle"
    titleStyle = "titleStyle"

    # ===== SUBTITLE CONFIG =====
    sl  = "subtitleLines"
    subtitleLines = "subtitleLines"

    sw  = "subtitleWidth"
    subtitleWidth = "subtitleWidth"

    sc  = "subtitleColor"
    subtitleColor = "subtitleColor"

    ss  = "subtitleStyle"
    subtitleStyle = "subtitleStyle"

    # ===== OPTIONS CONFIG =====
    k1  = "key1"
    key1 = "key1"

    k2  = "key2"
    key2 = "key2"

    oct = "optionsColorText"
    optionsColorText = "optionsColorText"

    ock = "optionsColorKeys"
    optionsColorKeys = "optionsColorKeys"

    os  = "optionsStyle"
    optionsStyle = "optionsStyle"

    # ===== BREAK CONFIG =====
    sB  = "showBreak"
    showBreak = "showBreak"

    bt  = "breakText"
    breakText = "breakText"

    bs  = "breakSimbol"
    breakSimbol = "breakSimbol"

    bct = "breakColorText"
    breakColorText = "breakColorText"

    bck = "breakColorKeys"
    breakColorKeys = "breakColorKeys"

    bst = "breakStyle"
    breakStyle = "breakStyle"

    # ===== INPUT CONFIG =====
    ic  = "inputColor"
    inputColor = "inputColor"

    isty = "inputStyle"
    inputStyle = "inputStyle"

    p   = "prompt"
    prompt = "prompt"

# ===== FUNCIONES DE FLUJO =====

line_break = "\n"
lb = line_break

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input(C.b + S.bd + "Press Enter..." + S.rs)


# ===== FUNCIONES DE MENU =====

def title(text="", margins="", numMargins=1,
          colorMargins=C.r, colorText=C.w, style=S.bd):

    line = margins * numMargins
    print(f"{colorMargins}{style}{line}{S.rs}")
    print(f"{colorText}{style}{text.center(numMargins)}{S.rs}")
    print(f"{colorMargins}{style}{line}{S.rs}")


def subtitle(text="", lines="", numLines=1, numCenter=20,
             color=C.w, style=S.italic):

    line = lines * numLines
    print(f"{color}{style}{(line + ' ' + text + ' ' + line).center(numCenter)}{S.rs}")


def option(text="", key1="[", key2="]", num=1,
           colorText=C.w, colorKeys=C.g, style=S.bd):

    print(
        f"{colorKeys}{style}{key1}{num}{key2}{S.rs} "
        f"{colorText}{text}{S.rs}"
    )


def opbreak(text="Salir", key1="[", key2="]", simbol="X",
            colorText=C.w, colorKeys=C.r, style=S.bd):

    print(
        f"{colorKeys}{style}{key1}{simbol}{key2}{S.rs} "
        f"{colorText}{text}{S.rs}"
    )


def menu(**kwargs):

    # ===== NORMALIZADOR =====
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

    # convertir claves cortas → largas
    normalized = {}
    for k, v in kwargs.items():
        normalized[alias_map.get(k, k)] = v

    # ===== ahora todo es largo =====
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
    subtitleWidth = normalized.get("subtitleWidth", 20)
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

    # ===== RENDER =====
    if showTitle:
        title(titleText, titleMargins, titleWidth, titleColorMargins, titleColorText, titleStyle)

    if showSubtitle and subtitleText:
        subtitle(subtitleText, subtitleLines, 3, subtitleWidth, subtitleColor, subtitleStyle)

    print()

    for i, opt in enumerate(options, 1):
        option(opt, key1, key2, i, optionsColorText, optionsColorKeys, optionsStyle)

    if showBreak:
        print()
        opbreak(breakText, key1, key2, breakSimbol, breakColorText, breakColorKeys, breakStyle)

    choice = input(f"{inputColor}{inputStyle}\n{prompt}{S.rs}")
    return choice