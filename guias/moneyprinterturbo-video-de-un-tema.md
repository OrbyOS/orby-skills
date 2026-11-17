# MoneyPrinterTurbo: escribes un tema y te devuelve el vídeo

MoneyPrinterTurbo genera un vídeo corto a partir de un tema: escribe el guion con IA, busca vídeos que encajan, le pone voz, subtítulos y música, y lo monta. Es de código abierto (licencia MIT) y tiene más de 140.000 estrellas en GitHub.

Revisada el 17 de noviembre de 2026.

---

## Qué hace

- **Guion:** lo escribe la IA que elijas (ChatGPT, Claude, Gemini, DeepSeek o un modelo gratis en tu ordenador).
- **Imágenes:** vídeos de bancos gratuitos como Pexels o Pixabay.
- **Voz, subtítulos y música** de fondo.
- **Formatos:** vertical para Reels, horizontal o cuadrado.

## Cómo instalarlo

- En Windows, hay un paquete que se instala con un clic (en el apartado Releases del repositorio).
- Con Python 3.11 o posterior: `pip install mpt` y después `mpt webui`.
- Con Docker: `docker compose -f docker-compose.release.yml up` y abre http://127.0.0.1:8501.

Las claves de cada servicio se ponen en los ajustes de su web.

## Lo que conviene saber

- La voz básica es gratis y no pide clave; otras voces y servicios piden la suya.
- Los vídeos salen con imágenes de bancos: sirven para temas generales. Para tu marca personal, tu cara y tu voz convierten mucho más.
