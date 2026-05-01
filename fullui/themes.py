"""
themes.py

Theme system for FULLUI.

Allows customization of UI appearance such as:
- colors
- styles
- text behavior

Designed to be lightweight and easily extendable.

v0.3.0 ADDITIONS:
- Festival themes added
- Gradients themes added
- Better system of themes
"""

# =========================================================
# IMPORTS
# =========================================================

from .colors import C, S, BG, G

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
        titleGradientMargins = None,

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
        
        # GRADIENTS (NEW)
        titleGradient = None,
        subtitleGradient = None,
        optionGradient = None,
        breakGradient = None,
        inputGradient = None,
        
        # OPTIONS FULL CONTROL
        optionGradientKeys = None,
        optionGradientNum = None,

        # BREAK FULL CONTROL
        breakGradientKeys = None,
        breakGradientText = None,
    ):
        self.name = name

        self.textColor = textColor
        self.textStyle = textStyle

        self.titleColor = titleColor
        self.titleStyle = titleStyle
        self.titleColorMargins = titleColorMargins
        self.titleGradientMargins = titleGradientMargins

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
        
        self.titleGradient = titleGradient
        self.subtitleGradient = subtitleGradient
        self.optionGradient = optionGradient
        self.breakGradient = breakGradient
        self.inputGradient = inputGradient
        
        self.optionGradientKeys = optionGradientKeys
        self.optionGradientNum = optionGradientNum

        # BREAK FULL CONTROL
        self.breakGradientKeys = breakGradientKeys
        self.breakGradientText = breakGradientText


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
# FESTIVE THEMES (v0.3.0)
# =========================================================

CHRISTMAS = Theme(
    name="christmas",
    titleColor=rgb(220, 30, 30),
    titleColorMargins=rgb(0, 120, 40),
    subtitleColor=rgb(255, 230, 230),
    optionColor=rgb(240, 255, 240),
    optionKeyColor=rgb(0, 180, 60),
    breakColor=rgb(255, 80, 80),
    breakKeyColor=rgb(255, 80, 80),
    inputColor=rgb(0, 200, 80),
)

HALLOWEEN = Theme(
    name="halloween",
    titleColor=rgb(255, 120, 0),
    titleColorMargins=rgb(40, 0, 60),
    subtitleColor=rgb(255, 180, 80),
    optionColor=rgb(255, 220, 180),
    optionKeyColor=rgb(180, 80, 255),
    breakColor=rgb(255, 60, 60),
    breakKeyColor=rgb(255, 60, 60),
    inputColor=rgb(255, 140, 40),
)

VALENTINE = Theme(
    name="valentine",
    titleColor=rgb(255, 60, 120),
    titleColorMargins=rgb(180, 20, 80),
    subtitleColor=rgb(255, 180, 210),
    optionColor=rgb(255, 220, 235),
    optionKeyColor=rgb(255, 100, 160),
    breakColor=rgb(255, 80, 120),
    breakKeyColor=rgb(255, 80, 120),
    inputColor=rgb(255, 130, 180),
)

EASTER = Theme(
    name="easter",
    titleColor=rgb(180, 120, 255),
    titleColorMargins=rgb(120, 200, 140),
    subtitleColor=rgb(255, 220, 180),
    optionColor=rgb(240, 230, 255),
    optionKeyColor=rgb(255, 160, 200),
    breakColor=rgb(255, 180, 120),
    breakKeyColor=rgb(255, 180, 120),
    inputColor=rgb(200, 180, 255),
)

NEW_YEAR = Theme(
    name="new_year",
    titleColor=rgb(255, 215, 0),
    titleColorMargins=rgb(40, 40, 60),
    subtitleColor=rgb(220, 220, 255),
    optionColor=rgb(255, 245, 200),
    optionKeyColor=rgb(255, 180, 0),
    breakColor=rgb(255, 100, 100),
    breakKeyColor=rgb(255, 100, 100),
    inputColor=rgb(255, 220, 80),
)

