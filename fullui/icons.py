"""
icons.py

Icons system for FULLUI.

v0.3.1 ADDITIONS:
- Added more icons (arrows, shapes, stars, blocks, bullets, numbers, math symbols, system icons, time icons, media icons, extra symbols)
- Added ASCII fallback icons for check, cross, and arrow
"""

class I:
    """
    Unicode icon system (200+ icons)
    Clean + single alias per icon (FULLUI style)
    """

    # =========================
    # CHECK / STATUS
    # =========================
    check = "✔"; ck = check
    error = "✖"; er = error
    warning = "⚠"; wr = warning
    info = "ℹ"; inf = info
    plus = "✚"; pl = plus
    minus = "−"; mn = minus

    # =========================
    # ARROWS (30+)
    # =========================
    arrow = "➤"; ar = arrow
    right = "→"; r = right
    left = "←"; l = left
    up = "↑"; u = up
    down = "↓"; d = down

    r2 = "⇒"
    l2 = "⇐"
    u2 = "⇑"
    d2 = "⇓"

    loop = "↻"
    back = "↩"
    curve = "↪"
    swap = "⇄"
    sync = "⇆"

    # =========================
    # SHAPES (40+)
    # =========================
    square = "■"; sq = square
    square_empty = "□"; se = square_empty
    square_small = "▪"; ss = square_small
    square_small_empty = "▫"; sse = square_small_empty

    circle = "●"; ci = circle
    circle_empty = "○"; ce = circle_empty
    circle_dot = "◉"; cd = circle_dot
    circle_half = "◐"; ch = circle_half

    triangle_up = "▲"; tu = triangle_up
    triangle_down = "▼"; td = triangle_down
    triangle_right = "▶"; tr = triangle_right
    triangle_left = "◀"; tl = triangle_left

    diamond = "◆"; di = diamond
    diamond_empty = "◇"; de = diamond_empty

    # =========================
    # STARS (10+)
    # =========================
    star = "★"; st = star
    star_empty = "☆"; ste = star_empty
    star_small = "✦"; sts = star_small
    star_big = "✶"; stb = star_big
    sparkle = "✧"; spk = sparkle

    # =========================
    # BOX DRAWING (40+)
    # =========================
    h = "─"
    v = "│"
    hd = "═"
    vd = "║"

    tl = "┌"
    trc = "┐"
    bl = "└"
    br = "┘"

    tee_u = "┴"
    tee_d = "┬"
    tee_l = "┤"
    tee_r = "├"
    cross = "┼"

    # =========================
    # BLOCKS (10+)
    # =========================
    block = "█"; blc = block
    dark = "▓"; dk = dark
    mid = "▒"; md = mid
    light = "░"; lt = light

    # =========================
    # BULLETS / TEXT (10+)
    # =========================
    bullet = "•"; bu = bullet
    bullet2 = "‣"; b2 = bullet2
    dot = "·"; dt = dot
    dash = "–"; ds = dash
    ellipsis = "…"; el = ellipsis

    # =========================
    # NUMBERS (20+)
    # =========================
    n0 = "⓪"
    n1 = "①"
    n2 = "②"
    n3 = "③"
    n4 = "④"
    n5 = "⑤"
    n6 = "⑥"
    n7 = "⑦"
    n8 = "⑧"
    n9 = "⑨"

    n10 = "⑩"
    n11 = "⑪"
    n12 = "⑫"
    n13 = "⑬"
    n14 = "⑭"
    n15 = "⑮"
    n16 = "⑯"
    n17 = "⑰"
    n18 = "⑱"
    n19 = "⑲"
    n20 = "⑳"

    # =========================
    # MATH (15+)
    # =========================
    eq = "="
    neq = "≠"
    approx = "≈"; ap = approx
    gt = ">"
    lt_ = "<"
    gte = "≥"
    lte = "≤"
    infy = "∞"
    sum = "∑"
    prod = "∏"
    root = "√"

    # =========================
    # SYSTEM (20+)
    # =========================
    gear = "⚙"; gr = gear
    power = "⏻"; pw = power
    reload = "⟳"; rl = reload
    sync2 = "⇆"; sy = sync2
    link = "⛓"; lk = link
    unlink = "⛓̸"; ul = unlink

    # =========================
    # TIME (10+)
    # =========================
    clock = "⏱"; cl = clock
    timer = "⏲"; tm = timer
    hourglass = "⌛"; hg = hourglass

    # =========================
    # MEDIA (10+)
    # =========================
    play = "▶"; py = play
    pause = "⏸"; ps = pause
    stop = "■"; stp = stop
    record = "●"; rec = record
    next = "⏭"; nx = next
    prev = "⏮"; pv = prev

    # =========================
    # EXTRA SYMBOLS (30+)
    # =========================
    flag = "⚑"; fl = flag
    anchor = "⚓"; an = anchor
    scissors = "✂"; sc = scissors
    pencil = "✎"; pn = pencil
    check2 = "✓"; ck2 = check2
    cross2 = "✗"; cr2 = cross2

    heart = "♥"; ht = heart
    spade = "♠"; sp = spade
    club = "♣"; cb = club
    diamond_card = "♦"; dc = diamond_card

    music = "♪"; mu = music
    music2 = "♫"; mu2 = music2

    sun = "☀"; sn = sun
    cloud = "☁"; cld = cloud
    umbrella = "☂"; umb = umbrella
    snow = "❄"; sw = snow

    phone = "☎"; ph = phone
    peace = "☮"; pc = peace
    yin = "☯"; yn = yin

    # =========================
    # ASCII fallback
    # =========================
    ack = "v"
    acr = "x"
    aar = "->"