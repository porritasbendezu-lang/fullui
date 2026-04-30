"""
ui.py

Core interface system for FULLUI.

v0.2.3 ADDITIONS:
- Book System
- Quiz System
- Add functions to colors.py and more
"""

# =========================================================
# IMPORTS
# =========================================================

from fullui import *
from .colors import C, S, BG
from .themes import apply_theme, get_theme, set_theme
from .layouts import Panel, stack
import textwrap
import os

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
    Alias registry for FULLUI.
    Organized by system: Menu / Input / Quiz
    """

    # =============== MENU TEXT ===============

    t = "titleText"
    titleText = "titleText"

    st = "subtitleText"
    subtitleText = "subtitleText"

    op = "options"
    options = "options"

    # =============== MENU VISIBILITY ===============

    sT = "showTitle"
    showTitle = "showTitle"

    sST = "showSubtitle"
    showSubtitle = "showSubtitle"

    sB = "showBreak"
    showBreak = "showBreak"

    # =============== MENU TITLE STYLE ===============

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

    # =============== MENU SUBTITLE ===============

    sl = "subtitleLines"
    subtitleLines = "subtitleLines"

    sw = "subtitleWidth"
    subtitleWidth = "subtitleWidth"

    sc = "subtitleColor"
    subtitleColor = "subtitleColor"

    ss = "subtitleStyle"
    subtitleStyle = "subtitleStyle"

    # =============== MENU OPTIONS ===============

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

    # =============== MENU BREAK ===============

    bt = "breakText"
    breakText = "breakText"

    bs = "breakSymbol"
    breakSymbol = "breakSymbol"

    bct = "breakColorText"
    breakColorText = "breakColorText"

    bck = "breakColorKeys"
    breakColorKeys = "breakColorKeys"

    bst = "breakStyle"
    breakStyle = "breakStyle"

    # =============== INPUT ===============

    ic = "inputColor"
    inputColor = "inputColor"

    isty = "inputStyle"
    inputStyle = "inputStyle"

    p = "prompt"
    prompt = "prompt"

    io = "invalidOption"
    invalidOption = "invalidOption"

    ioc = "invalidOptionColor"
    invalidOptionColor = "invalidOptionColor"

    # =============== QUIZ CORE ===============

    qs = "questions"
    questions = "questions"

    # =============== QUIZ TEXTS ===============

    twn = "textWin"
    textWin = "textWin"

    tf = "textFail"
    textFail = "textFail"

    tmid = "textMid"
    textMid = "textMid"

    # =============== QUIZ ===============

    qc = "questionColor"
    questionColor = "questionColor"

    qsty = "questionStyle"
    questionStyle = "questionStyle"

    okl = "optionKeyLeft"
    optionKeyLeft = "optionKeyLeft"

    okr = "optionKeyRight"
    optionKeyRight = "optionKeyRight"

    # reutiliza colores del sistema base

    rc = "resultColor"
    resultColor = "resultColor"

# =========================================================
# UTILITIES
# =========================================================

line_break = "\n"
lb = line_break

def p(text):
    print(text)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause(text="Press Enter for continue ...", colorText=C.m, style=S.bd):
    input(f"{colorText}{style}{text}{S.rs}")

# =========================================================
# HELPERS
# =========================================================

def success(text):
    """
    Success message style (green).
    """
    print(f"{C.g}{S.bd}✔︎  {text}{S.rs}")


def error(text):
    """
    Error message style (red bold).
    """
    print(f"{C.r}{S.bd}✖︎  {text}{S.rs}")


def warning(text):
    """
    Warning message style (yellow).
    """
    print(f"{C.y}{S.bd}⚠︎  {text}{S.rs}")


def info(text):
    """
    Info message style (black).
    """
    print(f"{C.k}{S.bd}🖥  {text}{S.rs}")

def message(text, line, width=20, colorMessage = C.c, style = S.bd):
    """
    Text message style (cyan) with automatic line wrapping.
    """
    lineUp = line*(width//2)
    lineDown = (line*width) + line*4
    print(f"{colorMessage}{style}{lineUp} ✉︎  {lineUp}{S.rs}".center(width))
    wrapped = textwrap.fill(text, width=width)

    for line in wrapped.split("\n"):
        print(f"{C.w}{line}{S.rs}".center(width))
    
    print(f"{colorMessage}{style}{lineDown}{S.rs}".center(width))

def miniTitle(text, color = C.m, style = S.bd):
    """
    Small styled title header.
    """
    print(f"{color}{style}=====》 {text} 《====={S.rs}")

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
# SYSTEM PANEL (DEV TOOL)
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
        ALERT, FROST, NATURE, DEV, GAMER, BRUTAL,
        SUNSET, OCEAN, FOREST, CYBERPUNK, LAVENDER,
        GOLD, ROSE, MIDNIGHT, EMBER, MINT,
        CRIMSON_GOLD, AQUA_LIME, PURPLE_PINK, 
        BLUE_ORANGE, EMERALD_GOLD, RED_BLACK, SKY_PURPLE, 
        MANGO_FIRE, TEAL_ROSE, INDIGO_CYAN
    )

    themes = [
        DEFAULT, DARK, NEON, FIRE, ICE,
        HACKER, VOID, ELECTRIC, NIGHT,
        ALERT, FROST, NATURE, DEV, GAMER, BRUTAL,
        SUNSET, OCEAN, FOREST, CYBERPUNK, LAVENDER,
        GOLD, ROSE, MIDNIGHT, EMBER, MINT,
        CRIMSON_GOLD, AQUA_LIME, PURPLE_PINK, 
        BLUE_ORANGE, EMERALD_GOLD, RED_BLACK, SKY_PURPLE, 
        MANGO_FIRE, TEAL_ROSE, INDIGO_CYAN
    ] + list(_THEME_REGISTRY.values())

    while True:
        
        # =============== THEMES MENU ===============

        choice = menu(
            t="THEMES MANAGER",
            st=f"Active: {get_theme().name}",
            op=[t.name for t in themes],
            bt="Back",
            bs="X"
        )

        if choice is None:
            return

        selected = themes[choice - 1]

        # =============== PREVIEW THEMES ===============

        while True:
            preview_choice = menu(
                t="THEME PREVIEW",
                st=f"Preview: {selected.name}",
                op=[
                    "Apply Theme",
                    "Preview Again"
                ],
                bt="Back",
                bs="X",

                # AQUÍ FORZAMOS ESTILO DEL THEME
                tcm=selected.titleColorMargins,
                tct=selected.titleColor,
                ts=selected.titleStyle,

                sc=selected.subtitleColor,
                ss=selected.subtitleStyle,

                ock=selected.optionKeyColor,
                oct=selected.optionColor,

                bck=selected.breakKeyColor,
                bct=selected.breakColor
            )

            if preview_choice is None:
                break

            if preview_choice == 1:
                set_theme(selected)
                menu(
                    t="SUCCESS",
                    st=f"{selected.name} applied!",
                    op=["Continue"],
                    sB=False
                )
                break

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
# COLOR INSPECTOR
# =========================================================

def show_colors():
    clear()
    title("COLOR INSPECTOR")

    # Obtener atributos válidos
    colors = {k: v for k, v in C.__dict__.items() if not k.startswith("_")}

    # Agrupar por valor (color real)
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
# BOOK VIEWER
# =========================================================

def book(pages, width=60):
    """
    Interactive book viewer (1 page)

    Controls:
    A -> previous
    D -> next
    X -> exit

    pages: list[str]
    """

    if not pages:
        return

    index = 0

    while True:
        clear()

        # =============== CURRENT PAGE ===============
        content = pages[index]

        panel = Panel(
            content,
            w=width,
            b="round",
            t=f"Page {index + 1}/{len(pages)}",
            a="left"
        )

        panel.show()

        print()
        print(f"{C.g}[A]{S.rs} Previous   {C.y}[D]{S.rs} Next   {C.r}[X]{S.rs} Exit")

        # =============== INPUT ===============
        choice = input(f"{C.c}{S.bd}\n> {S.rs}").lower()

        if choice == "x":
            break

        elif choice == "a":
            if index > 0:
                index -= 1

        elif choice == "d":
            if index < len(pages) - 1:
                index += 1
                
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
        "p": "prompt",
        "io": "invalidOption",
        "ioc": "invalidOptionColor"
    }

    normalized = {alias_map.get(k, k): v for k, v in kwargs.items()}
    normalized = apply_theme(normalized)

    while True:
        clear()

        options = normalized.get("options", [])
        breakSymbol = normalized.get("breakSymbol", "X")

        # =============== TITLE ===============

        if normalized.get("showTitle", True):
            title(
                normalized.get("titleText", ""),
                normalized.get("titleMargins", "="),
                normalized.get("titleWidth", 30),
                normalized.get("titleColorMargins", C.r),  # ✅ FIX
                normalized.get("titleColorText", C.w),
                normalized.get("titleStyle", S.bd)
            )

        # =============== SUBTITLE ===============

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

        # =============== OPTIONS ===============

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

        # =============== BREAK ===============

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

        # =============== INPUT ===============

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

        print(
            f"{normalized.get('invalidOptionColor', C.r)}"
            f"{normalized.get('invalidOption', "Opcion incorrecta")}{S.rs}"
            )
        pause()

# =========================================================
# MAIN QUIZ UI
# =========================================================

def quiz_title(text="", margins="=", width=30, colorMargins=C.r, colorText=C.w, style=S.bd):
    line = margins * width
    print(f"{colorText}{style}{text.center(width)}{S.rs}")
    print(f"{colorMargins}{style}{line}{S.rs}")

def quiz_question(text, color=C.w, style=S.bd):
    print(f"\n{color}{style}{text}{S.rs}\n")

def quiz_option(text, num, keyL="(", keyR=")", colorKey=C.y, colorText=C.w, style=S.bd):
    print(f"{colorKey}{style}{keyL}{num}{keyR}{S.rs} {colorText}{text}{S.rs}")


# =========================================================
# QUIZ
# =========================================================

def quiz(**kwargs):

    theme = get_theme()
    
    alias_map = {
        "t": "titleText",
        "tm": "titleMargins",
        "tw": "titleWidth",
        "tcm": "titleColorMargins",
        "tct": "titleColorText",
        "ts": "titleStyle",
        "qs": "question",

        "tw": "textWin",
        "tf": "textFail",
        "tmid": "textMid",

        "qc": "questionColor",
        "qsty": "questionStyle",

        "okl": "optionKeyLeft",
        "okr": "optionKeyRight",

        "ock": "optionColorKeys",
        "oct": "optionColorText",
        "os": "optionStyle",

        "ic": "inputColor",
        "isty": "inputStyle",
        "p": "prompt",

        "rc": "resultColor"
    }

    normalized = {alias_map.get(k, k): v for k, v in kwargs.items()}
    normalized = apply_theme(normalized)

    question = normalized.get("question", [])

    results = []
    score = 0

    # =============== QUESTIONS LOOP ===============

    for idx, q in enumerate(question, 1):

        while True:
            clear()

            if normalized.get("showTitle", True):
                quiz_title(
                    normalized.get("titleText", ""),
                    normalized.get("titleMargins", "="),
                    normalized.get("titleWidth", 30),
                    normalized.get("titleColorMargins", C.r),
                    normalized.get("titleColorText", C.w),
                    normalized.get("titleStyle", S.bd)
                )

            print(f"{theme.titleColorMargins}Pregunta {idx}/{len(question)}{S.rs}")

            quiz_question(
                q["question"],
                color=normalized.get("questionColor", theme.subtitleColor)
            )

            for i, opt in enumerate(q["options"], 1):
                quiz_option(
                    opt,
                    i,
                    normalized.get("optionKeyLeft", "("),
                    normalized.get("optionKeyRight", ")"),
                    normalized.get("optionColorKeys", theme.optionKeyColor),
                    normalized.get("optionColorText", theme.optionColor),
                    normalized.get("optionStyle", theme.optionStyle)
                )

            choice = input(
                f"{normalized.get('inputColor', C.c)}"
                f"{normalized.get('inputStyle', S.bd)}\n"
                f"{normalized.get('prompt', '> ')}{S.rs}"
            )

            if choice.isdigit():
                n = int(choice)

                if 1 <= n <= len(q["options"]):
                    correct = (n == q["correct"])

                    if correct:
                        score += 1

                    results.append({
                        "question": q["question"],
                        "options": q["options"],
                        "selected": n,
                        "correct": q["correct"]
                    })

                    break

            print(lb + f"{C.r}Opción inválida{S.rs}" + lb)
            pause()

    # =============== RESULTS ===============

    clear()

    panels = []

    for idx, r in enumerate(results, 1):

        lines = []

        for i, opt in enumerate(r["options"], 1):
            if i == r["selected"]:
                if i == r["correct"]:
                    lines.append(f"{BG.g}{C.w} {opt} {S.rs} ✔")
                else:
                    lines.append(f"{BG.r}{C.w} {opt} {S.rs} ✖")
            else:
                if i == r["correct"]:
                    lines.append(f"{C.g}{opt} ✔{S.rs}")
                else:
                    lines.append(opt)

        content = f"{r['question']}\n\n" + "\n".join(lines)

        panels.append(
            Panel(
                content,
                w=60,
                b="round",
                t=f"Pregunta {idx}",
                a="left"
            )
        )

    total = len(question)
    percent = int((score / total) * 100)

    if score == total:
        msg = f"{C.g}{normalized.get('textWin', 'Perfecto')}{S.rs}"
    elif score == 0:
        msg = f"{C.r}{normalized.get('textFail', 'Fallaste todo')}{S.rs}"
    else:
        msg = f"{C.y}{normalized.get('textMid', 'Resultado intermedio')}{S.rs}"

    score_panel = Panel(
        f"Puntaje: {score}/{total} ({percent}%)\n\n{msg}",
        w=60,
        b="double",
        t="RESULTADO FINAL",
        a="center"
    )

    stack(*panels)
    print()
    score_panel.show()

    pause()