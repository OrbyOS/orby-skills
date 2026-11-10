---
name: equipo-de-contenido
description: Reparte el trabajo de contenido de un negocio entre siete puestos (dirección, investigación, plan, guion, edición, publicación y comunidad), decide qué hace la IA y qué sigue haciendo el dueño en cada uno, dónde aprueba, y crea los agentes que quiera como subagentes de Claude Code. Úsala cuando alguien quiera montar un equipo de agentes de IA para su contenido, no sepa por dónde delegar el contenido en la IA, o pregunte cómo se organiza un equipo de contenido con IA.
---

# Equipo de contenido con IA

El contenido de un negocio no es una tarea: son siete trabajos distintos que suelen caer en la misma persona.
Separarlos es lo primero, porque cada uno se delega de una manera. Esta skill hace ese reparto para el negocio del
usuario y monta los agentes que quiera.

El modelo es el reparto de Orby, un equipo de agentes de código abierto, pero sirve sin usar Orby.

## Los siete puestos

| Puesto | En Orby | Qué recibe | Qué entrega | Dónde decide el dueño |
| --- | --- | --- | --- | --- |
| Dirección | Orby | Lo que han hecho los demás y los resultados | Un resumen corto y qué toca ahora | Aprueba prioridades |
| Investigación | Lupi | Cuentas que hablan a su mismo cliente y noticias del sector | Lo que destaca y por qué, y patrones que se pueden usar | Elige qué ideas valen |
| Plan | Plani | Lo que trae investigación y los temas fijos del negocio | El plan de la semana: qué pieza, con qué ángulo y cuándo | Aprueba el plan |
| Guion | Escri | El plan y el contexto del negocio (voz, pruebas, límites) | Estructuras o guiones con su gancho | Aprueba cada guion; graba |
| Edición | Monti | Lo que se ha grabado | Los vídeos montados | Da el visto bueno al montaje |
| Publicación | Publi | Los vídeos y sus textos | Todo programado en cada red | Aprueba antes de publicar |
| Comunidad | Chati | Comentarios y mensajes | Respuestas preparadas y contactos ordenados por interés | Aprueba lo que sale a una persona |

La regla que lo sostiene: cada puesto entrega algo concreto al siguiente y nada sale hacia fuera sin que el dueño
lo vea. Grabar y hablar con clientes siguen siendo suyos.

## Paso 1. Lo que hace hoy

Pregunta, de dos en dos:
1. ¿Qué vendes y a quién? (Si ya tiene un CONTEXTO.md de la skill `lente-de-negocio`, léelo y sáltate esto.)
2. ¿Qué publicas y dónde? ¿Con qué frecuencia?
3. De los siete puestos, ¿cuáles haces tú, cuáles hace otra persona y cuáles no hace nadie?
4. ¿Cuánto tiempo le dedicas al contenido a la semana y qué parte se te hace más pesada?
5. ¿Qué no soltarías nunca? (Por ejemplo: grabar, contestar a clientes, decidir los temas.)

## Paso 2. El reparto para su negocio

Para cada puesto, decide con él uno de estos tres niveles y escribe por qué:
- **La IA lo prepara y tú apruebas.** Para lo que se puede revisar antes de que salga.
- **La IA te ayuda y tú lo haces.** Para lo que depende de criterio o de conocer a la persona.
- **Sigue siendo tuyo.** Lo que ha dicho que no soltaría y lo que no se puede deshacer.

Criterios para proponer el nivel:
- Investigación, plan y guion suelen ser los primeros: son los que más tiempo quitan y todo pasa por el dueño
  antes de salir.
- Edición: la IA puede quitar silencios, tomas falsas y poner subtítulos (skill `editar-reels-con-claude`); el
  estilo lo decide él.
- Publicación: preparar textos y calendario, sí; publicar solo, únicamente si lo pide y con una revisión previa.
- Comunidad: borradores sí; los mensajes a una persona con un problema, siempre él.
- Dirección: empieza con un resumen semanal, no con decisiones.

Si no puede con todo a la vez, propón el orden de arranque: un puesto cada semana, empezando por el que más tiempo
le quita y se puede revisar.

## Paso 3. Entregar el EQUIPO.md

Escribe `EQUIPO.md` con:
1. La tabla de los siete puestos con su nivel, qué recibe, qué entrega y dónde aprueba él.
2. El flujo de la semana en una lista: qué día pasa cada cosa (por ejemplo, el lunes investigación y plan, el
   martes guiones, el miércoles graba, el jueves edición, de viernes a domingo publicación; comunidad, cada día).
3. El orden de arranque.
4. Lo que sigue siendo suyo, en una lista corta y clara.

## Paso 4. Crear los agentes (si quiere)

Por cada puesto de nivel «La IA lo prepara y tú apruebas», ofrece crearlo como subagente de Claude Code en
`.claude/agents/<puesto>.md`. Si tiene instalada la skill `reglas-de-un-agente`, úsala para cada uno. Si no,
escribe cada agente con estas partes: objetivo que se pueda comprobar, qué recibe y dónde está, pasos, qué hace
solo, qué necesita el OK del dueño, qué no hace nunca, cómo es una entrega buena, y una sección final «Lo que he
aprendido» para apuntar las correcciones.

Cada agente lee el contexto del negocio antes de trabajar y deja su entrega en una carpeta que el siguiente puesto
sepa dónde encontrar (por ejemplo, `semana/investigacion.md`, `semana/plan.md`, `semana/guiones/`). Así se pasan
el trabajo sin que el dueño haga de mensajero.

## Revisión antes de entregar

- ¿Todo lo que sale hacia fuera pasa por el dueño?
- ¿Lo que dijo que no soltaría está en «sigue siendo tuyo»?
- ¿Cada puesto entrega algo concreto que otro puesto usa?
- ¿El orden de arranque empieza por un solo puesto?
