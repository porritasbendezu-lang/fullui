"""
animations.py

Animated effects for terminal interfaces.

v0.3.1 ADDITIONS:
- Fix color handling in pulse_text
"""

# =========================================================
# IMPORTS
# =========================================================

import time
import sys
import random

# =============== EXCEPT ===============

try:
    from .colors import C, S, BG, G
    from .icons import I
except ImportError:
    from colors import C, S, BG, G
    from icons import I

# =========================================================
# RENDER
# =========================================================

def _render(text, color=None, gradient=None):
    # PRIORIDAD: gradient SOLO si se usa explícitamente
    if gradient is not None and color is None:
        return gradient(text)

    if color is not None and gradient is None:
        return f"{color}{text}{S.rs}"

    if gradient is not None and color is not None:
        # híbrido real (no uno reemplaza al otro)
        return gradient(f"{color}{text}{S.rs}")

    return text

# =========================================================
# GLOBAL CONFIG (EDITABLE SYSTEM)
# =========================================================

_ANIM_CONFIG = {
    # Base spinners
    "spinner_frames": [I.circle, I.circle_empty, I.circle_dot, I.circle_half],
    "spinner_dots_frames": ["⠁","⠃","⠇","⠧","⠷","⠿"],
    "spinner_bar_frames": ["▁","▂","▃","▄","▅","▆","▇","█"],
    "spiral_frames": ["◐","◓","◑","◒"],
    "icon_spin_frames": ["|","/","-","\\"],

    # Characters
    "glitch_chars": "@#$%&*!?",
    "glitch_heavy_chars": "@#$%&*!?<>[]{}",
    "matrix_chars": "01@#$%&",
    "type_shuffle_chars": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",

    # Colors
    "pulse_colors": [C.r, C.y, C.g, C.c, C.b, C.m],

    # Gradients
    "default_gradient": G.fire,
    "gradient_spinner_bar": G.ocean,
    "gradient_loading_blocks": G.neon,
    "gradient_scanner": G.ice,
    "gradient_fire": G.fire,
    "gradient_success": G.gold,

    # Icons
    "energy_icons": [I.circle, I.circle_dot, I.block],
    "burst_icons": [I.circle, I.star, I.sparkle, I.check],

    # Success frames
    "success_frames": [
        f"[{I.square_empty}]",
        f"[{I.check}]",
        f"[{I.check}{I.check}]"
    ],

    # Misc
    "shake_range": (0, 5),
}

def set_anim(key, value):
    _ANIM_CONFIG[key] = value

def get_anim(key, default=None):
    return _ANIM_CONFIG.get(key, default)

# =========================================================
# INTERNAL HELPERS
# =========================================================

def _flush(text=""):
    sys.stdout.write("\r" + text)
    sys.stdout.flush()

def _reset():
    sys.stdout.write(S.rs + "\n")
    sys.stdout.flush()

# =========================================================
# ANIMATIONS
# =========================================================

# =============== SPINNER ===============

def spinner(text="Loading", duration=3, speed=0.1,
            color=None, gradient=None, style=S.bd, frames=None):

    frames = frames or get_anim("spinner_frames")

    end = time.time() + duration
    i = 0

    while time.time() < end:
        frame = f"{frames[i % len(frames)]} {text}"
        _flush(_render(frame, color=color, gradient=gradient))
        time.sleep(speed)
        i += 1

    _reset()

# =============== DOT RIPPLE ===============

def dot_ripple(text="Loading", duration=3, speed=0.3,
               color=None, gradient=None, style=S.bd):

    pattern = ["", ".", "..", "..."]
    end = time.time() + duration

    i = 0

    while time.time() < end:
        for p in pattern:
            if time.time() >= end:
                break

            frame = f"{text}{p}"
            _flush(_render(frame, color=color, gradient=gradient))
            time.sleep(speed)

        i += 1

    _reset()

# =============== BOUNCE ===============

def bounce(text="UI", times=10, speed=0.05,
           color=None, gradient=None):

    width = 10

    for _ in range(times):
        for i in range(width):
            frame = " " * i + text
            _flush(_render(frame, color=color, gradient=gradient))
            time.sleep(speed)

        for i in range(width, 0, -1):
            frame = " " * i + text
            _flush(_render(frame, color=color, gradient=gradient))
            time.sleep(speed)

    _reset()

# =============== MATRIX ===============

def matrix(text="SYSTEM", speed=0.05,
           color=None, gradient=None):

    chars = "01@#$%&"

    for ch in text:
        for _ in range(3):
            _flush(_render(random.choice(chars), color=color, gradient=gradient))
            time.sleep(speed)

        _flush(_render(ch, color=color, gradient=gradient))

    _reset()

