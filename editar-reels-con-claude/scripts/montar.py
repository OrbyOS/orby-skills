#!/usr/bin/env python3
"""Monta el reel final: quita las frases que sobran, reencuadra a 9:16 (1080x1920), quema los subtítulos palabra a
palabra y deja el audio a -14 LUFS.

Los subtítulos se queman con libass si tu ffmpeg la trae (ffmpeg-full) y, si no, se dibujan como imágenes con
Pillow y se superponen con el ffmpeg normal. El resultado es el mismo; la segunda vía tarda algo más.

Uso:
    python3 montar.py limpio.mp4 trabajo/transcripcion.json reel.mp4 --quitar 3,7-8
    python3 montar.py limpio.mp4 trabajo/transcripcion.json reel.mp4 --encuadre 0.4 --estilo simple
    python3 montar.py limpio.mp4 trabajo/transcripcion.json reel.mp4 --sin-subtitulos
    python3 montar.py limpio.mp4 trabajo/transcripcion.json reel_2.mp4 --solo 12-20 --quitar 15

--quitar recibe los números de frase de transcripcion.txt (tomas falsas, repeticiones, frases a medias).
El orden de lo que se dice no se toca nunca: solo se quitan trozos.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comprobar import ffmpeg_con_subtitulos  # noqa: E402
from cortar_silencios import duracion  # noqa: E402

ANCHO, ALTO = 1080, 1920
ANTES, DESPUES = 0.04, 0.06  # margen al cortar una frase para no comerse el final de la anterior ni el principio
                             # de la siguiente


def numeros(texto: str) -> set[int]:
    salida = set()
    for parte in filter(None, (x.strip() for x in texto.split(","))):
        a, _, b = parte.partition("-")
        salida.update(range(int(a), int(b or a) + 1))
    return salida


def tramos_quitados(frases: list[dict], quitar: set[int], total: float) -> list[tuple[float, float]]:
    """De cada frase quitada se va desde su principio hasta el principio de la siguiente que se queda."""
    tramos = []
    for i, fr in enumerate(frases):
        if fr["n"] not in quitar:
            continue
        previa = frases[i - 1]["t1"] if i > 0 else 0.0
        a = max(previa + 0.02, fr["t0"] - ANTES) if i > 0 else 0.0
        b = frases[i + 1]["t0"] - DESPUES if i + 1 < len(frases) else total
        if tramos and a <= tramos[-1][1] + 0.01:
            tramos[-1] = (tramos[-1][0], max(tramos[-1][1], b))
        else:
            tramos.append((a, b))
    return [(a, b) for a, b in tramos if b > a]


def tramos_que_quedan(total: float, quitados: list[tuple[float, float]]) -> list[tuple[float, float]]:
    salida, cursor = [], 0.0
    for a, b in quitados:
        if a - cursor > 0.05:
            salida.append((cursor, a))
        cursor = b
    if total - cursor > 0.05:
        salida.append((cursor, total))
    return salida


def palabras_finales(datos: dict, quitar: set[int], quedan: list[tuple[float, float]]) -> list[dict]:
    """Las palabras que se quedan, con su tiempo ya en el vídeo montado."""
    fuera = set()
    for fr in datos["frases"]:
        if fr["n"] in quitar:
            fuera.update(range(fr["palabras"][0], fr["palabras"][1] + 1))
    salida = []
    for i, p in enumerate(datos["palabras"]):
        if i in fuera:
            continue
        desplazado = 0.0
        for a, b in quedan:
            if a - 0.1 <= p["t0"] <= b + 0.1:
                salida.append({"t0": max(0.0, p["t0"] - a + desplazado),
                               "t1": max(0.0, min(p["t1"], b) - a + desplazado), "texto": p["texto"]})
                break
            desplazado += b - a
    return salida




def limpiar(texto: str, mayusculas: bool) -> str:
    texto = texto.replace("{", "").replace("}", "").replace("\\", "")
    return texto.upper() if mayusculas else texto


def eventos(palabras: list[dict], estilo: str, por_linea: int, mayusculas: bool) -> list[tuple]:
    """Grupos cortos de palabras, uno detrás de otro y sin solaparse: (inicio, fin, palabras, cuál suena).
    En estilo «simple», «cuál suena» es None."""
    grupos, actual = [], []
    for i, p in enumerate(palabras):
        if actual and (len(actual) >= por_linea or p["t0"] - palabras[actual[-1]]["t1"] > 0.6
                       or palabras[actual[-1]]["texto"][-1] in ".?!…"):
            grupos.append(actual)
            actual = []
        actual.append(i)
    if actual:
        grupos.append(actual)
    salida = []
    for g, grupo in enumerate(grupos):
        siguiente = palabras[grupos[g + 1][0]]["t0"] if g + 1 < len(grupos) else palabras[grupo[-1]]["t1"] + 0.5
        fin_grupo = min(palabras[grupo[-1]]["t1"] + 0.35, siguiente)
        textos = [limpiar(palabras[i]["texto"], mayusculas) for i in grupo]
        inicio = max(palabras[grupo[0]]["t0"], salida[-1][1] if salida else 0.0)
        if estilo == "simple":
            salida.append((inicio, max(fin_grupo, inicio + 0.05), textos, None))
            continue
        for k, i in enumerate(grupo):
            ini = inicio if k == 0 else palabras[i]["t0"]
            fin = palabras[grupo[k + 1]]["t0"] if k + 1 < len(grupo) else fin_grupo
            salida.append((ini, max(fin, ini + 0.05), textos, k))
    return salida


# --- Vía 1: libass (ffmpeg-full). Rápida y con el texto vectorial. ---

def color_ass(hex_rgb: str) -> str:
    h = hex_rgb.lstrip("#")
    return f"&H00{h[4:6]}{h[2:4]}{h[0:2]}".upper()


def escribir_ass(lista: list[tuple], ruta: str, fuente: str, tamano: int, resaltado: str, altura: int):
    def t(s: float) -> str:
        cs = int(round(s * 100))
        return f"{cs // 360000}:{cs // 6000 % 60:02d}:{cs // 100 % 60:02d}.{cs % 100:02d}"

    cabecera = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {ANCHO}
PlayResY: {ALTO}
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Reel,{fuente},{tamano},&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,5,2,2,90,90,{ALTO - altura},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(cabecera)
        for ini, fin, textos, activo in lista:
            linea = " ".join(f"{{\\c{color_ass(resaltado)}}}{w}{{\\c&H00FFFFFF}}" if j == activo else w
                             for j, w in enumerate(textos))
            f.write(f"Dialogue: 0,{t(ini)},{t(fin)},Reel,,0,0,0,,{linea}\n")


def escapar_ruta(ruta: str) -> str:
    """Las rutas dentro de un filtro de ffmpeg necesitan escapar : , ' y \\."""
    return ruta.replace("\\", "/").replace(":", "\\:").replace("'", "\\'").replace(",", "\\,")


