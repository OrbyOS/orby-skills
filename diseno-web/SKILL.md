---
name: diseno-web
description: Diseña webs, landings y correos que no parecen hechos por una IA (sin degradados azules, botones brillantes ni el titular gigante en serif cursiva sobre fondo negro o crema), y revisa un diseño ya hecho con reglas medibles de tipografía, color, espacio, jerarquía y contraste, con la lista de arreglos en orden. Úsala cuando alguien pida diseñar o maquetar una web, una landing, una página de venta, un correo o un componente, quiera que su diseño «no parezca de plantilla» o «no huela a IA», o pida revisar o mejorar un diseño, aunque no diga «skill».
---

# Diseño web sin olor a IA

Lo que diseña una IA sin criterio se reconoce de lejos: degradado de azul a morado, botones que brillan, tres
tarjetas iguales, todo centrado y un titular enorme en cursiva. No es que esté mal hecho: es que cualquiera lo
habría hecho igual. Esta skill diseña con decisiones (pocas fuentes, pocos colores, una escala, mucho aire y una
cosa principal por pantalla) y revisa con números, no con impresiones.

Archivos de esta carpeta:
- `reglas.md`: las reglas medibles, con su porqué y un antes y un después. **Léelo antes de diseñar o revisar.**
- `olor-a-ia.md`: las señales que delatan un diseño hecho con prisa por una IA.
- `scripts/medir.py`: cuenta en un HTML o CSS lo que se puede contar (tamaños, pesos, familias, colores, espacios
  fuera de escala, degradados, sombras, radios y contraste).
- `ejemplos/`: una landing hecha «a lo IA» (`landing-antes.html`), su revisión completa, la misma landing rediseñada
  con estas reglas (`landing-despues.html`) y un correo (`correo.html`). Ábrelos para ver el nivel que se espera.

## Modo 1. Diseñar

### 1. Lo justo para empezar
Pregunta solo lo que falte:
1. **Qué es y para qué:** una landing para vender X, un correo de bienvenida, la portada de una web…
2. **La acción principal:** qué tiene que hacer quien lo ve (reservar, comprar, apuntarse, escribir).
3. **El contenido real:** los textos, o al menos qué vende, a quién, qué lo diferencia y las pruebas que tiene. Si
   no hay textos, escríbelos con frases concretas; lo que no sepas, márcalo como `[PENDIENTE: …]`. Nunca inventes
   cifras, clientes ni testimonios.
4. **La marca, si la hay:** su color, su tipografía y su logo. Si no la hay, propón tú: un acento y una familia.

### 2. Decidir el sistema antes de maquetar
Escribe primero, en el propio CSS como variables, el sistema completo:
- **Una familia** (dos como mucho) y **dos pesos**.
- **Una escala de 5 a 6 tamaños** con una proporción fija; cuerpo de 16 a 20 px.
- **Neutros más un acento**, 7 colores como mucho, todos con contraste comprobado.
- **Una escala de espacios** de 4 px.
- **Uno o dos radios** y, como mucho, una sombra.

Todo lo demás usa solo esas variables. Si necesitas un valor nuevo, la escala está mal: cámbiala, no añadas una
excepción.

### 3. Componer
- Empieza por el contenido en orden de importancia, no por las secciones de una plantilla. Pregunta qué necesita
  saber quien llega, en qué orden, para hacer la acción principal.
- Una idea y una acción principal por pantalla. Un solo botón primario por vista.
- Texto a la izquierda, columnas de 60 a 75 caracteres, mucho aire entre secciones (de 64 a 128 px).
- Fotos reales si las hay. Si no, mejor sin imagen que con una ilustración genérica.

Para un correo, sigue además la parte de correos de `reglas.md`: una columna, fuentes del sistema, estilos en línea y
un solo botón.

### 4. Medir y revisar antes de entregar
```bash
python3 SKILL/scripts/medir.py ruta/al/archivo.html
```
(`SKILL` es la carpeta de esta skill.) Arregla todos los avisos o explica por qué uno es intencionado. Después repasa
`olor-a-ia.md` señal por señal. Si puedes abrir el diseño en un navegador, haz una captura en escritorio y otra a 375
px de ancho y míralas: lo que se ve manda sobre lo que dice el código.

### 5. Entregar
El archivo, el sistema en cinco líneas (familia, escala, colores, espacios y radio) y la lista de `[PENDIENTE]` si
la hay.

## Modo 2. Revisar un diseño ya hecho

Con el rigor de un diseñador de producto exigente, que no deja pasar un píxel sin motivo:

1. **Mide.** Si hay HTML o CSS, pasa `medir.py`. Si solo hay una captura, mírala y estima lo mismo a ojo (cuenta
   tamaños de letra, pesos y colores distintos que ves) y dilo: «estimado a partir de la captura».
2. **Puntúa** de 0 a 10 cada apartado:

| Apartado | Qué miras |
| --- | --- |
| Tipografía | Familias, pesos, escala, tamaño del cuerpo, interlineado, largo de línea |
| Color | Número de colores, uso del acento, degradados, contraste |
| Espacio | Escala de espacios, agrupación por cercanía, aire entre secciones |
| Jerarquía | Una cosa principal por pantalla, un botón primario, qué se ve primero |
| Detalle | Radios, sombras, botones, iconos, alineación |
| Olor a IA | Cuántas señales de `olor-a-ia.md` tiene (0 señales = 10; 5 o más = 2 o menos) |

3. **Señala cada fallo con su medida:** «7 tamaños de letra entre 13 y 22 px» y no «tipografía desordenada»;
   «contraste de 2,5:1 en el texto gris del pie» y no «poco contraste».
4. **Da el arreglo exacto:** el valor nuevo («usa 14 · 17 · 21 · 27 · 33 · 42»), no un consejo general.
5. **Ordena los arreglos** de más a menos impacto: primero lo que impide leer o actuar (contraste, jerarquía, botón
   principal), después lo que huele a plantilla, y al final el detalle.
6. Ofrece aplicar los arreglos. Si acepta, aplícalos, vuelve a medir y enseña el antes y el después.

## Cómo pedírselo a Claude

- «Diséñame una landing para [qué vendes] a [quién]. La acción es [reservar una llamada]. Estos son mis textos: …»
- «Diseña el correo de bienvenida de mi newsletter, una columna y un solo botón.»
- «Revisa este diseño como un diseñador exigente: nota por apartado y los arreglos en orden.» (con el archivo o una
  captura)
