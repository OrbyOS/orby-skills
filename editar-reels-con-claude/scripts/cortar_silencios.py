#!/usr/bin/env python3
"""Quita los silencios de un vídeo hablado a cámara y deja el audio a -14 LUFS (el volumen de Instagram y TikTok).

Uso:
    python3 cortar_silencios.py bruto.mp4 limpio.mp4
    python3 cortar_silencios.py bruto.mp4 limpio.mp4 --umbral -35 --minimo 0.4 --margen 0.08

Solo necesita ffmpeg. No sube nada a ningún sitio: todo pasa en tu ordenador.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys


def duracion(video: str) -> float:
    salida = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json", video],
                            capture_output=True, text=True, check=True).stdout
    return float(json.loads(salida)["format"]["duration"])


def silencios(video: str, umbral_db: float, minimo: float) -> list[tuple[float, float]]:
    """Los tramos en silencio, según ffmpeg (silencedetect)."""
    proceso = subprocess.run(["ffmpeg", "-hide_banner", "-i", video, "-af",
                              f"silencedetect=noise={umbral_db}dB:d={minimo}", "-f", "null", "-"],
                             capture_output=True, text=True)
    inicios = [float(x) for x in re.findall(r"silence_start: (-?[\d.]+)", proceso.stderr)]
    finales = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", proceso.stderr)]
    if len(finales) < len(inicios):  # el vídeo acaba en silencio
        finales.append(duracion(video))
    return [(max(0.0, a), b) for a, b in zip(inicios, finales)]


def tramos_con_voz(total: float, mudos: list[tuple[float, float]], margen: float) -> list[tuple[float, float]]:
    """Lo que queda al quitar los silencios, con un pequeño margen para no comerse el principio ni el final de las
    palabras."""
    tramos, cursor = [], 0.0
    for a, b in mudos:
        fin = min(total, a + margen)
        if fin - cursor > 0.05:
            tramos.append((cursor, fin))
        cursor = max(cursor, b - margen)
    if total - cursor > 0.05:
        tramos.append((cursor, total))
    return tramos


def montar(video: str, salida: str, tramos: list[tuple[float, float]]):
    partes, entradas = [], []
    for i, (a, b) in enumerate(tramos):
        fundido = min(0.012, (b - a) / 4)  # un fundido de milisegundos evita el «clic» en cada corte
        partes.append(f"[0:v]trim=start={a:.3f}:end={b:.3f},setpts=PTS-STARTPTS[v{i}];"
                      f"[0:a]atrim=start={a:.3f}:end={b:.3f},asetpts=PTS-STARTPTS,afade=t=in:d={fundido:.3f},"
                      f"afade=t=out:st={b - a - fundido:.3f}:d={fundido:.3f}[a{i}];")
        entradas.append(f"[v{i}][a{i}]")
    filtro = "".join(partes) + "".join(entradas) + f"concat=n={len(tramos)}:v=1:a=1[v][a0];" \
        "[a0]loudnorm=I=-14:TP=-1.5:LRA=11[a]"
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", video, "-filter_complex", filtro,
                    "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "18", "-preset", "medium",
                    "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", salida], check=True)


def main():
    p = argparse.ArgumentParser(description="Quita los silencios de un vídeo hablado.")
    p.add_argument("entrada")
    p.add_argument("salida")
    p.add_argument("--umbral", type=float, default=-35, help="dB por debajo de los cuales se considera silencio")
    p.add_argument("--minimo", type=float, default=0.4, help="segundos de silencio a partir de los que se corta")
    p.add_argument("--margen", type=float, default=0.08, help="segundos que se dejan antes y después de cada frase")
    a = p.parse_args()
    total = duracion(a.entrada)
    tramos = tramos_con_voz(total, silencios(a.entrada, a.umbral, a.minimo), a.margen)
    if not tramos:
        sys.exit("No he encontrado voz: prueba con un --umbral más bajo (por ejemplo, -45).")
    montar(a.entrada, a.salida, tramos)
    final = sum(b - a for a, b in tramos)
    print(f"Listo: {total:.1f} s → {final:.1f} s ({len(tramos)} tramos). Guardado en {a.salida}")


if __name__ == "__main__":
    main()
