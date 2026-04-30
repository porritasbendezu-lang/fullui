"""
themes.py

Theme system for FULLUI.

Allows customization of UI appearance such as:
- colors
- styles
- text behavior

Designed to be lightweight and easily extendable.

v0.2.3 ADDITIONS:
- Fix parameters
- New themes RGB
"""

# =========================================================
# IMPORTS
# =========================================================

from .colors import C, S, BG

# =========================================================
# THEME CORE CLASS
# =========================================================

class Theme:
    """
    Defines a visual theme for FULLUI.

    This class only stores visual configuration.
    It does not handle logic or rendering.
    """

    def __init__(
        self,
        name="default",

        # TEXT
        textColor=C.w,
        textStyle=S.rs,
        
        # TITLE
        titleColor=C.w,
        titleStyle=S.bd,
        titleColorMargins=C.r,

        # SUBTITLE
        subtitleColor=C.w,
        subtitleStyle=S.it,

        # OPTIONS
        optionColor=C.w,
        optionKeyColor=C.g,
        optionStyle=S.bd,

        # BREAK
        breakColor=C.r,
        breakKeyColor=C.r,

        breakStyle=S.bd,

        # INPUT
        inputColor=C.c,
        inputStyle=S.bd,
    ):
        self.name = name

        self.textColor = textColor
        self.textStyle = textStyle

        self.titleColor = titleColor
        self.titleStyle = titleStyle
        self.titleColorMargins = titleColorMargins

        self.subtitleColor = subtitleColor
        self.subtitleStyle = subtitleStyle

        self.optionColor = optionColor
        self.optionKeyColor = optionKeyColor
        self.optionStyle = optionStyle

        self.breakColor = breakColor
        self.breakKeyColor = breakKeyColor
        self.breakStyle = breakStyle

        self.inputColor = inputColor
        self.inputStyle = inputStyle


# =========================================================
# PREDEFINED THEMES
# =========================================================

DEFAULT = Theme()

DARK = Theme(
    name="dark",
    titleColor=C.gray,
    titleColorMargins=C.k,
    subtitleColor=C.gray,
    optionColor=C.gray,
    optionKeyColor=C.k,
    breakColor=C.dr,
    breakKeyColor=C.dr,
    inputColor=C.dc
)

NEON = Theme(
    name="neon",
    titleColor=C.p,
    titleColorMargins=C.np,
    subtitleColor=C.c,
    optionColor=C.y,
    optionKeyColor=C.bc,
    breakColor=C.r,
    breakKeyColor=C.r,
    inputColor=C.ng
)

FIRE = Theme(
    name="fire",
    titleColor=C.gd,
    titleColorMargins=C.r,
    subtitleColor=C.o,
    optionColor=C.y,
    optionKeyColor=C.fo,
    breakColor=C.r,
    breakKeyColor=C.r,
    inputColor=C.o
)

ICE = Theme(
    name="ice",
    titleColor=C.lb,
    titleColorMargins=C.bc,
    subtitleColor=C.c,
    optionColor=C.w,
    optionKeyColor=C.lb,
    breakColor=C.c,
    breakKeyColor=C.c,
    inputColor=C.lb
)

# =========================================================
# NEW THEMES (v0.2.0)
# =========================================================

HACKER = Theme(
    name="hacker",
    titleColor=C.ng,
    titleColorMargins=C.k,
    subtitleColor=C.dg,
    optionColor=C.ng,
    optionKeyColor=C.ng,
    breakColor=C.r,
    breakKeyColor=C.r,
    inputColor=C.ng,
)

VOID = Theme(
    name="void",
    titleColor=C.gray,
    titleColorMargins=C.dr,
    subtitleColor=C.gray,
    optionColor=C.w,
    optionKeyColor=C.sg,
    breakColor=C.dr,
    breakKeyColor=C.dr,
    inputColor=C.w,
)

ELECTRIC = Theme(
    name="electric",
    titleColor=C.eb,
    titleColorMargins=C.gd,
    subtitleColor=C.bc,
    optionColor=C.b,
    optionKeyColor=C.bc,
    breakColor=C.y,
    breakKeyColor=C.y,
    inputColor=C.bc,
)

NIGHT = Theme(
    name="night",
    titleColor=C.gr,
    titleColorMargins=C.dc,
    subtitleColor=C.gray,
    optionColor=C.w,
    optionKeyColor=C.pu,
    breakColor=C.dr,
    breakKeyColor=C.dr,
    inputColor=C.pu,
)

