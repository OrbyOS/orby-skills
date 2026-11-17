# HyperFrames: vídeos que la IA escribe en código

HyperFrames es la herramienta de HeyGen para convertir una animación escrita como página web (HTML, CSS y JavaScript) en un vídeo MP4. Está pensada para que una IA como Claude escriba la animación y HyperFrames la grabe fotograma a fotograma. Es de código abierto (licencia Apache 2.0) y tiene más de 85.000 estrellas en GitHub. Los reels animados de @orbyos se hacen con ella.

Revisada el 17 de noviembre de 2026.

---

## Qué hace

- **Le pides el vídeo a Claude** y él escribe la animación: textos, gráficos, 3D y subtítulos.
- **HyperFrames la graba** con Chrome y FFmpeg y te devuelve el MP4.
- **Sale siempre igual:** la misma animación da el mismo vídeo, así que puedes corregir un detalle sin rehacerlo todo.
- Trae bloques listos para usar: transiciones, subtítulos y gráficas.

## Cómo instalarlo

En Claude Code:

`claude plugin marketplace add heygen-com/hyperframes`

y después:

`claude plugin install hyperframes@hyperframes`

En otros agentes: `npx skills add heygen-com/hyperframes`

Necesitas Node.js 22 o posterior y FFmpeg.

## Lo que conviene saber

- Es para vídeos animados (explicativos, gráficos, textos en movimiento), no para editar lo que grabas con la cámara.
- Con escenas 3D, cada vídeo tarda en generarse: cuenta con varios minutos por cada medio minuto de vídeo.
