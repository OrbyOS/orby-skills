# Astryx: el sistema de diseño de Meta, gratis y pensado para tu IA

Meta ha publicado Astryx, el sistema de diseño que ha crecido dentro de la empresa durante ocho años: más de 150 componentes accesibles (botones, formularios, tablas, menús…), con modo oscuro y temas. Está pensado para que una persona y una IA lo usen igual, desde la misma documentación.

Revisada el 13 de noviembre de 2026.

---

## Para quién es

Para apps hechas con React (por ejemplo, las que te monta Claude Code con Next.js o Vite).

## Cómo instalarlo

En tu proyecto:

```
npm install @astryxdesign/core @astryxdesign/theme-neutral @stylexjs/stylex
npm install -D @astryxdesign/cli
```

Y para que cualquier agente lo conozca:

```
npm i -g @astryxdesign/cli
```

Después pídele a Claude Code: «Usa Astryx para la pantalla de ajustes». Puede consultar la documentación con `astryx docs global`.

## Lo que conviene saber

- Todavía está en beta: puede cambiar.
- Solo sirve para React.
- Gratis y de código abierto (MIT): github.com/meta/astryx. Hay una zona de pruebas en astryx.atmeta.com.