ALERT = Theme(
    name="alert",
    titleColor=C.r,
    titleColorMargins=C.fo,
    subtitleColor=C.y,
    optionColor=C.o,
    optionKeyColor=C.r,
    breakColor=C.r,
    breakKeyColor=C.r,
    inputColor=C.y,
)

FROST = Theme(
    name="frost",
    titleColor=C.lb,
    titleColorMargins=C.bc,
    subtitleColor=C.w,
    optionColor=C.c,
    optionKeyColor=C.lb,
    breakColor=C.c,
    breakKeyColor=C.c,
    inputColor=C.lb,
)

NATURE = Theme(
    name="nature",
    titleColor=C.dg,
    titleColorMargins=C.br,
    subtitleColor=C.g,
    optionColor=C.g,
    optionKeyColor=C.dg,
    breakColor=C.br,
    breakKeyColor=C.br,
    inputColor=C.g,
)

DEV = Theme(
    name="dev",
    titleColor=C.w,
    titleColorMargins=C.sg,
    subtitleColor=C.gray,
    optionColor=C.c,
    optionKeyColor=C.ng,
    breakColor=C.gray,
    breakKeyColor=C.gray,
    inputColor=C.w,
)

GAMER = Theme(
    name="gamer",
    titleColor=C.p,
    titleColorMargins=C.np,
    subtitleColor=C.b,
    optionColor=C.y,
    optionKeyColor=C.ng,
    breakColor=C.r,
    breakKeyColor=C.r,
    inputColor=C.c,
)

BRUTAL = Theme(
    name="brutal",
    titleColor=C.dr,
    titleColorMargins=C.r,
    subtitleColor=C.dr,
    optionColor=C.gray,
    optionKeyColor=C.w,
    breakColor=C.r,
    breakKeyColor=C.r,
    inputColor=C.w,
)

# =========================================================
# RGB THEMES (v0.2.2)
# =========================================================

from .colors import rgb

SUNSET = Theme(
    name="sunset",
    titleColor=rgb(255, 120, 80),
    titleColorMargins=rgb(180, 60, 40),
    subtitleColor=rgb(255, 180, 120),
    optionColor=rgb(255, 200, 150),
    optionKeyColor=rgb(255, 140, 90),
    breakColor=rgb(255, 80, 80),
    breakKeyColor=rgb(255, 80, 80),
    inputColor=rgb(255, 150, 100),
)

OCEAN = Theme(
    name="ocean",
    titleColor=rgb(0, 180, 255),
    titleColorMargins=rgb(0, 90, 150),
    subtitleColor=rgb(100, 200, 255),
    optionColor=rgb(180, 220, 255),
    optionKeyColor=rgb(0, 150, 220),
    breakColor=rgb(255, 80, 80),
    breakKeyColor=rgb(255, 80, 80),
    inputColor=rgb(0, 200, 255),
)

FOREST = Theme(
    name="forest",
    titleColor=rgb(50, 200, 120),
    titleColorMargins=rgb(20, 100, 60),
    subtitleColor=rgb(120, 220, 160),
    optionColor=rgb(180, 255, 200),
    optionKeyColor=rgb(60, 180, 100),
    breakColor=rgb(200, 80, 80),
    breakKeyColor=rgb(200, 80, 80),
    inputColor=rgb(80, 220, 140),
)

CYBERPUNK = Theme(
    name="cyberpunk",
    titleColor=rgb(255, 0, 200),
    titleColorMargins=rgb(0, 255, 255),
    subtitleColor=rgb(255, 100, 220),
    optionColor=rgb(255, 200, 255),
    optionKeyColor=rgb(0, 255, 200),
    breakColor=rgb(255, 50, 100),
    breakKeyColor=rgb(255, 50, 100),
    inputColor=rgb(0, 255, 255),
)

LAVENDER = Theme(
    name="lavender",
    titleColor=rgb(180, 150, 255),
    titleColorMargins=rgb(120, 90, 200),
    subtitleColor=rgb(210, 190, 255),
    optionColor=rgb(230, 220, 255),
    optionKeyColor=rgb(160, 120, 255),
    breakColor=rgb(255, 120, 120),
    breakKeyColor=rgb(255, 120, 120),
    inputColor=rgb(200, 170, 255),
)

