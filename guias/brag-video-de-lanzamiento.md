# /brag: convierte tu proyecto en un vídeo de lanzamiento con Claude

/brag es una skill gratuita que lee tu proyecto, decide qué contar y te entrega un vídeo corto de lanzamiento con música y animaciones, más el texto para publicarlo. Sin escribir un prompt largo.

Revisada el 13 de noviembre de 2026.

---

## Qué necesitas

- Claude Code (o otro agente que use skills, como Codex u opencode).
- Node.js 22 o superior.
- FFmpeg instalado en tu ordenador.
- Hyperframes, que hace el montaje: compruébalo con `npx hyperframes doctor`.

## Cómo instalarla

Dentro de Claude Code:

```
/plugin marketplace add latent-spaces/brag
/plugin install brag@brag
```

O, para cualquier agente:

```
npx skills add https://github.com/latent-spaces/brag --skill brag
```

## Cómo usarla

1. Abre Claude Code dentro de la carpeta de tu proyecto.
2. Escribe `/brag`.
3. Claude lee el proyecto, elige el ángulo y los momentos que enseñar, y monta el vídeo.

Al terminar tienes una carpeta `brag-output/` con:

- `brag.mp4`, el vídeo.
- El texto para compartirlo.
- El plan que ha seguido.

## Opciones

- `--tone "..."` para cambiar el tono. Por ejemplo: `/brag --tone "anuncio de lanzamiento serio"`.
- `--voice` para que le ponga voz en off (por defecto va sin voz).

## Lo que conviene saber

- Lee tu proyecto, no tu web: tienes que tenerlo en tu ordenador. Si solo tienes la web, hay un servicio aparte (letsbrag.app) que lo hace a partir del enlace.
- La música que trae es de licencia libre (CC BY 4.0): si publicas el vídeo, cita al autor como pide la licencia.
- Revisa el vídeo antes de publicarlo: lo que cuenta sale de tu código y puede exagerar o quedarse corto.
