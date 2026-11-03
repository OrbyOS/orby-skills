# Cuatro reglas para que Claude Code no se pase de listo

Este es uno de los archivos de reglas más populares para Claude Code: cuatro principios que evitan que suponga cosas sin
preguntar, que complique lo sencillo y que toque lo que no le has pedido. Aquí tienes qué dice cada uno, cómo instalarlo y una
versión en español que sirve también si no programas.

Revisada el 3 de noviembre de 2026 con su repositorio (enlace al final). Ese día tenía 228k estrellas en GitHub. No hemos medido
cuánto mejora los resultados: el proyecto no da cifras, solo señales para comprobarlo tú.

> [!IMPORTANT]
> **Andrej Karpathy no lo ha escrito.** Es un proyecto de otra persona, basado en lo que Karpathy, investigador de IA, publicó
> sobre los fallos de los modelos al programar. El nombre lleva el suyo, pero no es un archivo oficial suyo ni de Anthropic.

---

## Las cuatro reglas

| Regla | Qué le pide a Claude | Qué evita |
| --- | --- | --- |
| **Piensa antes de programar** | Decir lo que está suponiendo, preguntar si no lo tiene claro y avisar si hay un camino más simple | Que elija una interpretación en silencio y siga adelante |
| **Lo simple primero** | El mínimo que resuelve el problema, sin nada que no hayas pedido | Mil líneas donde bastaban cien |
| **Cambios quirúrgicos** | Tocar solo lo necesario y limpiar solo lo que él ensucie | Que «mejore» de paso lo que funcionaba |
| **Orientado a objetivos** | Convertir la tarea en algo comprobable y repetir hasta que se cumpla | Dar por hecho algo que nadie ha comprobado |

El propio archivo avisa de que prefiere la cautela a la velocidad. Para un cambio de una palabra no hace falta tanto rigor.

## Cómo instalarlo

Necesitas Claude Code (capítulo 3.2). Elige una de estas dos formas, y antes lee el archivo, como con cualquier cosa de otra
persona: son solo [65 líneas de texto](https://github.com/multica-ai/andrej-karpathy-skills/blob/main/CLAUDE.md).

### Para todos tus proyectos: como plugin

Pega estas líneas una a una en Claude Code:

```text
/plugin marketplace add multica-ai/andrej-karpathy-skills
/plugin install andrej-karpathy-skills@karpathy-skills
```

El repositorio cambió de dueño y su documentación todavía usa la dirección antigua, `forrestchang/andrej-karpathy-skills`, que
redirige a esta.

### Para un solo proyecto: dentro de tu CLAUDE.md

Abre Claude Code en la carpeta del proyecto y pega esto:

```text
Lee https://raw.githubusercontent.com/multica-ai/andrej-karpathy-skills/main/CLAUDE.md y añádelo a mi CLAUDE.md, sin borrar ni
cambiar lo que ya hay. Si algo choca con mis reglas, no lo resuelvas tú: enséñamelo y pregúntame.
```

> [!CAUTION]
> Su documentación da un comando para proyectos nuevos que crea el archivo con `curl -o CLAUDE.md`. Si ya tienes un `CLAUDE.md`,
> ese comando lo sustituye y pierdes lo que hubiera. Por eso aquí se lo pedimos a Claude.

## Si no programas: la versión para cualquier tarea

Las reglas originales hablan de código. Esta es nuestra adaptación, para un `CLAUDE.md` o para las instrucciones de un proyecto
de Claude (capítulo 1.2):

```text
Cuando te pida algo:
1. Antes de empezar, dime qué estás suponiendo. Si hay dos formas de entender lo que pido, pregúntame cuál es. Si hay un camino más sencillo, dímelo.
2. Haz solo lo que te he pedido, de la forma más simple que funcione. Nada de añadidos que yo no haya pedido.
3. Toca únicamente lo necesario. Si ves otra cosa que se podría mejorar, me lo dices, pero no la cambias.
4. Antes de empezar, dime cómo vamos a comprobar que está bien. No me digas que está terminado hasta haberlo comprobado, y enséñame cómo.
Si la tarea es muy pequeña, usa el sentido común y no me hagas preguntas de más.
```

## Cómo saber si te funciona

Fíjate durante una semana en lo que el proyecto propone mirar:

- Claude pregunta **antes** de equivocarse, no después.
- En lo que te entrega solo cambia lo que pediste.
- Rehaces menos cosas por haber quedado demasiado complicadas.

Si no notas nada o te hace ir más lento, quítalo. Un archivo de reglas se carga en cada conversación y gasta parte de tu uso,
así que tiene que ganarse el sitio.

## Avisos

- **No hace milagros.** Son instrucciones, no un bloqueo: Claude puede saltárselas, sobre todo en sesiones largas. Si algo no se
  puede romper de ninguna manera, compruébalo tú.
- **Tus reglas mandan.** Añade debajo las de tu proyecto (capítulo 2.1) y revísalas cuando corrijas algo.
- **Se está moviendo poco.** El último cambio del repositorio es de abril de 2026. Para cuatro reglas de texto no es un problema,
  pero no esperes novedades.
- **La licencia.** El texto de su portada dice MIT, aunque el repositorio no incluye un archivo de licencia. Si quieres copiarlo
  dentro de un producto, tenlo en cuenta.

## En resumen

- Cuatro reglas: piensa antes, lo simple primero, cambios quirúrgicos y orientado a objetivos.
- No es de Karpathy: es de otra persona, a partir de lo que él publicó.
- Plugin para todos tus proyectos, o `CLAUDE.md` para uno solo, sin sustituir el que ya tengas.
- Si no programas, usa nuestra versión para cualquier tarea.
- Compruébalo una semana: si no te ayuda, quítalo.

---

## Fuentes

- [Repositorio del proyecto](https://github.com/multica-ai/andrej-karpathy-skills) (reglas, instalación, señales y licencia en su
  portada) y su [CLAUDE.md](https://github.com/multica-ai/andrej-karpathy-skills/blob/main/CLAUDE.md).

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
