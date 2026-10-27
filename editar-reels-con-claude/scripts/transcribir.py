#!/usr/bin/env python3
"""Transcribe un vídeo palabra a palabra con faster-whisper y lo parte en frases numeradas.

Uso:
    python3 transcribir.py limpio.mp4 trabajo/
    python3 transcribir.py limpio.mp4 trabajo/ --modelo medium --idioma es

Deja dos archivos en la carpeta de trabajo:
    transcripcion.json   las palabras con su tiempo y las frases (lo usa montar.py)
    transcripcion.txt    las frases numeradas, para leerlas y decidir qué tomas sobran

Todo pasa en tu ordenador. La primera vez descarga el modelo (small: unos 500 MB).
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys

PAUSA_FRASE = 0.45   # segundos de hueco que cierran una frase aunque no haya punto
MAX_PALABRAS = 22    # una frase más larga se parte en la siguiente pausa


def audio(video: str):
    """El audio en mono a 16 kHz, sacado con ffmpeg (más fiable que el lector interno de faster-whisper)."""
    import numpy as np
    crudo = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", video, "-vn", "-ac", "1",
                            "-ar", "16000", "-f", "f32le", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(crudo, dtype=np.float32)


def palabras(video: str, modelo: str, idioma: str | None) -> tuple[list[dict], str]:
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        sys.exit("Falta faster-whisper. Ejecuta comprobar.py: te dice cómo instalarlo.")
    whisper = WhisperModel(modelo, device="auto", compute_type="int8")
    segmentos, info = whisper.transcribe(audio(video), language=idioma, word_timestamps=True, vad_filter=True,
                                         condition_on_previous_text=False)
    salida = []
    for segmento in segmentos:
        for p in segmento.words or []:
            texto = p.word.strip()
            if texto:
                salida.append({"t0": round(p.start, 3), "t1": round(p.end, 3), "texto": texto})
    return salida, info.language


def frases(lista: list[dict]) -> list[dict]:
    """Agrupa las palabras en frases: corta en punto final o en una pausa clara."""
    grupos, actual = [], []
    for i, p in enumerate(lista):
        actual.append(i)
        siguiente = lista[i + 1] if i + 1 < len(lista) else None
        hueco = siguiente["t0"] - p["t1"] if siguiente else 99
        cierra = p["texto"][-1] in ".?!…" or hueco >= PAUSA_FRASE
        if cierra or (len(actual) >= MAX_PALABRAS and hueco > 0.15) or siguiente is None:
            grupos.append(actual)
            actual = []
    return [{"n": n, "t0": lista[g[0]]["t0"], "t1": lista[g[-1]]["t1"],
             "texto": " ".join(lista[i]["texto"] for i in g), "palabras": [g[0], g[-1]]}
            for n, g in enumerate(grupos, 1)]


def main():
    p = argparse.ArgumentParser(description="Transcribe un vídeo palabra a palabra.")
    p.add_argument("video")
    p.add_argument("carpeta", help="carpeta de trabajo donde dejar la transcripción")
    p.add_argument("--modelo", default="small", help="tiny, base, small, medium o large-v3 (más lento, más fino)")
    p.add_argument("--idioma", default=None, help="código del idioma (es, en, ca…); sin él, lo detecta")
    a = p.parse_args()
    os.makedirs(a.carpeta, exist_ok=True)
    lista, idioma = palabras(a.video, a.modelo, a.idioma)
    if not lista:
        sys.exit("No he oído ninguna palabra. ¿El vídeo tiene audio?")
    datos = {"video": os.path.abspath(a.video), "idioma": idioma, "palabras": lista, "frases": frases(lista)}
    with open(os.path.join(a.carpeta, "transcripcion.json"), "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=1)
    with open(os.path.join(a.carpeta, "transcripcion.txt"), "w", encoding="utf-8") as f:
        for fr in datos["frases"]:
            f.write(f"[{fr['n']}] {fr['t0']:6.2f}-{fr['t1']:6.2f}  {fr['texto']}\n")
    print(f"Listo: {len(lista)} palabras en {len(datos['frases'])} frases ({idioma}). "
          f"Lee {os.path.join(a.carpeta, 'transcripcion.txt')}")


if __name__ == "__main__":
    main()
