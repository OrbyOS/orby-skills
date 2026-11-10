# Elige un solo trabajo y valida un agente que lo haga

Pedirle a un agente «que lleve el marketing» o «que atienda a los clientes» es pedirle veinte trabajos a la vez, y así no
hay forma de saber si funciona. Esta guía hace lo contrario:
eliges un trabajo, escribes el examen antes de construir nada, y el agente no toca a un cliente hasta que lo aprueba
y pasa unas semanas trabajando en la sombra.

Revisada el 1 de noviembre de 2026 con las guías de Anthropic sobre agentes (enlaces al final). Los umbrales y plazos de
esta guía son un punto de partida: ajústalos a lo que te juegues.

---

## 1. Haz la lista de lo que repites

Durante una semana, o de memoria si lo tienes claro, apunta cada tarea que repites. Que te ayude Claude:

```text
Hazme preguntas, de dos en dos, para sacar las tareas que repito en mi negocio: qué hago cada semana, qué dejo para
el final, qué le pido a otros y qué se queda sin hacer. Mi negocio: [qué haces y para quién]. Al terminar, dame una
lista de tareas concretas, cada una con cuándo se hace, cuánto tiempo me lleva y dónde está la información que usa.
No me propongas agentes todavía.
```

## 2. Pásala por cinco preguntas

Una tarea es buena candidata si contesta que sí a las cinco. Si falla una, pasa a la siguiente de la lista.

| Pregunta | Si la respuesta es no |
| --- | --- |
| **¿Se repite** al menos cada semana? | No compensa: no tendrás casos para probarlo ni horas que ahorrar |
| **¿Hay que decidir algo** en cada caso? | Si siempre son los mismos pasos, te basta una automatización, más barata y más fiable |
| **¿Lo que necesita está escrito** y a su alcance? | Si está en tu cabeza, primero hay que escribirlo |
| **¿Sabes cómo es hacerlo bien?** | Si no lo sabes hacer tú, no podrás corregirlo |
| **¿Puedes ver el resultado antes de que salga?** | Si un error llega directo al cliente o no se puede deshacer, no es para empezar |

De las que queden, elige la que más horas te coma. No la más vistosa.

## 3. Escríbelo en una frase

```text
Cada [cuándo], con [qué recibe], entrega [qué], y ha terminado cuando [algo que se pueda comprobar].
```

Ejemplo inventado: «Cada lunes, con la hoja de presupuestos enviados, entrega un borrador de seguimiento para cada
presupuesto con más de 7 días sin respuesta, y ha terminado cuando no queda ninguno sin borrador».

Si te sale un «y además», son dos trabajos. Quédate con uno: el segundo agente llega cuando el primero funcione.

## 4. Escribe el examen antes de construir

Es fácil saltarse este paso, y es el que te dice si funciona. Tienes que escribirlo antes de ver lo que
hace el agente. Si no, acabarás dando por bueno lo que te enseñe.

Anthropic recomienda empezar con un conjunto de 20 a 50 casos sacados de lo real, y juzgar lo que el agente entrega, no
los pasos que da. Para un trabajo como este, empieza por 20:

- **Casos reales que ya has resuelto**, con lo que hiciste tú en cada uno. Quita los datos personales.
- **Unos cuantos difíciles:** falta información, el caso es dudoso o es de los que siempre te hacen dudar.
- **Unos cuantos que debe dejar pasar:** lo que no le toca, lo que tiene que pasarte a ti.

Y la nota, escrita ahora, con preguntas de sí o no. Separa lo que es un fallo de lo que es grave:

```text
Te paso 20 casos reales de esta tarea, con lo que hice en cada uno: [pega los casos o indica la carpeta]. El trabajo es:
[tu frase del paso 3]. Prepara un archivo EXAMEN.md con dos cosas. Primero, los casos, separando lo que recibe el agente
de lo que hice yo. Segundo, una lista de hasta 8 comprobaciones de sí o no para puntuar una entrega, marcando cuáles son
graves (por ejemplo, inventar un dato, prometer algo o tocar lo que no le toca). Pregúntame lo que no esté claro. No
construyas ningún agente todavía.
```

Decide también ahora la nota para aprobar. Un buen punto de partida: **18 de 20 correctos y ningún fallo grave**.

## 5. Construye el agente más pequeño posible

Con la skill `reglas-de-un-agente` (capítulo 4.2) lo tienes en unos minutos. Tres límites para esta fase:

