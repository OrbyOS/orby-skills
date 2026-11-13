# agent-desktop: tu IA ya puede usar cualquier aplicación del ordenador

agent-desktop es una herramienta gratuita de Vercel que da a tu agente de IA «manos» para usar las aplicaciones de tu ordenador. No hace capturas de pantalla: lee los botones y menús de cada aplicación y le pasa a tu agente la lista de lo que puede pulsar.

Revisada el 13 de noviembre de 2026.

---

## Dónde funciona

- Mac (macOS 13 o posterior), Windows 10/11 y Linux (Ubuntu 24.04 o posterior).

## Cómo instalarlo

```
npm install -g agent-desktop
agent-desktop status
agent-desktop permissions --guide
```

En Mac, el último comando te explica cómo dar el permiso de Accesibilidad.

## Cómo conectarlo a Claude Code

Como herramienta (MCP):

```
claude mcp add agent-desktop -- agent-desktop mcp
```

O como skill:

```
npx skills add https://github.com/vercel-labs/agent-desktop --skill agent-desktop
```

Después pídele cosas como: «Abre Finder y busca los PDF de esta semana».

## Cómo trabaja

1. Lee la aplicación y le da a tu agente la lista de botones y campos.
2. Tu agente decide qué pulsar o qué escribir.
3. Vuelve a leer la aplicación para comprobar que ha salido bien.

## Lo que conviene saber

- Ve lo que tienes abierto: no lo uses con datos privados a la vista ni compartas sus registros.
- Las contraseñas, mejor no pasárselas.
- Gratis y de código abierto (Apache 2.0): github.com/vercel-labs/agent-desktop.
