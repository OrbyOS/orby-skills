# Orby Skills

Skills y guías gratuitas para trabajar tu contenido con Claude. Cada una resuelve un problema concreto entero:
editar un reel, preparar una grabación, revisar lo que la IA toca en tus anuncios.

Las hace el equipo de [Orby](https://orbyos.es), un equipo de agentes de IA de código abierto que lleva el
contenido de una marca personal.

## Qué hay

| Carpeta | Tipo | Qué resuelve |
| --- | --- | --- |
| [`editar-reels-con-claude`](editar-reels-con-claude) | Skill | De un bruto grabado a cámara a un reel en 9:16: sin silencios ni tomas falsas, con subtítulos y el volumen de redes. También saca varios reels de una grabación larga. |
| [`manual-de-edicion`](manual-de-edicion) | Skill | Escribe las reglas de tu estilo de edición y convierte cada corrección en una regla, para no repetir el mismo error. |
| [`estructura-para-grabar`](estructura-para-grabar) | Skill | Una estructura para grabar unos minutos hablando libre, sin leer, y sacar de ahí tres o cuatro reels. |
| [`estudiar-videos-que-funcionan`](estudiar-videos-que-funcionan) | Skill | Elige qué vídeos de otras cuentas merece la pena estudiar, los desmonta y los convierte en ideas para tu negocio. |
| [`lente-de-negocio`](lente-de-negocio) | Skill | Saca lo que la IA necesita saber de tu negocio, lo deja escrito en un CONTEXTO.md y elige el primer proceso que pasar por la IA. |
| [`reglas-de-un-agente`](reglas-de-un-agente) | Skill | Escribe las reglas de tu primer agente (qué hace solo, qué te pregunta, qué no hace nunca) y lo crea en Claude Code. |
| [`equipo-de-contenido`](equipo-de-contenido) | Skill | Reparte el trabajo de contenido en siete puestos, decide qué hace la IA en cada uno y monta los agentes. |
| [`que-dejar-a-la-ia`](que-dejar-a-la-ia) | Skill | Decide con cuatro preguntas qué tareas puede hacer la IA sola, cuáles con revisión y cuáles nunca. |
| [`instalar-orbyos`](instalar-orbyos) | Skill | Instala OrbyOS, el equipo de agentes de Orby, en tu ordenador y te acompaña en los primeros pasos. |
| [`guias/instalar-orbyos.md`](guias/instalar-orbyos.md) | Guía | Lo mismo, para hacerlo tú paso a paso: OrbyOS funcionando en tu ordenador en unos veinte minutos. |
| [`guias/mejoras-ia-meta-ads.md`](guias/mejoras-ia-meta-ads.md) | Guía | Qué cambia la IA de Meta en tus anuncios, cuál dejar y dónde se apaga cada mejora. |

Las guías se leen tal cual, aquí mismo. Las skills se instalan en Claude Code.

## Qué es una skill

Una skill es una carpeta con instrucciones (y a veces scripts) que Claude Code carga cuando la necesita. Le
enseña a hacer una tarea concreta de principio a fin, siempre igual. No hace falta saber programar para usarla:
se instala una vez y luego se le pide en lenguaje normal.

## Cómo instalar una skill

Necesitas [Claude Code](https://code.claude.com) instalado y con tu cuenta de Claude.

1. Descarga este repositorio: botón verde **Code → Download ZIP** y descomprímelo.
2. Copia la carpeta de la skill que quieras dentro de la carpeta de skills de Claude:
   - Mac y Linux: `~/.claude/skills/` (la carpeta `.claude` está oculta: en el Finder, `Cmd + Mayús + .` la enseña).
   - Windows: `C:\Users\TU_USUARIO\.claude\skills\`.
   Si la carpeta `skills` no existe, créala.
3. Cierra y vuelve a abrir Claude Code.

Si te manejas con la terminal, lo mismo en una línea (cambia el nombre de la skill por la que quieras):

```bash
git clone https://github.com/OrbyOS/orby-skills.git /tmp/orby-skills && mkdir -p ~/.claude/skills && cp -R /tmp/orby-skills/editar-reels-con-claude ~/.claude/skills/
```

## Cómo usarla

Abre Claude Code en la carpeta donde tengas tus vídeos o tus documentos y pídeselo con tus palabras:

- «Edítame este reel» o «quítale los silencios y ponle subtítulos a este vídeo».
- «Prepárame una estructura para grabar sobre…».

Claude reconoce la tarea y usa la skill. También puedes llamarla por su nombre: `/editar-reels-con-claude`.

La primera vez, la skill comprueba qué te falta (por ejemplo, ffmpeg) y te dice cómo instalarlo antes de empezar.
No instala nada sin preguntarte.

## Tus datos

Las skills trabajan en tu ordenador. La edición de vídeo, incluida la transcripción, no sube nada a ningún sitio.
Lo que hablas con Claude sigue las condiciones de tu cuenta de Claude.

## Licencia

MIT. Úsalas, cámbialas y compártelas como quieras. Ver [LICENSE](LICENSE).
