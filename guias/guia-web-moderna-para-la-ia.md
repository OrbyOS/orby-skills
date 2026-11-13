# Modern Web Guidance: la guía de Google, Microsoft y Mozilla para que la IA haga webs

Los equipos de Chrome, Edge, Firefox y MDN han publicado una guía gratuita para agentes de programación como Claude Code. Le enseña a hacer webs con lo que los navegadores ya traen de serie, en lugar de código viejo y pesado.

Revisada el 13 de noviembre de 2026.

---

## Qué le enseña a tu IA

- **250 funciones modernas** de la web: maquetación, HTML y JavaScript.
- **Más de 200 casos reales**: formularios, accesibilidad, velocidad, seguridad, inicio de sesión sin contraseña, menús y ventanas.
- A usar lo que el navegador ya trae, en vez de librerías pesadas.

## Cómo instalarla

```
npx modern-web-guidance@latest install
```

El asistente te pregunta en qué agente la quieres.

## Cómo probarla sin instalar

- Buscar cómo hacer algo: `npx modern-web-guidance@latest search "animar una ventana emergente"`
- Revisar tu web y ver qué está anticuado: `npx modern-web-guidance@latest legacy-scan .`

## Lo que conviene saber

- Es para quien hace webs o apps con IA; si usas un creador visual (Wix, Framer…), no te hace falta.
- Gratis y de código abierto (Apache 2.0): github.com/GoogleChrome/modern-web-guidance.
