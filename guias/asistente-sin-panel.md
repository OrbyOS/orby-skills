# Un asistente sin panel: tus redes se publican solas

Muchos «paneles de IA» lucen mucho y no hacen nada: cifras, gráficos y luces que alguien tiene que mirar. Un asistente de verdad no necesita pantalla. Necesita tres cosas: **qué** tiene que hacer, **con qué** lo hace y **cuándo** lo hace. Aquí tienes cómo montarlo para publicar en redes: una tabla, tres conexiones y un reloj. Se lo pides a Claude y te lo monta.

Revisada el 9 de noviembre de 2026. Es como publicamos en @orbyos: cada reel sale solo a su hora y su fila se marca sola como publicada.

---

## 1. Las herramientas

| Pieza | Para qué | Qué usamos nosotros |
|---|---|---|
| Una tabla | La lista de lo que sale: vídeo, texto, hora y estado | Un archivo de texto con una tabla. Te vale una hoja de cálculo |
| Conexión para publicar | Subir el vídeo con su texto | La API oficial de Instagram (publicación de contenido) |
| Conexión para medir | Leer vistas, tiempo de visionado y comentarios de cada publicación | La misma API, en su parte de estadísticas |
| Conexión para contestar | Responder a quien comenta la palabra clave | La misma API, en su parte de mensajes |
| Un reloj | Que se ejecute a cada hora marcada, aunque tú duermas | Un temporizador en un servidor pequeño. Para empezar, tu ordenador encendido |
| Claude Code | Escribe el programa, lo prueba y lo arregla | Claude Code |

Hace falta una cuenta profesional de Instagram y una app de Meta para desarrolladores con permiso para publicar. No hace falta ningún panel.

## 2. El mensaje para Claude

```text
Quiero que mis vídeos de Instagram se publiquen solos, sin panel.
1. Hazme una tabla con estas columnas: vídeo, texto, hora y estado (pendiente o publicado).
2. Escribe un programa que, a cada hora de la tabla, publique el primer vídeo pendiente con la API oficial de Instagram, marque su fila como publicada y apunte el enlace.
3. Que una vez al día lea las estadísticas de cada publicación y las añada a la tabla.
4. Explícame sin tecnicismos qué tengo que crear en Meta y dónde guardar las claves. No me las pidas en el chat.
5. Antes de nada, pruébalo con un vídeo y en modo prueba.
```

## 3. Cómo se usa cada día

1. Creas el contenido.
2. Lo añades a la tabla con su hora.
3. Sale solo. Tú solo revisas que la fila pone «publicado» y miras los números.

**La prueba:** si sigue trabajando mientras duermes, es un asistente. Si solo te enseña gráficos, es decoración.

## Lo que conviene saber

- Las claves de Meta dan acceso a tu cuenta: en un archivo que no se suba a ningún sitio, nunca en un chat.
- Meta limita cuántas publicaciones puedes hacer al día por la API. Para una cuenta normal, caben de sobra.
- Empieza con una conexión, la de publicar, y añade las otras dos cuando funcione.

## Fuentes

- [Meta para desarrolladores: publicación de contenido en Instagram](https://developers.facebook.com/docs/instagram-platform/content-publishing).
- [Meta para desarrolladores: estadísticas de Instagram](https://developers.facebook.com/docs/instagram-platform/insights).

---
