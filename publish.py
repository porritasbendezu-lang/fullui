from fullui import ui, C, G, animations as anim
import os
import subprocess

VERSION = "v0.3.0"

# =========================================================
# CORE RUNNER
# =========================================================

def run(cmd, title):
    ui.clear()

    ui.title(
        title,
        icon="🚀",
        color=C.c,
        gradientText=G.ocean
    )

    ui.message(
        f"EXEC → {cmd}",
        line="─",
        width=65,
        colorMessage=C.sg
    )

    anim.progress_fill(
        total=100,
        width=45,
        speed=0.01,
        label="EXECUTING"
    )

    result = subprocess.run(cmd, shell=True)

    if result.returncode != 0:
        ui.error("BUILD FAILED ❌")
        anim.glitch_heavy("CRITICAL ERROR")
        ui.pause()
        exit()


# =========================================================
# VISUAL STAGE SYSTEM
# =========================================================

def stage(title, icon, gradient=None, anim_fx=None):
    ui.clear()

    ui.title(
        title,
        icon=icon,
        color=C.w,
        gradientText=gradient or G.neon
    )

    if anim_fx:
        anim_fx()


# =========================================================
# CLEAN
# =========================================================

def clean():
    stage(
        "CLEAN WORKSPACE",
        "🧹",
        gradient=G.ice,
        anim_fx=lambda: anim.loading_blocks(width=30, cycles=20)
    )

    os.system("rmdir /s /q dist")
    os.system("rmdir /s /q build")
    os.system("for /d %%i in (*.egg-info) do rmdir /s /q %%i")

    ui.success("Workspace cleaned ✔")
    anim.fade_in("READY FOR BUILD", gradient=G.ice)


# =========================================================
# BUILD
# =========================================================

def build():
    stage(
        "BUILD PACKAGE",
        "📦",
        gradient=G.fire,
        anim_fx=lambda: anim.energy_pulse("COMPILING")
    )

    anim.progress_fill(
        total=100,
        width=45,
        speed=0.015,
        label="BUILDING PACKAGE",
        gradient=G.fire
    )

    run("py -m build", "COMPILING PACKAGE")


# =========================================================
# UPLOAD
# =========================================================

def upload():
    stage(
        "UPLOAD TO PYPI",
        "📤",
        gradient=G.ocean,
        anim_fx=lambda: anim.loading_bar_wave(width=35, cycles=25)
    )

    ui.message(
        "Connecting to PyPI...",
        line="═",
        width=60,
        colorMessage=C.c
    )

    anim.scanline("uploading", speed=0.04)

    run("py -m twine upload dist/*", "PUBLISHING TO PYPI")

    ui.success("PUBLISHED SUCCESSFULLY ✔")

    anim.pulse_bar(
        cycles=20,
        gradient=G.gold
    )


# =========================================================
# GIT FLOW
# =========================================================

def git_flow():
    stage(
        "GIT DEPLOY PIPELINE",
        "🔧",
        gradient=G.cyber,
        anim_fx=lambda: anim.matrix("SYNCING")
    )

    steps = [
        ("git add .", "INDEXING CHANGES"),
        (f'git commit -m "release {VERSION}"', "CREATING COMMIT"),
        (f"git tag {VERSION}", "TAGGING VERSION"),
        ("git push origin main", "SYNC MAIN"),
        (f"git push origin {VERSION}", "PUSH TAG")
    ]

    for cmd, label in steps:
        ui.message(label, line="─", width=60, colorMessage=C.m)

        anim.loading_dots("executing", cycles=3)

        run(cmd, label)


# =========================================================
# MENU (CLEAN + MODERN UI)
# =========================================================

def menu():
    ui.clear()

    ui.title(
        "FULLUI RELEASE SYSTEM",
        icon="🚀",
        color=C.c,
        gradientText=G.cyber
    )

    ui.subtitle(
        f"VERSION {VERSION}",
        color=C.m,
        gradientText=G.purple
    )

    ui.message(
        "Select pipeline mode",
        line="─",
        width=55,
        colorMessage=C.sg
    )

    ui.p("1. FULL RELEASE (clean → build → upload → git)")
    ui.p("2. BUILD ONLY")
    ui.p("3. UPLOAD ONLY")
    ui.p("4. GIT ONLY")

    choice = input(f"\n{C.c}> {C.r}")

    if choice == "1":
        clean()
        build()
        upload()
        git_flow()

    elif choice == "2":
        clean()
        build()

    elif choice == "3":
        upload()

    elif choice == "4":
        git_flow()

    else:
        ui.error("INVALID OPTION")
        anim.glitch_heavy("INPUT ERROR")
        ui.pause()
        return menu()

    ui.clear()

    ui.title(
        "DEPLOY COMPLETE",
        icon="✔",
        color=C.g,
        gradientText=G.gold
    )

    anim.success_burst("FULLUI READY")

    ui.pause()


# =========================================================
# ENTRY
# =========================================================

if __name__ == "__main__":
    menu()