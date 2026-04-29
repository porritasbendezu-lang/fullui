"""
FULLUI
Advanced console UI system for Python terminals.
"""

# =========================================================
# VERSION
# =========================================================

__version__ = "0.2.0"


# =========================================================
# WINDOWS ANSI SUPPORT
# =========================================================

try:
    from colorama import just_fix_windows_console
    just_fix_windows_console()
except Exception:
    pass


# =========================================================
# IMPORT SUBMODULES
# =========================================================

from . import colors
from . import ui
from . import animations
from . import themes


# =========================================================
# PUBLIC API - COLORS
# =========================================================

from .colors import (
    C, BG, S,
    rgb, bg_rgb,

    success,
    error,
    warning,
    info,
    miniTitle,

    box1,
    box2,
    box3,
    box4,
    box5,
    box6,
    customBox,

    rainbow,
    blueGra,
    redGra,
    customGra
)


# =========================================================
# FULLUI BANNER
# Manual use:
# import fullui; fullui.banner()
# =========================================================

def banner():
    """
    Display FULLUI banner.
    """

    print(
f"""{C.c}{S.bd}

███████╗██╗   ██╗██╗     ██╗     ██╗   ██╗██╗
██╔════╝██║   ██║██║     ██║     ██║   ██║██║
█████╗  ██║   ██║██║     ██║     ██║   ██║██║
██╔══╝  ██║   ██║██║     ██║     ██║   ██║██║
██║     ╚██████╔╝███████╗███████╗╚██████╔╝██║
╚═╝      ╚═════╝ ╚══════╝╚══════╝ ╚═════╝ ╚═╝

🎨 FULLUI v{__version__}
Advanced Console UI Framework

{C.g}✔ Installed successfully

{C.y}Quick Start:{S.rs}

from fullui import *
menu(
    t="Main Menu",
    op=["Play","Exit"]
)

{C.m}Developer Tools:{S.rs}

system_panel()

{C.c}GitHub:{S.rs}
github.com/porritasbendezu-lang/fullui

{C.bc}Try:
python -c "import fullui; fullui.banner()"

{S.rs}"""
    )


# Alias
about = banner


# =========================================================
# PUBLIC API - UI
# =========================================================

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
    lb,

    # DEV TOOLS
    system_panel,
    themes_manager,
    animations_preview,
    system_info,
    registry_inspector,

    register_theme,
    register_color,
    register_animation
)


# =========================================================
# PUBLIC API - ANIMATIONS
# =========================================================

from .animations import (

    # Original
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
    glitch,

    # New v0.2.0
    loading_dots,
    progress_fill,
    typing,
    countdown,
    success_check,
    loading_bar_wave
)


# =========================================================
# PUBLIC API - THEMES
# =========================================================

from .themes import (
    Theme,

    DEFAULT,
    DARK,
    NEON,
    FIRE,
    ICE,

    HACKER,
    VOID,
    ELECTRIC,
    NIGHT,
    ALERT,
    FROST,
    NATURE,
    DEV,
    GAMER,
    BRUTAL,

    set_theme,
    get_theme,
    apply_theme,
    create_theme
)


# =========================================================
# STAR IMPORT CONTROL
# =========================================================

__all__ = [

    "__version__",

    "banner",
    "about",


    # COLORS
    "C",
    "BG",
    "S",

    "rgb",
    "bg_rgb",

    "success",
    "error",
    "warning",
    "info",
    "miniTitle",

    "box1",
    "box2",
    "box3",
    "box4",
    "box5",
    "box6",
    "customBox",

    "rainbow",
    "blueGra",
    "redGra",
    "customGra",


    # UI
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

    "system_panel",
    "themes_manager",
    "animations_preview",
    "system_info",
    "registry_inspector",

    "register_theme",
    "register_color",
    "register_animation",


    # ANIMATIONS
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

    "loading_dots",
    "progress_fill",
    "typing",
    "countdown",
    "success_check",
    "loading_bar_wave",


    # THEMES
    "Theme",

    "DEFAULT",
    "DARK",
    "NEON",
    "FIRE",
    "ICE",

    "HACKER",
    "VOID",
    "ELECTRIC",
    "NIGHT",
    "ALERT",
    "FROST",
    "NATURE",
    "DEV",
    "GAMER",
    "BRUTAL",

    "set_theme",
    "get_theme",
    "apply_theme",
    "create_theme",
]