# DeepTutor: un profesor particular de IA, gratis

DeepTutor es un profesor particular de IA de código abierto (licencia Apache 2.0): le das tus apuntes o un libro, te lo explica, te pone exámenes y recuerda lo que te cuesta. Tiene casi 60.000 estrellas en GitHub.

Revisada el 17 de noviembre de 2026.

---

## Qué hace

- **Aprende con tus documentos:** subes apuntes, libros o PDF y responde a partir de ellos.
- **Exámenes y práctica:** te pregunta, corrige y te propone un camino hasta que dominas el tema.
- **Memoria que puedes leer:** guarda lo que te cuesta y cómo prefieres aprender, en archivos que puedes revisar y corregir.
- También resuelve ejercicios paso a paso, hace esquemas y exporta tarjetas a Anki.

## Cómo instalarlo

La forma más rápida es con Docker:

`docker run -p 3782:3782 ghcr.io/hkuds/deeptutor:latest`

y después abre http://127.0.0.1:3782 en el navegador.

Con Python (3.11 o posterior): `pip install -U "deeptutor[full]"`, después `deeptutor init` y `deeptutor start`.

## Lo que conviene saber

- Necesitas conectarle un modelo de IA en Ajustes: puede ser uno de pago (Claude, ChatGPT, Gemini) o uno gratis que corra en tu ordenador.
- La versión de escritorio para Mac y Windows está en pruebas.
