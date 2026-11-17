# agent-browser: que tu IA use el navegador por ti

agent-browser es la herramienta de Vercel para que un agente de IA maneje el navegador: abre páginas, las lee y pulsa botones desde la terminal. Es de código abierto (licencia Apache 2.0) y tiene más de 52.000 estrellas en GitHub.

Revisada el 18 de noviembre de 2026.

---

## Qué hace

- **Lee la página como un texto ordenado,** con un nombre para cada botón y cada campo. Así la IA sabe dónde pulsar sin adivinar.
- **No finge:** si un botón está tapado, desactivado o fuera de la pantalla, avisa en lugar de decir que ha funcionado.
- **Mantiene el navegador abierto** entre órdenes, con sesiones separadas.
- Hace capturas, guarda PDF y se conecta también como servidor MCP.

## Cómo instalarlo

En la terminal:

`npm install -g agent-browser`

`agent-browser install`

Después, tu agente (Claude Code, Codex o el que uses) lo puede usar con órdenes como `agent-browser open tuweb.com` y `agent-browser snapshot`.

## Lo que conviene saber

- Maneja un navegador de verdad: no le des acceso a cuentas que no quieras que use.