GOLD = Theme(
    name="gold",
    titleColor=rgb(255, 215, 0),
    titleColorMargins=rgb(180, 140, 0),
    subtitleColor=rgb(255, 230, 120),
    optionColor=rgb(255, 240, 180),
    optionKeyColor=rgb(255, 200, 0),
    breakColor=rgb(255, 80, 80),
    breakKeyColor=rgb(255, 80, 80),
    inputColor=rgb(255, 215, 0),
)

ROSE = Theme(
    name="rose",
    titleColor=rgb(255, 100, 150),
    titleColorMargins=rgb(180, 50, 90),
    subtitleColor=rgb(255, 160, 190),
    optionColor=rgb(255, 210, 230),
    optionKeyColor=rgb(255, 120, 170),
    breakColor=rgb(255, 80, 100),
    breakKeyColor=rgb(255, 80, 100),
    inputColor=rgb(255, 140, 180),
)

MIDNIGHT = Theme(
    name="midnight",
    titleColor=rgb(120, 160, 255),
    titleColorMargins=rgb(40, 60, 120),
    subtitleColor=rgb(180, 200, 255),
    optionColor=rgb(220, 230, 255),
    optionKeyColor=rgb(100, 140, 255),
    breakColor=rgb(255, 90, 90),
    breakKeyColor=rgb(255, 90, 90),
    inputColor=rgb(140, 180, 255),
)

EMBER = Theme(
    name="ember",
    titleColor=rgb(255, 120, 0),
    titleColorMargins=rgb(120, 50, 0),
    subtitleColor=rgb(255, 180, 80),
    optionColor=rgb(255, 220, 150),
    optionKeyColor=rgb(255, 140, 0),
    breakColor=rgb(255, 60, 60),
    breakKeyColor=rgb(255, 60, 60),
    inputColor=rgb(255, 150, 50),
)

MINT = Theme(
    name="mint",
    titleColor=rgb(120, 255, 200),
    titleColorMargins=rgb(40, 150, 100),
    subtitleColor=rgb(180, 255, 220),
    optionColor=rgb(220, 255, 240),
    optionKeyColor=rgb(100, 220, 180),
    breakColor=rgb(255, 100, 100),
    breakKeyColor=rgb(255, 100, 100),
    inputColor=rgb(150, 255, 210),
)

CRIMSON_GOLD = Theme(
    name="crimson_gold",
    titleColor=rgb(220, 40, 60),
    titleColorMargins=rgb(120, 20, 30),
    subtitleColor=rgb(255, 180, 80),
    optionColor=rgb(255, 210, 140),
    optionKeyColor=rgb(200, 50, 70),
    breakColor=rgb(255, 70, 70),
    breakKeyColor=rgb(255, 70, 70),
    inputColor=rgb(255, 160, 90),
)

AQUA_LIME = Theme(
    name="aqua_lime",
    titleColor=rgb(0, 220, 200),
    titleColorMargins=rgb(0, 120, 110),
    subtitleColor=rgb(120, 255, 180),
    optionColor=rgb(180, 255, 220),
    optionKeyColor=rgb(0, 200, 160),
    breakColor=rgb(255, 100, 100),
    breakKeyColor=rgb(255, 100, 100),
    inputColor=rgb(80, 255, 200),
)

PURPLE_PINK = Theme(
    name="purple_pink",
    titleColor=rgb(180, 80, 255),
    titleColorMargins=rgb(100, 40, 160),
    subtitleColor=rgb(255, 140, 220),
    optionColor=rgb(255, 200, 240),
    optionKeyColor=rgb(200, 100, 255),
    breakColor=rgb(255, 90, 140),
    breakKeyColor=rgb(255, 90, 140),
    inputColor=rgb(220, 140, 255),
)

BLUE_ORANGE = Theme(
    name="blue_orange",
    titleColor=rgb(60, 140, 255),
    titleColorMargins=rgb(30, 70, 140),
    subtitleColor=rgb(255, 180, 100),
    optionColor=rgb(255, 210, 160),
    optionKeyColor=rgb(80, 160, 255),
    breakColor=rgb(255, 100, 80),
    breakKeyColor=rgb(255, 100, 80),
    inputColor=rgb(120, 180, 255),
)

