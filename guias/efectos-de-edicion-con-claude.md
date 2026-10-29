# 14 efectos de edición con Claude, con sus prompts

Claude puede montar efectos de edición que antes pedían horas de un programa de vídeo: texto detrás de la cabeza,
subtítulos palabra a palabra, transiciones, portadas o muros de vídeos. No los dibuja a mano: escribe el código que
los genera, así que puedes cambiar cualquier palabra, color o tiempo y volver a renderizar.

Aquí tienes la puesta a punto y los 14 efectos, cada uno con su prompt listo para copiar. Cambia lo que va entre
corchetes por tu estilo: tipografía, colores y tiempos.

---

## La puesta a punto

Todo funciona con **Claude Code** en tu ordenador y cinco herramientas gratuitas:

| Herramienta | Para qué |
| --- | --- |
| **Remotion** | Montar el vídeo con código: textos, animaciones y capas |
| **FFmpeg** | Cortar, unir, cambiar el color y exportar |
| **Whisper** (con marcas por palabra) | Saber en qué instante se dice cada palabra, para los subtítulos y los cortes |
| **Segmentación de personas** | Recortar a la persona del fondo: la de Apple Vision en Mac, o rembg en Windows y Linux |
| **yt-dlp** | Descargar vídeos tuyos o con permiso, para usarlos en el montaje |

No hace falta instalarlas a mano. Pídeselo a Claude Code:

```text
Prepara mi ordenador para editar vídeos con código. Comprueba si tengo Node.js, Python, FFmpeg y yt-dlp, e instala
lo que falte pidiéndome permiso antes de cada cosa. Crea un proyecto de Remotion en la carpeta [nombre], instala
faster-whisper para transcribir con marcas por palabra y prepara la segmentación de personas (la de Apple Vision si
estoy en Mac; rembg si no). Al terminar, dime qué tengo y prueba cada herramienta con un vídeo corto.
```

> [!TIP]
> Si solo quieres quitar silencios y tomas falsas, poner subtítulos y pasar el vídeo a vertical, no necesitas nada de
> esto: la skill [editar-reels-con-claude](../editar-reels-con-claude) lo hace sola con FFmpeg y Whisper (capítulo
> anterior). Los efectos de esta guía son el paso siguiente.

---

## 1. El guion gráfico, antes de nada

**Qué es:** una tabla con cada tramo del vídeo (tiempo, palabras exactas, qué sale en pantalla y con qué se hace)
que apruebas antes de que se renderice nada. Ahorra horas de rehacer.

```text
Transcribe [vídeo] con marcas por palabra y prepárame un guion gráfico en una tabla: tiempo de inicio y fin, las
palabras exactas de ese tramo, qué efecto o imagen sale en pantalla y con qué herramienta se hace. No renderices
nada hasta que lo apruebe.
```

## 2. Texto detrás de la cabeza

**Qué es:** el título queda entre el fondo y la persona, como si estuviera detrás de ella. Muy usado en los
primeros segundos.

```text
Recorta a la persona de [vídeo] en cada fotograma con la segmentación de personas. Coloca el título «[título]» en
dos líneas entre el fondo y el recorte, con [tipografía] en [color]. Que entre en 12 fotogramas con una curva suave
de salida, subiendo un poco; la segunda línea, 4 fotogramas después de la primera.
```

## 3. Subtítulos palabra a palabra

**Qué es:** bloques cortos que entran justo cuando se dicen, con la palabra que suena resaltada.

```text
Con las marcas por palabra de Whisper, añade subtítulos de hasta 3 palabras por bloque. Cada bloque entra en el
instante de su primera palabra. Resalta solo la palabra que suena con [color], sin poner caja al resto. Tipografía
[tipografía], tamaño [tamaño], centrados en [posición] y fuera de la zona que tapan los botones de la aplicación.
```

> [!TIP]
> Resaltar solo la palabra que suena se lee mejor que poner una caja detrás de todo el subtítulo.

## 4. Rótulo de una herramienta

**Qué es:** cuando nombras una herramienta, su nombre aparece en pantalla deslizándose.

```text
Cada vez que diga el nombre de una herramienta, muestra un rótulo con ese nombre que entre deslizándose desde la
izquierda en el instante en que lo digo y salga 1,5 segundos después. Tipografía [tipografía], fondo [color],
encima de mi cabeza y sin tapar la cara.
```

## 5. Tarjeta de repositorio

**Qué es:** al nombrar una herramienta de código abierto, una tarjeta con su nombre, su descripción y su número de
estrellas, al estilo de GitHub.

```text
Cuando diga «[nombre de la herramienta]», muestra arriba una tarjeta al estilo de GitHub en modo oscuro, con el
85 % del ancho: nombre del repositorio, descripción y estrellas reales, sacadas de su página. Que entre en 10
fotogramas y se quede mientras hablo de ella.
```

