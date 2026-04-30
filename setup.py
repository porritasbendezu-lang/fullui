from setuptools import setup
from setuptools.command.install import install


class PostInstallCommand(install):
    def run(self):
        install.run(self)

        print(r"""
╔══════════════════════════════════════╗
║      FULLUI v0.2.3 INSTALLED ✓       ║
║  Advanced Console UI Framework       ║
╚══════════════════════════════════════╝

Quick start:
from fullui import *
menu(t="Hello", op=["Start"])

Demo:
python -c "import fullui; fullui.banner()"
""")


setup(
    cmdclass={
        "install": PostInstallCommand
    }
)