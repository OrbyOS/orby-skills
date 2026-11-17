# ffmpeg-skill: edita tus vídeos con Claude, gratis y en tu ordenador

Son 42 herramientas que Claude Code (y también Cursor o Codex) usa por ti para editar vídeo: quitar silencios, poner subtítulos, pasarlo a vertical y ajustar el volumen. Todo se hace en tu ordenador, sin servicios de pago y sin claves. Es de código abierto (licencia MIT) y tiene más de 7.000 estrellas en GitHub.

Revisada el 17 de noviembre de 2026.

---

## Qué le puedes pedir

- **Quitar silencios** y tiempos muertos, dejando un margen para que no quede cortado.
- **Subtítulos** pegados al vídeo, también palabra a palabra.
- **Pasarlo a vertical** para Reels, TikTok o Shorts, recortando o con el fondo difuminado.
- **Ajustar el sonido:** limpiar, comprimir y dejar el volumen a −14 LUFS, el que piden las redes.
- **Cortar, unir y poner títulos o tu logo.**
- Exportarlo con el formato de cada plataforma y comprobar que lo cumple.

## Cómo instalarlo

Necesitas tener instalados FFmpeg (versión 6.1 o posterior) y Python 3.10 o posterior. Después, en la terminal:

`npx ffmpeg-skill`

Para comprobar que tienes todo lo necesario: `npx ffmpeg-skill doctor`

Con `--cursor`, `--codex` o `--all` lo instalas también en otros agentes.

Después, en Claude Code: «quita los silencios de este vídeo, ponle subtítulos y pásalo a vertical para Reels».

## Lo que conviene saber

- No usa internet ni ninguna API de pago: todo pasa en tu ordenador.
- La transcripción para subtítulos usa un motor local que descarga su modelo la primera vez; el audio no se sube a ningún sitio.
- Edita como un editor de línea de comandos: para cortes finos, revisa el resultado antes de publicarlo.