- Solo lee y prepara borradores. No envía, no publica, no borra.
- Solo las herramientas que necesita para este trabajo.
- Las reglas salen de tu frase. Nada de «y de paso».

```text
Monta el agente para este trabajo con la skill reglas-de-un-agente: [tu frase del paso 3]. Solo puede leer y dejar
borradores en una carpeta: no puede enviar, publicar ni borrar nada. Si le falta información, lo marca y no se lo
inventa. No mires la parte de EXAMEN.md con lo que hice yo.
```

## 6. Pásale el examen

Lo importante es que el agente no vea tus respuestas y que la nota la ponga alguien que no haya hecho el trabajo.

```text
Pasa el examen de EXAMEN.md. Primero, lanza el agente con cada caso, dándole solo lo que recibe, sin lo que hice yo, y
guarda cada entrega en examen/ronda-1/. Después, en una conversación aparte o con un subagente que no haya visto cómo se
hicieron, puntúa cada entrega con las comprobaciones de EXAMEN.md, con la prueba de cada una. Dame una tabla por caso, la
nota total, los fallos graves y qué tienen en común los fallos. Si no se puede saber si algo está bien, márcalo para que
lo mire yo: no lo des por bueno. No cambies las reglas del agente ni el examen.
```

Lee tú las entregas de varios casos, sobre todo donde ha aprobado por poco. Una nota automática también se equivoca.
Si suspende, arregla una regla, repite el examen entero y compara. Si cambias el examen para que apruebe, ya no estás
midiendo nada. Y si después de tres o cuatro rondas no mejora, seguramente el problema es el trabajo que elegiste, no el
agente.

## 7. Dos semanas en la sombra

Aprobar el examen no es funcionar. Durante unas dos semanas el agente trabaja con casos reales, pero **no sale nada**:
prepara sus borradores y tú sigues haciendo el trabajo como siempre, o lo revisas todo antes. Apunta en una hoja, por
cada caso:

| Apunta | Por qué |
| --- | --- |
| Si lo habrías mandado tal cual, con retoques o de nuevo | Es tu mejor medida de calidad |
| Los minutos que te ha llevado revisarlo | Lo que ahorras de verdad no es el tiempo de hacerlo, es ese menos revisar |
| Los errores nuevos | Cada uno se convierte en un caso más del examen |
| Lo que ha costado | El uso de la IA y de lo que tenga conectado |

## 8. Decide con los números

```text
Te paso la hoja de estas dos semanas del agente: [adjunta]. Dime qué porcentaje he mandado tal cual, con retoques o de
nuevo, cuánto tiempo neto me ha ahorrado (lo que me llevaba antes menos lo que me lleva revisar) y qué me cuesta. Con
los errores que han salido, proponme casos nuevos para EXAMEN.md. Dame tu recomendación: seguir, ajustar o dejarlo. Si
los datos no bastan para decidir, dímelo.
```

- **Seguir:** ahorra tiempo de verdad y no hay errores graves. Pasa al paso siguiente.
- **Ajustar:** va bien salvo en un tipo de caso. Saca ese caso del agente o arregla la regla, y repite el examen.
- **Dejarlo:** revisar te lleva casi lo mismo que hacerlo. También es un buen resultado: te ha costado dos semanas, no
  un año. Vuelve a tu lista.

## 9. Suéltalo poco a poco

Quita la revisión por partes: primero, los casos fáciles; luego, por muestreo. Lo que no se puede deshacer, como enviar,
pagar o publicar, sigue pasando por ti hasta que tengas motivos muy claros. Y cuando cambies sus reglas o el modelo,
pásale otra vez el examen: para eso lo escribiste.

Cuando este agente funcione, vuelve a la lista: el siguiente trabajo. Si quieres que varios se pasen el trabajo, sigue con
el capítulo 4.7. Si quieres venderlo como servicio, con el 6.5.

## En resumen

- Un trabajo, escrito en una frase con su final comprobable. Si hay un «y además», son dos.
- El examen, antes de construir: unos 20 casos reales y la nota decidida de antemano.
- El agente más pequeño posible, solo con borradores, y una nota que no ponga quien hizo el trabajo.
- Dos semanas en la sombra y decidir con números: seguir, ajustar o dejarlo.

---

## Fuentes

- Anthropic: [cómo evaluar agentes de IA](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) (empezar
  con 20 a 50 casos reales y juzgar el resultado, no los pasos) y
  [cómo construir agentes eficaces](https://www.anthropic.com/engineering/building-effective-agents) (empezar por lo más
  simple y añadir complejidad solo si hace falta).

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
