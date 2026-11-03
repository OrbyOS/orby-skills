# Monta tu Jarvis con nueve piezas

Un asistente personal que te escribe por Telegram, recuerda quién eres y hace cosas por ti no es un solo programa: son nueve piezas. Si las separas, puedes elegir y cambiar cada una. Aquí tienes cuáles son, con Hermes Agent como cuerpo, y el orden para montarlas.

Revisada el 3 de noviembre de 2026 con la documentación de Hermes Agent (enlaces al final). Ese día tenía 260k estrellas en GitHub y licencia MIT. El reparto en nueve piezas es nuestro, y el orden, una recomendación.

---

## Las nueve piezas

| Pieza | Qué es | Con qué |
| --- | --- | --- |
| **1. Casa** | Donde vive, encendido | Tu ordenador, o un servidor si quieres que no se apague (capítulo 3.7) |
| **2. Cuerpo** | El programa que lo une todo | [Hermes Agent](https://github.com/NousResearch/hermes-agent) |
| **3. Cerebro** | El modelo que piensa | El que elijas, con `hermes model` |
| **4. Quién es y quién eres** | Su personalidad y lo que debe saber de ti | `SOUL.md` y `USER.md` |
| **5. Memoria** | Lo que recuerda entre conversaciones | `MEMORY.md` y la búsqueda en sesiones pasadas |
| **6. Habilidades** | Cómo se hace cada tarea | Skills (capítulo 2.7) |
| **7. Herramientas** | Lo que puede tocar | `hermes tools` y conectores MCP (capítulo 3.13) |
| **8. Canales** | Por dónde le hablas | Telegram, WhatsApp, Discord, Slack o Signal |
| **9. Cara** | Cómo se ve | La terminal o Hermes Desktop |

## Móntalo en este orden

### 1. Casa y cuerpo

Empieza en tu ordenador. En Mac, Linux o WSL2:

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

En Windows, con PowerShell:

```powershell
iex (irm https://hermes-agent.nousresearch.com/install.ps1)
```

Cierra la terminal, vuelve a abrirla y ejecuta el asistente de configuración. Si ya usas Claude Code, te ofrece importar lo que tengas.

```bash
hermes setup
```

### 2. Cerebro

```bash
hermes model
```

Elige proveedor y modelo. Lo puedes cambiar cuando quieras, sin tocar nada más. Un agente que funciona todo el día puede gastar mucho, así que mira el precio y pon un límite en tu proveedor.

### 3. Quién es y quién eres

Abre `hermes` y dile esto:

```text
Hazme una entrevista, de dos en dos preguntas, para saber quién soy, a qué me dedico y cómo quiero que trabajes conmigo. Después propón tu SOUL.md y mi USER.md. Enséñamelos antes de guardarlos, y no guardes contraseñas ni datos de clientes.
```

Si ya tienes tu «Sobre mí» del capítulo 0.6, pégaselo. `USER.md` y `MEMORY.md` son breves a propósito, unas pocas líneas cada uno: lo esencial.

### 4. Memoria

No hay que montar nada. Hermes guarda lo que aprende y busca en sesiones anteriores. Dos consejos de su documentación: abre una sesión nueva con `/new` al terminar una tarea, y revisa de vez en cuando qué ha apuntado.

### 5. Habilidades

Las primeras, las que ya conoces: tus skills de Claude Code se pueden importar. Hermes además crea las suyas después de las tareas complicadas, así que léelas de vez en cuando. Si te ha hecho falta corregirle algo, pídele que lo apunte.

### 6. Herramientas

Enciende solo lo que vayas a usar con `hermes tools`. Empieza por leer y añade poco a poco.

```bash
hermes tools
```

### 7. Canales

Para hablarle desde el móvil, crea un bot en Telegram y conéctalo:

```bash
hermes gateway setup
hermes gateway start
```

Haz que solo te responda a ti. Quien pueda escribirle puede pedirle cosas.

### 8. Una tarea real, a una hora

Hermes tiene tareas programadas en lenguaje normal. Pruébalo con algo que no toque nada:

```text
Cada mañana a las 8, mándame por Telegram lo que tengo hoy en el calendario y lo más urgente de mi correo. No envíes ni cambies nada.
```

### 9. La cara

Cuando el resto funcione, instala [Hermes Desktop](https://hermes-agent.nousresearch.com/) si prefieres una ventana. Es lo último: es lo que menos importa y lo que más entretiene.

> [!CAUTION]
> **Un agente que lee tu correo y puede actuar es un riesgo real.** Cualquiera puede mandarte un correo con instrucciones escondidas. Enviar, pagar, borrar o publicar, siempre con tu aprobación, y sin dejarle tus contraseñas.

## En resumen

- Casa, cuerpo, cerebro, quién es, memoria, habilidades, herramientas, canales y cara.
- Hermes Agent es el cuerpo, y el resto se puede cambiar.
- Monta en este orden, y deja la cara para el final.
- Una tarea real, a una hora, que no toque nada.
- Lo irreversible, siempre con tu aprobación.

---

## Fuentes

- Hermes Agent: [repositorio](https://github.com/NousResearch/hermes-agent) (funciones, instalación, modelos, canales y tareas programadas), [personalidad y SOUL.md](https://hermes-agent.nousresearch.com/docs/user-guide/features/personality), [memoria](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory) y [conectores MCP](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp).

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
