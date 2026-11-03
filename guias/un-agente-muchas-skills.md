# Un solo agente y un manual por tarea

Dos personas de Anthropic, en la charla «Don't Build Agents, Build Skills Instead», defienden algo que ahorra mucho trabajo: no construyas un agente nuevo para cada cosa. Un agente general ya es listo. Lo que le
falta es saber cómo se hace tu trabajo, y eso se le da con skills. Aquí tienes la idea y un método para escribir la primera.

Revisada el 3 de noviembre de 2026 con la [página de la charla](https://www.ai.engineer/talks/CEvIs9y1uog-agent-skills), de 16 minutos, en el congreso AI Engineer Code de 2025. El método de abajo es nuestro, a partir de esa idea.

---

## La idea de la charla

Su ejemplo: para hacer tu declaración de la renta, ¿prefieres un genio de las matemáticas que tenga que deducir toda la normativa desde cero o a un asesor con años de experiencia? Hoy, un agente es como ese genio. **No le falta inteligencia: le falta oficio.**

| Pieza | Qué aporta | En tu trabajo |
| --- | --- | --- |
| **El agente** | Razona y mantiene la conversación | Claude |
| **El entorno** | Archivos y poder ejecutar cosas | Tu ordenador con Claude Code |
| **Los conectores (MCP)** | A qué puede llegar | Correo, calendario, tu base de datos (capítulo 3.13) |
| **Las skills** | Qué sabe hacer | «Así preparamos una propuesta» |

Una skill es solo una carpeta: un archivo `SKILL.md` con las instrucciones y, si hacen falta, plantillas y programas. El agente solo lee primero el nombre y la descripción, y abre el resto cuando lo necesita. Por eso puedes tener muchas sin llenarle la cabeza.

## Por qué te importa

- **No mantienes diez agentes.** Mantienes uno y una biblioteca que crece.
- **Lo aprendido se queda.** Corriges una vez, lo apuntas en el manual y vale para siempre.
- **Lo reparte tu equipo.** Es una carpeta: se copia y se comparte.

Usa varios agentes solo cuando haga falta de verdad, por ejemplo para que uno revise el trabajo de otro (capítulo 4.3).

## Escribe tu primer manual en tres pasos

Elige una tarea que repitas cada semana y que sepas hacer bien. Si dudas, usa las preguntas del capítulo 2.1.

### 1. La entrevista: que te saque lo que sabes

```text
Quiero convertir esta tarea en una skill: [tarea]. Hazme una entrevista, de dos en dos preguntas, para sacar cómo la hago yo: por dónde empiezo, qué decisiones tomo y según qué, qué errores son los típicos y qué no hago
nunca. Pídeme dos ejemplos reales, uno bueno y uno malo. No escribas nada hasta que no te quede ninguna duda.
```

### 2. La caja de herramientas: qué necesita

```text
Con lo que te he contado, lista lo que necesita esta tarea: documentos que debe leer, programas o conectores que debe usar y plantillas. De cada cosa, dime si ya la tengo o si falta. Lo que se haga siempre igual, propón convertirlo en una plantilla o un pequeño programa, para que no lo rehaga cada vez.
```

### 3. La lista de terminado: cómo sabe que acabó

```text
Escribe una lista de comprobaciones de sí o no para saber si esta tarea está bien hecha, a partir de mis dos ejemplos. Marca las graves. El agente tiene que repasarla antes de entregarme nada, y decirme lo que no ha podido comprobar.
```

### Y júntalo

```text
Con la entrevista, la caja de herramientas y la lista de terminado, crea una skill en ~/.claude/skills/[nombre]/. En la descripción, di exactamente cuándo debe usarse. Que el SKILL.md sea corto y deje los detalles en archivos aparte. Pruébala con una tarea real y enséñame el resultado antes de darla por buena.
```

El plugin `skill-creator` lo hace más cómodo (capítulo 2.5).

## Cómo saber que va bien

La charla insiste en tratar las skills serias como programas: se prueban, se versionan y se mide si funcionan. A tu escala, basta con dos preguntas:

- **¿Se activa cuando toca?** Pídele la tarea con palabras normales, sin nombrar la skill.
- **¿El resultado pasa tu lista?** Si no pasa, no parchees el resultado: corrige la skill.

> [!CAUTION]
> Una skill puede ejecutar programas. Lee las de otras personas antes de instalarlas (capítulo 2.1), y no guardes contraseñas dentro.

## En resumen

- A un agente no le falta inteligencia, le falta oficio. Eso se le da con skills.
- Un agente general y un manual por tarea, no un agente por tarea.
- Tres pasos: entrevista, caja de herramientas y lista de terminado.
- Prueba si se activa sola y si el resultado pasa la lista.
- Cada corrección, a la skill.

---

## Fuentes

- Anthropic, en AI Engineer Code 2025: [«Don't Build Agents, Build Skills Instead»](https://www.ai.engineer/talks/CEvIs9y1uog-agent-skills) (hemos usado el resumen de esa página, no la grabación completa).

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
