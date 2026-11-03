# SupoClip: la alternativa abierta a Opus Clip

SupoClip coge un vídeo largo, encuentra los mejores momentos y te los entrega en vertical, con la cara centrada y subtítulos palabra a palabra. Lo puedes usar en su web o montarlo en tu ordenador con Docker, sin marca de agua y sin límite de plan.

Revisada el 3 de noviembre de 2026 con su documentación (enlaces al final). Ese día tenía 2,5k estrellas en GitHub y licencia AGPL-3.0.

---

## Lo que hace

- **Elige los momentos:** una IA lee la transcripción y escoge de 3 a 7, con una nota por gancho, interés, valor y facilidad para compartir.
- **Recorta en vertical,** siguiendo la cara de quien habla.
- **Pone subtítulos** sincronizados por palabra y un titular arriba.
- **Lo edita y lo publica:** puedes recortar y unir clips, y exportar para Reels, TikTok o Shorts.
- **Acepta** YouTube, Twitch, Kick o tu propio archivo. Los directos, no.

## Dos formas de usarlo

| | Su web | En tu ordenador con Docker |
| --- | --- | --- |
| **Montaje** | Ninguno: entras en [supoclip.com](https://www.supoclip.com) | Docker y dos claves |
| **Coste** | Mira su web: no hemos podido leer sus precios | El programa, gratis. Pagas las claves o usas la vía local |
| **Límite** | El de su plan | El de tu ordenador |
| **Tus vídeos** | Pasan por sus servidores | En tu ordenador, salvo lo que mandes a esas claves |

Para probarlo, empieza por la web. Si te convence y lo vas a usar mucho, móntalo.

## Montarlo con Claude Code

Necesitas [Docker](https://www.docker.com/products/docker-desktop/), una clave de [AssemblyAI](https://www.assemblyai.com/) para transcribir y una clave de un modelo (Google, OpenAI o Anthropic). Pega esto en Claude Code (capítulo 3.2):

```text
Monta SupoClip en mi ordenador siguiendo https://github.com/FujiwaraChoki/supoclip y su guía de Docker. Pídeme permiso antes de instalar nada. Crea el archivo .env vacío y ábremelo para que yo pegue las claves: no me las pidas ni las leas. Cuando esté, comprueba que abre en http://localhost:3107 y dime si algo ha fallado.
```

Si no quieres ninguna clave, tiene una vía local con Whisper y Ollama. Su [guía](https://www.supoclip.com/blog/self-host-supoclip-docker) la explica. Va más lenta y depende de tu ordenador:

```text
Mira mi ordenador y dime si puede con la vía totalmente local de SupoClip, con Whisper y Ollama. Si no, dímelo antes de instalar nada.
```

## Tu primer clip

1. Crea tu cuenta local en `http://localhost:3107` y pega el enlace de un vídeo tuyo de unos 20 minutos.
2. Espera a que termine y ordena los clips por su nota.
3. Míralos todos. Quédate con los que se entienden solos desde el primer segundo.
4. Corrige los subtítulos: los nombres propios y las cifras son lo que más falla.

**La nota es una opinión de la IA, no una predicción.** Lo que de verdad te dice qué funciona son tus datos (capítulo 5.13).

Usa solo vídeos tuyos o de quien te haya dado permiso. Si prefieres no montar nada y hacerlo con Claude Code, mira el capítulo 5.12.

## En resumen

- De un vídeo largo a clips verticales con subtítulos, cara centrada y titular.
- Web para probar, Docker para usarlo a lo grande.
- El programa es gratis; las claves de transcripción y del modelo, no, salvo con la vía local.
- Revisa cada clip y corrige los subtítulos antes de publicar.

---

## Fuentes

- SupoClip: [repositorio y documentación](https://github.com/FujiwaraChoki/supoclip) (funciones, opciones, requisitos y licencia) y [guía para montarlo](https://www.supoclip.com/blog/self-host-supoclip-docker).

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
