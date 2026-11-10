---
name: manual-de-edicion
description: Escribe el manual de edición de los vídeos de una persona (las reglas de su estilo, empezando por cinco que no se rompen nunca) y convierte cada corrección que hace a un montaje en una regla nueva con su ejemplo, para que la IA no repita el error. Úsala cuando alguien quiera que la IA edite con su estilo, esté harto de corregir lo mismo en cada vídeo, pida un manual o una guía de estilo de edición, o diga cosas como «otra vez los subtítulos tapan la cara».
---

# Manual de edición

La IA no ve los vídeos como los ves tú: trabaja con la transcripción, los tiempos y lo que le digas. Por eso el
estilo no puede vivir en tu cabeza ni en un mensaje que se olvida en la siguiente conversación. Tiene que estar
escrito como reglas. Esta skill escribe ese manual y lo mantiene vivo: cada corrección se convierte en una regla.

El manual es un archivo, `MANUAL-EDICION.md`, en la carpeta donde se editan los vídeos. Cualquier skill o agente
de edición lo lee antes de montar (la skill `editar-reels-con-claude` lo hace sola).

## Modo 1. Escribir el manual desde cero

### Las cinco reglas que no se rompen

Empieza por estas cinco preguntas. Cada respuesta es una regla del bloque «Nunca se rompe»:
1. **Qué no se corta nunca.** ¿El orden de lo que dices se puede tocar o solo se quitan trozos? ¿Las pausas de
   efecto se respetan?
2. **Qué se quita siempre.** Silencios, tomas falsas, muletillas, frases a medias. ¿Algo más?
3. **El texto en pantalla.** ¿Subtítulos sí o no? ¿Cómo: palabra a palabra, frases, mayúsculas, color? ¿Dónde, para
   que no tapen la cara ni la interfaz de la red?
4. **Lo que no quieres ver nunca.** Por ejemplo: emoticonos, efectos de plantilla, música encima de la voz,
   transiciones llamativas, filtros de color.
5. **Duración y ritmo.** Cuánto dura un reel como mínimo y como máximo, y cuánto silencio se deja entre frases.

Si no sabe qué contestar, pídele dos o tres vídeos suyos que le gusten y dos de otros que quiera parecerse: que te
cuente qué le gusta de cada uno y saca las reglas de ahí. Si te los pasa como archivos, puedes extraer fotogramas
con ffmpeg y mirarlos; describe lo que ves y que él confirme cada regla.

### Escribirlo

Usa `plantilla-manual.md` (en esta carpeta). Cada regla:
- en una línea y en imperativo («Corta…», «No pongas…»);
- comprobable: que se pueda mirar un vídeo y decir si se cumple o no («subtítulos por encima del 75 % de la altura»,
  no «subtítulos bien colocados»);
- con un ejemplo cuando ayude.

## Modo 2. Convertir una corrección en regla

Cuando el usuario corrija un montaje («los subtítulos tapan la barbilla», «ese corte se come la última palabra»,
«hay un parpadeo»):

1. **Arregla el vídeo** si estás editando.
2. **Saca la regla general**, no la anécdota. «En el segundo 12 tapa la barbilla» es la anécdota; la regla es
   «la base de los subtítulos, por encima de la barbilla de la persona en todo el vídeo: si no cabe, súbelos».
3. **Escríbela en el manual**, en la sección «Aprendido de las correcciones», con la fecha, el ejemplo que la
   provocó y cómo comprobarla.
4. **Comprueba si choca con otra regla.** Si choca, pregunta cuál manda y deja solo una.
5. Dile en una línea qué regla has añadido.

Formato de cada regla aprendida:

```markdown
- **[fecha] Subtítulos por encima de la barbilla.** La base del subtítulo no puede tapar la cara en ningún
  momento; si no cabe, se sube. Ejemplo: reel de la entrevista, segundo 12. Cómo se comprueba: en la hoja de
  fotogramas, ningún subtítulo toca la cara.
```

## Modo 3. Revisar un vídeo con el manual

Si te piden revisar un montaje: saca una hoja de fotogramas (por ejemplo, con
`ffmpeg -i video.mp4 -vf "fps=1/2,scale=270:-1,tile=4x3" -frames:v 1 hoja.jpg`), mírala, lee la transcripción si
la hay y repasa el manual regla por regla. Entrega la lista de las que no se cumplen, con el segundo en que pasa.
No digas que algo se cumple si no lo has podido comprobar: dilo.

## Revisión antes de entregar

- ¿Las cinco reglas de «Nunca se rompe» están y son comprobables?
- ¿Cada regla aprendida es general, tiene fecha y ejemplo?
- ¿Hay dos reglas que se contradigan? Deja solo una.
- ¿El manual cabe en una pantalla o dos? Si crece mucho, agrupa las parecidas.