EMERALD_GOLD = Theme(
    name="emerald_gold",
    titleColor=rgb(0, 180, 120),
    titleColorMargins=rgb(0, 90, 60),
    subtitleColor=rgb(255, 210, 120),
    optionColor=rgb(255, 230, 170),
    optionKeyColor=rgb(0, 160, 100),
    breakColor=rgb(255, 90, 90),
    breakKeyColor=rgb(255, 90, 90),
    inputColor=rgb(80, 200, 140),
)

RED_BLACK = Theme(
    name="red_black",
    titleColor=rgb(255, 60, 60),
    titleColorMargins=rgb(80, 0, 0),
    subtitleColor=rgb(255, 120, 120),
    optionColor=rgb(220, 220, 220),
    optionKeyColor=rgb(255, 80, 80),
    breakColor=rgb(255, 40, 40),
    breakKeyColor=rgb(255, 40, 40),
    inputColor=rgb(255, 100, 100),
)

SKY_PURPLE = Theme(
    name="sky_purple",
    titleColor=rgb(120, 180, 255),
    titleColorMargins=rgb(60, 90, 180),
    subtitleColor=rgb(200, 160, 255),
    optionColor=rgb(220, 210, 255),
    optionKeyColor=rgb(140, 200, 255),
    breakColor=rgb(255, 100, 150),
    breakKeyColor=rgb(255, 100, 150),
    inputColor=rgb(160, 200, 255),
)

MANGO_FIRE = Theme(
    name="mango_fire",
    titleColor=rgb(255, 160, 0),
    titleColorMargins=rgb(150, 70, 0),
    subtitleColor=rgb(255, 200, 100),
    optionColor=rgb(255, 230, 160),
    optionKeyColor=rgb(255, 140, 0),
    breakColor=rgb(255, 70, 50),
    breakKeyColor=rgb(255, 70, 50),
    inputColor=rgb(255, 180, 60),
)

TEAL_ROSE = Theme(
    name="teal_rose",
    titleColor=rgb(0, 180, 160),
    titleColorMargins=rgb(0, 90, 80),
    subtitleColor=rgb(255, 140, 160),
    optionColor=rgb(255, 200, 210),
    optionKeyColor=rgb(0, 200, 180),
    breakColor=rgb(255, 90, 120),
    breakKeyColor=rgb(255, 90, 120),
    inputColor=rgb(120, 220, 200),
)

INDIGO_CYAN = Theme(
    name="indigo_cyan",
    titleColor=rgb(90, 100, 255),
    titleColorMargins=rgb(40, 50, 150),
    subtitleColor=rgb(100, 220, 255),
    optionColor=rgb(180, 240, 255),
    optionKeyColor=rgb(120, 140, 255),
    breakColor=rgb(255, 100, 100),
    breakKeyColor=rgb(255, 100, 100),
    inputColor=rgb(140, 180, 255),
)

# =========================================================
# GLOBAL STATE
# =========================================================

_current_theme = DEFAULT


def set_theme(theme: Theme):
    """
    Set global active theme.
    """
    global _current_theme
    _current_theme = theme


def get_theme():
    """
    Return currently active theme.
    """
    return _current_theme


# =========================================================
# APPLY THEME TO MENU CONFIG
# =========================================================

def apply_theme(menu_kwargs: dict, theme: Theme = None):
    """
    Apply theme values to a menu configuration dictionary.
    """

    theme = theme or _current_theme

    # TITLE
    menu_kwargs["titleColorText"] = theme.titleColor
    menu_kwargs["titleStyle"] = theme.titleStyle
    menu_kwargs["titleColorMargins"] = theme.titleColorMargins

    menu_kwargs["subtitleColor"] = theme.subtitleColor
    menu_kwargs["subtitleStyle"] = theme.subtitleStyle

    menu_kwargs["optionsColorText"] = theme.optionColor
    menu_kwargs["optionsColorKeys"] = theme.optionKeyColor
    menu_kwargs["optionsStyle"] = theme.optionStyle

    menu_kwargs["breakColorText"] = theme.breakColor
    menu_kwargs["breakColorKeys"] = theme.breakKeyColor
    menu_kwargs["breakStyle"] = theme.breakStyle

    menu_kwargs["inputColor"] = theme.inputColor
    menu_kwargs["inputStyle"] = theme.inputStyle

    return menu_kwargs


# =========================================================
# THEME FACTORY
# =========================================================

def create_theme(**kwargs):
    """
    Create a custom theme dynamically.
    """
    return Theme(**kwargs)