# Editar tus vídeos con Claude, paso a paso

Una guía de principio a fin para editar con Claude desde cero: cómo ordenar las carpetas, qué entrevista hacer para que
aprenda tu estilo, qué mensaje mandar la primera vez y cómo corregir para que cada vídeo salga mejor que el anterior. Para
vídeos hablados a cámara, en tu ordenador y sin abrir un programa de edición.

Revisada el 1 de noviembre de 2026.

---

## Lo que vas a conseguir y lo que no

Claude quita los silencios y las tomas falsas, pone subtítulos palabra a palabra, pasa el vídeo a vertical (1080x1920) y
deja el volumen a punto. No cambia el orden de lo que dices, y antes de cortar te enseña lo que va a quitar.

Trabaja con la transcripción y los tiempos, no ve el vídeo como tú: por eso funciona mejor en vídeos en los que hablas.
Para efectos más elaborados, sigue después con el capítulo 5.5.

## 1. Prepara el equipo

- **Claude Code** en tu ordenador (capítulo 3.2), con un plan de pago de Claude.
- **Las skills del manual.** En el Mac, abre la Terminal, pega esta línea y pulsa Intro:

```bash
curl -fsSL https://raw.githubusercontent.com/OrbyOS/orby-skills/main/instalar.sh | bash
```

¿Prefieres que lo haga Claude? Pégale este prompt en Claude Code:

```text
Instala las skills de edición de este repositorio público: https://github.com/OrbyOS/orby-skills. Necesito editar-reels-con-claude,
manual-de-edicion y estudiar-videos-que-funcionan. Léeme antes lo que vas a ejecutar, instálalas en ~/.claude/skills y dime
cuándo tengo que reiniciar Claude Code.
```

Sirven para cortar el vídeo, poner subtítulos y animaciones, estudiar los vídeos que te gustan y sacar su estilo.

Instala las skills en `~/.claude/skills`. Luego cierra Claude Code y vuelve a abrirlo. Los programas que hacen el trabajo
(ffmpeg y faster-whisper) te los comprueba Claude al empezar y te pide permiso antes de instalarlos. Son gratis y funcionan
en tu ordenador; la primera transcripción descarga unos cientos de megas.

## 2. Crea las carpetas

Una carpeta para todo lo que editas, siempre con la misma forma, y Claude no tiene que preguntarte dónde está cada cosa.
Abre esa carpeta en Claude Code y pídeselo:

```text
Crea esta estructura aquí: brutos/ (los vídeos tal cual los grabo), referencias/ (vídeos que me gustan), imagenes/ (las
capturas y fotos que yo te dejo para un vídeo) y terminados/ (los vídeos listos para publicar). No toques nada de lo que ya
haya en la carpeta.
```

Te queda así:

```text
Mis videos/
├── MANUAL-EDICION.md   Tu estilo, por escrito. Sale en el paso 3
├── brutos/             Lo que grabas. Nunca se borra ni se toca
├── referencias/        Dos o tres vídeos tuyos o de otros que te gustan
├── imagenes/           Capturas y fotos que eliges tú
└── terminados/         Lo que ya se puede publicar
```

Cuando edites un bruto, Claude crea a su lado una carpeta de trabajo con los archivos intermedios. Se pueden borrar al
terminar; él te pregunta antes.

## 3. La entrevista de estilo

Tu estilo no puede vivir en tu cabeza. Esta entrevista lo deja escrito en un archivo que Claude lee antes de editar. Si
puedes, deja antes en `referencias/` dos o tres vídeos que te gusten. Pega este mensaje:

```text
Hazme la entrevista para escribir mi manual de edición, con la skill manual-de-edicion. Hazme las preguntas de dos en dos y
espera a que conteste. Quiero acabar con las cinco reglas que no se rompen: qué no se corta nunca, qué se quita siempre, cómo
es el texto en pantalla, lo que no quiero ver nunca, y la duración y el ritmo. Si no sé qué contestar, usa los vídeos de la
carpeta referencias: dime qué ves y pregúntame si lo quiero. Guarda el resultado en MANUAL-EDICION.md, en esta carpeta, con
reglas que se puedan comprobar mirando el vídeo.
```

