# Vídeos animados como los nuestros, hechos con IA

Las historias de miedo, los retos y los explicativos animados que ves en @orbyos no se editan a mano: Claude escribe el guion, una voz de IA lo narra y una herramienta gratuita convierte una página web animada en un vídeo vertical. Aquí tienes las piezas y los mensajes para hacer el primero sin saber editar.

Revisada el 9 de noviembre de 2026 con la documentación de HyperFrames (código abierto, de HeyGen, licencia Apache 2.0).

---

## Las piezas

| Pieza | Para qué | Coste |
| --- | --- | --- |
| **Claude Code** | Escribe el guion y programa cada escena | Incluido en el plan de pago de Claude |
| **HyperFrames** | Convierte las escenas (HTML animado) en un MP4 | Gratis, código abierto |
| **Una voz** | Narra el guion | Gratis con la voz del ordenador; ElevenLabs si quieres una voz natural |

Necesitas Node.js 22 o más reciente y FFmpeg. Si no los tienes, pídeselo a Claude Code: «Instálame Node 22 y FFmpeg».

## 1. Instala HyperFrames en Claude Code

En la terminal:

```text
claude plugin marketplace add heygen-com/hyperframes
claude plugin install hyperframes@hyperframes
```

## 2. El guion

Pégalo en Claude Code y cambia lo que va entre corchetes:

```text
Escríbeme el guion de un reel vertical de 40 segundos sobre [tu tema o tu historia].
Primera frase: un gancho que dé ganas de quedarse. Frases cortas, una idea por frase.
Al final: «Sígueme y comenta [PALABRA] y te paso [lo que regalas]».
Debajo de cada frase, describe la escena que se ve mientras se dice.
```

## 3. El vídeo

Cuando el guion te guste:

```text
Usando /hyperframes, convierte este guion en un vídeo vertical de 1080 x 1920.
Una escena por frase, animada palabra a palabra, con subtítulos grandes.
Colores: [tus colores]. Nada fijo en pantalla: todo entra y sale.
Genera la voz con [la voz del sistema / mi clave de ElevenLabs] y sincroniza cada escena con la frase que la nombra.
Renderiza el MP4 y enséñame fotogramas de cada escena antes de darlo por bueno.
```

## Cómo sacarle partido

- Pide fotogramas sueltos antes de renderizar entero: es más rápido corregir una escena que repetir el vídeo.
- Si una animación no te gusta, descríbela con un ejemplo («que el número caiga y rebote, como una moneda»).
- Cuando tengas un estilo que te guste, pídele que lo guarde como skill para que todos tus vídeos salgan iguales.

## Lo que conviene saber

- Renderizar usa mucho el ordenador: uno a la vez.
- Las imágenes, músicas y voces que metas tienen que ser tuyas o de uso libre.
