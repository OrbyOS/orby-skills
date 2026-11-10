# Una fábrica de agentes: planifican, construyen y revisan, y tú apruebas

Un agente solo se revisa mal a sí mismo: hace el trabajo, lo da por bueno y te lo entrega. La solución es la de
cualquier taller: uno planifica, otro construye y otro revisa sin haber construido nada. Tú apruebas el plan antes de
empezar y la entrega antes de darla por buena. No hace falta saber programar: se monta con Claude Code, pidiéndoselo
con los mensajes de esta guía, y sirve igual para una página web, una propuesta o el boletín de la semana.

Revisada el 1 de noviembre de 2026 con la documentación oficial de Claude Code (enlaces al final).

---

## Las tres condiciones

Tener varios agentes no te da una fábrica. Te la dan estas tres cosas:

| Condición | Qué quiere decir | Cómo se consigue aquí |
| --- | --- | --- |
| **Repetible** | Cada encargo pasa por los mismos pasos, lo lances hoy o dentro de un mes | Un solo comando, `/fabrica`, con el proceso escrito |
| **Cada paso deja rastro** | Puedes ver qué se planificó, qué se hizo, qué se revisó y quién lo aprobó | Una carpeta por encargo, con un archivo por paso |
| **Memoria del proyecto** | No explicas lo mismo cada vez, y un error corregido no vuelve | Un archivo, `CLAUDE.md`, que se lee en cada sesión |

## Lo que vas a montar

```text
mi-proyecto/
├── CLAUDE.md                  La memoria: qué es esto y sus reglas
├── .claude/
│   ├── agents/
│   │   ├── planificador.md    Hace el plan. No construye
│   │   ├── constructor.md     Hace el trabajo, siguiendo el plan
│   │   └── revisor.md         Comprueba. No puede cambiar nada
│   └── skills/
│       └── fabrica/SKILL.md   El proceso, con sus dos paradas
└── encargos/
    └── 2026-11-02-landing/    Un encargo: su rastro completo
        ├── 1-plan.md
        ├── 2-hecho.md
        ├── 3-revision.md
        └── 4-decision.md
```

## Lo que hace falta

- **Claude Code**, en la aplicación de escritorio o en la terminal (capítulo 3.2).
- **Una carpeta para el proyecto.** Ábrela en Claude Code. Empieza con una copia si ya tiene trabajo dentro.

---

## 1. La memoria: quién eres y qué reglas hay

Este archivo se lee al empezar cada sesión. Es para lo que le repetirías a alguien nuevo, no para contarlo todo: la
documentación oficial recomienda menos de 200 líneas.

```text
Crea un archivo CLAUDE.md en esta carpeta, de menos de 60 líneas, y pregúntame lo que te falte. Tiene que decir:
qué es este proyecto y para quién es; qué significa aquí «bien hecho»; las reglas que no se rompen; y una sección
final, «Aprendido», vacía, donde se apuntará cada corrección como una regla nueva con su fecha. No inventes datos
de mi negocio. Mi proyecto: [qué es y para quién].
```

## 2. Los tres agentes: cada uno con lo justo

Lo importante es lo que cada uno **no** puede hacer. El revisor solo puede leer: si encuentra un fallo, lo cuenta,
no lo tapa arreglándolo.

```text
Crea tres subagentes en .claude/agents/ con estos permisos exactos:
- planificador (tools: Read, Glob, Grep, Write). Lee CLAUDE.md y escribe el plan en la carpeta del encargo, en
  1-plan.md: qué se va a entregar, los pasos, lo que queda fuera, las dudas para mí y entre 3 y 7 criterios de
  aceptación que se puedan comprobar con un sí o un no. No hace el trabajo.
- constructor (tools: Read, Glob, Grep, Write, Edit). Lee CLAUDE.md y 1-plan.md, hace solo lo que dice el plan y
  apunta en 2-hecho.md qué archivos ha creado o cambiado. Si el plan se queda corto, para y lo dice. No publica, no
  envía y no borra nada.
- revisor (tools: Read, Glob, Grep). Lee CLAUDE.md, 1-plan.md y lo entregado sin fiarse de lo que diga 2-hecho.md, y
  responde con cada criterio marcado como Cumple o No cumple, con la prueba de cada uno, y otros problemas que vea.
  No arregla nada.
En la descripción de cada uno, di cuándo hay que usarlo.
```

> [!NOTE]
> Si es la primera vez que esta carpeta tiene agentes, cierra Claude Code y vuelve a abrirlo para que los vea.

