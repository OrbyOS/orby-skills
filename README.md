# Orby Skills

Skills gratuitas para que Claude te haga el trabajo de contenido: editar tus reels, preparar lo que grabas, sacar
ideas y montar tus propios agentes. Cada una resuelve una tarea entera, de principio a fin.

Las hace el equipo de [Orby](https://orbyos.es), un equipo de agentes de IA de código abierto que lleva el
contenido de una marca personal.

## Instálalas en 2 minutos

Necesitas [Claude Code](https://code.claude.com) con tu cuenta de Claude (sirve el plan Pro). Abre la **Terminal**
(en el Mac: `Cmd + espacio`, escribe «Terminal» e Intro), pega esta línea y pulsa Intro:

```bash
curl -fsSL https://raw.githubusercontent.com/OrbyOS/orby-skills/main/instalar.sh | bash
```

Instala todas las skills en `~/.claude/skills`. No instala programas ni toca nada más; puedes leer lo que hace en
[`instalar.sh`](instalar.sh). Si ya las tenías, las actualiza.

Luego abre Claude Code (o ciérralo y vuelve a abrirlo) y pídele lo que quieras con tus palabras. Por ejemplo:
«edítame este reel».

## ¿Por cuál empiezo?

| Si quieres… | Empieza por | Pídele a Claude |
| --- | --- | --- |
| Que te edite los reels: silencios, tomas falsas, subtítulos y vertical | [`editar-reels-con-claude`](editar-reels-con-claude) | «Edítame este reel» |
| Grabar una vez y sacar varios reels, sin leer guion | [`estructura-para-grabar`](estructura-para-grabar) | «Prepárame una estructura para grabar sobre…» |
| Que la IA edite con tu estilo y no repita errores | [`manual-de-edicion`](manual-de-edicion) | «Escribe mi manual de edición» |
| Ideas de vídeos a partir de lo que ya funciona en tu nicho | [`estudiar-videos-que-funcionan`](estudiar-videos-que-funcionan) | «Dime qué vídeos de estas cuentas merece la pena estudiar» |
| Que la IA deje de darte respuestas genéricas sobre tu negocio | [`lente-de-negocio`](lente-de-negocio) | «Hazme la entrevista de mi negocio» |
| Montar tu primer agente | [`reglas-de-un-agente`](reglas-de-un-agente) | «Quiero un agente que…» |
| Repartir todo el contenido entre agentes | [`equipo-de-contenido`](equipo-de-contenido) | «Monta mi equipo de contenido» |
| Saber qué dejarle a la IA y qué no | [`que-dejar-a-la-ia`](que-dejar-a-la-ia) | «¿Qué tareas de mi negocio puedo dejarle a la IA?» |
| El equipo entero de siete agentes, gratis en tu ordenador | [`instalar-orbyos`](instalar-orbyos) | «Instálame OrbyOS» |

Si no sabes cuál, empieza por **`editar-reels-con-claude`**: con un vídeo tuyo, en unos minutos ves lo que hace.

## Guías para leer

No hace falta instalar nada: se leen aquí mismo.

- [Instala OrbyOS en tu ordenador](guias/instalar-orbyos.md): el equipo de siete agentes de Orby funcionando en
  unos veinte minutos.
- [Frases que delatan que lo ha escrito una IA](guias/frases-que-delatan-a-la-ia.md), con una instrucción para que
  tu IA no escriba así.
- [Puntúa tu perfil de Instagram sobre 100](guias/puntua-tu-perfil.md) y sabrás qué arreglar primero.
- [Qué toca la IA de Meta en tus anuncios y dónde se apaga](guias/mejoras-ia-meta-ads.md).

---

## Otras formas de instalarlas

**Solo una skill.** Añade su nombre al final de la línea:

```bash
curl -fsSL https://raw.githubusercontent.com/OrbyOS/orby-skills/main/instalar.sh | bash -s editar-reels-con-claude
```

**Sin Terminal.**
1. Pulsa el botón verde **Code → Download ZIP** de esta página y descomprímelo.
2. Copia la carpeta de la skill dentro de la carpeta de skills de Claude (si la carpeta `skills` no existe, créala):
   - Mac y Linux: `~/.claude/skills/`. La carpeta `.claude` está oculta: en el Finder, `Cmd + Mayús + .` la enseña.
   - Windows: `C:\Users\TU_USUARIO\.claude\skills\`.

**En claude.ai, sin Claude Code.** Las skills que solo trabajan con texto también funcionan en la web y en la app
de Claude: `estructura-para-grabar`, `manual-de-edicion`, `lente-de-negocio`, `reglas-de-un-agente`,
`equipo-de-contenido` y `que-dejar-a-la-ia`. Pasos:
1. Comprime la carpeta de la skill en un ZIP.
2. En Claude, ve a **Customize → Skills** («Personalizar» si la tienes en español) y pulsa **Upload skill**.
3. Comprueba que tienes activada la ejecución de código en los ajustes.

Las que trabajan con archivos de tu ordenador (`editar-reels-con-claude`, `estudiar-videos-que-funcionan` e
`instalar-orbyos`) necesitan Claude Code.

## Qué es una skill

Una carpeta con instrucciones, y a veces scripts, que Claude carga cuando la necesita. Le enseña a hacer una tarea
concreta de principio a fin, siempre igual. Se instala una vez y luego se le pide en lenguaje normal. También se
puede llamar por su nombre: `/editar-reels-con-claude`.

La primera vez, cada skill comprueba qué te falta (por ejemplo, ffmpeg para el vídeo) y te dice cómo instalarlo.
No instala nada sin preguntarte.

## Tus datos

Las skills trabajan en tu ordenador. La edición de vídeo, transcripción incluida, no sube nada a ningún sitio. Lo
que hablas con Claude sigue las condiciones de tu cuenta de Claude.

## Licencia

MIT. Úsalas, cámbialas y compártelas como quieras. Ver [LICENSE](LICENSE).
