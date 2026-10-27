#!/usr/bin/env python3
"""Encuentra los vídeos que han funcionado mucho mejor de lo normal para su propia cuenta.

Uso:
    python3 destacados.py videos.csv
    python3 destacados.py videos.csv --minimo 3 --dias 60

El CSV necesita estas columnas (el orden da igual):
    cuenta, enlace, vistas, fecha (AAAA-MM-DD)
y, si quieres, tema o texto con lo que dice el gancho.

Compara cada vídeo con la mediana de su cuenta, no con las demás cuentas: un vídeo de 20.000 vistas en una cuenta
que suele tener 2.000 dice más que uno de 200.000 en una que suele tener 300.000. Solo necesita Python.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import statistics
import sys
from collections import defaultdict


def leer(ruta: str) -> list[dict]:
    with open(ruta, encoding="utf-8-sig", newline="") as f:
        filas = list(csv.DictReader(f))
    faltan = {"cuenta", "enlace", "vistas", "fecha"} - set(filas[0] if filas else {})
    if faltan:
        sys.exit(f"Al CSV le faltan columnas: {', '.join(sorted(faltan))}")
    for fila in filas:
        fila["vistas"] = int(str(fila["vistas"]).replace(".", "").replace(",", "").strip() or 0)
        fila["fecha"] = dt.date.fromisoformat(fila["fecha"].strip()[:10])
    return filas


def destacados(filas: list[dict], minimo: float, dias: int, hoy: dt.date) -> tuple[list[dict], dict]:
    por_cuenta = defaultdict(list)
    for fila in filas:
        por_cuenta[fila["cuenta"]].append(fila)
    medianas, salida = {}, []
    for cuenta, videos in por_cuenta.items():
        if len(videos) < 5:
            medianas[cuenta] = None  # con menos de cinco vídeos la mediana no dice nada
            continue
        mediana = statistics.median(v["vistas"] for v in videos) or 1
        medianas[cuenta] = mediana
        for v in videos:
            v["veces"] = v["vistas"] / mediana
            v["dias"] = (hoy - v["fecha"]).days
            if v["veces"] >= minimo and v["dias"] <= dias:
                salida.append(v)
    return sorted(salida, key=lambda v: v["veces"], reverse=True), medianas


def main():
    p = argparse.ArgumentParser(description="Vídeos que destacan sobre la media de su cuenta.")
    p.add_argument("csv")
    p.add_argument("--minimo", type=float, default=3, help="cuántas veces por encima de lo normal (por defecto, 3)")
    p.add_argument("--dias", type=int, default=90, help="solo vídeos de los últimos N días (por defecto, 90)")
    p.add_argument("--hoy", help="fecha de hoy (AAAA-MM-DD), para pruebas")
    a = p.parse_args()
    hoy = dt.date.fromisoformat(a.hoy) if a.hoy else dt.date.today()
    lista, medianas = destacados(leer(a.csv), a.minimo, a.dias, hoy)
    sin_datos = [c for c, m in medianas.items() if m is None]
    if sin_datos:
        print("Con menos de 5 vídeos, sin comparar: " + ", ".join(sin_datos))
    if not lista:
        print(f"Ningún vídeo pasa de {a.minimo:g} veces lo normal en los últimos {a.dias} días. "
              "Prueba con --minimo 2 o con más vídeos por cuenta.")
        return
    print(f"{'Veces':>6}  {'Vistas':>9}  {'Normal':>8}  {'Días':>4}  Cuenta · enlace · tema")
    for v in lista:
        tema = v.get("tema") or v.get("texto") or ""
        print(f"{v['veces']:6.1f}  {v['vistas']:9d}  {medianas[v['cuenta']]:8.0f}  {v['dias']:4d}  "
              f"{v['cuenta']} · {v['enlace']}" + (f" · {tema}" if tema else ""))


if __name__ == "__main__":
    main()
