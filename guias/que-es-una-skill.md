# Qué es una skill y cuándo usarla

Una skill es una carpeta con instrucciones (y, a veces, archivos y código) que le enseña a Claude a hacer una tarea
concreta de principio a fin, siempre igual. La instalas una vez y Claude la usa sola cuando le pides esa tarea.

Revisada el 30 de octubre de 2026 con la ayuda oficial de Claude y la web de skills.sh (enlaces al final).

---

## 1. Skill, proyecto o buen pedido

| Herramienta | Qué guarda | Úsala cuando |
| --- | --- | --- |
| **Un buen pedido** (capítulo 0.3) | Nada: vale para esa conversación | Es una tarea puntual |
| **Un proyecto** (capítulo 1.2) | Instrucciones y documentos de un tema o un cliente | Necesitas el mismo contexto en muchas conversaciones |
| **Una skill** | Una forma de hacer una tarea, paso a paso | Repites la misma tarea y quieres que salga siempre igual de bien |

Un ejemplo para verlo: el proyecto «Mi negocio» guarda quién eres y qué vendes; la skill «guiones con criterio»
guarda cómo se escribe y se revisa un guion. Juntos, Claude escribe guiones buenos y con tu voz.

## 2. Dónde funcionan

- **En Claude (web y aplicación):** en todos los planes, también el gratuito, con la ejecución de código activada.
- **En Claude Code:** se instalan en tu ordenador y Claude las usa al trabajar con tus archivos.
- Las skills que subes a tu cuenta de Claude también se cargan en Claude Code si inicias sesión con la misma cuenta.

Claude ya trae algunas de serie, por ejemplo para trabajar con Excel, Word, PowerPoint y PDF, y las usa solo cuando
hacen falta.

## 3. Cómo se activan y se suben

1. **Activa la ejecución de código:** en **Settings → Capabilities** (en los planes de empresa lo decide quien
   administra la cuenta).
2. **Entra en Customize → Skills:** ahí puedes encender o apagar cada skill.
3. **Para subir una tuya o de este manual:** pulsa **+**, elige **Create skill** y **Upload a skill**, y sube la
   carpeta comprimida en ZIP.

Para instalar todas las del manual en Claude Code de una vez, mira el catálogo (capítulo 2.4).

> [!NOTE]
> Según la ayuda oficial, las skills pasarán a llamarse «Plugins» el 30 de noviembre de 2026. Si ves «Plugins» en
> lugar de «Skills» en el menú, es lo mismo.

## 4. Cuándo merece la pena una skill

- Haces la misma tarea al menos una vez por semana.
- Tienes una forma de hacerla que funciona y que podrías explicar paso a paso.
- Te cansas de explicarle lo mismo a Claude en cada conversación.

Si cumple las tres, conviértela en skill (capítulo 2.3).

> [!CAUTION]
> Instala skills solo de fuentes de confianza y, si vienen de alguien que no conoces, revisa sus archivos antes de
> activarlas: una skill puede llevar código.

## 5. Antes de instalar una skill

Hay skills hechas por otros para casi todo, y la mayoría no pasan ningún filtro antes de publicarse. El orden que
evita sustos: **la encuentras, miras su auditoría y solo entonces la instalas.**

### La encuentras

**skills.sh** es un directorio abierto de skills para agentes de IA, con un ranking por instalaciones. El contador
de su ranking pasa de un millón y medio. La número uno es **find-skills**, con más de 4 millones de instalaciones: una
skill que busca skills por ti. Se instala con:

```bash
npx skills add https://github.com/vercel-labs/skills --skill find-skills
```

Después, pídele a Claude Code lo que necesitas:

```text
Busca una skill para [tarea], dime las tres mejores con sus instalaciones y su auditoría de seguridad, y no instales
ninguna hasta que elija.
```

### Miras la auditoría

skills.sh tiene una página de **auditorías de seguridad** (skills.sh/audits) y cada skill enseña la suya en su página.
La revisan tres auditores, cada uno en su columna: **Gen**, **Socket** y **Snyk**. Lo que vas a ver:

| Etiqueta | Qué te dice |
| --- | --- |
| **Safe** o **Pass** | Ese auditor no ha encontrado nada |
| **0 alerts**, **1 alerts**… | Las alertas que ha encontrado Socket. Cero es lo que buscas |
| **Low Risk** | Riesgo bajo: lee qué hace antes de instalarla |
| **Med Risk** o **Warn** | Riesgo medio o un aviso: mira sus archivos o pídele a Claude que los revise contigo |
| **High Risk** | Riesgo alto: no la instales |
| **Pending** | La auditoría aún no ha terminado: espera |

La web no explica el detalle de cada etiqueta, así que tómalas como una señal, no como un veredicto. Y la propia web
avisa de que no puede garantizar la calidad ni la seguridad de cada skill, y pide revisarlas antes de instalarlas.

### La instalas

Solo si la auditoría está limpia y la skill viene de alguien de confianza. Si tienes dudas, pídeselo así:

```text
Antes de instalar esta skill, lee todos sus archivos y dime qué hace, qué comandos ejecuta, a qué webs se conecta y si
toca mis archivos o mis claves: [enlace a la skill].
```

## 6. En resumen

- Un pedido para lo puntual, un proyecto para el contexto y una skill para la tarea que repites.
- Funcionan en Claude y en Claude Code, en todos los planes.
- Se activan en Customize → Skills; si ves «Plugins», es lo mismo.
- Antes de instalar una de otro: la encuentras, miras su auditoría y solo entonces la instalas.

---

## Fuentes

- Ayuda de Claude: [usar skills en Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude) y
  [plugins, skills y conectores en una sola página](https://support.claude.com/en/articles/17740565-manage-plugins-skills-and-connectors-from-one-plugins-page).
- skills.sh: [ranking](https://skills.sh), [auditorías de seguridad](https://skills.sh/audits) y
  [preguntas frecuentes](https://skills.sh/docs) (consultado el 30/10/2026).

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