# =============== FADE IN ===============

def fade_in(text, speed=0.05,
            color=None, gradient=None):

    out = ""
    for ch in text:
        out += ch
        _flush(_render(out, color=color, gradient=gradient))
        time.sleep(speed)

    _reset()

# =============== PULSE BAR ===============

def pulse_bar(text="FULLUI", cycles=10, speed=0.1,
              color=None, gradient=None):

    colors = [C.r, C.y, C.g, C.c, C.b, C.m]

    for i in range(cycles):
        c = colors[i % len(colors)]

        frame = text

        if gradient is not None:
            out = gradient(frame)

        elif color is None:
            out = f"{c}{frame}{S.rs}"

        else:
            out = f"{color}{frame}{S.rs}"

        _flush(out)
        time.sleep(speed)

    _reset()

# =============== TYPESHUFFLE ===============

def type_shuffle(text, speed=0.03,
                 color=None, gradient=None):

    chars = "abcdefghijklmnopqrstuvwxyz0123456789"

    for i in range(len(text)):
        fake = "".join(random.choice(chars) for _ in text)

        _flush(_render(fake, color=color, gradient=gradient))
        time.sleep(speed)

        _flush(_render(text[:i+1], color=color, gradient=gradient))

    _reset()

# =============== WAVE ===============

def wave(text, speed=0.1,
         color=None, gradient=None):

    for i in range(len(text)):
        frame = " " * i + text
        _flush(_render(frame, color=color, gradient=gradient))
        time.sleep(speed)

    _reset()

# =============== BLINK ===============

def blink(text="READY", times=5, speed=0.3,
          color=None, gradient=None):

    for _ in range(times):
        _flush(_render(text, color=color, gradient=gradient))
        time.sleep(speed)

        _flush(_render(" " * len(text), color=color, gradient=gradient))
        time.sleep(speed)

    _flush(_render(text, color=color, gradient=gradient) + "\n")

# =============== ENERGY PULSE ===============

def energy_pulse(text="SYSTEM", cycles=10, speed=0.05,
                 color=None, gradient=None):

    icons = [I.circle, I.circle_dot, I.block]

    for i in range(cycles):
        glow = icons[i % len(icons)] * (i % 5)
        frame = f"{text} {glow}"

        _flush(_render(frame, color=color, gradient=gradient))
        time.sleep(speed)

    _reset()

# =============== SCANLINE ===============

def scanline(text="Scanning", speed=0.05,
             color=None, gradient=None):

    for i in range(len(text)):
        frame = text[:i] + "█"
        _flush(_render(frame, color=color, gradient=gradient))
        time.sleep(speed)

    _reset()

# =============== GLITCH ===============

def glitch(text, intensity=10, speed=0.05,
           color=None, gradient=None):

    chars = "@#$%&*!?"

    for _ in range(intensity):
        out = "".join(
            c if random.random() > 0.3 else random.choice(chars)
            for c in text
        )

        _flush(_render(out, color=color, gradient=gradient))
        time.sleep(speed)

    _flush(_render(text, color=color, gradient=gradient) + "\n")

# =============== LOADING DOTS ===============

def loading_dots(text="Loading", cycles=6, speed=0.4,
                 color=None, gradient=None):

    dots = ["", ".", "..", "..."]

    for _ in range(cycles):
        for d in dots:
            _flush(_render(text + d, color=color, gradient=gradient))
            time.sleep(speed)

    _reset()

# =============== PROGRESS FILL ===============

def progress_fill(total=100, width=40, speed=0.02,
                  color=None, gradient=None, label="Progress"):

    for i in range(total + 1):
        percent = i / total
        filled = int(width * percent)

        bar = I.block * filled + I.light * (width - filled)
        text = f"{label} [{bar}] {int(percent*100)}%"

        if gradient is not None and color is None:
            out = gradient(text)

        elif color is not None and gradient is None:
            out = f"{color}{text}{S.rs}"

        elif color is not None and gradient is not None:
            out = gradient(f"{color}{text}{S.rs}")

        else:
            out = text

        _flush(out)
        time.sleep(speed)

    _reset()


# =============== TYPING ===============

def typing(text, speed=0.03,
           color=None, gradient=None):

    out = ""
    for ch in text:
        out += ch
        _flush(_render(out, color=color, gradient=gradient))
        time.sleep(speed)

    _reset()

# =============== COUNTDOWN ===============

