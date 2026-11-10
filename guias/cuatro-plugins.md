# Cuatro plugins para Claude Code que cambian lo que puede hacer

Con un plugin, Claude Code deja de darte instrucciones y lo hace él: crear tu base de datos, publicar tu web, repartir el trabajo entre agentes o abrir tu web en Chrome para ver qué falla. Aquí tienes cuatro, con su instalación y un primer mensaje.

Revisada el 3 de noviembre de 2026 con la documentación de cada uno (enlaces al final). Las estrellas son de ese día. Necesitas Claude Code (capítulo 3.2).

| Plugin | Para qué | De quién | Licencia |
| --- | --- | --- | --- |
| **Supabase** | Base de datos, cuentas de usuario y archivos | Supabase (su conector, 3k estrellas) | Apache-2.0 (conector) |
| **Vercel** | Publicar tu web y ver qué falla | Vercel (326 estrellas) | Mira su repositorio |
| **Oh My Claude Code** | Varios agentes trabajando a la vez | Proyecto de la comunidad (40,5k estrellas) | MIT |
| **Chrome DevTools MCP** | Claude abre tu web en Chrome y la revisa | Equipo de Chrome (54,7k estrellas) | Apache-2.0 |

---

## 1. Supabase: la base de datos sin saber de bases de datos

Trae su conector y sus skills para consultar tu base de datos, cambiarla y publicar funciones.

```bash
npx plugins add supabase-community/supabase-plugin
```

Primer mensaje:

```text
Conéctate a mi proyecto de Supabase en modo solo lectura. Explícame qué tablas tengo y dime si hay algún dato de usuarios al que se pueda llegar sin permiso. No cambies nada.
```

**Lo que importa:** usa un proyecto de pruebas y limítalo a un solo proyecto y en modo lectura si hay datos reales. Supabase lo recomienda así y pide revisar cada acción, porque un texto de un cliente podría colarle instrucciones.

## 2. Vercel: de tu carpeta a internet

Le da a Claude el conocimiento de Vercel y comandos para publicar. Necesita Node.js 18 o posterior y [Bun](https://bun.sh).

```bash
npx plugins add vercel/vercel-plugin
```

Primer mensaje:

```text
Mira este proyecto y dime si está listo para publicar en Vercel. Comprueba que no suba claves. Publica una versión de prueba, no la definitiva, y dame el enlace.
```

**Lo que importa:** Vercel te puede cobrar según el uso. Mira el capítulo 3.7 antes de abrir algo al público.

## 3. Oh My Claude Code: un equipo de agentes

Reparte una tarea entre varios agentes especializados. Pega estas líneas una a una:

```text
/plugin marketplace add https://github.com/Yeachan-Heo/oh-my-claudecode
/plugin install oh-my-claudecode
/omc-setup
```

Primer mensaje:

```text
/autopilot Haz una página sencilla con [lo que necesitas]. Antes de construir, enséñame el plan y espera a que te diga que sí.
```

También tiene `/team 3:executor "tarea"` para poner a tres agentes a la vez, y `/deep-interview` para que te pregunte antes de empezar.

**Lo que importa:** varios agentes gastan tu plan mucho más deprisa. Empieza por una tarea pequeña y mira cuánto consume.

## 4. Chrome DevTools MCP: que vea lo que ves tú

Claude abre tu web en Chrome, hace clics, lee los errores y mide lo que tarda. Es del equipo de Chrome. Necesita Node.js.

```text
/plugin marketplace add ChromeDevTools/chrome-devtools-mcp
/plugin install chrome-devtools-mcp@chrome-devtools-plugins
```

Primer mensaje:

```text
Abre [dirección de tu web] y prueba el formulario con datos inventados, sin enviarlo. Dime qué errores salen en la consola, qué tarda más en cargar y cómo se ve en móvil. No cambies nada.
```

**Lo que importa:** puede ver y cambiar todo lo que haya en ese navegador, según avisa su documentación. No lo uses con tus cuentas abiertas. Google recoge estadísticas de uso por defecto: su documentación explica cómo apagarlo con `--no-usage-statistics`.

---

## Por cuál empiezo

- **Tienes una web y algo falla:** Chrome DevTools.
- **Vas a publicar tu primera app:** Vercel, y Supabase si necesita guardar datos.
- **Ya usas Claude Code a diario y se te queda corto:** Oh My Claude Code.

Instala uno cada vez. Cada plugin añade cosas que Claude tiene presentes, y lee antes lo que instalas (capítulo 2.1).

## En resumen

- Supabase para los datos, Vercel para publicar, Oh My Claude Code para repartir y Chrome DevTools para comprobar.
- En cada uno, empieza con un mensaje que no cambie nada.
- Con datos reales, solo lectura y un único proyecto.
- Varios agentes gastan mucho más.

---

## Fuentes

- Supabase: [plugin](https://supabase.com/docs/guides/ai-tools/plugins) y [conector y seguridad](https://supabase.com/docs/guides/getting-started/mcp).
- Vercel: [repositorio del plugin](https://github.com/vercel/vercel-plugin) y [documentación](https://www.vercel.com/docs/agent-resources/vercel-plugin).
- [Oh My Claude Code](https://github.com/Yeachan-Heo/oh-my-claudecode) y [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp).

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
