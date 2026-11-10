# Que Claude te interrogue antes de construir nada

Casi todo lo que sale mal con una IA viene de lo mismo: le diste una idea a medias y la rellenó por su cuenta. `grill-me` le da
la vuelta. En lugar de ponerse a hacer, Claude te pregunta hasta que no quede ninguna decisión sin tomar. Y no hace falta
programar: sirve para una campaña, una web, una app o una decisión de negocio.

Revisada el 3 de noviembre de 2026 con su documentación (enlaces al final). `grill-me` forma parte de un paquete de skills con
310k estrellas en GitHub y licencia MIT. No hemos medido sus resultados: lo que sigue viene de su documentación y es nuestra
adaptación a tareas sin código.

---

## Lo que hace

- **Pregunta por rondas.** En cada una, todas las preguntas que ya se pueden contestar, sin adelantarse a lo que todavía no le has dicho.
- **Te da su recomendación** en cada pregunta, para que contestes «sí» o le lleves la contraria.
- **Lo que pueda averiguar, lo averigua.** Las decisiones son tuyas.
- **No escribe ningún archivo.** El resultado es tu idea, más clara.
- **No hace nada hasta que le confirmas** que ya estáis de acuerdo.

La documentación del proyecto dice que 46 preguntas en cuatro rondas es una sesión normal. Reserva un rato.

## Instalarla

Pega esta línea en la terminal, con Claude Code instalado (capítulo 3.2):

```text
claude plugin install mattpocock-skills@claude-plugins-official
```

Instala el paquete entero, con muchas skills pensadas para programar. Para `grill-me` no necesitas ninguna otra, ni el paso de
configuración `/setup-matt-pocock-skills`, que es para las de código.

Lee antes los archivos, como con cualquier skill de otra persona (capítulo 2.1).

## Usarla

1. Abre una **conversación nueva**, sin un plan previo encima.
2. **Deja apagado el modo plan:** ese modo le mete prisa por entregar un plan, y aquí quieres que siga preguntando.
3. Escribe `/grill-me` seguido de tu idea. Si no te sale, escribe `/grill` y elígela en la lista.

Tres formas de empezar:

```text
/grill-me Quiero lanzar una campaña para vender mi taller de marzo. Todavía no tengo decidido ni el canal ni el mensaje.
```

```text
/grill-me Quiero una web para mi negocio de [qué haces]. Aún no sé qué páginas necesito ni qué tiene que hacer quien entre.
```

```text
/grill-me Quiero una app sencilla para que mis clientes [lo que tienen que poder hacer]. No sé programar. Pregúntame también lo
que yo no sabría que tengo que decidir.
```

## Sin Claude Code: nuestra versión

Si usas Claude en la web o en el móvil, puedes pegar esto. Lo hemos escrito nosotros siguiendo la misma idea:

```text
Quiero que me interrogues sobre esta idea hasta que no quede ninguna decisión sin tomar: [tu idea].

Hazlo por rondas. En cada ronda, numera todas las preguntas que ya puedo contestar. Deja para más adelante las que dependan de una
respuesta que aún no te he dado. En cada pregunta, dame tu recomendación y por qué.

Lo que puedas averiguar por tu cuenta, averígualo y no me lo preguntes. Las decisiones son mías. No hagas nada todavía. Cuando no
quede ninguna pregunta, resume lo que hemos decidido y espera a que te confirme que estamos de acuerdo.
```

## Cómo sacarle partido

Según su documentación, el fallo típico es contestar «de acuerdo» cuarenta veces. Parece productivo porque dura mucho, pero sales con
un plan que escribió la IA y que tú solo has aprobado.

- **Llévale la contraria.** Si no has discrepado en nada, seguramente no te hacía falta.
- **«No lo sé» es una respuesta.** Dilo. No te inventes algo para seguir.
- **Corta lo que no se decide hablando.** Si la pregunta es cómo se va a ver algo, pide una prueba rápida, mírala y contesta en una línea.
- **Si te hace doscientas preguntas,** la idea era demasiado grande. Pide que la parta en trozos y haz una sesión por trozo.
- **Usa tu mejor modelo.** Lo recomienda el proyecto: aquí importa lo que el modelo sabe sobre cómo se rompen las cosas.

Sabes que ha funcionado si puedes defender cada decisión ante alguien que no estaba y si has acabado en un sitio que no esperabas.

## Y después

Cuando terminéis, en la misma conversación, pide lo que toque: «Con lo que hemos decidido, escribe el brief de la campaña» o
«Prepara el plan de la web y espera mi OK». No abras otra conversación, porque se perdería todo lo que acabáis de hablar.

Si quieres preguntas de una en una, añade esta línea a tu `CLAUDE.md`:

```text
When grilling, ask one question at a time.
```

## En resumen

- Claude te pregunta por rondas, con su recomendación, y no hace nada hasta que confirmas.
- Sirve sin código: campañas, webs, apps y decisiones.
- Conversación nueva, modo plan apagado y la idea detrás de `/grill-me`.
- Sin Claude Code, usa nuestro mensaje.
- Discute sus recomendaciones: si solo apruebas, el plan es suyo y no tuyo.

---

## Fuentes

- [Repositorio de las skills](https://github.com/mattpocock/skills) (instalación y licencia), [documentación de
  `grill-me`](https://github.com/mattpocock/skills/blob/main/docs/productivity/grill-me.md) y [la skill
  `grilling`](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md), que hace las preguntas.

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
