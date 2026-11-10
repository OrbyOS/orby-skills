---
name: editar-reels-con-claude
description: Edita un vídeo hablado a cámara y lo deja listo para Instagram, TikTok o Shorts. Quita silencios y tomas falsas, añade subtítulos quemados palabra a palabra, lo pasa a vertical 9:16 (1080x1920) y deja el volumen a -14 LUFS, todo en el ordenador con ffmpeg y faster-whisper. Úsala cuando alguien pida editar, limpiar o montar un reel o un bruto, quitar silencios o fallos, poner subtítulos o pasar un vídeo a vertical, aunque no diga «skill».
---

# Editar reels con Claude

Convierte un bruto grabado a cámara en un reel limpio: sin silencios, sin tomas falsas, con subtítulos y en 9:16.
Nada sale del ordenador: la transcripción también se hace en local.

Los scripts están en `scripts/`, dentro de la carpeta de esta skill. En los comandos de abajo, `SKILL` es la ruta
de esa carpeta (normalmente `~/.claude/skills/editar-reels-con-claude`) y `PY` es el Python de la skill:
`SKILL/.venv/bin/python` si existe; si no, `python3`.

## Reglas de edición

- Se quitan trozos; el orden de lo que dice la persona no se cambia nunca.
- De una frase repetida se queda la última versión completa, que suele ser la buena.
- Fuera: frases a medias, arranques en falso, comentarios a la cámara («espera», «lo repito», «corta») y muletillas
  sueltas que no forman parte de una frase.
- Dentro: todo lo que aporte contenido, aunque tenga alguna duda o pausa natural. Ante la duda, se queda y se
  pregunta.
- Nada de inventar texto: los subtítulos dicen lo que se oye.
- Si en la carpeta del bruto (o en la de trabajo del usuario) hay un `MANUAL-EDICION.md`, léelo antes de empezar:
  sus reglas mandan sobre los valores por defecto de esta skill (estilo y color de subtítulos, altura, duración).
- Cuando el usuario corrija algo del montaje, arréglalo y pregúntale si quiere apuntarlo como regla en
  `MANUAL-EDICION.md` para la próxima vez (la skill `manual-de-edicion` explica cómo escribirla).

## Que no parezca hecho con inteligencia artificial

Si el usuario no ha pedido otra cosa, cualquier añadido al reel sigue estas reglas:
- **Subtítulos:** tipografía sencilla y gruesa, sin remates ni cursivas (`--fuente "Arial Black"`, o el archivo de
  una fuente así con `--fuente-archivo`).
- **Texto del gancho:** sin fondo, o sobre un fondo liso blanco o negro. Nada de degradados ni de cristal.
- **Imágenes y capturas:** solo las que el usuario deja en una carpeta. No busques ni descargues imágenes por tu
  cuenta: si son de otros y se publican sin permiso, la red puede quitar el vídeo o cerrar la cuenta.
- **Cómo entran:** rectas, sin esquinas redondeadas, sin bordes blancos y sin animarlas por encima.
- **Ritmo:** cortes secos en cada silencio de más de una décima (`cortar_silencios.py --minimo 0.1`), sin
  transiciones. Alguna animación suelta, pero nunca letras que bailan.

## Paso 0. Comprobar el equipo

```bash
python3 SKILL/scripts/comprobar.py
```

- Si falta **faster-whisper o Pillow**, el informe da un comando que crea el entorno de la skill (`SKILL/.venv`) y
  los instala. Pide permiso al usuario antes de ejecutarlo: descarga unos 200 MB, y la primera transcripción baja
  además el modelo (small, unos 500 MB).
- Si falta **ffmpeg**: `brew install ffmpeg` en Mac. Sin ffmpeg no se puede seguir.
- **Subtítulos y libass.** El ffmpeg normal de Homebrew no trae libass ni drawtext, así que no puede quemar
  subtítulos por sí solo. Díselo al usuario con estas palabras o parecidas y dale a elegir:
  1. Seguir así: `montar.py` dibuja los subtítulos como imágenes con Pillow y los superpone con el ffmpeg normal.
     Mismo resultado, algo más lento. Es lo que se hace si no dice nada.
  2. Instalar `brew install ffmpeg-full`: va aparte (no sustituye al normal) y los scripts lo encuentran solos.
     Avisa de que en versiones antiguas de macOS Homebrew no tiene el paquete precompilado y lo compila, lo que
     puede llevar horas. No lo instales sin su OK.
  Si ya tiene un ffmpeg con libass en otra ruta, se puede indicar con la variable `FFMPEG_SUBTITULOS`.

## Paso 1. Pedir el bruto

Pide al usuario:
1. El vídeo: que arrastre el archivo a la terminal para pegar su ruta, o que la escriba.
2. Solo si no lo ha dicho ya: si quiere subtítulos (por defecto sí) y de qué tipo: «resaltado» (la palabra que
   suena cambia de color, por defecto) o «simple» (blanco).

No pidas más: el resto tiene valores por defecto razonables. Crea la carpeta de trabajo junto al bruto:
`<nombre del bruto>_reel/`.

