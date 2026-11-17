# Chrome DevTools MCP: Claude abre tu web en Chrome y te dice qué falla

Es la herramienta del equipo de Chrome DevTools para que un agente de IA controle e inspeccione un Chrome de verdad: graba cómo carga tu página, lee los errores y navega por ella. Es de código abierto (licencia Apache 2.0) y tiene casi 58.000 estrellas en GitHub.

Revisada el 17 de noviembre de 2026.

---

## Qué hace

- **Rendimiento:** graba cómo carga tu página y te explica qué la hace lenta.
- **Errores:** lee la consola y las peticiones de red que fallan.
- **Capturas:** hace capturas de pantalla de lo que ve.
- **Navega por tu web** como lo haría un cliente: entra, pulsa y espera a que cargue.

Funciona con Claude Code, Cursor, Copilot, Gemini CLI y otros agentes.

## Cómo instalarlo

En Claude Code, en la terminal:

`claude mcp add chrome-devtools -- npx -y chrome-devtools-mcp@latest`

En otros agentes, añádelo como servidor MCP con la orden `npx -y chrome-devtools-mcp@latest`.

Después pídele: «abre [tu web] en Chrome, mide cuánto tarda en cargar y dime qué la frena y cómo arreglarlo».

## Lo que conviene saber

- Abre un Chrome que controla el agente: no le des acceso a cuentas que no quieras que vea.
- Necesitas tener instalado Node.js.
