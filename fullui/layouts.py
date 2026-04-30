"""
layouts.py

Layout system for FULLUI.
Fully customizable + Layout Presets + Compatibility safe.
"""

# =========================================================
# IMPORTS
# =========================================================

from .colors import C, S

# =========================================================
# ALIAS SYSTEM
# =========================================================

LAYOUT_ALIAS = {
    "w": "width",
    "b": "border",
    "c": "color",
    "t": "title",
    "tc": "titleColor",
    "p": "padding",
    "a": "align",
    "g": "gap",
    "lw": "leftWidth",
    "rw": "rightWidth"
}

def _normalize(kwargs):
    return {LAYOUT_ALIAS.get(k, k): v for k, v in kwargs.items()}

# =========================================================
# PANEL CORE
# =========================================================

class Panel:

    def __init__(self, text="", **kwargs):
        from .themes import get_theme

        cfg = _normalize(kwargs)
        theme = get_theme()

        self.text = text
        self.width = cfg.get("width", 50)
        self.border = cfg.get("border", "single")
        self.color = cfg.get("color", theme.textColor)

        self.title = cfg.get("title", None)
        self.titleColor = cfg.get("titleColor", theme.titleColor)

        self.padding = cfg.get("padding", 1)
        self.align = cfg.get("align", "left")

        self.theme = theme

    def _chars(self):
        styles = {
            "single": ("┌","┐","└","┘","─","│"),
            "double": ("╔","╗","╚","╝","═","║"),
            "round":  ("╭","╮","╰","╯","─","│"),
            "heavy":  ("┏","┓","┗","┛","━","┃")
        }
        return styles.get(self.border, styles["single"])

    def _align(self, text, width):
        if self.align == "center":
            return text.center(width)
        elif self.align == "right":
            return text.rjust(width)
        return text.ljust(width)

    def _wrap(self, text, width):
        words = text.split(" ")
        lines = []
        current = ""

        for w in words:
            if len(current + w) + 1 <= width:
                current += w + " "
            else:
                lines.append(current.strip())
                current = w + " "

        if current:
            lines.append(current.strip())

        return lines

    def render(self):
        tl,tr,bl,br,h,v = self._chars()
        inner = self.width - 2

        raw_lines = self.text.split("\n")
        lines = []

        for line in raw_lines:
            lines.extend(self._wrap(line, inner))

        top = tl + h*inner + tr
        bottom = bl + h*inner + br

        out = []

        out.append(self.color + self.theme.titleStyle + top + S.rs)

        if self.title:
            title = self.title[:inner]  # evita overflow
            pad_total = inner - len(title)
            pad_left = pad_total // 2
            pad_right = pad_total - pad_left

            centered = (" " * pad_left) + title + (" " * pad_right)

            out.append(
                self.titleColor +
                self.theme.titleStyle +
                v +
                centered +
                v +
                S.rs
            )

        for _ in range(self.padding):
            out.append(v + " "*inner + v)

        for line in lines:
            out.append(
                self.theme.optionColor +
                v +
                self._align(line, inner) +
                v +
                S.rs
            )

        for _ in range(self.padding):
            out.append(v + " "*inner + v)

        out.append(self.color + bottom + S.rs)

        return "\n".join(out)

    def show(self):
        print(self.render())

# =========================================================
# QUICK PANEL
# =========================================================

def panel(text="", **kwargs):
    Panel(text, **kwargs).show()

# =========================================================
# COMPAT PANELS
# =========================================================

def info_panel(text, **kwargs):
    from .themes import get_theme
    t = get_theme()
    panel(text, t="INFO", c=t.subtitleColor, b="round", **kwargs)

def warning_panel(text, **kwargs):
    from .themes import get_theme
    t = get_theme()
    panel(text, t="WARNING", c=t.optionColor, b="double", **kwargs)

def error_panel(text, **kwargs):
    from .themes import get_theme
    t = get_theme()
    panel(text, t="ERROR", c=t.breakColor, b="heavy", **kwargs)

# =========================================================
# COLUMNS
# =========================================================

def columns(*items, **kwargs):
    cfg = _normalize(kwargs)
    gap = cfg.get("gap", 4)

    blocks = []

    for item in items:
        if isinstance(item, Panel):
            blocks.append(item.render().split("\n"))
        else:
            blocks.append(str(item).split("\n"))

    max_lines = max(len(b) for b in blocks)

    for b in blocks:
        while len(b) < max_lines:
            b.append("")

    for i in range(max_lines):
        print((" " * gap).join(block[i] for block in blocks))

# =========================================================
# SPLIT
# =========================================================

def split(left, right, **kwargs):
    cfg = _normalize(kwargs)
    width = cfg.get("width", 35)

    columns(
        Panel(left, width=width),
        Panel(right, width=width),
        **kwargs
    )

# =========================================================
# DASHBOARD CORE
# =========================================================

def stat(label, value, **kwargs):
    return Panel(
        f"{label}: {value}",
        w=24,
        a="center",
        b="round",
        **kwargs
    )

def dashboard(stats, **kwargs):
    panels = [stat(k, v, **kwargs) for k, v in stats]
    columns(*panels, **kwargs)

# =========================================================
# LAYOUT PRESETS SYSTEM
# =========================================================

_LAYOUT_PRESETS = {}

def register_layout(name, func):
    _LAYOUT_PRESETS[name] = func

def use_layout(name, *args, **kwargs):
    if name in _LAYOUT_PRESETS:
        return _LAYOUT_PRESETS[name](*args, **kwargs)
    else:
        raise ValueError(f"Layout '{name}' not found")

# =========================================================
# PRESETS
# =========================================================

def sidebar(menu_text, content, **kwargs):
    cfg = _normalize(kwargs)
    lw = cfg.get("leftWidth", 30)
    rw = cfg.get("rightWidth", 50)

    left = Panel(menu_text, width=lw, title="MENU")
    right = Panel(content, width=rw, title="CONTENT")

    columns(left, right, **kwargs)

def dashboard_layout(stats, **kwargs):
    panels = [
        Panel(f"{k}: {v}", w=24, a="center", b="round")
        for k, v in stats
    ]
    columns(*panels, **kwargs)

def split_layout(left, right, **kwargs):
    cfg = _normalize(kwargs)
    width = cfg.get("width", 40)

    columns(
        Panel(left, width=width),
        Panel(right, width=width),
        **kwargs
    )

def stack(*items, **kwargs):
    for item in items:
        if isinstance(item, Panel):
            print(item.render())
        else:
            panel(str(item), **kwargs)

def hero(title, subtitle="", **kwargs):
    cfg = _normalize(kwargs)
    width = cfg.get("width", 60)

    content = f"{title}\n\n{subtitle}"

    Panel(
        content,
        width=width,
        border="double",
        align="center",
        padding=2
    ).show()

# =========================================================
# REGISTER DEFAULT PRESETS
# =========================================================

register_layout("sidebar", sidebar)
register_layout("dashboard", dashboard_layout)
register_layout("split", split_layout)
register_layout("stack", stack)
register_layout("hero", hero)

# =========================================================
# GRID (FUTURE)
# =========================================================

class Grid:
    def __init__(self, **kwargs):
        self.items = []
        self.kwargs = kwargs

    def add(self, item):
        self.items.append(item)

    def show(self):
        columns(*self.items, **self.kwargs)

