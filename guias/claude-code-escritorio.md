# Claude Code en el escritorio, sin saber programar

Claude Code es Claude trabajando en tu ordenador: con tus archivos, tus carpetas y tus herramientas. Antes se usaba
desde la terminal; ahora tiene su propia pestaña, **Code**, en la aplicación de Claude para el ordenador, y se maneja
con botones como cualquier otra aplicación. Es donde funcionan las skills de este manual que trabajan con archivos,
como la de editar reels.

Revisada el 29 de octubre de 2026 con la documentación oficial de Claude Code (enlaces al final). Algunas funciones
están en beta y llegan poco a poco: puede que todavía no las veas.

---

## 1. Lo básico de la aplicación

- **Sesiones:** cada conversación de la pestaña Code es una sesión, con su historial y su carpeta de trabajo.
- **+ New** (o Cmd + N en el Mac, Ctrl + N en Windows): abre una sesión nueva.
- **Customize:** conectores, skills y plugins, todo en un mismo sitio.
- **El uso:** junto al selector de modelo (o en la tarjeta **Context** del panel de la sesión) ves cuánto llevas de
  la conversación; pulsándolo, cuánto llevas de tu plan, que es el mismo para todos los sitios donde usas Claude Code.
- **`/context`:** escrito en la caja de mensajes, te da el detalle de qué ocupa la conversación.
- **`/compact`:** resume la conversación para liberar espacio. Claude lo hace solo cuando se llena, pero puedes
  adelantarlo cuando cambias de tema.

## 2. Sesiones en la nube y verlas desde el móvil

- **Sesiones en la nube:** trabajan en los servidores de Anthropic y **siguen aunque cierres la aplicación o apagues
  el ordenador**. Las ves en claude.ai/code o en la aplicación de Claude del móvil. Cuentan para los límites de tu
  plan, sin coste aparte.
- **Remote Control:** para seguir desde el móvil una sesión que trabaja en tu ordenador, activa su interruptor
  **Remote Control** o escribe `/remote-control` en ella. Aparecerá en claude.ai/code y en las aplicaciones de Claude
  donde tengas tu cuenta abierta. En los ajustes puedes hacer que todas las sesiones nuevas se conecten solas.

## 3. Trabajar con varias cosas a la vez

- **Chat lateral:** Cmd + ; en el Mac (Ctrl + ; en Windows), o `/btw`. Abre una conversación aparte que puede leer
  la principal sin meterse en ella. Útil para preguntar algo sin desviar la tarea. No se guarda al cerrar la
  aplicación.
- **Pantalla dividida:** mantén Option (Alt en Windows) y haz clic en una sesión de la barra lateral, o clic derecho
  → **Open in** → **Split view**. Para sacar una sesión de la pantalla dividida: Cmd + Ctrl + W en el Mac
  (Ctrl + Alt + W en Windows).

## 4. Proyectos de Claude Code: un coordinador y varios hilos

Son distintos de los proyectos del chat (capítulo 1.2). Aquí, un proyecto es **una conversación en la que Claude hace
de coordinador**: le mandas el trabajo y él abre un **hilo** por tarea, que trabaja en paralelo en la nube y le
informa al terminar.

- **Instrucciones y memoria del proyecto:** lo que le dices una vez llega a todos los hilos. Si le pides que recuerde
  una decisión, la apunta en la memoria del proyecto y los hilos siguientes la tienen.
- **Overview:** el panel que te dice qué hilos han terminado, cuáles esperan tu respuesta y cuáles siguen trabajando.
- **Library:** la pestaña con los archivos que subes y los que producen los hilos.
- **No solo para código:** puedes subir documentos (contratos, exportaciones de soporte) y pedir informes; cada hilo
  entrega su resultado como archivo en Library.
- **Disponibilidad:** beta pública en los planes **Pro y Max**, llegando poco a poco. No están en Team ni Enterprise.
  Si no ves **Projects** en la barra lateral, mira en **More**.

> [!IMPORTANT]
> Un proyecto gasta tu plan más deprisa que una sesión, porque varios hilos trabajan a la vez. Al principio, pídele
> que te proponga los hilos antes de empezarlos y que lleve pocos a la vez.

## 5. Comandos de diagnóstico

| Comando | Para qué |
| --- | --- |
| `/doctor` | Revisa la instalación y la configuración, y arregla lo que puede |
| `/doctor prompt-audit` | Revisa tus archivos de instrucciones: indicaciones pensadas para modelos antiguos, referencias a archivos que no existen o archivos que se contradicen. No cambia nada hasta que aceptas las propuestas |
| `/skill-doctor` | Te dice cuánto cuesta y cuánto se usa cada una de tus skills, para decidir cuáles apagar |

`/doctor prompt-audit` pide Claude Code 2.1.283 o posterior, y `/skill-doctor`, la 2.1.252 o posterior. Escribe
`/status` para ver tu versión.

## 6. Mods: cambiar cómo se ve y cómo se comporta

Un mod es un plugin que cambia la apariencia y el comportamiento de Claude Code: puede añadir un panel, cambiar
partes de la interfaz, añadir un comando o intervenir antes de que Claude use una herramienta (por ejemplo, para
pedirte confirmación antes de un comando arriesgado).

- **Se instalan como un plugin**, desde un marketplace: `/plugin install nombre@marketplace`.
- **Puedes pedirle a Claude que te escriba uno**, describiendo lo que quieres.
- **Funcionan** en la pestaña Code de la aplicación de escritorio, en la terminal y en la extensión de VS Code.

> [!CAUTION]
> Un mod es código que se ejecuta con tus permisos: puede leer y escribir tus archivos, leer tus claves y actuar sin
> preguntarte. Instala solo mods de autores en los que confíes, y antes de instalar uno, revisa qué hace con
> `claude plugin validate`.

## 7. En resumen

- La pestaña Code de la aplicación de escritorio es Claude Code con botones.
- Las sesiones en la nube siguen aunque apagues; Remote Control te deja seguirlas desde el móvil.
- Los proyectos de Claude Code coordinan varios hilos en paralelo (beta, Pro y Max).
- `/doctor` revisa tu instalación; `/skill-doctor`, tus skills.
- Mods, solo de fuentes de confianza.

---

## Fuentes

- Claude Code: [aplicación de escritorio](https://code.claude.com/docs/en/desktop),
  [proyectos](https://code.claude.com/docs/en/claude-projects),
  [mods](https://code.claude.com/docs/es/plugins/mods/overview),
  [comandos](https://code.claude.com/docs/en/commands) y [skills](https://code.claude.com/docs/en/skills).

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
