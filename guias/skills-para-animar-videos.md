# Seis skills de Claude que te hacen vídeos animados

Seis skills que salieron el 12 de noviembre de 2026: escribes una orden en Claude Code y te devuelven un vídeo vertical (1080×1920) de 5 a 7 segundos, listo para subir.

Revisada el 13 de noviembre de 2026.

---

## Las seis

- `/graph`: tus números convertidos en un gráfico que se va dibujando. Ejemplo: `/graph enero 200, febrero 650, marzo 1500`.
- `/map-route`: una ruta que se pinta sola entre dos puntos sobre un mapa real en 3D. Ejemplo: `/map-route Puerta del Sol a Retiro`.
- `/breakdown`: tu producto (por nombre o con una foto) girando en 3D y desmontándose, con cada pieza rotulada.
- `/stick-figure`: una idea explicada con muñecos de palo y bocadillos.
- `/minimal-graphics`: una idea explicada con formas simples y puntos en movimiento.
- `/zachdfilms`: un plano de estilo película con tu pregunta en grande. Es la única que cuesta dinero: necesita el conector de Higgsfield y créditos (unos 80 por plano de 5 segundos).

## Cómo instalarlas en Claude Code

Abre Claude Code y pega:

«Instala las seis skills de https://github.com/maverickmaltin/claude-animate-skills en mi carpeta ~/.claude/skills.»

Abre una sesión nueva y escribe `/` para ver que aparecen. La primera vez que hagas un vídeo, Claude te ofrecerá instalar Playwright y ffmpeg, que son los que graban y montan el vídeo.

## En la app de Claude (claude.ai)

Cada skill tiene su propio ZIP en la página de descargas (Releases) del repositorio. Activa Ajustes → Capacidades → Crear y editar archivos, y súbelo en Personalizar → Skills → Añadir.

## Lo que conviene saber

- Las skills son gratis, pero Claude Code necesita un plan de pago de Claude.
- Necesitas Python 3 y Google Chrome en el ordenador.
- Son muy nuevas (salieron el 12/11/2026): pruébalas con algo sencillo, como `/graph`, antes de usarlas para un cliente.
