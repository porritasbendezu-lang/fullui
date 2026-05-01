"""
FULLUI
Advanced console UI system for Python terminals.
"""

# =========================================================
# VERSION
# =========================================================

__version__ = "0.3.0"

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
from . import layouts
from . import icons

# =========================================================
# FULLUI BANNER
# =========================================================

from .colors import C, S

def banner():
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

{C.y}Features:{S.rs}
• Menus
• Themes
• Animations
• Layout System

{C.y}Quick Start:{S.rs}

from fullui import *

panel("Welcome", t="HOME")
menu(t="Main Menu", op=["Play","Exit"])

{C.m}Developer Tools:{S.rs}
systemPanel()

{C.c}GitHub:{S.rs}
github.com/porritasbendezu-lang/fullui

{S.rs}"""
    )

about = banner

# =========================================================
# PUBLIC API - COLORS
# =========================================================

from .colors import (
    C, BG, S, G,
    rgb, bg_rgb,
    box1, box2, box3, box4, box5, box6, customBox,
    rainbow, blueGra, redGra, customGra,
    gradientSmooth, randomColor, randomRGB, randomGradient
)

# =========================================================
# PUBLIC API - ICONS
# =========================================================

from .icons import I

# =========================================================
# PUBLIC API - UI
# =========================================================

from .ui import (
    INFO, render, book,
    quiz, titleQuiz, question, answers,
    menu, title, subtitle, option, opbreak, uinput,
    success, error, warning, info, message, miniTitle,
    p, clear, pause, line_break, lb,
    systemPanel, themes_manager, animations_preview,
    system_info, registry_inspector,
    registerTheme, registerColor, registerAnim
)

# =========================================================
# PUBLIC API - LAYOUTS
# =========================================================

from .layouts import (
    Panel, panel,
    infoPanel, warningPanel, errorPanel,
    columns, split,
    stat, dashboard,
    registerLayout, useLayout,
    sidebar, dashboardLayout, splitLayout,
    stack, hero, Grid
)

# =========================================================
# PUBLIC API - ANIMATIONS
# =========================================================

from .animations import (
    # CORE
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
    loading_dots,
    progress_fill,
    typing,
    countdown,
    success_check,
    loading_bar_wave,

    # EXTRA
    spinner_dots,
    spinner_bar,
    loading_blocks,
    pulse_text,
    scanner,
    reverse_type,
    icon_spin,
    glitch_heavy,
    bar_wave_color,
    shake,
    fire_text,
    progress_ping,
    dot_matrix,
    spiral,
    success_burst,

    # SYSTEM
    A,
    set_anim,
)

# =========================================================
# PUBLIC API - THEMES
# =========================================================

from .themes import (
    Theme,
    DEFAULT, DARK, NEON, FIRE, ICE,
    HACKER, VOID, ELECTRIC, NIGHT,
    ALERT, FROST, NATURE, DEV, GAMER, BRUTAL,
    SUNSET, OCEAN, FOREST, CYBERPUNK, LAVENDER,
    GOLD, ROSE, MIDNIGHT, EMBER, MINT, CRIMSON_GOLD,
    AQUA_LIME, PURPLE_PINK, BLUE_ORANGE, EMERALD_GOLD,
    RED_BLACK, SKY_PURPLE, MANGO_FIRE, TEAL_ROSE,
    INDIGO_CYAN,
    CHRISTMAS, HALLOWEEN, VALENTINE,
    EASTER, NEW_YEAR, BIRTHDAY, CARNIVAL, INDEPENDENCE,
    SPRING_FEST, WINTER_FEST, OKTOBERFEST, DIWALI,
    FIRE_STORM, ICE_NEON, CYBER_VOID, FOREST_LIGHT, COSMIC_GOLD,
    setTheme, getTheme, applyTheme, createTheme
)

# =========================================================
# STAR IMPORT CONTROL
# =========================================================

__all__ = [

    "__version__",
    "banner",
    "about",

    # COLORS
    "C","BG","S","G",
    "rgb","bg_rgb",
    "box1","box2","box3","box4","box5","box6","customBox",
    "rainbow","blueGra","redGra","customGra",
    "gradientSmooth","randomColor","randomRGB","randomGradient",

    # ICONS
    "I",

    # UI
    "INFO","render","book",
    "quiz","titleQuiz","question","answers",
    "success","error","warning","info","message","miniTitle",
    "menu","title","subtitle","option","opbreak","uinput",
    "p","clear","pause","line_break","lb",
    "systemPanel","themes_manager","animations_preview",
    "system_info","registry_inspector",
    "registerTheme","registerColor","registerAnim",

    # LAYOUTS
    "Panel","panel",
    "infoPanel","warningPanel","errorPanel",
    "columns","split","stat","dashboard",
    "registerLayout","useLayout",
    "sidebar","dashboardLayout","splitLayout",
    "stack","hero","Grid",

    # ANIMATIONS   
    "spinner","dot_ripple","bounce","matrix","fade_in",
    "pulse_bar","type_shuffle","wave","blink","energy_pulse",
    "scanline","glitch","loading_dots","progress_fill",
    "typing","countdown","success_check","loading_bar_wave",
    "spinner_dots","spinner_bar","loading_blocks","pulse_text",
    "scanner","reverse_type","icon_spin","glitch_heavy",
    "bar_wave_color","shake","fire_text","progress_ping",
    "dot_matrix","spiral","success_burst","A","set_anim",

    # THEMES
    "Theme",
    "DEFAULT","DARK","NEON","FIRE","ICE",
    "HACKER","VOID","ELECTRIC","NIGHT",
    "ALERT","FROST","NATURE","DEV","GAMER","BRUTAL",
    "SUNSET","OCEAN","FOREST","CYBERPUNK","LAVENDER",
    "GOLD","ROSE","MIDNIGHT","EMBER","MINT","CRIMSON_GOLD",
    "AQUA_LIME","PURPLE_PINK","BLUE_ORANGE","EMERALD_GOLD",
    "RED_BLACK","SKY_PURPLE","MANGO_FIRE","TEAL_ROSE",
    "INDIGO_CYAN",
    "CHRISTMAS","HALLOWEEN","VALENTINE",
    "EASTER","NEW_YEAR","BIRTHDAY","CARNIVAL","INDEPENDENCE",
    "SPRING_FEST","WINTER_FEST","OKTOBERFEST","DIWALI",
    "FIRE_STORM", "ICE_NEON", "CYBER_VOID", "FOREST_LIGHT", "COSMIC_GOLD",
    "setTheme","getTheme","applyTheme","createTheme",
]