#!/usr/bin/env python3
"""Control de calidad del reel: medidas, volumen y una hoja de fotogramas para mirarla antes de entregar.

Uso:
    python3 revisar.py reel.mp4
    python3 revisar.py reel.mp4 --hoja trabajo/hoja.jpg

Comprueba que sale en 1080x1920, cuánto dura, que el volumen está cerca de -14 LUFS y que no hay silencios largos.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cortar_silencios import duracion, silencios  # noqa: E402


def medidas(video: str) -> tuple[int, int]:
    salida = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                             "stream=width,height", "-of", "json", video], capture_output=True, text=True,
                            check=True).stdout
    s = json.loads(salida)["streams"][0]
    return s["width"], s["height"]


def volumen(video: str) -> float:
    proceso = subprocess.run(["ffmpeg", "-hide_banner", "-i", video, "-af", "ebur128", "-f", "null", "-"],
                             capture_output=True, text=True)
    valores = re.findall(r"I:\s+(-?[\d.]+) LUFS", proceso.stderr)
    return float(valores[-1]) if valores else float("nan")


def hoja(video: str, ruta: str, total: float, n: int = 12):
    """Doce fotogramas repartidos por el reel en una sola imagen (4 x 3)."""
    paso = max(total / n, 0.1)
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", video, "-vf",
                    f"fps=1/{paso:.3f},scale=270:480,tile=4x3:padding=6:color=black", "-frames:v", "1", ruta],
                   check=True)


def main():
    p = argparse.ArgumentParser(description="Revisa un reel antes de entregarlo.")
    p.add_argument("video")
    p.add_argument("--hoja", help="ruta de la hoja de fotogramas (por defecto, junto al vídeo)")
    a = p.parse_args()
    total = duracion(a.video)
    ancho, alto = medidas(a.video)
    lufs = volumen(a.video)
    mudos = [(x, y) for x, y in silencios(a.video, -40, 0.7) if y - x >= 0.7]
    ruta_hoja = a.hoja or os.path.splitext(a.video)[0] + "_hoja.jpg"
    hoja(a.video, ruta_hoja, total)

    fallos = []
    if (ancho, alto) != (1080, 1920):
        fallos.append(f"mide {ancho}x{alto}, no 1080x1920")
    if not -15.5 <= lufs <= -12.5:
        fallos.append(f"volumen en {lufs:.1f} LUFS (objetivo -14)")
    if mudos:
        fallos.append("silencios de más de 0,7 s en " + ", ".join(f"{x:.1f} s" for x, _ in mudos[:5]))
    print(f"Duración: {total:.1f} s · {ancho}x{alto} · {lufs:.1f} LUFS")
    print(f"Hoja de fotogramas: {ruta_hoja}")
    print("Sin fallos." if not fallos else "Revisar:\n  - " + "\n  - ".join(fallos))
    sys.exit(1 if fallos else 0)


if __name__ == "__main__":
    main()
