# PaperOrchestra: un equipo de IA que escribe artículos científicos

PaperOrchestra es un proyecto de investigadores de Google: un equipo de agentes de IA que convierte una idea y los datos de tus experimentos en un artículo científico completo. Es de código abierto (licencia Apache 2.0).

Revisada el 18 de noviembre de 2026.

---

## Qué hace

- **Un agente hace el esquema** del artículo.
- **Otro busca y resume la bibliografía.**
- **Otro escribe cada sección,** y otro la revisa.
- **Otro dibuja los gráficos** a partir de tus datos.

El resultado es un artículo en LaTeX, con la plantilla de la revista o el congreso que elijas.

## Cómo usarlo

Necesitas Python y una clave de Gemini (Vertex AI) o de OpenAI, y otra de Semantic Scholar para la bibliografía. Clona el repositorio github.com/google-research/paper-orchestra, prepara una carpeta con tu idea y tus datos, y lánzalo con su script.

## Lo que conviene saber

- No es un producto oficial de Google: es investigación.
- Sirve para un primer borrador. La revisión de una persona experta sigue siendo imprescindible.
