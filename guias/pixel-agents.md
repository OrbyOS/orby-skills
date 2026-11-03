# Pixel Agents: tus agentes de Claude Code, en una oficina

Cuando tienes varios agentes a la vez, cuesta saber qué hace cada uno. Pixel Agents convierte cada terminal de Claude Code en un muñequito que trabaja en una oficina: se sienta, teclea cuando escribe, lee cuando busca y avisa cuando te necesita. Es gratis y, además de gracioso, útil.

Revisada el 3 de noviembre de 2026 con su documentación (enlace al final). Ese día tenía 10k estrellas en GitHub y licencia MIT.

---

## Lo que hace

- **Un agente, un muñeco.** Cada terminal de Claude Code tiene el suyo, y los subagentes aparecen como otros muñecos.
- **Se mueve según lo que hace de verdad:** escribir, leer o ejecutar.
- **Bocadillos y avisos** cuando un agente espera tu respuesta o tu permiso. Puede sonar una campanita.
- **Tu propia oficina:** suelos, paredes, muebles y zonas por proyecto.

No hace el trabajo ni cambia cómo trabajan: solo te enseña lo que está pasando.

## Instalarlo

Necesitas Claude Code por terminal (capítulo 3.2) y VS Code 1.105 o posterior. Funciona en Mac, Windows y Linux.

1. Abre VS Code y busca **Pixel Agents** en Extensiones, o entra en [su página](https://marketplace.visualstudio.com/items?itemName=pablodelucca.pixel-agents).
2. Instálala y abre el panel **Pixel Agents**, junto a la terminal.
3. Pulsa **+ Agent**, elige una carpeta y Claude Code arranca en ella.

Si quieres ver también las sesiones de otras carpetas, activa **Settings, Watch All Sessions**.

### Sin VS Code

Con Node.js 20 o posterior, abre la terminal en tu proyecto y pega esto. Se abre la oficina en tu navegador:

```bash
npx pixel-agents
```

## Para sacarle partido

- **Una zona por proyecto.** Pinta zonas en la oficina y asigna una carpeta a cada una: cada agente se sentará en la suya.
- **Atiende los bocadillos.** Es lo más útil: ves de un vistazo qué agente lleva rato esperándote.
- **Déjalo en una segunda pantalla** si trabajas con varios a la vez.

> [!CAUTION]
> Tiene un ajuste, **Skip Permissions**, que deja a tus agentes actuar sin pedirte permiso, y se queda encendido para todos los que abras. Déjalo apagado: la oficina se ve igual, y solo tú decides qué se borra o se envía.

## En resumen

- Cada terminal de Claude Code es un muñeco en una oficina.
- Gratis, como extensión de VS Code o con `npx pixel-agents`.
- Su mayor utilidad es ver quién te está esperando.
- No hace el trabajo: solo lo enseña.
- Deja **Skip Permissions** apagado.

---

## Fuentes

- Pixel Agents: [repositorio y documentación](https://github.com/pixel-agents-hq/pixel-agents) (funciones, requisitos, instalación y ajustes).

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
