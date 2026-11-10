# Cinco conectores que convierten a Claude en un equipo

Un conector le da a Claude una herramienta que no trae de serie: buscar en internet con fuentes, leer webs enteras,
mirar las métricas de tu web, manejar un navegador o trabajar dentro de tus aplicaciones. Esta guía explica cinco:
qué hace cada uno, para qué te sirve en un negocio, cómo conectarlo paso a paso y qué cuidar.

Revisada el 28 de octubre de 2026 en la documentación oficial de cada uno (enlaces al final). Los menús cambian a
menudo: si algo no está donde dice la guía, busca el nombre del conector en el directorio de Claude.

| Conector | Qué le da a Claude | Dónde funciona | Coste |
| --- | --- | --- | --- |
| Perplexity | Buscar en internet con fuentes e investigar a fondo | Claude (web y app) y Claude Code | De pago por uso |
| Firecrawl | Leer webs enteras y sacar datos ordenados | Claude (web y app) y Claude Code | Gratis hasta 1.000 créditos al mes |
| PostHog | Consultar las métricas de tu web o tu app | Claude (web y app) y Claude Code | Gratis con el plan gratuito de PostHog |
| Playwright | Manejar un navegador: entrar, hacer clic, rellenar | Claude Code y Claude Desktop, en tu ordenador | Gratis |
| Composio | Trabajar dentro de cientos de aplicaciones (correo, calendario, hojas, CRM…) | Claude (web y app) y Claude Code | Gratis hasta 100.000 acciones al mes |

## ¿Por cuál empiezo?

| Si lo que más te cuesta es… | Empieza por |
| --- | --- |
| Investigar y comprobar datos antes de escribir | Perplexity |
| Copiar a mano información de webs (la tuya o la de tu competencia) | Firecrawl |
| Saber qué pasa en tu web sin abrir paneles | PostHog |
| Probar tu web o tareas repetitivas en el navegador | Playwright |
| Pasar información de una aplicación a otra (correo, calendario, hojas) | Composio |

Uno a uno: conecta el primero, úsalo una semana y después añade el siguiente.

---

## Antes de empezar: cómo se añade un conector

**En Claude (web y app de escritorio):**
1. Ve a **Customize → Connectors** («Personalizar → Conectores» si lo tienes en español).
2. Si el conector está en el directorio, búscalo y pulsa **Connect**. Si no, pulsa **+ Add → Add custom connector**,
   escribe el nombre y pega la dirección del servidor que te da esta guía.
3. Inicia sesión en el servicio cuando te lo pida y revisa los permisos que te pide.
4. En cada conversación, el botón **+** junto a la caja de texto → **Connectors** enseña cuáles están activos.

Con el plan gratuito de Claude puedes añadir **un** conector personalizado. En los planes de equipo, los añade quien
administra la cuenta.

**En Claude Code (terminal):** cada conector se añade con un comando `claude mcp add …` que tienes en su apartado.
Después, dentro de Claude Code, escribe `/mcp` para iniciar sesión y comprobar que está conectado.

---

## Los que ya trae Claude: Gmail, Google Calendar y Google Drive

Antes de los cinco de esta guía, mira los que Claude ya trae para Google Workspace. Están en todos los planes y se
conectan iniciando sesión con tu cuenta de Google desde **Customize → Connectors**. En una conversación, el botón **+**
→ **Connectors** enciende o apaga cada uno.

| Conector | Lo que puede leer | Lo que puede hacer |
| --- | --- | --- |
| **Gmail** | Buscar y leer correos (los adjuntos, no) | Preparar borradores; enviar, responder o reenviar, con tu aprobación por defecto |
| **Google Calendar** | Tus calendarios y los compartidos, y buscar huecos comunes | Crear, cambiar y borrar eventos y responder a invitaciones |
| **Google Drive** | Buscar y leer documentos, hojas, presentaciones y PDF | Subir archivos y guardar en Drive lo que crea Claude; compartir, mover o borrar, con tu aprobación por defecto |

Además, hay conectores de Google Docs, Sheets y Slides para editar esos archivos en un panel junto a la conversación.

**Para qué en un negocio:** «¿Qué clientes me han escrito esta semana pidiendo presupuesto y a cuáles no he
contestado?», «Busca un hueco de una hora con Marta la semana que viene» o «Resume el contrato de [cliente] que está
en Drive». En los planes Team y Enterprise, quien administra la cuenta tiene que activarlos antes.

## 1. Perplexity: buscar con fuentes

**Qué hace.** Claude busca en internet a través de Perplexity y te devuelve respuestas con sus fuentes. Tiene cuatro
modos: búsqueda rápida, pregunta con búsqueda, investigación a fondo con citas y razonamiento paso a paso.

