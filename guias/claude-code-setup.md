# Claude Code Setup y los 40 plugins oficiales de Anthropic

Claude Code Setup es un plugin de Anthropic que mira tu proyecto y te dice qué automatizaciones le faltan: hooks, skills, servidores MCP y subagentes. Solo lee: no cambia ningún archivo, así que tú decides qué aplicar. Aquí tienes cómo instalarlo, el primer mensaje y la lista de los 40 plugins que publica Anthropic en su marketplace oficial.

Revisada el 7 de noviembre de 2026 con el repositorio `anthropics/claude-plugins-official` (enlaces al final). Ese día el marketplace tenía 317 plugins: 40 hechos por Anthropic y el resto de empresas y de la comunidad. Necesitas Claude Code (capítulo 3.2).

---

## 1. Instálalo

Dentro de Claude Code, pega:

```text
/plugin install claude-code-setup@claude-plugins-official
```

Si te dice que no encuentra el marketplace, añádelo antes con `/plugin marketplace add anthropics/claude-plugins-official`.

## 2. Primer mensaje

Abre Claude Code en la carpeta de tu proyecto y escribe:

```text
Recomiéndame automatizaciones para este proyecto. Dime qué me sobra y qué me falta, y por qué. No cambies nada: primero quiero ver la lista.
```

Te recomienda una o dos cosas de cada tipo:

- **Hooks:** acciones que se hacen solas, como ordenar el código al guardar o bloquear archivos con claves.
- **Skills:** conocimiento empaquetado para una tarea, como diseñar páginas o planificar.
- **Servidores MCP:** conexiones con otras herramientas, como la documentación al día o un navegador.
- **Subagentes:** revisores especializados en seguridad, rendimiento o accesibilidad.
- **Comandos:** atajos como `/test` o `/pr-review`.

**Lo que importa:** que te lo recomiende no quiere decir que te haga falta. Pide que te explique cada uno en una frase y aplica solo lo que entiendas.

## 3. Los 40 plugins de Anthropic

| Plugin | Para qué |
| --- | --- |
| `claude-code-setup` | Recomienda hooks, skills, MCP y subagentes para tu proyecto |
| `claude-md-management` | Revisa y mantiene al día tu CLAUDE.md, la memoria del proyecto |
| `skill-creator` | Crea skills nuevas, las mejora y mide si funcionan |
| `frontend-design` | Interfaces web con diseño cuidado, que no parecen hechas por IA |
| `playground` | Páginas interactivas de un solo archivo para explorar ideas |
| `feature-dev` | Desarrollo de una función con agentes que exploran, diseñan y revisan |
| `code-review` | Revisión automática de cambios con varios agentes |
| `pr-review-toolkit` | Revisores de comentarios, pruebas, errores y calidad |
| `code-simplifier` | Simplifica el código reciente sin cambiar lo que hace |
| `code-modernization` | Plan para modernizar un proyecto antiguo, con `/modernize` |
| `commit-commands` | Comandos para guardar cambios, subirlos y abrir revisiones en git |
| `claude-security` | Busca fallos de seguridad en tu propio código |
| `security-guidance` | Avisos de seguridad mientras Claude escribe código |
| `hookify` | Crea hooks a partir de reglas escritas en texto |
| `ralph-loop` | Claude repite la misma tarea viendo lo anterior hasta terminarla |
| `session-report` | Informe de lo que gastan tus sesiones: tokens, skills y subagentes |
| `receipts` | Resumen de lo que has hecho con Claude Code y en qué proyectos |
| `project-artifact` | Página de estado de un proyecto, que se puede compartir |
| `champion-kit` | Para quien enseña Claude Code en su empresa: talleres y madurez |
| `explanatory-output-style` | Claude explica por qué elige cada cosa mientras trabaja |
| `learning-output-style` | Modo aprendizaje: te pide que escribas tú partes del código |
| `plugin-dev` | Kit para crear tus propios plugins |
| `mcp-server-dev` | Guía para diseñar y construir servidores MCP |
| `mcp-tunnels` | Conectar Claude a un servidor MCP privado |
| `agent-sdk-dev` | Kit para trabajar con el Agent SDK de Claude |
| `math-olympiad` | Problemas de matemáticas de competición, con verificación |
| `math-proof` | Demostraciones matemáticas largas, paso a paso |
| `cwc-makers` | Prepara el dispositivo Cardputer del programa Code with Claude Makers |
| `pyright-lsp` | Ayuda de código para Python |
| `typescript-lsp` | Ayuda de código para TypeScript y JavaScript |
| `gopls-lsp` | Ayuda de código para Go |
| `rust-analyzer-lsp` | Ayuda de código para Rust |
| `jdtls-lsp` | Ayuda de código para Java |
| `kotlin-lsp` | Ayuda de código para Kotlin |
| `swift-lsp` | Ayuda de código para Swift |
| `csharp-lsp` | Ayuda de código para C# |
| `clangd-lsp` | Ayuda de código para C y C++ |
| `php-lsp` | Ayuda de código para PHP |
| `ruby-lsp` | Ayuda de código para Ruby |
| `lua-lsp` | Ayuda de código para Lua |

Los que acaban en `-lsp` solo te sirven si programas en ese lenguaje. Si no programas, empieza por `claude-code-setup`, `claude-md-management` y `skill-creator`.

## Lo que conviene saber

- Que estén en el marketplace oficial no quiere decir que Anthropic responda de todos: los de otras empresas son suyos. Anthropic pide revisar un plugin antes de instalarlo.
- Cada plugin añade instrucciones a tu sesión. Instala pocos y quita los que no uses con `/plugin`.

## Fuentes

- [Marketplace oficial de plugins de Claude Code](https://github.com/anthropics/claude-plugins-official).
- [Claude Code Setup en el marketplace](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-code-setup).

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