def countdown(seconds=5,
              color=None, gradient=None):

    for i in range(seconds, 0, -1):
        frame = f"Starting in {i}..."
        _flush(_render(frame, color=color, gradient=gradient))
        time.sleep(1)

    _flush(_render("GO!", color=color, gradient=gradient) + "\n")

# =============== SUCCESS CHECK ===============

def success_check(text="Success", speed=0.1,
                  color=None, gradient=None):

    frames = ["[ ]", "[✓]", "[✓✓]", "[✓✓✓]"]

    for f in frames:
        frame = f"{f} {text}"
        _flush(_render(frame, color=color, gradient=gradient))
        time.sleep(speed)

    _reset()

# =============== LOADING BAR WAVE ===============

def loading_bar_wave(width=30, cycles=20, speed=0.05,
                     color=None, gradient=None):

    for i in range(cycles):
        bar = ["-"] * width
        bar[i % width] = "█"

        frame = "[" + "".join(bar) + "]"
        _flush(_render(frame, color=color, gradient=gradient))
        time.sleep(speed)

    _reset()

# =========================================================
# NEW ANIMATIONS (v0.3.0)
# =========================================================

# =============== SPINNER DOTS ===============

def spinner_dots(text="Loading", duration=3, speed=0.2, color=None, gradient=None):
    frames = get_anim("spinner_dots_frames")
    end = time.time() + duration
    i = 0

    while time.time() < end:
        txt = f"{frames[i % len(frames)]} {text}"
        _flush(_render(txt, color=color, gradient=gradient))
        time.sleep(speed)
        i += 1

    _reset()

# =============== SPINNER BAR ===============

def spinner_bar(text="Loading", duration=3, speed=0.1, color=None, gradient=None):
    frames = get_anim("spinner_bar_frames")
    gradient = gradient or get_anim("gradient_spinner_bar")

    end = time.time() + duration
    i = 0

    while time.time() < end:
        txt = f"{frames[i % len(frames)]} {text}"
        _flush(_render(txt, color=color, gradient=gradient))
        time.sleep(speed)
        i += 1

    _reset()

# =============== LOADING BLOCKS ===============

def loading_blocks(width=20, cycles=20, speed=0.05, color=None, gradient=None):
    gradient = gradient or get_anim("gradient_loading_blocks")

    for i in range(cycles):
        bar = [I.light] * width
        bar[i % width] = I.block

        text = "".join(bar)
        _flush(_render(text, color=color, gradient=gradient))

        time.sleep(speed)

    _reset()

# =============== PULSE TEXT ===============

def pulse_text(text="FULLUI", cycles=10, speed=0.1, color=None, gradient=None):
    colors = get_anim("pulse_colors")

    for i in range(cycles):
        c = colors[i % len(colors)]

        styled = f"{c}{S.bd}{text}{S.rs}"

        _flush(_render(styled, color=None, gradient=gradient))
        time.sleep(speed)

    _reset()

# =============== SCANNER ===============

def scanner(width=30, cycles=15, speed=0.05, color=None, gradient=None):
    gradient = gradient or get_anim("gradient_scanner")

    for i in range(cycles):
        line = [I.light] * width
        pos = i % width
        line[pos] = I.block

        base = "".join(line[:pos]) + _render(line[pos], gradient=gradient) + "".join(line[pos+1:])

        _flush(base)
        time.sleep(speed)

    _reset()

# =============== REVERSE TYPE ===============

def reverse_type(text, speed=0.05):
    for i in range(len(text), 0, -1):
        _flush(C.y + text[:i] + S.rs)
        time.sleep(speed)
    _reset()

# =============== ICON SPIN ===============

def icon_spin(icon=I.circle, cycles=20, speed=0.1):
    frames = get_anim("icon_spin_frames")

    for i in range(cycles):
        _flush(f"{C.c}{frames[i%len(frames)]} {icon}{S.rs}")
        time.sleep(speed)
    _reset()

# =============== GLITCH HEAVY ===============

def glitch_heavy(text, cycles=15, speed=0.03):
    chars = get_anim("glitch_heavy_chars")

    for _ in range(cycles):
        out = "".join(random.choice(chars) for _ in text)
        _flush(C.r + out + S.rs)
        time.sleep(speed)

    _flush(C.g + text + S.rs + "\n")

# =============== BAR WAVE COLOR ===============

def bar_wave_color(width=30, cycles=30, speed=0.05):
    for i in range(cycles):
        bar = ""
        for j in range(width):
            if j == i % width:
                bar += C.c + I.block
            else:
                bar += C.b + I.light
        _flush(bar + S.rs)
        time.sleep(speed)
    _reset()

