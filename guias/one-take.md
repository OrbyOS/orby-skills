# One Take: vídeos con IA que no parecen un PowerPoint

Casi todos los vídeos de producto hechos con IA se notan: título, fundido, tarjeta, fundido. Cada escena borra la anterior y el resultado parece una presentación. One Take es una skill de Claude con una sola regla: algo de cada escena sobrevive a la siguiente. Una barra se abre en un anuncio, una línea cruza la pantalla y se convierte en otra cosa, una tarjeta crece. Aquí tienes cómo instalarla y los primeros mensajes.

Revisada el 7 de noviembre de 2026 con el repositorio del proyecto (enlace al final). Ese día tenía 3.895 estrellas en GitHub. Necesitas Claude Code (capítulo 3.2).

---

## Qué hace

- **Una sola toma.** Cada momento del vídeo sale del anterior, sin cortes a la siguiente diapositiva.
- **Mide el ritmo antes de enseñártelo.** Un programa revisa cada vídeo fotograma a fotograma. Si parece una presentación, lo rechaza con un 0,00 y lo vuelve a montar.
- **Desenfoque de movimiento real.** Lo que se mueve deprisa se difumina como en una cámara, en vez de saltar.
- **Sonido en una sola sala.** Los efectos salen de lo que pasa en pantalla y comparten la misma reverberación.
- **Borradores a 1080p y finales en 4K a 60 imágenes por segundo.**

## Lo que hace falta

- Claude Code en tu ordenador.
- Python 3 con estas librerías: `playwright` (con Chromium), `numpy`, `scipy`, `Pillow` y `matplotlib`. No hace falta que sepas instalarlas: pídeselo a Claude.

## 1. Instálala

Pídele a Claude Code:

```text
Instala la skill One Take: clona https://github.com/feitangyuan/onetake.git en ~/.claude/skills/onetake e instala lo que necesita en Python (playwright con Chromium, numpy, scipy, Pillow y matplotlib). Explícame cada paso antes de hacerlo.
```

## 2. Primeros mensajes

```text
Hazme un vídeo de lanzamiento de 15 segundos para [tu producto]. Te paso capturas de la web: [ruta]. Sin grabación de pantalla.
```

```text
Este vídeo parece una presentación: [ruta del vídeo]. Arréglalo para que sea una sola toma.
```

## Lo que conviene saber

- **Licencia:** es gratis para uso no comercial (PolyForm Noncommercial). Si haces vídeos para clientes o para tu negocio, el autor vende una licencia comercial.
- **Tarda.** Un vídeo de verdad necesita varias vueltas y el ordenador trabaja un buen rato con el render final. Empieza por borradores cortos.

## Fuentes

- [Repositorio de One Take](https://github.com/feitangyuan/onetake).

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
