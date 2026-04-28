# 🎨 FULLUI - Console UI System

Librería para crear interfaces de consola avanzadas en Python con:

* 🎨 Colores ANSI y RGB
* ✨ Estilos de texto
* 🧱 Cajas decorativas
* 🌈 Gradientes de texto
* 🎮 Sistema de menús totalmente personalizable

Diseñada para:

* Juegos en consola
* Herramientas CLI
* Interfaces interactivas

---

# 📦 Instalación

```bash
pip install fullui
```

---

# 🚀 Uso básico

```python
from fullui import *

menu(
    t="Menu",
    op=["Jugar", "Salir"]
)
```

---

# 🚀 Importación modular (recomendada)

```python
from fullui.colors import C, S
from fullui.ui import menu, clear, pause, I

menu(
    t="Menu",
    op=["Jugar", "Salir"]
)

print(C.r + "Texto en rojo" + S.rs)
```

---

# 🚀 Todos los módulos disponibles

```python
from fullui import (
    # ===== COLORES =====
    C, BG, S,

    # ===== RGB =====
    rgb, bg_rgb,

    # ===== HELPERS =====
    success, error, warning, info, miniTitle,

    # ===== CAJAS =====
    box1, box2, box3, box4, box5, box6, customBox,

    # ===== GRADIENTES =====
    rainbow, blueGra, redGra, customGra,

    # ===== UI =====
    I, menu, title, subtitle, option, opbreak,

    # ===== FLUJO =====
    clear, pause
)
```

---

# 🎨 colors.py

Sistema completo de colores, estilos y utilidades visuales.

---

## 🧱 Colores de texto (`C`)

```python
C.r  # rojo
C.g  # verde
C.b  # azul
C.y  # amarillo
C.c  # cyan
C.w  # blanco
```

Incluye colores extendidos:

* orange
* pink
* brown
* purple
* dark variants

Uso:

```python
print(C.r + "Hola" + S.rs)
```

---

## 🎭 Colores de fondo (`BG`)

```python
BG.r  # fondo rojo
BG.b  # fondo azul
```

---

## ✨ Estilos (`S`)

```python
S.bd  # bold
S.it  # italic
S.ul  # underline
S.rs  # reset
```

---

## 🎯 Colores RGB

```python
rgb(255, 0, 0)
bg_rgb(0, 0, 255)
```

---

## ⚡ Helpers

```python
success("OK")
error("Error")
warning("Cuidado")
info("Info")
miniTitle("Titulo")
```

---

## 📦 Cajas

```python
box1("Texto")
box2("Texto")
box3("Texto")
box4("Texto")
box5("Texto")
box6("Texto")

customBox("Texto", "*", C.r)
```

---

## 🌈 Gradientes

```python
rainbow("Hola")
blueGra("Texto")
redGra("Texto")

customGra("Texto", C.r, C.g, C.b)
```

---

# 🖥️ ui.py

Sistema de interfaz para consola totalmente configurable.

---

## 🧠 Clase `I` (alias de parámetros)

Permite usar parámetros en formato corto o largo.

```python
I.t   # titleText
I.op  # options
I.k1  # key1
```

Ejemplo:

```python
menu(
    t="Menu",
    op=["Jugar", "Salir"]
)
```

---

## 🔄 Funciones de flujo

```python
clear()  # limpia consola
pause()  # pausa ejecución
```

---

## 🏷️ title()

```python
title(
    text="Titulo",
    margins="=",
    numMargins=30
)
```

---

## 🧾 subtitle()

```python
subtitle("Subtitulo")
```

---

## 🔢 option()

```python
option("Jugar", "[", "]", 1)
```

---

## ❌ opbreak()

```python
opbreak("Salir", "[", "]", "X")
```

---

# 🎮 menu()

Función principal del sistema.

Permite crear menús totalmente personalizables.

---

## 📌 Parámetros

### TEXTOS

* titleText
* subtitleText
* options

### ESTRUCTURA

* showTitle
* showSubtitle

### TITLE

* titleMargins
* titleWidth
* titleColorMargins
* titleColorText
* titleStyle

### SUBTITLE

* subtitleLines
* subtitleWidth
* subtitleColor
* subtitleStyle

### OPTIONS

* key1
* key2
* optionsColorText
* optionsColorKeys
* optionsStyle

### BREAK

* showBreak
* breakText
* breakSimbol
* breakColorText
* breakColorKeys
* breakStyle

### INPUT

* inputColor
* inputStyle
* prompt

---

## 🔥 Ejemplo completo

```python
menu(
    t="ZofA",
    st="Menu principal",
    op=["Jugar", "Opciones", "Salir"],

    tm="═",
    tw=40,
    tcm=C.p,
    tct=C.lb,

    k1="⟨",
    k2="⟩",
    ock=C.y,

    bt="Salir",
    bs="0",

    ic=C.g,
    p=">> "
)
```

---

## ⚡ Alias (corto vs largo)

Puedes usar ambos:

```python
menu(titleText="Menu")
menu(t="Menu")
```

Internamente se normalizan automáticamente.

---

# 🧩 Características

* 🎨 Colores ANSI + RGB
* 🧠 Alias inteligente (corto/largo)
* 🧱 Sistema de cajas
* 🌈 Gradientes de texto
* 🎮 Menús configurables
* ⚡ Fácil integración

---

# 🎯 Casos de uso

* Juegos en consola
* Herramientas CLI
* Interfaces interactivas
* Prototipos rápidos

---

# 🚀 Roadmap

* Navegación con teclado (↑ ↓)
* Sistema de temas
* Soporte multilinea
* Motor UI avanzado

---

# 📄 Licencia

MIT License

---

# 👨‍💻 Autor

Desarrollado como parte del sistema **LeonardX007 UI (LXT)**.