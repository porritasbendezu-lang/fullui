import time
import sys
import random


"""
animations.py

Animated effects for terminal interfaces.

Includes:
- Loading spinners
- Progress animations
- Text reveal effects
- Glitch and pulse effects
"""


# =========================================================
# IMPORTS
# =========================================================

try:
    from .colors import C, S, BG
except ImportError:
    from colors import C, S, BG


# =========================================================
# INTERNAL HELPERS
# =========================================================

def _flush(text=""):
    """
    Overwrite current terminal line.
    """
    sys.stdout.write("\r" + text)
    sys.stdout.flush()


def _reset():
    """
    Reset styles and move to next line.
    """
    sys.stdout.write(S.rs + "\n")
    sys.stdout.flush()


# =========================================================
# SPINNER
# =========================================================

def spinner(
    text="Loading",
    duration=3,
    speed=0.1,
    color=C.c,
    style=S.bd
):
    """
    Classic rotating loading spinner.

    Parameters:
        text (str): Prefix text.
        duration (int|float): Total seconds.
        speed (float): Frame speed.
    """

    frames = ["|", "/", "-", "\\"]
    end = time.time() + duration
    i = 0

    while time.time() < end:
        _flush(
            f"{color}{style}{text} {frames[i % 4]}{S.rs}"
        )
        time.sleep(speed)
        i += 1

    _reset()


# =========================================================
# DOT RIPPLE
# =========================================================

def dot_ripple(
    text="Loading",
    duration=3,
    speed=0.3,
    color=C.y,
    style=S.bd
):
    """
    Animated growing dot loader.
    """

    end = time.time() + duration
    pattern = [".", "..", "...", "...."]

    while time.time() < end:
        for p in pattern:
            if time.time() >= end:
                break

            _flush(
                f"{color}{style}{text}{p}{S.rs}"
            )
            time.sleep(speed)

    _reset()


# =========================================================
# BOUNCE
# =========================================================

def bounce(
    text="UI",
    times=10,
    speed=0.05,
    color=C.m,
    style=S.bd
):
    """
    Horizontal bouncing text animation.
    """

    width = 10

    for _ in range(times):

        for i in range(width):
            _flush(
                " " * i +
                f"{color}{style}{text}{S.rs}"
            )
            time.sleep(speed)

        for i in range(width, 0, -1):
            _flush(
                " " * i +
                f"{color}{style}{text}{S.rs}"
            )
            time.sleep(speed)

    _reset()


# =========================================================
# MATRIX
# =========================================================

def matrix(
    text="SYSTEM",
    speed=0.05,
    color=C.g,
    style=S.bd
):
    """
    Matrix-style character reveal effect.
    """

    chars = "01!@#$%"

    for ch in text:

        for _ in range(3):
            _flush(
                f"{color}{style}"
                f"{random.choice(chars)}"
                f"{S.rs}"
            )
            time.sleep(speed)

        _flush(
            f"{color}{style}{ch}{S.rs}"
        )

    _reset()


# =========================================================
# FADE IN
# =========================================================

def fade_in(
    text,
    speed=0.05,
    color=C.w,
    style=S.bd
):
    """
    Reveal text progressively.
    """

    for i in range(1, len(text)+1):

        _flush(
            f"{color}{style}"
            f"{text[:i]}"
            f"{S.rs}"
        )
        time.sleep(speed)

    _reset()


# =========================================================
# PROGRESS BAR
# =========================================================

def pulse_bar(
    total=100,
    width=30,
    speed=0.02,
    color=C.g,
    style=S.bd
):
    """
    Animated progress bar.
    """

    for i in range(total+1):

        percent = i / total

        bar = (
            "█" * int(width * percent)
            + "-" * (width - int(width * percent))
        )

        _flush(
            f"{color}{style}"
            f"[{bar}] {int(percent*100)}%"
            f"{S.rs}"
        )

        time.sleep(speed)

    _reset()


# =========================================================
# TYPE SHUFFLE
# =========================================================

def type_shuffle(
    text,
    speed=0.03,
    color=C.c,
    style=S.bd
):
    """
    Glitch-like fake typing reveal.
    """

    chars = (
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "0123456789"
    )

    for i in range(len(text)):

        for _ in range(2):

            fake = "".join(
                random.choice(chars)
                for _ in text
            )

            _flush(
                f"{color}{style}{fake}{S.rs}"
            )

            time.sleep(speed)

        _flush(
            f"{color}{style}"
            f"{text[:i+1]}"
            f"{S.rs}"
        )

    _reset()


# =========================================================
# WAVE
# =========================================================

def wave(
    text,
    speed=0.1,
    color=C.b,
    style=S.bd
):
    """
    Wave-like horizontal movement.
    """

    for i in range(len(text)):

        _flush(
            " " * i +
            f"{color}{style}{text}{S.rs}"
        )

        time.sleep(speed)

    _reset()


# =========================================================
# BLINK
# =========================================================

def blink(
    text="READY",
    times=5,
    speed=0.3,
    color=C.r,
    style=S.bd
):
    """
    Blinking text effect.
    """

    for _ in range(times):

        _flush(
            f"{color}{style}{text}{S.rs}"
        )

        time.sleep(speed)

        _flush(" " * len(text))
        time.sleep(speed)

    _flush(
        f"{color}{style}{text}{S.rs}\n"
    )


# =========================================================
# ENERGY PULSE
# =========================================================

def energy_pulse(
    text="SYSTEM",
    cycles=10,
    speed=0.05,
    color=C.p,
    style=S.bd
):
    """
    Pulsing energy indicator effect.
    """

    for i in range(cycles):

        glow = "●" * (i % 5)

        _flush(
            f"{color}{style}"
            f"{text} {glow}"
            f"{S.rs}"
        )

        time.sleep(speed)

    _reset()


# =========================================================
# SCANLINE
# =========================================================

def scanline(
    text="Scanning",
    speed=0.05,
    color=C.c,
    style=S.bd
):
    """
    Moving scan cursor effect.
    """

    for i in range(len(text)):

        _flush(
            f"{color}{style}"
            f"{text[:i]}█"
            f"{S.rs}"
        )

        time.sleep(speed)

    _reset()


# =========================================================
# GLITCH
# =========================================================

def glitch(
    text,
    intensity=10,
    speed=0.05,
    color=C.r,
    style=S.bd
):
    """
    Random glitch distortion effect.
    """

    chars = "@#$%&*!?"

    for _ in range(intensity):

        glitched = "".join(
            c if random.random() > 0.3
            else random.choice(chars)
            for c in text
        )

        _flush(
            f"{color}{style}"
            f"{glitched}"
            f"{S.rs}"
        )

        time.sleep(speed)

    _flush(
        f"{color}{style}{text}{S.rs}\n"
    )