## 6. Barra de prompt

**Qué es:** una barra como la de un chat, con el texto escribiéndose letra a letra y el botón de enviar. Sirve para
enseñar qué le pides a la IA.

```text
Crea un componente reutilizable de barra de prompt, como la caja de un chat: el texto «[prompt]» se escribe letra a
letra al ritmo de mi voz y, al terminar, el botón de enviar se pulsa. Colores [colores], esquinas redondeadas y
centrada en la mitad inferior.
```

## 7. Cambio de color con cortinilla

**Qué es:** una línea vertical barre la imagen y, a su paso, el vídeo cambia a otra versión de color. Para marcar un
antes y un después.

```text
Haz con FFmpeg una versión de [vídeo] con [cambio de color, por ejemplo: tonos más cálidos]. En el segundo [x],
haz que una línea vertical fina barra la imagen de izquierda a derecha en 30 fotogramas y que, a su paso, se vea la
versión nueva.
```

## 8. Portada de revista

**Qué es:** el plano se convierte en la portada de una revista: marco fino, la cabecera detrás de la persona,
titulares en las esquinas y un código de barras.

```text
Convierte el plano de [segundo inicial] a [segundo final] en una portada de revista: un marco fino, la cabecera
«[nombre]» detrás de mi cabeza (usa el recorte de la persona), titulares en las esquinas con lo que voy diciendo y
un código de barras abajo. Que cada elemento entre en una de las palabras que acentúo.
```

## 9. Capturas reales

**Qué es:** cuando nombras una web, un documento o un dato, sale la captura real encima de tu cabeza.

```text
Cuando diga [lo que nombro], muestra la captura real de [web o archivo] encima de mi cabeza, con el 90 % del ancho,
esquinas redondeadas y una sombra suave. Que entre en 8 fotogramas y salga cuando cambie de tema.
```

> [!TIP]
> Una captura real convence más que una imitación hecha para el vídeo. Si no tienes la captura, mejor no poner nada.

## 10. Barrido rápido entre planos

**Qué es:** la transición en la que la cámara parece girar de golpe de un plano a otro.

```text
Entre el plano [A] y el [B], haz un barrido rápido: en los últimos 6 fotogramas de [A], la imagen se desplaza
hacia un lado con un desenfoque de movimiento que va creciendo; corte; y [B] entra desde el lado contrario y se
asienta en 6 fotogramas.
```

## 11. Ajuste de color explicado con un panel

**Qué es:** mientras explicas un retoque de color, en pantalla aparece un panel con sus controles moviéndose.

```text
Mientras explico el retoque, aplica al vídeo [ajustes: curvas, saturación, viñeta] de forma gradual y muestra al
lado un panel con esos controles, que se mueven a la vez que cambia la imagen.
```

## 12. Muro de vídeos

**Qué es:** tu plano en el centro de una cuadrícula de 3x3 y los otros ocho huecos llenándose de vídeos, uno detrás
de otro.

```text
Haz una cuadrícula de 3x3 con mi plano en el centro. Llena los otros 8 huecos con los vídeos de la carpeta
[carpeta], que entren de uno en uno, uno por fotograma, en el instante en que digo «[palabra]».
```

> [!CAUTION]
> Usa vídeos tuyos o con permiso de su autor. Descargar y publicar vídeos de otras personas sin permiso puede
> infringir sus derechos.

## 13. Pausa y explicación

**Qué es:** el vídeo que estás enseñando se congela con un clic, el contador se para y la ventana se hace pequeña a
un lado mientras lo explicas.

```text
Muestra el clip [clip] en una ventana. En el segundo [x], que se oiga un clic, el clip se congele y su contador se
pare, y la ventana se encoja hacia [lado] mientras explico qué está pasando. Cuando termine, que vuelva a su tamaño
y siga.
```

## 14. Cortes en seco

**Qué es:** el montaje sin adornos: se quitan todas las pausas y se alternan dos encuadres para que no se noten los
cortes.

```text
Con las marcas por palabra, corta todas las pausas de más de 0,22 segundos, sin cortar nunca dentro de una palabra.
En cada corte, alterna entre el encuadre normal y uno más cerrado (1,15 veces). Sin zooms ni transiciones.
```

---

## Cómo usarlos sin que el vídeo parezca una plantilla

- **Pocos y con motivo:** un efecto cuando ayuda a entender algo, no en cada frase.
- **Primero el guion gráfico (efecto 1):** decide qué va en cada tramo antes de renderizar.
- **Tu estilo, no el de otro:** cambia la tipografía, los colores y los tiempos de cada prompt por los tuyos, y
  apúntalos en tu manual de edición (capítulo 5.6) para que salgan siempre igual.

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