BIRTHDAY = Theme(
    name="birthday",
    titleColor=rgb(255, 100, 180),
    titleColorMargins=rgb(100, 180, 255),
    subtitleColor=rgb(255, 220, 120),
    optionColor=rgb(255, 230, 240),
    optionKeyColor=rgb(180, 120, 255),
    breakColor=rgb(255, 120, 120),
    breakKeyColor=rgb(255, 120, 120),
    inputColor=rgb(255, 160, 220),
)

CARNIVAL = Theme(
    name="carnival",
    titleColor=rgb(255, 0, 200),
    titleColorMargins=rgb(0, 220, 180),
    subtitleColor=rgb(255, 220, 80),
    optionColor=rgb(255, 230, 180),
    optionKeyColor=rgb(120, 80, 255),
    breakColor=rgb(255, 80, 100),
    breakKeyColor=rgb(255, 80, 100),
    inputColor=rgb(0, 255, 220),
)

INDEPENDENCE = Theme(
    name="independence",
    titleColor=rgb(220, 30, 30),
    titleColorMargins=rgb(255, 255, 255),
    subtitleColor=rgb(220, 220, 220),
    optionColor=rgb(255, 240, 240),
    optionKeyColor=rgb(180, 0, 0),
    breakColor=rgb(255, 80, 80),
    breakKeyColor=rgb(255, 80, 80),
    inputColor=rgb(220, 50, 50),
)

SPRING_FEST = Theme(
    name="spring_fest",
    titleColor=rgb(80, 220, 120),
    titleColorMargins=rgb(255, 180, 200),
    subtitleColor=rgb(180, 255, 200),
    optionColor=rgb(220, 255, 230),
    optionKeyColor=rgb(255, 120, 180),
    breakColor=rgb(255, 150, 150),
    breakKeyColor=rgb(255, 150, 150),
    inputColor=rgb(120, 255, 180),
)

WINTER_FEST = Theme(
    name="winter_fest",
    titleColor=rgb(180, 220, 255),
    titleColorMargins=rgb(80, 120, 180),
    subtitleColor=rgb(240, 250, 255),
    optionColor=rgb(220, 240, 255),
    optionKeyColor=rgb(140, 200, 255),
    breakColor=rgb(255, 140, 160),
    breakKeyColor=rgb(255, 140, 160),
    inputColor=rgb(180, 230, 255),
)

OKTOBERFEST = Theme(
    name="oktoberfest",
    titleColor=rgb(40, 120, 220),
    titleColorMargins=rgb(180, 100, 40),
    subtitleColor=rgb(255, 220, 180),
    optionColor=rgb(240, 230, 200),
    optionKeyColor=rgb(60, 150, 255),
    breakColor=rgb(220, 120, 60),
    breakKeyColor=rgb(220, 120, 60),
    inputColor=rgb(80, 180, 255),
)

DIWALI = Theme(
    name="diwali",
    titleColor=rgb(255, 180, 0),
    titleColorMargins=rgb(140, 40, 80),
    subtitleColor=rgb(255, 220, 140),
    optionColor=rgb(255, 240, 200),
    optionKeyColor=rgb(255, 120, 40),
    breakColor=rgb(255, 90, 90),
    breakKeyColor=rgb(255, 90, 90),
    inputColor=rgb(255, 200, 80),
)

# =========================================================
# GRADIENTS THEMES
# =========================================================

FIRE_STORM = Theme(
    name="fire_storm",

    titleColor=C.r,
    titleGradient=G.fire,
    titleGradientMargins=G.fire,

    subtitleColor=C.o,
    subtitleGradient=G.sunset,

    optionColor=C.y,
    optionGradient=G.gold,

    optionKeyColor=C.fo,

    breakColor=C.r,
    breakGradient=G.fire,

    breakKeyColor=C.r,

    inputColor=C.o,
    inputGradient=G.sunset
)

ICE_NEON = Theme(
    name="ice_neon",

    titleColor=C.lb,
    titleGradient=G.ice,
    titleGradientMargins=G.ice,

    subtitleColor=C.c,
    subtitleGradient=G.ocean,

    optionColor=C.w,
    optionGradient=G.ice,

    optionKeyColor=C.bc,

    breakColor=C.c,
    breakGradient=G.ocean,

    breakKeyColor=C.c,

    inputColor=C.lb,
    inputGradient=G.ice
)

