# Crawl4AI: convierte cualquier web en texto limpio para tu IA

Crawl4AI es una herramienta de código abierto (licencia Apache 2.0, más de 80.000 estrellas en GitHub) que lee páginas web y te las devuelve en texto ordenado, sin menús ni pies de página, listo para pasárselo a ChatGPT o a Claude.

Revisada el 14 de noviembre de 2026.

---

## Qué hace

- **Una página, en texto limpio:** le das la dirección y te devuelve el contenido en Markdown, con títulos, listas y tablas.
- **Una web entera:** recorre las páginas una a una, hasta el límite que le pongas.
- **Solo los datos que quieras:** precios, nombres, fechas, en un formato que se puede abrir como tabla.
- También saca capturas de pantalla y PDF de las páginas.

## Para qué sirve en tu negocio

- Estudiar a tu competencia: sus servicios, sus precios y cómo lo cuentan, en una tarde.
- Darle a tu IA el contenido de tu propia web para que conteste con tus datos.
- Reunir en un solo documento las preguntas frecuentes de un sector.

## Cómo instalarlo

Necesitas Python. En la terminal:

`pip install -U crawl4ai`

`crawl4ai-setup`

Para leer una página:

`crwl https://tuweb.com -o markdown`

Para recorrer una web entera, con un máximo de 10 páginas:

`crwl https://tuweb.com --deep-crawl bfs --max-pages 10`

La forma más cómoda: abre Claude Code y pídele «Instala Crawl4AI y sácame en texto la web de este competidor».

## Lo que conviene saber

- La herramienta es gratis en tu ordenador. Tiene además un servicio en la nube de pago, con 1.000 créditos gratis al mes.
- Respeta las condiciones de uso de cada web y no la uses para copiar contenido ni datos personales.
- Si `crawl4ai-setup` falla, el navegador se instala con `python -m playwright install --with-deps chromium`.
