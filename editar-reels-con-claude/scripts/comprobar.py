#!/usr/bin/env python3
"""Comprueba que el ordenador tiene lo necesario para editar reels y dice cómo arreglar lo que falte.

Uso:
    python3 comprobar.py            # informe para leer
    python3 comprobar.py --json     # lo mismo, para otros scripts

Busca un ffmpeg capaz de quemar subtítulos (con libass). El ffmpeg normal de Homebrew no lo trae: hace falta
`brew install ffmpeg-full`, que se instala aparte, sin sustituir al normal.
"""
from __future__ import annotations

import json
import os
import platform
import shutil
import subprocess
import sys

# Sitios donde suele quedar un ffmpeg completo, además del que haya en el PATH.
CANDIDATOS = [
    "/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg",  # Mac con Apple Silicon
    "/usr/local/opt/ffmpeg-full/bin/ffmpeg",     # Mac con Intel
]


def filtros(ffmpeg: str) -> str:
    try:
        return subprocess.run([ffmpeg, "-hide_banner", "-filters"], capture_output=True, text=True,
                              timeout=20).stdout
    except (OSError, subprocess.TimeoutExpired):
        return ""


def quema_subtitulos(ffmpeg: str) -> bool:
    return any(linea.split()[1:2] == ["subtitles"] for linea in filtros(ffmpeg).splitlines())


def ffmpeg_con_subtitulos() -> str | None:
    """La ruta de un ffmpeg que puede quemar subtítulos, o None."""
    rutas = [os.environ.get("FFMPEG_SUBTITULOS", ""), shutil.which("ffmpeg") or ""] + CANDIDATOS
    for ruta in rutas:
        if ruta and os.path.exists(ruta) and quema_subtitulos(ruta):
            return ruta
    return None


CARPETA_SKILL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VENV = os.path.join(CARPETA_SKILL, ".venv")


def python_whisper() -> str:
    """El Python con el que se transcribe: el entorno propio de la skill si existe; si no, el actual."""
    propio = os.path.join(VENV, "bin", "python")
    return propio if os.path.exists(propio) else sys.executable


def tiene(python: str, modulo: str) -> bool:
    return subprocess.run([python, "-c", f"import {modulo}"], capture_output=True).returncode == 0


def informe() -> dict:
    ffmpeg = shutil.which("ffmpeg")
    ffprobe = shutil.which("ffprobe")
    python = python_whisper()
    whisper = tiene(python, "faster_whisper")
    pillow = tiene(python, "PIL")
    con_subs = ffmpeg_con_subtitulos()
    mac = platform.system() == "Darwin"
    arreglos = []
    if not ffmpeg or not ffprobe:
        arreglos.append("brew install ffmpeg" if mac else "Instala ffmpeg: https://ffmpeg.org/download.html")
    if not whisper or not pillow:
        arreglos.append(f'python3 -m venv "{VENV}" && "{VENV}/bin/pip" install faster-whisper pillow')
    return {
        "ffmpeg": ffmpeg,
        "ffprobe": ffprobe,
        "ffmpeg_subtitulos": con_subs,
        "faster_whisper": whisper,
        "pillow": pillow,
        "python": python,
        "listo": bool(ffmpeg and ffprobe and whisper and (con_subs or pillow)),
        "arreglos": arreglos,
    }


def main():
    datos = informe()
    if "--json" in sys.argv:
        print(json.dumps(datos, ensure_ascii=False))
        return
    marca = lambda ok: "OK " if ok else "FALTA"  # noqa: E731
    print(f"[{marca(datos['ffmpeg'] and datos['ffprobe'])}] ffmpeg y ffprobe (cortar y medir)")
    print(f"[{marca(datos['faster_whisper'])}] faster-whisper (transcribir) en {datos['python']}")
    print(f"[{marca(datos['pillow'])}] Pillow (dibujar subtítulos con el ffmpeg normal)")
    libass = datos["ffmpeg_subtitulos"]
    print(f"[{'OK ' if libass else 'NO '}] ffmpeg con libass (quemar subtítulos más rápido)"
          + (f": {libass}" if libass else ""))
    if datos["arreglos"]:
        print("\nPara arreglarlo:")
        for comando in datos["arreglos"]:
            print(f"    {comando}")
    if not libass:
        print("\nTu ffmpeg no trae libass ni drawtext (el normal de Homebrew no los trae), así que no puede quemar\n"
              "subtítulos por sí solo. Dos salidas:\n"
              "  1. Seguir así: montar.py dibuja los subtítulos con Pillow. Funciona, tarda algo más.\n"
              + ("  2. Instalar el completo: brew install ffmpeg-full (va aparte, no sustituye al normal, y los\n"
                 "     scripts lo encuentran solos). En versiones antiguas de macOS puede compilar durante horas.\n"
                 if platform.system() == "Darwin" else "  2. Instalar un ffmpeg compilado con libass (en Linux: sudo apt install ffmpeg).\n"))
    print("\nTodo listo." if datos["listo"] else "\nFalta algo: arréglalo antes de editar.")
    sys.exit(0 if datos["listo"] else 1)


if __name__ == "__main__":
    main()
