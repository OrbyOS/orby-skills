# Herramientas de IA gratis que funcionan en tu ordenador

Cuatro herramientas gratuitas y de código abierto. Tus archivos no salen de tu ordenador, no pagas suscripción y, una vez instaladas, casi todo funciona sin internet.

Revisada el 1 de noviembre de 2026. Los programas cambian de versión: si un paso no coincide, sigue las instrucciones de su página oficial.

---

## Upscayl: ampliar una imagen sin que se pixele

Sirve para agrandar una foto pequeña o borrosa: la IA rellena el detalle que falta.

1. Descárgala desde [upscayl.org](https://upscayl.org) (Mac, Windows o Linux) e instálala.
2. Arrastra la foto a la ventana.
3. Elige el modelo y pulsa el botón de ampliar.

El detalle nuevo lo inventa la IA: sirve para que una imagen se vea bien, no como prueba de lo que había en la foto original.

## Ollama: tu propio chat de IA, sin internet

Sirve para tener un chat parecido a ChatGPT dentro de tu ordenador, también para textos que no quieres subir a ningún sitio.

1. Descárgalo desde [ollama.com](https://ollama.com) e instálalo.
2. Abre la Terminal y escribe esta línea (la primera vez descarga el modelo, que ocupa unos gigas):

```
ollama run llama3.2
```

3. Escribe lo que quieras preguntarle. Para salir, escribe `/bye`.

Va más lento y acierta menos que los mejores modelos de pago, y depende de la memoria de tu ordenador.

## Whisper: todo lo que dices en un vídeo, por escrito

Sirve para sacar la transcripción de un vídeo o un audio, con sus tiempos, lista para subtítulos. Es de OpenAI.

1. Necesitas Python y ffmpeg instalados. Si no sabes qué es, pídele a Claude que te guíe paso a paso.
2. Instálalo desde la Terminal:

```
pip install -U openai-whisper
```

3. Pásale tu vídeo:

```
whisper mivideo.mp4 --language Spanish
```

Al terminar tienes el texto y un archivo de subtítulos `.srt` en la misma carpeta. Más información en [su página de GitHub](https://github.com/openai/whisper).

## rembg: quitar el fondo de una foto

Sirve para dejar una foto sin fondo, o una carpeta entera de golpe. Con el pelo suelto, a veces toca retocar.

1. Necesitas Python instalado.
2. Instálalo desde la Terminal:

```
pip install "rembg[cli]"
```

3. Pásale tu foto:

```
rembg i foto.jpg foto-sin-fondo.png
```

Para una carpeta entera: `rembg p carpeta-entrada carpeta-salida`. Más información en [su página de GitHub](https://github.com/danielgatis/rembg).
