"""
layouts.py

Layout system for FULLUI.
"""

from .colors import C, S


# =========================================================
# BASE PANEL
# =========================================================

class Panel:
    """
    Generic bordered panel.
    """

    def __init__(
        self,
        text="",
        width=50,
        border="single",
        color=C.w,
        title=None,
        padding=1
    ):
        self.text = text
        self.width = width
        self.border = border
        self.color = color
        self.title = title
        self.padding = padding


    def _chars(self):

        styles = {
            "single": ("┌","┐","└","┘","─","│"),
            "double": ("╔","╗","╚","╝","═","║"),
            "round":  ("╭","╮","╰","╯","─","│"),
            "heavy":  ("┏","┓","┗","┛","━","┃")
        }

        return styles.get(
            self.border,
            styles["single"]
        )


    def render(self):

        tl,tr,bl,br,h,v = self._chars()

        lines = self.text.split("\n")

        inner_width = self.width - 2

        top = tl + h*inner_width + tr
        bottom = bl + h*inner_width + br

        output = []

        output.append(self.color + top)

        if self.title:
            title_line = (
                v +
                self.title.center(inner_width) +
                v
            )
            output.append(title_line)

        for _ in range(self.padding):
            output.append(v + " "*inner_width + v)

        for line in lines:
            output.append(
                v +
                line[:inner_width].ljust(inner_width) +
                v
            )

        for _ in range(self.padding):
            output.append(v + " "*inner_width + v)

        output.append(bottom + S.rs)

        return "\n".join(output)


    def show(self):
        print(self.render())


# =========================================================
# QUICK PANELS
# =========================================================

def panel(text, **kwargs):
    Panel(text, **kwargs).show()


def info_panel(text):
    panel(
        text,
        title="INFO",
        color=C.c,
        border="round"
    )


def warning_panel(text):
    panel(
        text,
        title="WARNING",
        color=C.y,
        border="double"
    )


def error_panel(text):
    panel(
        text,
        title="ERROR",
        color=C.r,
        border="heavy"
    )


# =========================================================
# COLUMNS LAYOUT
# =========================================================

def columns(*texts, width=30, gap=4):
    """
    Side by side columns.
    """

    blocks=[]

    for t in texts:
        lines=t.split("\n")
        blocks.append(lines)

    max_lines=max(len(b) for b in blocks)

    for b in blocks:
        while len(b)<max_lines:
            b.append("")

    for i in range(max_lines):
        row=[]
        for block in blocks:
            row.append(
                block[i][:width].ljust(width)
            )
        print((" "*gap).join(row))


# =========================================================
# SPLIT SCREEN
# =========================================================

def split(left,right,width=35):
    columns(
        left,
        right,
        width=width
    )


# =========================================================
# DASHBOARD ROW
# =========================================================

def stat(label,value,color=C.g):

    txt=(
        f"{label}: {value}"
    )

    return Panel(
        txt,
        width=24,
        color=color,
        border="round"
    ).render()


def dashboard(stats):
    """
    stats=[("HP",100), ("Gold",999)]
    """

    rendered=[]

    for label,value in stats:
        rendered.append(
            stat(label,value)
            .split("\n")
        )

    max_lines=max(len(x) for x in rendered)

    for i in range(max_lines):
        row=[]
        for panel in rendered:
            row.append(panel[i])
        print("  ".join(row))


# =========================================================
# FUTURE GRID CLASS (v0.2.2)
# =========================================================

class Grid:
    """
    Placeholder for future upgrade.
    """

    def __init__(self):
        self.items=[]

    def add(self,item):
        self.items.append(item)

    def show(self):
        for item in self.items:
            print(item)