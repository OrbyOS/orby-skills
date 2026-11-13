# claude-mem: que Claude no se olvide de nada entre sesiones

Cada vez que abres una sesión nueva, Claude Code empieza de cero: vuelve a leer los mismos archivos, te hace las mismas preguntas y repite errores que ya arreglasteis. claude-mem lo soluciona. Es de código abierto (licencia Apache 2.0) y tiene más de 100.000 estrellas en GitHub.

Revisada el 13 de noviembre de 2026.

---

## Qué hace

- **Un segundo agente toma notas** de lo que hace Claude mientras trabajas.
- **La siguiente sesión empieza con un resumen** corto de lo que importa.
- **Busca los detalles solo cuando los necesita**, así no llena la conversación.
- Funciona con Claude Code, Codex, Cursor y otros agentes.
- Tu memoria se guarda en tu ordenador, en la carpeta `~/.claude-mem`. Sincronizarla en la nube es opcional.

## Cómo instalarlo

En la terminal:

`npx claude-mem install`

El instalador busca los agentes que tienes y te pregunta cuáles configurar. Desde la segunda sesión en un proyecto, ya abre con la memoria de la primera.

También desde Claude Code, como plugin: `/plugin marketplace add thedotmack/claude-mem`, después `/plugin install claude-mem`, y reinicia Claude Code.

## Lo que conviene saber

- No lo instales con `npm install -g claude-mem`: eso solo instala la librería, no la memoria.
- Al instalar te ofrece iniciar sesión y una prueba de 30 días de su servicio de notas. Si no lo quieres, el propio instalador te deja usar otro proveedor sin cuenta.
- Envía estadísticas anónimas de uso; se apagan con `npx claude-mem telemetry disable`.
