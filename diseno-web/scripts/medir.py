#!/usr/bin/env python3
"""Mide un diseño web (HTML o CSS) contra las reglas de la skill diseno-web.

Uso:
    python3 medir.py pagina.html
    python3 medir.py estilos.css otra.html --json

Lee el CSS de las etiquetas <style>, de los atributos style="" y de los archivos .css que le pases. No necesita
nada instalado más que Python. Cuenta lo que se puede contar: tamaños de letra, pesos, familias, colores, valores de
espaciado fuera de la escala de 4 px, degradados, sombras, radios y el contraste de cada texto con su fondo (el de
su regla o, si no tiene, el de la página). Los fondos con degradado o imagen no se miden. Lo que no se puede medir
(jerarquía, ritmo, si suena a IA) lo revisa Claude.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter

LIMITES = {"tamanos": 6, "pesos": 3, "familias": 2, "colores": 7, "radios": 2, "sombras": 2}
ESCALA = 4  # px: los espaciados deberían ser múltiplos de 4

NOMBRES = {"white": "#ffffff", "black": "#000000", "transparent": None, "currentcolor": None, "inherit": None,
           "initial": None, "none": None}


def css_de(ruta: str) -> str:
    texto = open(ruta, encoding="utf-8", errors="ignore").read()
    if ruta.lower().endswith(".css"):
        return texto
    bloques = re.findall(r"<style[^>]*>(.*?)</style>", texto, re.S | re.I)
    en_linea = re.findall(r'style\s*=\s*"([^"]*)"', texto, re.I) + re.findall(r"style\s*=\s*'([^']*)'", texto, re.I)
    return "\n".join(bloques) + "\n" + "\n".join(f"x{{{d}}}" for d in en_linea)


def reglas(css: str) -> list[dict]:
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    salida = []
    for selector, cuerpo in re.findall(r"([^{}]+)\{([^{}]*)\}", css):
        decl = {}
        for parte in cuerpo.split(";"):
            if ":" in parte:
                k, v = parte.split(":", 1)
                decl[k.strip() if k.strip().startswith("--") else k.strip().lower()] = \
                    v.strip().replace("!important", "").strip()
        salida.append({"selector": selector.strip(), "decl": decl})
    # Las variables (--nombre) se sustituyen por su valor, para medir lo que de verdad se usa.
    variables = {k: v for r in salida for k, v in r["decl"].items() if k.startswith("--")}

    def resolver(valor: str, profundidad: int = 0) -> str:
        if "var(" not in valor or profundidad > 5:
            return valor
        def uno(m):
            nombre, _, defecto = m.group(1).partition(",")
            return variables.get(nombre.strip(), defecto.strip())
        return resolver(re.sub(r"var\(\s*([^()]*?)\s*\)", uno, valor), profundidad + 1)

    for r in salida:
        r["decl"] = {k: resolver(v) for k, v in r["decl"].items() if not k.startswith("--")}
    return salida


def a_px(valor: str) -> float | None:
    m = re.match(r"^(-?[\d.]+)(px|rem|em)?$", valor.strip())
    if not m:
        return None
    n = float(m.group(1))
    return n * 16 if m.group(2) in ("rem", "em") else n


def hex_rgb(color: str) -> tuple[float, float, float] | None:
    c = NOMBRES.get(color.strip().lower(), color.strip()) if color else None
    if not c:
        return None
    m = re.match(r"^#([0-9a-f]{3}|[0-9a-f]{6})$", c, re.I)
    if m:
        h = m.group(1)
        h = "".join(ch * 2 for ch in h) if len(h) == 3 else h
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
    m = re.match(r"^rgba?\(\s*(\d+)[ ,]+(\d+)[ ,]+(\d+)", c, re.I)
    if m:
        return tuple(float(x) for x in m.groups())
    return None


def luminancia(rgb) -> float:
    def canal(c):
        c = c / 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (canal(x) for x in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contraste(a, b) -> float:
    la, lb = sorted((luminancia(a), luminancia(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


COLOR = re.compile(r"#[0-9a-fA-F]{3,6}\b|rgba?\([^)]*\)")


def medir(css: str) -> dict:
    rs = reglas(css)
    tamanos, pesos, familias, colores, radios, sombras = Counter(), Counter(), Counter(), Counter(), Counter(), Counter()
    fuera_escala, degradados, contrastes = Counter(), 0, []
    pagina = None  # el fondo de la página: contra él se mide el texto que no declara fondo propio
    for r in rs:
        if re.search(r"(^|[\s,])(body|html)\b", r["selector"]):
            f = r["decl"].get("background-color") or r["decl"].get("background", "")
            if f and "(" not in f.split()[0] and hex_rgb(f.split()[0]):
                pagina = f.split()[0]
    for r in rs:
        d = r["decl"]
        if "font-size" in d and (px := a_px(d["font-size"])):
            tamanos[round(px, 1)] += 1
        if "font-weight" in d:
            peso = {"normal": "400", "bold": "700"}.get(d["font-weight"], d["font-weight"])
            pesos[peso] += 1
        if "font-family" in d:
            familias[d["font-family"].split(",")[0].strip().strip("'\"").lower()] += 1
        for k, v in d.items():
            if k in ("color", "background", "background-color", "border-color", "fill", "stroke") or k.startswith("border"):
                for c in COLOR.findall(v):
                    rgb = hex_rgb(c)
                    if rgb:
                        colores["#%02x%02x%02x" % tuple(int(x) for x in rgb)] += 1
            if "gradient(" in v:
                degradados += 1
            if re.match(r"^(margin|padding|gap|row-gap|column-gap)(-|$)", k):
                for parte in v.split():
                    px = a_px(parte)
                    if px is not None and px not in (0, 1) and px % ESCALA:
                        fuera_escala[f"{k}: {parte}"] += 1
        if "border-radius" in d:
            radios[d["border-radius"]] += 1
        if d.get("box-shadow", "none") != "none" and "box-shadow" in d:
            sombras[d["box-shadow"]] += 1
        fondo = d.get("background-color") or (d.get("background") if not d.get("background", "").count("(") else None)
        fondo = (fondo.split()[0] if fondo else None) or pagina
        if "color" in d and fondo:
            a, b = hex_rgb(d["color"]), hex_rgb(fondo)
            if a and b:
                contrastes.append({"selector": r["selector"][:60], "texto": d["color"], "fondo": fondo,
                                   "ratio": round(contraste(a, b), 2)})
    avisos = []
    for clave, contador in (("tamanos", tamanos), ("pesos", pesos), ("familias", familias), ("colores", colores),
                            ("radios", radios), ("sombras", sombras)):
        if len(contador) > LIMITES[clave]:
            avisos.append(f"{clave}: {len(contador)} distintos (máximo recomendado {LIMITES[clave]})")
    if degradados:
        avisos.append(f"degradados: {degradados} (por defecto, ninguno)")
    if fuera_escala:
        avisos.append(f"espaciados fuera de la escala de {ESCALA} px: {sum(fuera_escala.values())}")
    bajos = [c for c in contrastes if c["ratio"] < 4.5]
    if bajos:
        avisos.append(f"contraste por debajo de 4,5:1 en {len(bajos)} regla(s)")
    cuerpo = [px for px in tamanos if 14 <= px <= 20]
    if tamanos and not any(16 <= px <= 20 for px in tamanos):
        avisos.append("ningún tamaño de texto entre 16 y 20 px: el cuerpo de texto probablemente es pequeño")
    if tamanos and max(tamanos) > 96:
        avisos.append(f"titular de {max(tamanos):g} px: más de 96 px suele ser un efecto, no jerarquía")
    return {"tamanos": sorted(tamanos), "pesos": sorted(pesos), "familias": sorted(familias),
            "colores": sorted(colores), "radios": sorted(radios), "sombras": len(sombras), "degradados": degradados,
            "fuera_de_escala": dict(fuera_escala.most_common(8)), "contrastes_bajos": bajos, "avisos": avisos,
            "_cuerpo": cuerpo}


def main():
    p = argparse.ArgumentParser(description="Mide un diseño web contra las reglas de diseno-web.")
    p.add_argument("archivos", nargs="+")
    p.add_argument("--json", action="store_true")
    a = p.parse_args()
    datos = medir("\n".join(css_de(r) for r in a.archivos))
    datos.pop("_cuerpo")
    if a.json:
        print(json.dumps(datos, ensure_ascii=False, indent=1))
        return
    print(f"Tamaños de letra ({len(datos['tamanos'])}): {', '.join(f'{x:g}' for x in datos['tamanos'])} px")
    print(f"Pesos ({len(datos['pesos'])}): {', '.join(datos['pesos'])}")
    print(f"Familias ({len(datos['familias'])}): {', '.join(datos['familias'])}")
    print(f"Colores ({len(datos['colores'])}): {', '.join(datos['colores'])}")
    print(f"Radios ({len(datos['radios'])}): {', '.join(datos['radios'])} · sombras distintas: {datos['sombras']} · "
          f"degradados: {datos['degradados']}")
    for c in datos["contrastes_bajos"]:
        print(f"  contraste {c['ratio']}:1 en «{c['selector']}» ({c['texto']} sobre {c['fondo']})")
    for k, n in datos["fuera_de_escala"].items():
        print(f"  fuera de escala: {k} ({n})")
    print("\nSin avisos." if not datos["avisos"] else "\nAvisos:\n  - " + "\n  - ".join(datos["avisos"]))
    sys.exit(1 if datos["avisos"] else 0)


if __name__ == "__main__":
    main()
