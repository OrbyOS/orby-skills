# El agente de Instagram para Claude: trece skills gratis para tu cuenta

Trece skills de Claude, gratis y de código abierto, que hacen el trabajo de llevar una cuenta de Instagram: te escriben el reel, buscan qué funciona en tu nicho, puntúan tu perfil, planifican la semana y contestan comentarios. No te piden la contraseña y no publican nada: el último paso lo das tú.

Revisada el 13 de noviembre de 2026.

---

## Qué hace cada skill

- `/ig-reel`: de una idea saca el reel entero: ganchos puntuados, guion, texto en pantalla y tiempos.
- `/ig-viral`: busca qué está funcionando en tu nicho y lo compara con lo normal de cada cuenta.
- `/ig-caption`: escribe el texto del post y te enseña la parte que se ve en el feed.
- `/ig-carousel`: escribe un carrusel (portada y diapositivas) y prepara los archivos en 1080×1350.
- `/ig-story`: planifica las historias del día.
- `/ig-profile`: puntúa tu perfil sobre 100 y te lo reescribe.
- `/ig-plan`: planifica la semana: qué publicar, en qué formato y a qué hora.
- `/ig-human`: quita las frases que suenan a IA.
- `/ig-comment` y `/ig-reply`: comentarios en otras cuentas y respuestas a los tuyos, en orden.
- `/ig-dm`: mensajes de palabra clave, primer mensaje y propuestas de colaboración.
- `/ig-repurpose`: convierte un vídeo, un pódcast o una newsletter en una semana de reels y carruseles.
- `/ig-audit`: repasa tus publicaciones y te dice cuáles destacaron y por qué.

## Cómo instalarlo en Claude Code

La forma fácil: abre Claude Code y pega esto:

«Instala esta skill: https://github.com/Jakeschincariol/instagram-agent-skill y comprueba que /ig-reel funciona.»

A mano:

1. `git clone https://github.com/Jakeschincariol/instagram-agent-skill.git`
2. `cp -r instagram-agent-skill/skills/ig-* ~/.claude/skills/`

Como plugin: `/plugin marketplace add Jakeschincariol/instagram-agent-skill` y después `/plugin install instagram-agent`.

## El paso que no te puedes saltar

Copia `templates/voice.md` en `~/.claude/instagram/voice.md` y rellénalo con cómo hablas. Si no te apetece, pásale a Claude tres de tus reels y pídele que lo escriba él. Todas las skills leen ese archivo: sin él, todo suena genérico.

## Lo que conviene saber

- Las skills son gratis (licencia MIT), pero Claude Code necesita un plan de pago de Claude.
- No se conecta a tu cuenta: los datos de `/ig-viral` y `/ig-audit` se los das tú (o los mira contigo en tu navegador).
- Es un proyecto de la comunidad: revisa los archivos antes de activarlo.