CYBER_VOID = Theme(
    name="cyber_void",

    titleColor=C.np,
    titleGradient=G.neon,
    titleGradientMargins=G.neon,

    subtitleColor=C.bc,
    subtitleGradient=G.ocean,

    optionColor=C.c,
    optionGradient=G.rg,

    optionKeyColor=C.ng,

    breakColor=C.r,
    breakGradient=G.br,

    breakKeyColor=C.r,

    inputColor=C.ng,
    inputGradient=G.neon
)

FOREST_LIGHT = Theme(
    name="forest_light",

    titleColor=C.dg,
    titleGradient=G.forest,
    titleGradientMargins=G.forest,

    subtitleColor=C.g,
    subtitleGradient=G.gb,

    optionColor=C.g,
    optionGradient=G.forest,

    optionKeyColor=C.dg,

    breakColor=C.br,
    breakGradient=G.rg,

    breakKeyColor=C.br,

    inputColor=C.g,
    inputGradient=G.forest
)

COSMIC_GOLD = Theme(
    name="cosmic_gold",

    titleColor=C.gd,
    titleGradient=G.gold,
    titleGradientMargins=G.gold,

    subtitleColor=C.y,
    subtitleGradient=G.sunset,

    optionColor=C.y,
    optionGradient=G.gold,

    optionKeyColor=C.gd,

    breakColor=C.r,
    breakGradient=G.fire,

    breakKeyColor=C.r,

    inputColor=C.gd,
    inputGradient=G.gold
)

CYBER_NEON = Theme(
    name="cyber_neon",

    titleColor=C.eb,
    titleGradient=G.cyber,
    titleGradientMargins=G.cyber,

    subtitleColor=C.bc,
    subtitleGradient=G.rgb13,

    optionColor=C.c,
    optionGradient=G.rgb6,

    optionKeyColor=C.ng,

    breakColor=C.r,
    breakGradient=G.rgb5,

    breakKeyColor=C.r,

    inputColor=C.ng,
    inputGradient=G.rgb13
)


TOXIC_WASTE = Theme(
    name="toxic_waste",

    titleColor=C.ln,
    titleGradient=G.toxic,
    titleGradientMargins=G.toxic,

    subtitleColor=C.ng,
    subtitleGradient=G.rgb7,

    optionColor=C.ln,
    optionGradient=G.rgb2,

    optionKeyColor=C.ng,

    breakColor=C.r,
    breakGradient=G.rgb12,

    breakKeyColor=C.r,

    inputColor=C.ng,
    inputGradient=G.rgb7
)


BLOOD_MOON = Theme(
    name="blood_moon",

    titleColor=C.dr,
    titleGradient=G.blood,
    titleGradientMargins=G.blood,

    subtitleColor=C.r,
    subtitleGradient=G.rgb12,

    optionColor=C.gray,
    optionGradient=G.rgb16,

    optionKeyColor=C.r,

    breakColor=C.r,
    breakGradient=G.rgb5,

    breakKeyColor=C.r,

    inputColor=C.r,
    inputGradient=G.rgb12
)


DEEP_OCEAN = Theme(
    name="deep_ocean",

    titleColor=C.b,
    titleGradient=G.deepsea,
    titleGradientMargins=G.deepsea,

    subtitleColor=C.c,
    subtitleGradient=G.rgb6,

    optionColor=C.lb,
    optionGradient=G.rgb17,

    optionKeyColor=C.c,

    breakColor=C.dc,
    breakGradient=G.rgb20,

    breakKeyColor=C.dc,

    inputColor=C.lb,
    inputGradient=G.rgb6
)


SUNCORE = Theme(
    name="suncore",

    titleColor=C.y,
    titleGradient=G.sun,
    titleGradientMargins=G.sun,

    subtitleColor=C.o,
    subtitleGradient=G.rgb10,

    optionColor=C.y,
    optionGradient=G.rgb1,

    optionKeyColor=C.fo,

    breakColor=C.r,
    breakGradient=G.rgb5,

    breakKeyColor=C.r,

    inputColor=C.o,
    inputGradient=G.rgb10
)


