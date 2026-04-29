"""
FULLUI
Advanced console UI system for Python terminals.
"""

# ===== VERSION =====

__version__ = "0.1.2"


# ===== WINDOWS ANSI SUPPORT =====

try:
    from colorama import just_fix_windows_console
    just_fix_windows_console()
except Exception:
    pass


# ===== IMPORT SUBMODULES =====

from . import colors
from . import ui
from . import animations
from . import themes


# ===== PUBLIC API =====

from .colors import (
    C, BG, S,
    rgb, bg_rgb,
    success, error, warning, info, miniTitle,
    box1, box2, box3, box4, box5, box6, customBox,
    rainbow, blueGra, redGra, customGra
)

from .ui import (
    I,
    menu,
    title,
    subtitle,
    option,
    opbreak,
    clear,
    pause,
    line_break,
    lb
)

from .animations import (
    spinner,
    dot_ripple,
    bounce,
    matrix,
    fade_in,
    pulse_bar,
    type_shuffle,
    wave,
    blink,
    energy_pulse,
    scanline,
    glitch
)

from .themes import (
    Theme,
    DEFAULT,
    DARK,
    NEON,
    FIRE,
    ICE,
    set_theme,
    get_theme,
    apply_theme,
    create_theme
)


# ===== STAR IMPORT CONTROL =====

__all__ = [

    # meta
    "__version__",

    # colors
    "C","BG","S",
    "rgb","bg_rgb",

    "success","error","warning","info","miniTitle",

    "box1","box2","box3","box4","box5","box6","customBox",

    "rainbow","blueGra","redGra","customGra",

    # ui
    "I",
    "menu",
    "title",
    "subtitle",
    "option",
    "opbreak",
    "clear",
    "pause",
    "line_break",
    "lb",

    # animations
    "spinner",
    "dot_ripple",
    "bounce",
    "matrix",
    "fade_in",
    "pulse_bar",
    "type_shuffle",
    "wave",
    "blink",
    "energy_pulse",
    "scanline",
    "glitch",

    # themes
    "Theme",
    "DEFAULT",
    "DARK",
    "NEON",
    "FIRE",
    "ICE",
    "set_theme",
    "get_theme",
    "apply_theme",
    "create_theme",
]