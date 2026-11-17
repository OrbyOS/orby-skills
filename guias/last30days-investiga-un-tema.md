# last30days: lo que se ha dicho de un tema en el último mes

Le pides un tema y se lee lo que se ha publicado sobre él en los últimos 30 días en Reddit, X, YouTube, TikTok, Hacker News, GitHub y más sitios. Después te devuelve un resumen ordenado por lo que más ha movido a la gente, con la fuente de cada cosa. Es de código abierto (licencia MIT) y tiene más de 68.000 estrellas en GitHub.

Revisada el 17 de noviembre de 2026.

---

## Qué hace

- **Busca en muchas fuentes a la vez:** Reddit (con comentarios), X, YouTube (con transcripciones), TikTok, Instagram, Hacker News, GitHub y búsqueda web, entre otras.
- **Ordena por interés real:** votos, me gusta y comentarios, no lo que decide un editor.
- **Une lo que se repite:** si el mismo tema sale en varias redes, lo junta en una sola historia.
- **Te da las fuentes:** cada punto del resumen dice de dónde sale.
- Tiene un modo sin tema que te enseña lo que está saliendo ahora.

## Cómo instalarlo

En Claude Code:

`/plugin marketplace add mvanhorn/last30days-skill`

y después:

`/plugin install last30days`

En otros agentes (Codex, Cursor, Gemini CLI y otros): `npx skills add mvanhorn/last30days-skill -g`

Después le pides, por ejemplo: «investiga qué se dice este mes sobre [tu tema]».

## Para qué te sirve si haces contenido

- Antes de grabar, saber qué preguntas y quejas se repiten sobre tu tema.
- Ver qué vídeos y publicaciones han funcionado este mes en tu nicho.
- Sacar ideas con las palabras exactas que usa tu público.

## Lo que conviene saber

- Reddit, Hacker News, GitHub y Polymarket funcionan sin configurar nada.
- X, TikTok, Instagram, Threads y LinkedIn necesitan una clave o un servicio aparte. Sin ellos, el resumen sale con menos fuentes.
- Para las transcripciones de YouTube necesita `yt-dlp`, que es gratis.
