"""
themes.py

Theme system for FULLUI.

Allows customization of UI appearance such as:
- colors
- styles
- text behavior

Designed to be lightweight and easily extendable.
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
    titleColorMargins=C.sb,
    subtitleColor=C.gray,
    optionColor=C.w,
    optionKeyColor=C.sg,  # 🔥 mejor contraste
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
    titleColor=C.pu,
    titleColorMargins=C.dc,
    subtitleColor=C.gray,
    optionColor=C.w,
    optionKeyColor=C.pu,
    breakColor=C.dr,
    breakKeyColor=C.dr,
    inputColor=C.c,
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
    titleColor=C.k,
    titleColorMargins=C.dr,
    subtitleColor=C.gray,
    optionColor=C.w,
    optionKeyColor=C.w,  # 🔥 más visible
    breakColor=C.r,
    breakKeyColor=C.r,
    inputColor=C.w,
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
    menu_kwargs.setdefault("titleColorText", theme.titleColor)
    menu_kwargs.setdefault("titleStyle", theme.titleStyle)
    menu_kwargs.setdefault("titleColorMargins", theme.titleColorMargins)

    # SUBTITLE
    menu_kwargs.setdefault("subtitleColor", theme.subtitleColor)
    menu_kwargs.setdefault("subtitleStyle", theme.subtitleStyle)

    # OPTIONS
    menu_kwargs.setdefault("optionsColorText", theme.optionColor)
    menu_kwargs.setdefault("optionsColorKeys", theme.optionKeyColor)
    menu_kwargs.setdefault("optionsStyle", theme.optionStyle)

    # BREAK
    menu_kwargs.setdefault("breakColorText", theme.breakColor)
    menu_kwargs.setdefault("breakColorKeys", theme.breakKeyColor)  # 🔥 FIX
    menu_kwargs.setdefault("breakStyle", theme.breakStyle)

    # INPUT
    menu_kwargs.setdefault("inputColor", theme.inputColor)
    menu_kwargs.setdefault("inputStyle", theme.inputStyle)

    return menu_kwargs


# =========================================================
# THEME FACTORY
# =========================================================

def create_theme(**kwargs):
    """
    Create a custom theme dynamically.
    """
    return Theme(**kwargs)