**Para qué en un negocio.**
- Antes de grabar sobre una novedad, comprobar qué ha pasado de verdad y quién lo dice.
- Preparar una reunión con un cliente: qué ha publicado, qué ha cambiado en su sector.
- Comprobar una cifra antes de ponerla en un post: de dónde sale y de qué año es.

**Cómo conectarlo.**
1. Crea una cuenta en la plataforma de la API de Perplexity (console.perplexity.ai) y añade una forma de pago.
   Para conectarte con tu cuenta necesitas ser administrador de una organización de la API que pueda pagar.
2. En Claude: **Add custom connector**, nombre `Perplexity`, dirección `https://api.perplexity.ai/mcp`. Inicia
   sesión con tu cuenta de Perplexity.
3. En Claude Code:
   ```bash
   claude mcp add --transport http perplexity https://api.perplexity.ai/mcp
   ```
   y luego `/mcp` para iniciar sesión.

**Cuidados.**

> [!IMPORTANT]
> **Es aparte de Perplexity Pro.** La suscripción de la app no cubre la API: cada búsqueda se cobra a tu cuenta de la
> API. Como referencia, la búsqueda cuesta 5 $ por cada 1.000 consultas (1 $ en el modo rápido); la investigación a
> fondo cuesta más. Pon un límite de gasto en la consola.

- Si usas una clave en vez de iniciar sesión, no la pegues en un chat ni la guardes en un archivo que compartas.

## 2. Firecrawl: leer webs enteras

**Qué hace.** Claude lee una página o una web completa y la convierte en texto limpio o en datos ordenados. También
puede buscar, navegar, hacer clic y rellenar formularios sencillos.

**Para qué en un negocio.**
- Leer las páginas de venta de tu competencia y sacar una tabla con precios, garantías y lo que prometen.
- Pasar todas las preguntas frecuentes de tu web a un documento para entrenar tus respuestas.
- Revisar tu propia web y listar textos repetidos, enlaces rotos o páginas sin llamada a la acción.

**Cómo conectarlo.**
1. En Claude: búscalo en el directorio de conectores y pulsa **Connect**. Si no aparece, **Add custom connector**,
   nombre `firecrawl`, dirección `https://mcp.firecrawl.dev/v2/mcp-oauth`.
2. Inicia sesión en Firecrawl, elige tu equipo y acepta.
3. En Claude Code:
   ```bash
   claude mcp add --transport http firecrawl https://mcp.firecrawl.dev/v2/mcp-oauth
   ```

**Cuidados.**
- **Coste:** el plan gratuito trae 1.000 créditos al mes; el primero de pago, 19 $ al mes por 5.000 créditos. Leer
  una web entera gasta un crédito por página: pide a Claude que lea solo las páginas que necesitas.
- Esa dirección es para Claude, no para abrirla en el navegador.
- Lee solo webs públicas y respeta sus condiciones. Para datos personales de otras personas, no.

## 3. PostHog: tus métricas, en una pregunta

**Qué hace.** Si tu web o tu app usa PostHog para medir visitas, Claude consulta tus datos: cuánta gente entra, por
dónde se va, qué páginas convierten, qué errores salen. También puede gestionar ajustes como los interruptores de
funciones.

**Para qué en un negocio.**
- «¿Cuántos visitantes llegaron desde Instagram la semana pasada y cuántos se apuntaron?»
- «¿En qué paso de la página de reserva se va más gente?»
- Un resumen semanal de tu web sin abrir ningún panel.

**Cómo conectarlo.**
1. Necesitas una cuenta de PostHog con tu web conectada. El plan gratuito incluye un millón de eventos y 5.000
   grabaciones de sesión web al mes.
2. En Claude: búscalo en el directorio de conectores, pulsa **Connect** e inicia sesión en PostHog. La dirección, si
   la necesitas, es `https://mcp.posthog.com/mcp`.
3. En Claude Code:
   ```bash
   claude mcp add --transport http posthog https://mcp.posthog.com/mcp -s user
   ```
   La primera vez que lo uses te pedirá iniciar sesión.

**Cuidados.**
- Claude ve los datos de tu proyecto. Si en PostHog guardas correos o datos de clientes, piensa qué conversaciones
  abres con el conector activo.
- Puede cambiar cosas (por ejemplo, encender o apagar una función). Lee cada acción antes de aprobarla.

## 4. Playwright: un navegador que maneja Claude

**Qué hace.** Claude abre un navegador en tu ordenador y lo maneja: entra en páginas, hace clic, rellena formularios
y lee lo que ve. Lo hace leyendo la estructura de la página, no mirando capturas.

**Para qué en un negocio.**
- Probar tu propia web como lo haría un cliente: el formulario de contacto, la reserva o el pago de prueba.
- Comprobar cada semana que tus enlaces importantes funcionan.
- Sacar datos de una página que no tiene forma fácil de exportarlos (si es tuya o tienes permiso).

