# Clips de un vídeo largo con Claude, sin pagar Opus Clip

De un vídeo largo salen muchos vídeos cortos, pero solo si cada trozo se entiende por sí solo. Las aplicaciones de
recortar clips lo hacen en un clic, y a veces te dan trozos que solo entiende quien ha visto el vídeo entero. Esta
guía explica cómo hacerlo con Claude Code en tu ordenador: transcribir, que Claude proponga los clips con su título,
aprobarlos y que los corte él. Con dos reglas que marcan la diferencia: la prueba del extraño y cortar siempre en una
pausa.

Revisada el 30 de octubre de 2026.

---

## 1. Por qué fallan los clips automáticos

Las aplicaciones de recortar clips eligen los trozos con una nota de viralidad: puntúan cada tramo por palabras,
ritmo o emoción, y te dan los que más sacan. El problema es que esa nota no comprueba si el trozo se entiende solo.
Así salen clips que empiezan con «y por eso…», que hablan de «esto» sin decir qué es o que se cortan antes de la
idea. Quien llega a ese clip desde el móvil, sin haber visto el vídeo, no sabe de qué va y se va.

Lo que importa no es si un trozo tiene buena nota, sino si **alguien que llega de cero lo entiende**.

## 2. El proceso

1. **Transcribir:** el vídeo se pasa a texto en tu ordenador con Whisper, palabra a palabra y con el segundo exacto
   de cada una. Gratis y sin subir el vídeo a ningún sitio.
2. **Proponer:** Claude lee la transcripción entera y te propone los clips: dónde empieza y acaba cada uno, por qué
   funciona y un título.
3. **Aprobar:** tú decides cuáles salen y cambias lo que quieras. Hasta que no dices que sí, no se corta nada.
4. **Cortar y rotular:** Claude corta los aprobados con FFmpeg, los pasa a vertical y les pone el título encima.

## 3. La prueba del extraño

Antes de proponer un clip, Claude lee sus **dos primeras frases como si no hubiera visto el vídeo**. Si alguien que
llega de cero no entiende de qué va, ese clip no sale así: o se mueve el inicio a una frase que sí se entienda, o se
descarta.

Señales de que no pasa la prueba:
- Empieza con un conector: «y», «pero», «por eso», «entonces».
- Habla de algo que se ha explicado antes: «esto», «lo que te decía», «el segundo paso».
- La primera frase no dice de qué va ni abre ninguna pregunta.

Un buen arranque se entiende solo y engancha: una situación, un dato que choca, un error común o una afirmación
contraria a lo que se suele pensar.

## 4. Cómo se corta

- **Siempre en una pausa y al final de una frase.** Nunca a mitad de palabra ni a mitad de una idea. Con la
  transcripción palabra a palabra, Claude sabe dónde termina cada una.
- **Nunca hacia atrás en el tiempo.** Dentro de un clip, los trozos van en el orden en que se dijeron. Se puede quitar
  algo del medio (una divagación), pero no traer una frase de más adelante al principio: cambiaría lo que dijiste.
- **Una idea, un clip.** Si dos clips hablan de lo mismo, se quedan en uno.
- **Que cierre.** El clip acaba cuando la idea termina, no cuando se cumple un tiempo.

## 5. Lo que hace falta

| Qué | Para qué | Precio |
| --- | --- | --- |
| **Claude Code** | Lee la transcripción, propone los clips y los corta | Con tu plan de Claude |
| **Whisper** (faster-whisper) | Pasa el vídeo a texto en tu ordenador, con el segundo exacto de cada palabra | Gratis |
| **FFmpeg** | Corta, pasa a vertical y pone el título encima | Gratis |

No hace falta instalar nada a mano: Claude Code lo instala si le das permiso. Si ya tienes la skill
[editar-reels-con-claude](../editar-reels-con-claude) (capítulo 5.4), su script `transcribir.py` sirve para el primer
paso.

## 6. El prompt

Abre Claude Code en la carpeta del vídeo y pídeselo así:

```text
Quiero sacar clips verticales de este vídeo largo: [nombre del archivo]. Sigue estos pasos:
1. Comprueba que tengo FFmpeg y faster-whisper; si falta algo, pídeme permiso antes de instalarlo.
2. Transcribe el vídeo en mi ordenador con marcas de tiempo por palabra.
3. Léelo entero y proponme entre 8 y 10 clips de 30 a 60 segundos. De cada uno: inicio y fin, la idea en una frase,
   las dos primeras frases literales y un título de dos líneas cortas.
4. Antes de proponer cada clip, haz la prueba del extraño: lee sus dos primeras frases como alguien que no ha visto
   el vídeo. Si no se entiende de qué va, mueve el inicio a una frase que sí se entienda o descártalo, y dime cuál
   de las dos cosas has hecho.
5. Corta siempre en una pausa y al final de una frase, nunca a mitad de palabra. Dentro de un clip, nunca saltes
   hacia atrás en el tiempo ni cambies el orden de lo que digo.
6. No cortes nada hasta que te diga qué clips apruebo.
7. Con los aprobados: córtalos, pásalos a vertical 9:16 centrados en mi cara, pon el título arriba en una
   tipografía sencilla y gruesa, y guárdalos en una carpeta «clips».
```

> [!TIP]
> Cuando corrijas algo (un título, un inicio, un tipo de letra), pídele a Claude que lo apunte como regla para la
> próxima vez. El capítulo 5.6 explica cómo tener tu manual de edición.

## 7. En resumen

- Un clip solo funciona si se entiende sin haber visto el vídeo.
- Transcribe en tu ordenador, deja que Claude proponga, aprueba tú y que él corte.
- La prueba del extraño: las dos primeras frases, leídas por alguien que llega de cero.
- Cortes en pausas y al final de frase, y siempre en el orden en que lo dijiste.

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