# =============== SHAKE ===============

def shake(text="ERROR", cycles=20, speed=0.03):
    min_s, max_s = get_anim("shake_range")

    for _ in range(cycles):
        offset = random.randint(min_s, max_s)
        _flush(" " * offset + C.r + text + S.rs)
        time.sleep(speed)
    _reset()

# =============== FIRE TEX ===============

def fire_text(text="FIRE", cycles=20, speed=0.05):

    fire_colors = [C.r, C.y, C.r, C.m]

    for i in range(cycles):
        colored = ""

        for j, ch in enumerate(text):
            c = fire_colors[(i + j) % len(fire_colors)]
            colored += f"{c}{ch}"

        colored += S.rs

        _flush(colored)
        time.sleep(speed)

    _reset()

# =============== PROGRESS PING ===============

def progress_ping(width=30, cycles=20, speed=0.05):
    for i in range(cycles):
        bar = [I.light]*width
        bar[i % width] = I.circle
        _flush(C.c + "".join(bar) + S.rs)
        time.sleep(speed)
    _reset()

# =============== DOT MATRIX ===============

def dot_matrix(width=20, height=5, cycles=20, speed=0.05):
    for _ in range(cycles):
        lines = []
        for _ in range(height):
            line = "".join(random.choice([I.dot, I.bullet]) for _ in range(width))
            lines.append(line)
        _flush("\n".join(lines))
        time.sleep(speed)
    _reset()

# =============== SPIRAL ===============

def spiral(text="Loading", cycles=20, speed=0.1):
    frames = get_anim("spiral_frames")

    for i in range(cycles):
        _flush(f"{C.m}{frames[i%len(frames)]} {text}{S.rs}")
        time.sleep(speed)
    _reset()

# =============== SUCCES BURST ===============

def success_burst(text="SUCCESS", speed=0.1, color=None, gradient=None):
    frames = get_anim("burst_icons")
    gradient = gradient or get_anim("gradient_success")

    for f in frames:
        _flush(_render(f"{f} {text}", color=color, gradient=gradient))
        time.sleep(speed)

    _reset()

# =========================================================
# WRAPPER
# =========================================================

class A:
    # =============== CORE ===============
    spinner = spinner
    dot_ripple = dot_ripple
    bounce = bounce
    matrix = matrix
    fade_in = fade_in
    pulse_bar = pulse_bar
    type_shuffle = type_shuffle
    wave = wave
    blink = blink
    energy = energy_pulse
    scanline = scanline
    glitch = glitch

    loading_dots = loading_dots
    progress_fill = progress_fill
    typing = typing
    countdown = countdown
    success_check = success_check
    loading_bar_wave = loading_bar_wave

    # =============== SHORT ALIASES ===============

    sp = spinner
    dr = dot_ripple
    bn = bounce
    mx = matrix
    fi = fade_in
    pb = pulse_bar
    ts = type_shuffle
    wv = wave
    bl = blink
    en = energy_pulse
    sc = scanline
    gl = glitch

    ld = loading_dots
    pr = progress_fill
    ty = typing
    cd = countdown
    ok = success_check
    wb = loading_bar_wave

    # =============== LONG ALIASES ===============
    
    dot = dot_ripple
    fade = fade_in
    bar = pulse_bar
    shuffle = type_shuffle
    scan = scanline
    dots = loading_dots
    progress = progress_fill
    success = success_check
    wavebar = loading_bar_wave

    # =============== NEW (v0.3.0) ===============

    spinner_dots = spinner_dots
    spinner_bar = spinner_bar
    loading_blocks = loading_blocks
    pulse_text = pulse_text
    scanner = scanner
    reverse_type = reverse_type
    icon_spin = icon_spin
    glitch_heavy = glitch_heavy
    bar_wave_color = bar_wave_color
    shake = shake
    fire_text = fire_text
    progress_ping = progress_ping
    dot_matrix = dot_matrix
    spiral = spiral
    success_burst = success_burst
    
    # =============== SHORT ALIASES (v0.3.0) ===============
    
    spd = spinner_dots
    spb = spinner_bar
    lb = loading_blocks
    pt = pulse_text
    sn = scanner
    rt = reverse_type
    isp = icon_spin
    gh = glitch_heavy
    bwc = bar_wave_color
    sk = shake
    ft = fire_text
    pp = progress_ping
    dm = dot_matrix
    srl = spiral
    sb = success_burst