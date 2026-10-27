---
name: reglas-de-un-agente
description: Ayuda a escribir las reglas de un agente de IA para un negocio (qué objetivo tiene, qué recibe, qué puede hacer solo, qué necesita aprobación, qué no hace nunca y cuándo ha terminado) y lo deja creado como subagente de Claude Code, listo para usar. Úsala cuando alguien quiera montar su primer agente, convertir una tarea repetida en un agente, escribir las instrucciones de un agente o un subagente, o cuando un agente que ya tiene hace cosas que no debería.
---

# Reglas de un agente

Un chat responde cuando le preguntas. Una automatización repite siempre lo mismo. Un agente tiene un objetivo y
decide los pasos para llegar a él. Por eso necesita dos cosas que un chat no: reglas claras y alguien que revise lo
importante. Esta skill escribe esas reglas con el usuario y crea el agente.

## Paso 1. ¿Hace falta un agente?

Antes de nada, comprueba que es un trabajo de agente. Pregunta qué tarea quiere darle y aplica esto:
- Si siempre se hace igual, con los mismos pasos y los mismos datos, es una **automatización**: díselo y propón
  hacerla con una herramienta de automatización o con un script. No sigas con el agente si está de acuerdo.
- Si es una pregunta suelta de vez en cuando, basta con un **chat**.
- Si hay que mirar una situación, decidir qué hacer y prepararlo, es un **agente**. Sigue.

## Paso 2. Las preguntas

Haz estas preguntas de dos en dos. Pide ejemplos reales siempre que puedas: un ejemplo vale más que una norma.

1. **Objetivo.** ¿Qué tiene que conseguir, en una frase y con algo que se pueda comprobar? («Que ningún cliente
   pase más de una semana sin respuesta», no «mejorar la comunicación».)
2. **Cuándo trabaja.** ¿Cuándo se le llama? (cada lunes, cuando llega un correo, cuando tú se lo pides)
3. **Qué recibe.** ¿Qué información necesita y dónde está? (una carpeta, una hoja de cálculo, un documento de
   contexto del negocio)
4. **Pasos.** ¿Cómo lo harías tú? Que te lo cuente como si se lo explicara a alguien nuevo.
5. **Lo que puede hacer solo.** Leer, ordenar, resumir, preparar borradores…
6. **Lo que necesita tu OK.** Todo lo que sale hacia fuera o cuesta dinero: enviar, publicar, pagar, borrar,
   cambiar un precio.
7. **Lo que no hace nunca.** Aunque parezca buena idea.
8. **Cuándo ha terminado.** Cómo es una entrega buena: qué formato, qué tiene que incluir.
9. **Un ejemplo bueno y uno malo** de lo que tendría que entregar.
10. **Cuando no sabe algo.** ¿Pregunta, lo marca como pendiente o lo deja? (Por defecto: lo marca y pregunta.)

Si no tiene claro qué dejarle hacer solo, aplica este criterio y díselo: solo lo que se puede deshacer y lo que
pasa por él antes de llegar a nadie.

## Paso 3. Escribir las reglas

Usa `plantilla-agente.md` (en esta carpeta). Reglas al escribir:
- Frases cortas y en imperativo: «Lee…», «Prepara…», «No envíes…».
- Cada «necesita tu OK» y cada «nunca» va en su lista, no escondido en un párrafo.
- Los ejemplos del usuario van tal cual, marcados como ejemplo bueno y ejemplo malo.
- Nada que el usuario no haya dicho. Lo que falte, a «Pendiente».
- Al final, siempre, la sección «Lo que he aprendido», vacía al principio: ahí se apunta cada corrección como una
  regla nueva, con fecha.

## Paso 4. Crear el agente

Pregunta dónde lo va a usar:

- **En Claude Code** (por defecto): créalo como subagente en `.claude/agents/<nombre>.md` dentro de su carpeta de
  trabajo (o en `~/.claude/agents/` si lo quiere en todos sus proyectos). Formato:

  ```markdown
  ---
  name: seguimiento-clientes
  description: Revisa qué clientes llevan más de una semana sin respuesta y prepara un borrador para cada uno. Úsalo los lunes o cuando se pida un repaso de seguimientos.
  tools: Read, Glob, Grep, Write
  ---

  (las reglas del paso 3)
  ```

  El `name` va en minúsculas y con guiones. La `description` dice qué hace y cuándo usarlo: Claude la lee para
  decidir cuándo llamarlo. En `tools`, solo las herramientas que necesita: si no tiene que ejecutar comandos, sin
  `Bash`; si no tiene que escribir archivos, sin `Write`. Menos herramientas, menos sorpresas.

- **En otra herramienta** (Claude.ai, otra IA, una plataforma de agentes): entrega las reglas en un `.md` para
  pegar como instrucciones.

## Paso 5. Probarlo

No lo des por bueno sin una prueba:
1. Pídele que haga su trabajo con un caso de ejemplo (datos de prueba, no de clientes reales si no hace falta).
2. Comprueba que no hace nada de la lista de «necesita tu OK» sin preguntar y nada de la lista de «nunca».
3. Compara lo que entrega con el ejemplo bueno.
4. Si falla, corrige la regla que falta o que se entiende mal, y apúntalo en «Lo que he aprendido».

Explícale al usuario cómo mejorarlo con el uso: cada vez que corrija algo, que le diga a Claude «apunta esto como
regla en el agente»; la regla va a «Lo que he aprendido» y el agente no repite el error.

## Revisión antes de entregar

- ¿El objetivo se puede comprobar?
- ¿Todo lo que sale hacia fuera, cuesta dinero o no se puede deshacer está en «necesita tu OK» o en «nunca»?
- ¿Tiene un ejemplo bueno de entrega?
- ¿Las herramientas son solo las que necesita?
