# Que Claude vea cualquier vídeo y lo convierta en skill

Claude no ve vídeos por sí solo. La skill gratuita **Watch** (proyecto claude-video, de código abierto, licencia MIT, más de 20.000 estrellas en GitHub) se los descarga, saca los fotogramas con su minuto y la transcripción, y se lo pasa todo. Con eso puede aprender de un tutorial de YouTube, de tus propios vídeos o de una reunión grabada, y guardarlo en una skill que usarás siempre.

Revisada el 9 de noviembre de 2026 con el repositorio github.com/bradautomates/claude-video. No es de Anthropic.

---

## 1. Instálala

En Claude Code, dentro de una sesión:

```text
/plugin marketplace add bradautomates/claude-video
/plugin install watch@claude-video
```

En la app de escritorio: Personalizar → Plugins → Añadir → Añadir marketplace → desde un repositorio, pega `https://github.com/bradautomates/claude-video` e instala **Watch**.

Necesita Python 3.10 o más reciente, FFmpeg y la última versión de yt-dlp. En Mac: `brew install python ffmpeg yt-dlp`. Si falta algo, pídele a Claude que ejecute el `setup.py` de la skill para comprobarlo.

## 2. Pruébala con un vídeo

```text
/watch [enlace de YouTube o ruta de un vídeo] --detail efficient
```

Con `--start 2:15 --end 2:45` mira solo un trozo.

## 3. Conviértelo en skill

```text
Mira estos vídeos con la skill watch: [enlaces].
Aprende lo que enseñan y conviértelo en una skill que pueda usar siempre: el método paso a paso, los ejemplos y los errores que avisan.
Antes de crearla, enséñame un resumen de lo que has aprendido y de dónde sale cada cosa (vídeo y minuto).
```

## Lo que conviene saber

- Usa primero los subtítulos del vídeo. Si no hay, transcribe en tu ordenador (gratis, necesita espacio y memoria) o con una clave de Groq u OpenAI.
- Con una clave de Gemini va más rápido, pero entonces el vídeo pasa por Google.
- No funciona en el chat de Claude ni en Cowork: en Claude Code sí.
- Los fotogramas son una muestra: si algo pasa muy rápido, puede no verlo. Pídele el minuto exacto con `--timestamps`.