ROYAL_LUX = Theme(
    name="royal_lux",

    titleColor=C.gd,
    titleGradient=G.royal,
    titleGradientMargins=G.royal,

    subtitleColor=C.pu,
    subtitleGradient=G.rgb15,

    optionColor=C.gd,
    optionGradient=G.rgb16,

    optionKeyColor=C.pu,

    breakColor=C.r,
    breakGradient=G.rgb9,

    breakKeyColor=C.r,

    inputColor=C.gd,
    inputGradient=G.rgb16
)


STEEL_CORE = Theme(
    name="steel_core",

    titleColor=C.sg,
    titleGradient=G.steel,
    titleGradientMargins=G.steel,

    subtitleColor=C.gray,
    subtitleGradient=G.rgb18,

    optionColor=C.w,
    optionGradient=G.rgb8,

    optionKeyColor=C.sg,

    breakColor=C.r,
    breakGradient=G.rgb11,

    breakKeyColor=C.r,

    inputColor=C.gray,
    inputGradient=G.rgb18
)


PINK_VIBE = Theme(
    name="pink_vibe",

    titleColor=C.dp,
    titleGradient=G.pinkfire,
    titleGradientMargins=G.pinkfire,

    subtitleColor=C.p,
    subtitleGradient=G.rgb4,

    optionColor=C.p,
    optionGradient=G.rgb9,

    optionKeyColor=C.dp,

    breakColor=C.r,
    breakGradient=G.rgb14,

    breakKeyColor=C.r,

    inputColor=C.dp,
    inputGradient=G.rgb4
)


NIGHT_GLITCH = Theme(
    name="night_glitch",

    titleColor=C.np,
    titleGradient=G.rgb3,
    titleGradientMargins=G.rgb3,

    subtitleColor=C.bc,
    subtitleGradient=G.rgb13,

    optionColor=C.c,
    optionGradient=G.rgb19,

    optionKeyColor=C.np,

    breakColor=C.r,
    breakGradient=G.rgb11,

    breakKeyColor=C.r,

    inputColor=C.np,
    inputGradient=G.rgb3
)


AURORA = Theme(
    name="aurora",

    titleColor=C.bc,
    titleGradient=G.rgb2,
    titleGradientMargins=G.rgb2,

    subtitleColor=C.ng,
    subtitleGradient=G.rgb15,

    optionColor=C.c,
    optionGradient=G.rgb20,

    optionKeyColor=C.ng,

    breakColor=C.r,
    breakGradient=G.rgb19,

    breakKeyColor=C.r,

    inputColor=C.ng,
    inputGradient=G.rgb2
)

# =========================================================
# GLOBAL STATE
# =========================================================

_current_theme = DEFAULT


def setTheme(theme: Theme):
    """
    Set global active theme.
    """
    global _current_theme
    _current_theme = theme


def getTheme():
    """
    Return currently active theme.
    """
    return _current_theme


# =========================================================
# APPLY THEME TO MENU CONFIG
# =========================================================

def applyTheme(menu_kwargs: dict, theme: Theme = None):

    theme = theme or _current_theme

    # COLORS
    menu_kwargs["titleColorText"] = theme.titleColor
    menu_kwargs["titleStyle"] = theme.titleStyle
    menu_kwargs["titleColorMargins"] = theme.titleColorMargins
    menu_kwargs["titleGradientMargins"] = theme.titleGradientMargins

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

    #GRADIENTS
    menu_kwargs["titleGradient"] = theme.titleGradient
    menu_kwargs["subtitleGradient"] = theme.subtitleGradient
      
    menu_kwargs["optionsGradient"] = theme.optionGradient
    menu_kwargs["breakGradient"] = theme.breakGradient
    menu_kwargs["inputGradient"] = theme.inputGradient

    return menu_kwargs


# =========================================================
# THEME FACTORY
# =========================================================

def createTheme(**kwargs):
    """
    Create a custom theme dynamically.
    """
    return Theme(**kwargs)