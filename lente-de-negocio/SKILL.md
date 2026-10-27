---
name: lente-de-negocio
description: Entrevista al dueño de un negocio para sacar lo que la IA necesita saber de él (cliente, oferta, voz, pruebas y límites), lo deja escrito en un CONTEXTO.md reutilizable y decide qué proceso del negocio conviene pasar primero por la IA, con un plan de prueba de una semana. Úsala cuando alguien diga que la IA le da respuestas genéricas, quiera que la IA «conozca» su negocio, pida un documento de contexto o un CLAUDE.md para su negocio, o no sepa por dónde empezar a usar IA.
---

# Lente de negocio

Todo el mundo tiene ya las mismas herramientas de IA. Lo que cambia el resultado es lo que la IA sabe del negocio:
cómo habla su cliente, qué le frena, qué no se promete nunca. Esta skill saca eso del dueño, lo deja escrito para
reutilizarlo en cualquier conversación y elige el primer proceso que merece la pena pasar por la IA.

Tres partes. Si el usuario solo quiere una, haz solo esa.

## Parte 1. La entrevista

Pregunta por bloques, de tres en tres preguntas como mucho, y espera la respuesta antes de seguir. Si contesta con
generalidades («gente que quiere mejorar»), pide un caso: «piensa en tu último cliente: ¿qué te dijo en la primera
conversación?». Lo literal vale más que lo resumido.

**Cliente**
1. ¿Quién te compra? Una persona concreta: a qué se dedica, en qué momento está cuando te encuentra.
2. ¿Qué frases te dice antes de comprar? Literales, como las dice él. Pide de tres a cinco.
3. ¿Qué le frena? Las dudas y objeciones que más oyes.
4. ¿Qué ha probado antes de llegar a ti y por qué no le funcionó?
5. ¿Para quién NO es lo tuyo? A quién prefieres no venderle.

**Oferta**
6. ¿Qué vendes, en una frase que entendería tu cliente?
7. ¿Qué cambia para él cuando termina contigo? El resultado, sin adornos.
8. ¿Qué no prometes nunca, aunque te lo pidan?

**Voz**
9. ¿Cómo hablas: de tú o de usted, con humor o serio, frases cortas o largas?
10. Palabras o expresiones que usas mucho, y palabras que no usarías nunca.
11. Pega dos o tres textos tuyos que te gusten (un post, un correo, un mensaje a un cliente).

**Pruebas y límites**
12. Casos o resultados que puedes contar, y si tienes permiso para nombrar al cliente.
13. Temas de los que no hablas, datos que no se dan y cifras que no quieres que salgan.

No rellenes huecos con suposiciones. Lo que no conteste se queda como «pendiente» en el documento.

## Parte 2. Escribir el CONTEXTO.md

Con las respuestas, escribe `CONTEXTO.md` con la plantilla de `plantilla-contexto.md` (en esta carpeta). Reglas:
- Las frases del cliente van **entre comillas y literales**. No las mejores: su valor es que son suyas.
- Lo que el usuario no dijo no aparece. Ni cifras, ni casos, ni promesas inventadas.
- Corto: si pasa de dos páginas, recorta. Es para que la IA lo lea en cada conversación, no para archivarlo.

Explícale cómo usarlo, en tres líneas:
- En Claude Code: guárdalo en la carpeta de trabajo y añade al `CLAUDE.md` de esa carpeta la línea
  «Antes de escribir nada para el negocio, lee CONTEXTO.md».
- En Claude.ai: crea un Proyecto y súbelo como conocimiento del proyecto.
- En cualquier otra IA: pégalo al principio de la conversación.

## Parte 3. Qué proceso pasar primero por la IA

Pide la lista de tareas que repite cada semana (de 5 a 10). Si se queda corto, sugiere las típicas para que diga
cuáles hace: responder preguntas frecuentes, preparar propuestas, escribir publicaciones, resumir reuniones, hacer
seguimiento a quien no contesta, preparar informes, ordenar facturas.

Puntúa cada tarea de 1 a 3 en estas cinco preguntas y enséñale la tabla:

| Pregunta | 1 | 3 |
| --- | --- | --- |
| ¿Cuánto tiempo te quita a la semana? | Menos de 1 h | Más de 3 h |
| ¿Se hace siempre más o menos igual? | Cada vez es distinta | Mismos pasos siempre |
| ¿Tienes ejemplos buenos de cómo se hace? | Ninguno | Varios, guardados |
| ¿Se puede revisar antes de que llegue a nadie? | Sale directa al cliente | Pasa por ti antes |
| Si sale mal, ¿se arregla fácil? | Cuesta dinero o un cliente | Se rehace y ya |

La primera candidata es la de más puntos; si hay empate, la que más tiempo quita. Descarta de entrada lo que tenga
un 1 en cualquiera de las dos últimas preguntas: eso no se delega para empezar, por muchos puntos que sume.

Para la elegida, entrega un **plan de prueba de una semana**:
1. Qué se le da a la IA: el CONTEXTO.md y de dos a cinco ejemplos buenos de esa tarea.
2. La instrucción exacta para pedírselo, escrita para su caso y lista para copiar.
3. Cómo se revisa: qué mirar antes de darlo por bueno.
4. Cómo saber si ha funcionado: una medida sencilla (lo que tarda ahora frente a lo que tarda con IA, o cuántas
   correcciones necesita cada versión).
5. Qué hacer después: si funciona, la segunda tarea de la tabla; si no, qué ajustar (más ejemplos, una instrucción
   más concreta o una tarea más sencilla).

## Revisión antes de entregar

- ¿Las frases del cliente son literales y van entre comillas?
- ¿Hay algo en el CONTEXTO.md que el usuario no haya dicho? Fuera.
- ¿La tarea elegida se puede revisar antes de llegar a un cliente?
- ¿La instrucción del plan de prueba se puede copiar y usar tal cual?