## Paso 2. Quitar los silencios

```bash
python3 SKILL/scripts/cortar_silencios.py BRUTO TRABAJO/limpio.mp4
```

Imprime cuánto duraba y cuánto dura ahora. Si apenas ha recortado y el bruto tiene pausas claras, el ruido de fondo
está por encima del umbral: repite con `--umbral -30`. Si se come el final de las palabras, sube `--margen 0.12`.
Si el vídeo no tiene voz, avisa y para.

## Paso 3. Transcribir

```bash
PY SKILL/scripts/transcribir.py TRABAJO/limpio.mp4 TRABAJO --idioma es
```

Usa el idioma del vídeo (es, en, ca…). Deja `transcripcion.txt` (frases numeradas con su tiempo) y
`transcripcion.json` (palabra a palabra). Con mucho ruido o acentos marcados, `--modelo medium` acierta más y tarda
más.

## Paso 4. Decidir qué sobra

Lee `TRABAJO/transcripcion.txt` entero y aplica las reglas de edición. Enseña al usuario una tabla corta con lo que
propones quitar:

| Frase | Texto | Por qué |
| --- | --- | --- |
| 2 | Lo primero es quitar los sil… | Arranque en falso: la 3 lo repite completo |

Espera su OK o sus cambios. Si no sobra nada, dilo y sigue.

Mientras, revisa las palabras mal entendidas en las frases que se quedan (nombres propios, marcas, términos
técnicos). Corrígelas en `transcripcion.json`, en `palabras[i].texto`, sin tocar los tiempos. Así los subtítulos
salen bien escritos.

## Paso 5. Encuadre

Si el bruto es horizontal, hay que elegir qué parte se queda en el 9:16. Saca un fotograma y míralo:

```bash
ffmpeg -loglevel error -y -ss 2 -i TRABAJO/limpio.mp4 -frames:v 1 -vf scale=640:-1 TRABAJO/encuadre.jpg
```

Si la persona está centrada, `--encuadre 0.5` (por defecto); a la izquierda, entre 0.2 y 0.35; a la derecha, entre
0.65 y 0.8. Si el bruto ya es vertical, no hace falta.

## Paso 6. Montar

```bash
PY SKILL/scripts/montar.py TRABAJO/limpio.mp4 TRABAJO/transcripcion.json TRABAJO/reel.mp4 --quitar 2,5-6
```

Opciones útiles:
- `--estilo simple` subtítulos en blanco, sin resaltar.
- `--color "#7CC4FF"` color de la palabra resaltada (por defecto, amarillo).
- `--palabras 2` menos palabras a la vez, para ritmos rápidos.
- `--minusculas` si no los quiere en mayúsculas.
- `--altura 1300` sube los subtítulos si tapan algo; por debajo de 1440 los tapa la interfaz de Instagram.
- `--sin-subtitulos` solo corte y vertical.

### Varios reels de una grabación

Si el bruto es una charla larga con varios temas (por ejemplo, grabada con la skill `estructura-para-grabar`), no se
monta entera: se sacan varios reels. Con la transcripción delante:
1. Marca dónde empieza y acaba cada tema. Un reel tiene que entenderse solo: si arranca con «como decía antes», ese
   arranque se quita o el reel empieza en la frase siguiente.
2. La primera frase de cada reel es su gancho. Elige el inicio que mejor enganche dentro del bloque, sin cambiar el
   orden de lo que se dice.
3. Propón al usuario la lista (reel, frases, primera frase y duración aproximada) y espera su OK. Un reel por
   debajo de 20 segundos o por encima de 90 suele funcionar peor: dilo si pasa.
4. Monta cada uno con `--solo` y, dentro, quita las tomas falsas con `--quitar`:

```bash
PY SKILL/scripts/montar.py TRABAJO/limpio.mp4 TRABAJO/transcripcion.json TRABAJO/reel_1.mp4 --solo 1-9 --quitar 4
PY SKILL/scripts/montar.py TRABAJO/limpio.mp4 TRABAJO/transcripcion.json TRABAJO/reel_2.mp4 --solo 11-19
```

## Paso 7. Revisar antes de entregar

```bash
python3 SKILL/scripts/revisar.py TRABAJO/reel.mp4
```

Comprueba las medidas (1080x1920), el volumen (cerca de -14 LUFS) y los silencios largos, y deja una hoja con doce
fotogramas (`reel_hoja.jpg`). **Abre la hoja y mírala**: que los subtítulos se lean, que no tapen la cara y que el
encuadre no corte a la persona. Si algo falla, corrige y vuelve a montar. No entregues un reel sin haber mirado la
hoja.

## Paso 8. Entregar

Dile al usuario:
- dónde está el reel (`TRABAJO/reel.mp4`) y cuánto dura frente al bruto;
- qué frases has quitado;
- que si quiere otro estilo de subtítulos o cambiar un corte, basta con decirlo: se vuelve a montar desde el paso 6
  sin transcribir de nuevo.

Los archivos intermedios (`limpio.mp4`, la hoja, `encuadre.jpg`) se pueden borrar al terminar; pregunta antes. El
bruto no se toca nunca.