# --- Vía 2: imágenes con Pillow. Funciona con el ffmpeg normal; algo más lenta. ---

FUENTES = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",       # Mac
    "/Library/Fonts/Arial Bold.ttf",
    "C:/Windows/Fonts/arialbd.ttf",                             # Windows
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",     # Linux
]


def archivo_fuente(nombre: str | None) -> str:
    for ruta in ([nombre] if nombre else []) + FUENTES:
        if ruta and os.path.exists(ruta):
            return ruta
    sys.exit("No encuentro una fuente en negrita. Pasa una con --fuente-archivo /ruta/a/la/fuente.ttf")


def imagenes(lista: list[tuple], carpeta: str, fuente: str, tamano: int, resaltado: str, altura: int) -> str:
    """Una imagen transparente por evento y una lista ffconcat con su duración. Devuelve la ruta de la lista."""
    try:
        from PIL import Image, ImageDraw, ImageFilter, ImageFont
    except ImportError:
        sys.exit("Falta Pillow para dibujar los subtítulos. Ejecuta comprobar.py: te dice cómo instalarlo.")
    letra = ImageFont.truetype(fuente, tamano)
    borde = max(3, tamano // 16)
    color = tuple(int(resaltado.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))
    espacio = letra.getlength(" ")

    def lineas(textos: list[str]) -> list[list[int]]:
        salida, actual, ancho = [], [], 0.0
        for j, w in enumerate(textos):
            w_ancho = letra.getlength(w)
            if actual and ancho + espacio + w_ancho > ANCHO - 180:
                salida.append(actual)
                actual, ancho = [], 0.0
            ancho += (espacio if actual else 0) + w_ancho
            actual.append(j)
        return salida + [actual]

    vacia = os.path.join(carpeta, "vacia.png")
    Image.new("RGBA", (ANCHO, ALTO), (0, 0, 0, 0)).save(vacia)
    entradas, cursor = [], 0.0
    for n, (ini, fin, textos, activo) in enumerate(lista):
        if ini - cursor > 0.001:
            entradas.append((vacia, ini - cursor))
        texto_capa = Image.new("RGBA", (ANCHO, ALTO), (0, 0, 0, 0))
        sombra = Image.new("RGBA", (ANCHO, ALTO), (0, 0, 0, 0))
        dibujo, dibujo_sombra = ImageDraw.Draw(texto_capa), ImageDraw.Draw(sombra)
        filas = lineas(textos)
        alto_linea = int(tamano * 1.12)
        y = altura - alto_linea * len(filas)
        for fila in filas:
            ancho = sum(letra.getlength(textos[j]) for j in fila) + espacio * (len(fila) - 1)
            x = (ANCHO - ancho) / 2
            for j in fila:
                relleno = color if j == activo else (255, 255, 255)
                dibujo_sombra.text((x + 3, y + 5), textos[j], font=letra, fill=(0, 0, 0, 150),
                                   stroke_width=borde, stroke_fill=(0, 0, 0, 150))
                dibujo.text((x, y), textos[j], font=letra, fill=relleno, stroke_width=borde,
                            stroke_fill=(0, 0, 0))
                x += letra.getlength(textos[j]) + espacio
            y += alto_linea
        capa = Image.alpha_composite(sombra.filter(ImageFilter.GaussianBlur(4)), texto_capa)
        ruta = os.path.join(carpeta, f"s{n:04d}.png")
        capa.save(ruta)
        entradas.append((ruta, fin - ini))
        cursor = fin
    entradas.append((vacia, 1.0))
    lista_ruta = os.path.join(carpeta, "subtitulos.ffconcat")
    with open(lista_ruta, "w", encoding="utf-8") as f:
        f.write("ffconcat version 1.0\n")
        for ruta, d in entradas:
            f.write(f"file '{ruta}'\nduration {d:.3f}\n")
        f.write(f"file '{vacia}'\n")
    return lista_ruta


def montar(video: str, salida: str, quedan: list[tuple[float, float]], encuadre: float, ffmpeg: str,
           ass: str | None = None, capas: str | None = None):
    partes, entradas = [], []
    for i, (a, b) in enumerate(quedan):
        d = b - a
        fundido = min(0.012, d / 4)
        partes.append(f"[0:v]trim=start={a:.3f}:end={b:.3f},setpts=PTS-STARTPTS[v{i}];"
                      f"[0:a]atrim=start={a:.3f}:end={b:.3f},asetpts=PTS-STARTPTS,"
                      f"afade=t=in:d={fundido:.3f},afade=t=out:st={d - fundido:.3f}:d={fundido:.3f}[a{i}];")
        entradas.append(f"[v{i}][a{i}]")
    vertical = (f"crop=w='trunc(min(iw\\,ih*9/16)/2)*2':h='trunc(min(ih\\,iw*16/9)/2)*2'"
                f":x='(iw-ow)*{encuadre:.3f}':y='(ih-oh)/2',scale={ANCHO}:{ALTO}:flags=lanczos,setsar=1,fps=30")
    if ass:
        vertical += f",subtitles=filename='{escapar_ruta(ass)}'"
    filtro = "".join(partes) + "".join(entradas) + f"concat=n={len(quedan)}:v=1:a=1[vc][ac];[vc]{vertical}"
    if capas:
        filtro += "[vb];[1:v]fps=30,format=rgba[sub];[vb][sub]overlay=0:0:eof_action=pass"
    filtro += ",format=yuv420p[v];[ac]loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[a]"
    extra = ["-f", "concat", "-safe", "0", "-i", capas] if capas else []
    subprocess.run([ffmpeg, "-hide_banner", "-loglevel", "error", "-y", "-i", video, *extra,
                    "-filter_complex", filtro, "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "18",
                    "-preset", "medium", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", salida],
                   check=True)


def main():
    p = argparse.ArgumentParser(description="Monta el reel final en 9:16 con subtítulos.")
    p.add_argument("video", help="el vídeo ya sin silencios (el mismo que se transcribió)")
    p.add_argument("transcripcion", help="transcripcion.json de transcribir.py")
    p.add_argument("salida")
    p.add_argument("--quitar", default="", help="frases que sobran, por ejemplo 3,7-8")
    p.add_argument("--solo", default="", help="frases que forman este reel (el resto fuera), por ejemplo 12-20; "
                                              "para sacar varios reels de una grabación")
    p.add_argument("--encuadre", type=float, default=0.5,
                   help="si el vídeo es horizontal, dónde poner el recorte: 0 izquierda, 0.5 centro, 1 derecha")
    p.add_argument("--sin-subtitulos", action="store_true")
    p.add_argument("--via", choices=["auto", "libass", "imagenes"], default="auto",
                   help="cómo se queman los subtítulos: libass (ffmpeg-full) o imágenes (ffmpeg normal + Pillow)")
    p.add_argument("--estilo", choices=["resaltado", "simple"], default="resaltado")
    p.add_argument("--palabras", type=int, default=3, help="palabras como máximo en pantalla a la vez")
    p.add_argument("--fuente", default="Arial", help="nombre de la fuente (vía libass)")
    p.add_argument("--fuente-archivo", help="archivo .ttf u .otf de la fuente (vía imágenes)")
    p.add_argument("--tamano", type=int, default=82)
    p.add_argument("--color", default="#FFD43B", help="color de la palabra que suena (estilo resaltado)")
    p.add_argument("--minusculas", action="store_true", help="no pasar los subtítulos a mayúsculas")
    p.add_argument("--altura", type=int, default=1380,
                   help="píxel (de 1920) donde va la base del subtítulo; por debajo de 1440 lo tapa la interfaz")
    a = p.parse_args()

    with open(a.transcripcion, encoding="utf-8") as f:
        datos = json.load(f)
    todas = {fr["n"] for fr in datos["frases"]}
    quitar = numeros(a.quitar) | (todas - numeros(a.solo) if a.solo else set())
    desconocidas = (numeros(a.quitar) | numeros(a.solo)) - todas
    if desconocidas:
        sys.exit(f"Esas frases no existen: {sorted(desconocidas)}")
    total = duracion(a.video)
    quedan = tramos_que_quedan(total, tramos_quitados(datos["frases"], quitar, total))
    if not quedan:
        sys.exit("Si quito esas frases no queda nada.")

    with tempfile.TemporaryDirectory() as tmp:
        if a.sin_subtitulos:
            montar(a.video, a.salida, quedan, a.encuadre, "ffmpeg")
        else:
            lista = eventos(palabras_finales(datos, quitar, quedan), a.estilo, a.palabras, not a.minusculas)
            con_libass = ffmpeg_con_subtitulos() if a.via != "imagenes" else None
            if a.via == "libass" and not con_libass:
                sys.exit("Tu ffmpeg no puede quemar subtítulos (le falta libass).\n"
                         "En Mac:  brew install ffmpeg-full   (se instala aparte; este script lo encuentra solo)\n"
                         "O usa --via imagenes, que funciona con el ffmpeg normal.")
            if con_libass:
                ass = os.path.splitext(a.salida)[0] + ".ass"
                escribir_ass(lista, ass, a.fuente, a.tamano, a.color, a.altura)
                montar(a.video, a.salida, quedan, a.encuadre, con_libass, ass=ass)
            else:
                if a.via == "auto":
                    print("Sin libass en tu ffmpeg: dibujo los subtítulos como imágenes (más lento, mismo resultado).")
                capas = imagenes(lista, tmp, archivo_fuente(a.fuente_archivo), a.tamano, a.color, a.altura)
                montar(a.video, a.salida, quedan, a.encuadre, "ffmpeg", capas=capas)
    final = sum(b - a for a, b in quedan)
    print(f"Listo: {total:.1f} s → {final:.1f} s, {len(quitar)} frases fuera. Guardado en {a.salida}")


if __name__ == "__main__":
    main()
