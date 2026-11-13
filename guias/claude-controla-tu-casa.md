# Controla tu casa hablando con Claude (Home Assistant + ha-mcp)

ha-mcp conecta Claude (y otros asistentes, como ChatGPT) con Home Assistant, el sistema gratuito para domótica. Con él, le pides en lenguaje normal que cree automatizaciones, escenas o paneles, o que te diga por qué falla una, y lo monta en tu casa.

Revisada el 13 de noviembre de 2026.

---

## Qué necesitas

- Home Assistant instalado (versión 2026.8 o posterior para la integración).
- Un asistente compatible: Claude Desktop, Claude.ai o Claude Code, ChatGPT, Gemini CLI, Cursor y más de quince en total.
- Si no tienes Home Assistant, hay un modo de prueba para verlo funcionar antes.

## Cómo instalarlo (la vía recomendada)

1. En Home Assistant, instala la integración HA-MCP desde HACS o desde el Marketplace de Home Assistant.
2. Reinicia Home Assistant.
3. Crea un token de acceso (o un usuario administrador solo para esto) y añade la integración.
4. Copia la dirección de conexión que te da y pégala en tu asistente (en Claude, como conector).

Hay otras vías (complemento de Home Assistant, Docker o uvx) explicadas en el repositorio.

## Qué le puedes pedir

- «Crea una automatización que encienda la luz del porche cuando se ponga el sol.»
- «Crea un modo película: baja las luces, cierra las persianas y enciende la tele.»
- «Añade una tarjeta con el tiempo a mi panel.»
- «El sensor de movimiento del pasillo no salta: mira su historial y dime por qué.»
- «Añade la cafetera a mi rutina de por la mañana.»

## Lo que conviene saber

- Antes de dejarle cambiar cosas, haz una copia de seguridad de Home Assistant (también se lo puedes pedir).
- Solo controla lo que ya está conectado a tu Home Assistant: no añade aparatos que no tengas.
- Revisa cada automatización que cree antes de dejarla funcionando sola.
- Es gratis y de código abierto (licencia MIT): github.com/homeassistant-ai/ha-mcp.
