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

        # SUBTITLE
        subtitleColor=C.w,
        subtitleStyle=S.it,

        # OPTIONS
        optionColor=C.w,
        optionKeyColor=C.g,
        optionStyle=S.bd,

        # BREAK
        breakColor=C.r,
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

        self.subtitleColor = subtitleColor
        self.subtitleStyle = subtitleStyle

        self.optionColor = optionColor
        self.optionKeyColor = optionKeyColor
        self.optionStyle = optionStyle

        self.breakColor = breakColor
        self.breakStyle = breakStyle

        self.inputColor = inputColor
        self.inputStyle = inputStyle


# =========================================================
# PREDEFINED THEMES
# =========================================================

DEFAULT = Theme()

DARK = Theme(
    name="dark",
    titleColor=C.c,
    subtitleColor=C.gray,
    optionColor=C.w,
    optionKeyColor=C.g,
    inputColor=C.c
)

NEON = Theme(
    name="neon",
    titleColor=C.p,
    subtitleColor=C.c,
    optionColor=C.y,
    optionKeyColor=C.c,
    breakColor=C.r,
    inputColor=C.g
)

FIRE = Theme(
    name="fire",
    titleColor=C.r,
    subtitleColor=C.o,
    optionColor=C.y,
    optionKeyColor=C.r,
    breakColor=C.r,
    inputColor=C.o
)

ICE = Theme(
    name="ice",
    titleColor=C.lb,
    subtitleColor=C.c,
    optionColor=C.w,
    optionKeyColor=C.lb,
    breakColor=C.c,
    inputColor=C.lb
)


# =========================================================
# GLOBAL STATE
# =========================================================

_current_theme = DEFAULT


def set_theme(theme: Theme):
    """
    Set global active theme.

    Args:
        theme (Theme): Theme instance to apply globally.
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

    Keeps existing user-defined values (does not override them).

    Args:
        menu_kwargs (dict): menu configuration
        theme (Theme): optional theme override
    """

    theme = theme or _current_theme

    # TITLE
    menu_kwargs.setdefault("titleColorText", theme.titleColor)
    menu_kwargs.setdefault("titleStyle", theme.titleStyle)

    # SUBTITLE
    menu_kwargs.setdefault("subtitleColor", theme.subtitleColor)
    menu_kwargs.setdefault("subtitleStyle", theme.subtitleStyle)

    # OPTIONS
    menu_kwargs.setdefault("optionsColorText", theme.optionColor)
    menu_kwargs.setdefault("optionsColorKeys", theme.optionKeyColor)
    menu_kwargs.setdefault("optionsStyle", theme.optionStyle)

    # BREAK
    menu_kwargs.setdefault("breakColorText", theme.breakColor)
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

    Example:
        create_theme(titleColor=C.r, inputColor=C.g)
    """
    return Theme(**kwargs)