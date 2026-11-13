# El profesor de IA de Jane Street: aprende cualquier tema con preguntas

Jane Street, una de las grandes empresas de trading de Wall Street, ha publicado gratis una skill que convierte a Claude (o a ChatGPT) en un tutor estricto. Le dices qué quieres aprender y te enseña con el método socrático: preguntas, una a una, sin darte la respuesta.

Revisada el 13 de noviembre de 2026.

---

## Qué hace

- **Un diagnóstico primero**, para ver de qué nivel partes.
- **Un mapa de niveles del 0 al 5** del tema que elijas.
- **Una pregunta cada vez**: te obliga a pensar en lugar de leer.
- **Repaso espaciado**: vuelve a lo que ya viste para que no se te olvide.
- **Un examen final** para comprobar lo aprendido.

## Cómo usarlo sin instalar nada (Claude.ai o ChatGPT)

1. Abre github.com/janestreet/agent_skills y entra en la carpeta `socratic-tutor`.
2. Abre el archivo `SKILL.md` y copia todo su texto.
3. Pégalo en un chat nuevo (o en las instrucciones de un proyecto) y escribe: «Enséñame X».

## Cómo instalarlo en Claude Code

1. Descarga el repositorio: `git clone https://github.com/janestreet/agent_skills`
2. Copia la carpeta `socratic-tutor` dentro de `~/.claude/skills/`.
3. Abre Claude Code y pídele: «Usa el tutor socrático para enseñarme X».

## Lo que conviene saber

- Es estricto a propósito: no te va a dar la respuesta aunque se la pidas. Esa es la gracia.
- Funciona para cualquier tema: un idioma, finanzas, marketing, programación…
- Es gratis y de código abierto (licencia MIT).
