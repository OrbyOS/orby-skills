# Revisión de `landing-antes.html`

Una landing hecha «a lo IA» para un taller de cerámica inventado, revisada con el modo 2 de la skill. El rediseño
está en `landing-despues.html`.

## Medidas (`medir.py`)

- 10 tamaños de letra (12 a 110 px), 7 pesos (del 300 al 900), 2 familias, 16 colores.
- 4 degradados, 2 sombras de color, radios de 24 y 999 px.
- 17 espaciados fuera de la escala de 4 px.
- Contraste de 4,06:1 en el pie (`#6b7280` sobre `#0b0b12`). Además, el subtítulo de 15 px en `#9ca3af` y peso 300
  sobre un fondo con degradado no se puede medir, y a la vista cuesta leerlo.

## Notas

| Tipografía | Color | Espacio | Jerarquía | Detalle | Olor a IA | Media |
| --- | --- | --- | --- | --- | --- | --- |
| 2 | 1 | 4 | 3 | 2 | 0 | 2,0 |

Olor a IA: tiene 9 señales de la lista. Degradado de azul a morado, titular en serif cursiva de 110 px con degradado,
botones con resplandor, insignia con brillos, tres tarjetas iguales con emojis, todo centrado, redondeo máximo,
textos vacíos («Revoluciona», «Desbloquea», «al siguiente nivel») y cifras inventadas («+10.000», «10x», «99 %»).

## Arreglos, en orden

1. **La acción principal.** Hay dos botones del mismo peso («Empezar ahora» y «Descubrir más») y ninguno dice qué
   pasa al pulsar. Uno solo: «Reservar una clase de prueba».
2. **El titular.** «Revoluciona tu creatividad» no dice qué vendes. Escribe lo que consigue el cliente: «Haz tu
   primera taza en el torno en una tarde». A 42 px (2,5 veces el cuerpo), en peso 600, sin cursiva ni degradado.
3. **Contraste y tamaño del texto.** El subtítulo, de 15 px y peso 300, pasa a 21 px en peso 400 y `#5c554d` sobre
   `#faf8f5` (unos 7:1).
4. **Fuera las cifras inventadas** y los logos o testimonios que no existan. Donde falte una prueba, `[PENDIENTE]`.
5. **Color.** De 16 colores a 7: cuatro neutros cálidos, casi negro, blanco y un acento terracota solo en los
   botones. Ningún degradado.
6. **Tipografía.** Una familia (la del sistema), dos pesos (400 y 600), escala de 1,25 sobre 17 px: 14 · 17 · 21 ·
   27 · 33 · 42 px.
7. **Las tres tarjetas** («Creatividad», «Rapidez», «Calidad») sirven para cualquier negocio. Sustitúyelas por los
   tres pasos reales de la clase: centrar, abrir y subir, esmaltar.
8. **Espacios** en la escala de 4 px y 96 px entre secciones; un radio de 8 px y ninguna sombra.

## Después (`landing-despues.html`)

6 tamaños, 2 pesos, 1 familia, 7 colores, 0 degradados y 0 sombras. `medir.py`: sin avisos.