Lo que te va a preguntar, para que lo vayas pensando:

| Pregunta | Una respuesta que sirve | Una que no |
| --- | --- | --- |
| **¿Qué no se corta nunca?** | «Nunca cambies el orden de lo que digo» | «Lo importante» |
| **¿Qué se quita siempre?** | «Silencios de más de medio segundo, frases a medias y arranques en falso» | «Lo que sobre» |
| **¿Cómo es el texto?** | «Subtítulos blancos, en mayúsculas, de dos o tres palabras y sin tapar la cara» | «Que quede bien» |
| **¿Qué no quieres ver?** | «Emoticonos, transiciones, música debajo de la voz» | «Nada cutre» |
| **¿Duración y ritmo?** | «Entre 30 y 60 segundos, sin pausas largas» | «Dinámico» |

## 4. El primer mensaje

Copia el vídeo en `brutos/` y pega este mensaje, cambiando el nombre del archivo:

```text
Edítame este reel: brutos/[nombre del vídeo]. Lee antes MANUAL-EDICION.md. Comprueba primero que tengo lo necesario y
pídeme permiso antes de instalar nada. Antes de montar, enséñame en una tabla lo que propones quitar, con el texto de cada
frase y el motivo, y espera mi OK. Se puede quitar lo que sobra, pero no cambies el orden de lo que digo ni el bruto.
Al terminar, revisa la hoja de fotogramas, deja una copia en terminados/ y dime qué has quitado y cuánto dura.
```

Empieza por un vídeo corto, de uno a tres minutos: si algo no te gusta, lo verás antes.

## 5. Revisa la tabla y mira el vídeo

Dos momentos en los que manda tu criterio:

1. **La tabla de lo que quita.** Léela antes de darle el OK. Es el momento de decir «la frase 12 se queda».
2. **El vídeo terminado.** Míralo entero en el móvil, con sonido. Claude ha comprobado las medidas, el volumen y los
   fotogramas, pero no sabe si te convence.

No hace falta transcribir de nuevo para cambiar un corte o los subtítulos: se vuelve a montar desde lo que ya hay.

## 6. Cada corrección, una regla

Aquí está la diferencia entre usar una herramienta y entrenarla. Cuando algo no te guste, corrígelo así:

```text
Los subtítulos tapan la barbilla en el segundo 12. Arréglalo y apúntalo como regla general en MANUAL-EDICION.md, con la
fecha, este ejemplo y cómo se comprueba, para que no vuelva a pasar en ningún vídeo.
```

Fíjate en que no pide la anécdota («en el segundo 12»), sino la regla («la base de los subtítulos, por encima de la barbilla
en todo el vídeo»). Cada regla es una corrección que no tienes que volver a hacer.

## 7. A partir del segundo vídeo

Con todo montado, el mensaje se queda en esto:

```text
Edítame brutos/[nombre del vídeo] con mi manual. Enséñame lo que quitas antes de montar y deja el resultado en terminados/.
```

Si has grabado una charla larga con varios temas, pídele varios reels:

```text
Este bruto tiene varios temas: brutos/[nombre del vídeo]. Proponme una lista de reels con su primera frase y duración, cada
uno tiene que entenderse solo, y espera mi OK antes de montar.
```

## Errores que se repiten

- **Corregir sin apuntar.** Lo arreglas en ese vídeo y vuelve a pasar en el siguiente.
- **Reglas que no se pueden comprobar.** «Que tenga ritmo» no sirve; «ningún silencio de más de medio segundo», sí.
- **Pedirle que busque imágenes por internet.** Si son de otros y se publican sin permiso, te pueden quitar el vídeo.
  Baja tú las que quieras y déjalas en `imagenes/`.
- **Empezar por un vídeo de una hora.** Primero uno corto. Para sacar clips de uno largo, mira el capítulo 5.12.

## En resumen

- Carpetas siempre iguales, y los brutos no se tocan.
- La entrevista de estilo deja cinco reglas en `MANUAL-EDICION.md`.
- El primer mensaje pide ver lo que quita antes de montar y prohíbe cambiar el orden.
- Cada corrección se convierte en una regla general.

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