**Cómo conectarlo.** Funciona en tu ordenador, no en la web de Claude. Necesitas Node.js 18 o más reciente
(nodejs.org).
1. En Claude Code:
   ```bash
   claude mcp add playwright npx @playwright/mcp@latest
   ```
2. En Claude Desktop: **Settings → Developer → Edit Config** y añade esto a `claude_desktop_config.json`:
   ```json
   {
     "mcpServers": {
       "playwright": {
         "command": "npx",
         "args": ["@playwright/mcp@latest"]
       }
     }
   }
   ```
   Guarda y reinicia la app. La primera vez descarga el navegador.

**Cuidados.**

> [!CAUTION]
> **No es una barrera de seguridad:** lo que hace Claude con el navegador, lo hace en tu ordenador. No le dejes
> entrar en tu banco, tu correo o cuentas con datos de clientes.

- Es gratis y de código abierto (de Microsoft).
- Hay una herramienta que ejecuta código dentro del navegador: apruébala solo si sabes qué va a hacer.
- Usa páginas tuyas o con permiso. Muchas webs prohíben la automatización en sus condiciones.

## 5. Composio: Claude dentro de tus aplicaciones

**Qué hace.** Con un solo conector, Claude puede trabajar con cientos de aplicaciones: Gmail, Google Calendar, Google
Sheets, Slack, Notion, HubSpot, GitHub y muchas más. Conectas cada aplicación una vez y Claude puede leer y actuar
en ellas.

**Para qué en un negocio.**
- «Busca los correos de esta semana de clientes que no he contestado y prepárame un borrador para cada uno.»
- «Pasa las reservas de hoy del calendario a la hoja de seguimiento.»
- «Crea una tarea en Notion por cada persona que haya pedido información por la web.»

**Cómo conectarlo.**
1. Crea una cuenta en composio.dev (el plan gratuito no pide tarjeta).
2. En Claude: **Add custom connector**, nombre `Composio`, dirección `https://connect.composio.dev/mcp`. Pulsa **Add**
   e inicia sesión.
3. En Claude Code:
   ```bash
   claude mcp add --transport http composio https://connect.composio.dev/mcp
   ```
   y luego `/mcp` para iniciar sesión.
4. Desde Composio, conecta las aplicaciones que quieras usar, una a una.

Si ves guías antiguas que hablan de «Rube», era el nombre de su conector anterior: hoy se usa esta dirección.

**Cuidados.**

> [!CAUTION]
> **Es el más potente y el que más cuidado pide:** puede enviar correos, borrar archivos o cambiar datos en tus
> aplicaciones. Conecta solo las que necesites y, al principio, aprueba cada acción a mano. Nunca marques «permitir
> siempre» en acciones que envían, publican o borran.

- **Coste:** el plan gratuito trae 100.000 acciones al mes; el de pago empieza en 29 $ al mes.
- Revisa los permisos que pide cada aplicación al conectarla y quita los que no hagan falta.

---

## Cuidados para todos

- **Solo conectores de confianza.** Anthropic no revisa los conectores personalizados. Una web o un correo pueden
  esconder instrucciones para que Claude haga algo que no pediste: lee lo que va a hacer antes de aprobarlo.
- **Activa solo lo que usas.** En cada conversación, desde el botón **+**, apaga los conectores que no necesites.
- **Claves fuera del chat.** Si un conector te pide una clave, va en su sitio (la configuración del conector), nunca
  en un mensaje ni en un archivo que compartas.
- **Pon límites de gasto** en los que cobran por uso (Perplexity, Firecrawl, Composio de pago).
- **Datos de clientes:** antes de conectar algo que los contenga, decide qué puede ver Claude y qué no.

## Fuentes

- Claude: [conectores personalizados](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp)
  y [conectores de Google Workspace](https://support.claude.com/en/articles/10166901-use-google-workspace-connectors).
- Perplexity: [servidor MCP](https://docs.perplexity.ai/docs/getting-started/integrations/mcp-server) y [precios](https://docs.perplexity.ai/getting-started/pricing).
- Firecrawl: [Claude Desktop](https://docs.firecrawl.dev/quickstarts/claude-desktop), [servidor MCP](https://docs.firecrawl.dev/mcp-server) y [precios](https://www.firecrawl.dev/pricing).
- PostHog: [Claude Desktop](https://posthog.com/docs/model-context-protocol/claude-desktop), [Claude Code](https://posthog.com/docs/model-context-protocol/claude-code) y [precios](https://posthog.com/product-analytics/pricing).
- Playwright: [repositorio oficial de Microsoft](https://github.com/microsoft/playwright-mcp).
- Composio: [Claude](https://composio.dev/claude) y [precios](https://composio.dev/pricing).

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