## 3. El proceso: un comando con dos paradas

Este es el mensaje que convierte a los tres agentes en una fábrica. Las dos paradas son lo que deja la decisión en
tus manos.

```text
Crea la skill .claude/skills/fabrica/SKILL.md, con disable-model-invocation: true para que solo se lance cuando yo
escriba /fabrica, y con $ARGUMENTS como encargo. Tiene que seguir estos pasos, siempre en este orden:
1. Crea la carpeta encargos/AAAA-MM-DD-nombre-corto/ con la fecha de hoy.
2. Llama al planificador con el encargo y enséñame 1-plan.md.
3. PARADA: no sigas hasta que yo escriba «apruebo el plan». Si pido cambios, vuelve a llamar al planificador.
4. Llama al constructor.
5. Llama al revisor y guarda su respuesta tal cual en 3-revision.md.
6. Si algo no cumple, vuelve a llamar al constructor con ese informe y después al revisor. Dos vueltas como máximo;
   si sigue sin cumplir, para y dímelo.
7. PARADA: enséñame la revisión y lo entregado, y no des nada por terminado hasta que yo escriba «apruebo la entrega».
8. Escribe en 4-decision.md qué he aprobado, cuándo y qué he pedido cambiar. Si te he corregido algo que puede volver
   a pasar, propón la regla y, con mi OK, añádela a la sección «Aprendido» de CLAUDE.md.
Publicar, enviar, pagar o borrar no forman parte de este proceso: eso lo hago yo o me lo pides aparte.
```

## 4. El primer encargo: que sea pequeño

Pruébalo con algo que puedas juzgar en cinco minutos y que no salga de tu ordenador:

```text
/fabrica Una página sencilla en HTML que explique mi servicio de [servicio], con el precio y un botón de contacto.
```

Lee el plan con calma: es el momento más barato para corregir. Fíjate sobre todo en los criterios de aceptación, porque
el revisor comprobará esos y no otros. Cuando te convenza, escribe **apruebo el plan**. Si la revisión marca algo, mira
si la fábrica lo arregla sola. Al final, abre la carpeta del encargo: ahí tienes el rastro.

## 5. Que aprenda: cada corrección, una regla

Una corrección que se queda en la conversación se pierde. Cuando corrijas algo, deja que la fábrica proponga la regla.
Y si te fallan varias veces en lo mismo, mira de dónde viene:

```text
Lee los últimos encargos de la carpeta encargos/, sobre todo 3-revision.md y 4-decision.md. Dime qué fallos se repiten y
en qué paso habría que evitarlos: una regla en CLAUDE.md, un criterio que el planificador debería incluir siempre o
un cambio en un agente. Propónmelo y no cambies nada sin mi OK.
```

---

## Dónde se rompe

- **Criterios que no se pueden comprobar.** «Que quede bien» no le sirve al revisor. «Tiene precio y botón de contacto»,
  sí. Si el plan trae criterios vagos, recházalo.
- **Aprobar sin leer.** Si escribes «apruebo» siempre sin mirar, tienes un trámite, no una revisión.
- **Fiarse de una frase para lo grave.** La documentación de Claude Code lo avisa: `CLAUDE.md` orienta, pero no obliga. Lo
  que no debe pasar nunca, no lo dejes en una regla escrita: quítale la herramienta al agente, como aquí con el revisor,
  y no apruebes tú en Claude Code las acciones que salgan hacia fuera.
- **Montarla para una tarea de una vez.** La fábrica compensa con lo que se repite. Para una tarea suelta, basta con
  pedirla.

## En resumen

- Tres agentes separados: el que planifica no construye y el que revisa no puede cambiar nada.
- Dos paradas tuyas: el plan antes de empezar y la entrega antes de terminar.
- Repetible con `/fabrica`, con rastro en una carpeta por encargo y con memoria en `CLAUDE.md`.
- Empieza por un encargo pequeño y convierte cada corrección en una regla.

Para escribir mejor las reglas de cada agente, mira el capítulo 4.2. Si todavía no sabes qué trabajo darle, empieza por
el capítulo 4.8.

---

## Fuentes

- Claude Code: [subagentes](https://code.claude.com/docs/en/sub-agents) (archivos, permisos por herramienta),
  [skills](https://code.claude.com/docs/en/skills) (comandos, `disable-model-invocation`, `$ARGUMENTS`) y
  [memoria](https://code.claude.com/docs/en/memory) (`CLAUDE.md`, tamaño recomendado y que orienta pero no obliga).

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
