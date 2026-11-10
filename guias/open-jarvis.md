# OpenJarvis: tu asistente personal, en tu ordenador

OpenJarvis es un proyecto abierto desarrollado en dos laboratorios de Stanford, Hazy Research y Scaling Intelligence Lab, para tener una IA personal que funciona
en tu propio ordenador en lugar de en un servidor ajeno. Puede resumirte el día a partir de tu correo y tu calendario, y leértelo en voz alta. Y lo puede instalar Claude Code por ti.

Revisada el 3 de noviembre de 2026 con su documentación (enlaces al final). Ese día tenía 13k estrellas en GitHub y licencia Apache-2.0.

> [!IMPORTANT]
> **Local, con un matiz.** El modelo de texto corre en tu ordenador, pero la voz del resumen diario usa por defecto Cartesia u OpenAI, con tu clave y fuera de tu ordenador. Si
> quieres que todo se quede en casa, pide a Claude que lo configure con un motor de voz local, como Kokoro, que aparece en su documentación.

---

## Instálalo con Claude Code

Abre Claude Code (capítulo 3.2) en una carpeta nueva y pega este mensaje:

```text
Instala OpenJarvis siguiendo https://github.com/open-jarvis/OpenJarvis y su documentación. Antes de empezar, mira mi ordenador y dime qué modelo local
me conviene y cuánto espacio ocupará. Pídeme permiso antes de instalar. Cuando termine, comprueba que funciona con `jarvis doctor`, hazle una pregunta de prueba y dime qué ha contestado.
Si le falta algo o algo falla, dímelo. No conectes ninguna cuenta todavía.
```

Si lo prefieres a mano, en Mac o Linux basta con una línea, y en Windows y para escritorio hay [otras opciones](https://github.com/open-jarvis/OpenJarvis#installation):

```bash
curl -fsSL https://open-jarvis.github.io/OpenJarvis/install.sh | bash
```

Instala lo que necesita, incluidos Ollama y un primer modelo. Calculan unos 3 minutos con buena conexión, y después `jarvis` arranca el chat. Los modelos grandes siguen bajando en segundo plano.

## Conecta Gmail y el calendario

Hazlo cuando el chat te funcione. Una sola autorización de Google cubre Gmail, Calendar y Tasks:

```bash
jarvis init --preset morning-digest-mac --force
jarvis connect gdrive
jarvis digest --fresh
```

Si usas Linux, cambia el primero por `morning-digest-linux`, o por `morning-digest-minimal` para una versión reducida. Ojo: `--force` sustituye la configuración que tuvieras.

La primera línea deja preparado el resumen, la segunda abre la autorización en tu navegador y la tercera genera y reproduce tu primer resumen. Para que te hable, añade la clave de voz siguiendo su [guía del resumen](https://open-jarvis.github.io/OpenJarvis/user-guide/morning-digest/).

## Qué más trae

| Modo | Para qué |
| --- | --- |
| `morning-digest` | Resumen hablado del día con correo, calendario, salud y noticias |
| `deep-research` | Investiga en tus documentos, con citas |
| `code-assistant` | Agente que ejecuta código y toca archivos |
| `scheduled-monitor` | Vigila algo con una frecuencia y con memoria |
| `chat-simple` | Conversación, sin herramientas |

Empieza por `chat-simple` y el resumen. `code-assistant` puede usar tu terminal, así que déjalo para cuando sepas revisar lo que hace.

## Qué esperar

Un modelo pequeño en tu ordenador no rinde como Claude. Para resumir tu correo y responder lo cotidiano puede bastar. Para trabajo difícil, la calidad y la velocidad dependen de tu
máquina y del modelo. Prueba con esto y juzga tú:

```text
Resume mis correos de hoy en cinco líneas. Cita de cada punto quién lo envía. Si no estás seguro de algo, dilo y no lo completes.
```

> [!CAUTION]
> **Un correo puede traer instrucciones escondidas para la IA.** Si le das permiso para actuar, no solo para leer, alguien de fuera podría colarle órdenes. Empieza solo leyendo y revisa cualquier acción antes de aprobarla.

## En resumen

- Proyecto abierto de dos laboratorios de Stanford, con modelo en tu ordenador.
- Pégale el mensaje a Claude Code y deja que lo instale.
- Una autorización de Google y ya puedes tener un resumen hablado de tu día.
- La voz sale por defecto de un servicio externo: hay que elegir un motor local si no quieres eso.
- Empieza solo leyendo.

---

## Fuentes

- OpenJarvis: [repositorio](https://github.com/open-jarvis/OpenJarvis) (laboratorios, instalación, modos y agentes), [web del proyecto](https://openjarvis.stanford.edu/) y [guía del resumen diario](https://open-jarvis.github.io/OpenJarvis/user-guide/morning-digest/).

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
