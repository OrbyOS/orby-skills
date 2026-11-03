# Nueve apps gratis de GitHub para dejar de pagar suscripciones

Hay proyectos abiertos que sustituyen a herramientas de pago: Notion, Loom, Calendly, Semrush y otras. Aquí tienes nueve, con lo
que sustituyen, lo que hay que instalar y lo que pierdes, que es lo que no suele contarse. Porque casi nunca es gratis del todo.

Revisada el 3 de noviembre de 2026 con la documentación y las páginas de precios de cada proyecto (enlaces en cada una). No las hemos
instalado todas: lo que sigue viene de esa documentación. Las estrellas son de ese día.

> [!IMPORTANT]
> **Gratis no es sin coste.** En las que van en un servidor, el servidor lo pagas tú y las actualizaciones, las copias de seguridad, la
> seguridad y los fallos son cosa tuya. Si guardan datos de clientes, también la responsabilidad. Si tu hora vale más que la
> suscripción, paga la suscripción.

---

## De un vistazo

| App | Sustituye a | Dónde va | Lo que te puede costar |
| --- | --- | --- | --- |
| **OpenWhispr** | Wispr Flow, Granola | Tu ordenador | Nada con modelos locales |
| **VoiceStudio** | ElevenLabs | Tu ordenador | Nada, pero con límites de licencia |
| **AppFlowy** | Notion | Tu ordenador o servidor | Nada para uso personal, con poco espacio |
| **Cap** | Loom | Tu ordenador | Licencia de 29 $ al año si es para trabajar |
| **Open Generative AI** | Higgsfield y similares | Tu ordenador | Cada generación, salvo con modelos locales |
| **OpenSEO** | Semrush, Ahrefs | Servidor | Datos de pago: recarga mínima de 50 $ |
| **Chatwoot** | Intercom, Zendesk | Servidor | Servidor y tiempo |
| **OpenProject** | Jira, Asana | Servidor | Servidor y tiempo |
| **Cal.diy** | Calendly | Servidor | Servidor y tiempo. No es para producción |

Empieza por las que se descargan. Son las que menos te complican la vida.

---

## Las que se descargan

### OpenWhispr: dictar con tu voz en cualquier programa

[Repositorio](https://github.com/OpenWhispr/openwhispr) · 10,6k estrellas · MIT · Mac, Windows y Linux

- **Sustituye a:** Wispr Flow y Granola: pulsas una tecla, hablas y el texto aparece. También transcribe reuniones.
- **Instalar:** descargar y abrir.
- **Lo que pierdes:** su [plan gratuito](https://openwhispr.com/pricing) da dictado local ilimitado, pero su nube se queda en 2.000
  palabras a la semana y 5 horas de reuniones al mes. El modo agente, la sincronización y la app del iPhone son de pago. Sin nube,
  la velocidad y la calidad dependen del modelo y de tu ordenador.

### VoiceStudio: clonar voces y doblar vídeos

[Repositorio](https://github.com/debpalash/VoiceStudio) · 99,6k estrellas · AGPL-3.0 · Mac, Windows y Linux

- **Sustituye a:** ElevenLabs.
- **Instalar:** descargar y bajar el modelo que elijas. Sin tarjeta gráfica funciona, pero más lento.
- **Lo que pierdes:** el modelo que trae por defecto es de **uso no comercial**, según su propio inventario. Mira el capítulo 5.16 antes de usarlo en un negocio.

### AppFlowy: tus documentos y tareas

[Repositorio](https://github.com/AppFlowy-IO/AppFlowy) · 78,1k estrellas · AGPL-3.0 · Ordenador, iPhone y Android

- **Sustituye a:** Notion.
- **Instalar:** descargar. También hay [guía para tu propio servidor](https://appflowy.com/docs/Step-by-step-Self-Hosting-Guide---From-Zero-to-Production), más trabajosa.
- **Lo que pierdes:** su [plan gratuito](https://appflowy.com/pricing) es para una persona, con 100 MB, archivos de hasta 7 MB, historial
  de 7 días y la IA como prueba limitada. El de pago cuesta 12 $ por persona al mes con pago anual.

### Cap: grabar tu pantalla y compartirla

[Repositorio](https://github.com/CapSoftware/Cap) · 24,3k estrellas · AGPL-3.0 · Mac, Windows y Linux

- **Sustituye a:** Loom.
- **Instalar:** descargar y crear una cuenta. Autoalojar es opcional, con Docker.
- **Lo que pierdes:** en su [página de precios](https://cap.so/pricing) el plan gratuito **no incluye el uso comercial**, y deja 25 enlaces al
  mes de hasta 5 minutos, sin nube ni IA. Para trabajar, la licencia de escritorio cuesta 29 $ al año o 58 $ una sola vez. Cap Pro, 12 $ al mes.

### Open Generative AI: imagen y vídeo con muchos modelos

[Repositorio](https://github.com/Anil-matcha/Open-Generative-AI) · 32,1k estrellas · MIT · Mac, Windows y Linux

- **Sustituye a:** Higgsfield y estudios parecidos. Antes se llamaba Open Higgsfield AI, y ese nombre lo usan también otros proyectos: comprueba que sea este.
- **Instalar:** descargar. En Windows puede saltar un aviso porque el instalador no está firmado.
- **Lo que pierdes:** el programa es gratis, pero la mayoría de sus modelos se generan por MuAPI, con tu clave y a tu cargo. Mira sus precios
  antes. En local es gratis, pero más limitado: imágenes con el motor incluido, y vídeo solo con otra instalación y tarjeta gráfica CUDA o ROCm, así que no directamente en un Mac.
- **Cuidado:** presume de no tener filtros de contenido. Eso no te quita ninguna responsabilidad: nada de personas reales sin su permiso ni de marcas ajenas.

---

## Las que necesitan un servidor

Para estas, mira antes el capítulo 3.7, y pídele a Claude que te explique cada paso antes de ejecutarlo. Haz copias de seguridad desde el primer día.

### OpenSEO: palabras clave, posiciones y enlaces

[Repositorio](https://github.com/every-app/open-seo) · 26,2k estrellas · MIT

- **Sustituye a:** Semrush y Ahrefs, con conexión para Claude Code.
- **Instalar:** Docker, o Cloudflare, que funciona con su plan gratuito.
- **Lo que pierdes:** los datos no son gratis. Necesitas una clave de [DataForSEO](https://dataforseo.com/pricing), con recarga mínima de 50 $ y 1 $ de prueba, y
  pagas por consulta. Menos herramientas que una suite grande. Su versión alojada se puede probar gratis y cuesta 10 $ al mes más un 28 % sobre las consultas.

### Chatwoot: atención al cliente en una sola bandeja

[Repositorio](https://github.com/chatwoot/chatwoot) · 38,8k estrellas · MIT, salvo su parte enterprise

- **Sustituye a:** Intercom y Zendesk: web, correo, WhatsApp, Instagram y más.
- **Instalar:** Docker o los despliegues que indica su documentación. Conectar cada canal lleva su propio trabajo.
- **Lo que pierdes:** su [edición gratuita](https://www.chatwoot.com/pricing/self-hosted-plans/) no trae Captain, su agente de IA, ni llamadas, marca
  propia, roles ni capacidad por agente. Si la conversación se queda sin responder porque el servidor se ha caído, es cosa tuya.

### OpenProject: proyectos y equipos

[Repositorio](https://github.com/opf/openproject) · 17k estrellas · GPL-3.0

- **Sustituye a:** herramientas como Jira y Asana, para planificar proyectos, tareas y tiempos. Su tabla de ediciones dice qué funciones entran gratis.
- **Instalar:** tiene [guías para instalarlo](https://www.openproject.org/docs/) y una prueba de 14 días en su nube.
- **Lo que pierdes:** en su [edición gratuita](https://www.openproject.org/pricing/) no hay planificador de equipo ni gestión de recursos, y el soporte
  es comunitario. Está pensado para equipos: para una o dos personas, seguramente es demasiado.

### Cal.diy: que te reserven citas

[Repositorio](https://github.com/calcom/cal.diy) · 49,7k estrellas · MIT

- **Sustituye a:** Calendly. Es la edición comunitaria de Cal.com.
- **Instalar:** Docker o Node.js con PostgreSQL. Ellos mismos dicen que pide conocimientos avanzados de servidores.
- **Lo que pierdes:** **su propia documentación lo recomienda solo para uso personal y fuera de producción**, y para uso comercial remite a Cal.com. No
  trae equipos, flujos automáticos, estadísticas ni inicio de sesión de empresa. Si tu agenda es clave para vender, no es esta.

---

## Antes de instalar cualquiera

Pégale esto a Claude:

```text
Estoy pensando en sustituir [herramienta de pago] por [proyecto y enlace]. Pago [precio] al mes y lo uso para [para qué]. Lee su
documentación y su página de precios, y dime: qué función mía se pierde, cuánto me costaría de verdad contando servidor y servicios de pago,
si su licencia permite mi uso, cuándo fue su último cambio y cuánto trabajo me daría al mes. Si no merece la pena, dímelo. No instales nada.
```

Y antes de cancelar nada:

- **Pruébala una semana a la vez** que la de pago.
- **Saca tus datos antes** y comprueba que los puedes llevarte de vuelta.
- **Lee la licencia si es para vender.** Las AGPL piden compartir el código si ofreces una versión modificada por internet.

## En resumen

- Empieza por las que se descargan: OpenWhispr, AppFlowy, Cap y VoiceStudio.
- Gratis de verdad son pocas. OpenSEO y Open Generative AI cobran por lo que generas o consultas.
- Cap, VoiceStudio y Cal.diy tienen límites para usarlos en un negocio: léelos.
- Autoalojar sale a cuenta si tu tiempo sale más barato que la suscripción.
- Prueba las dos a la vez antes de cancelar.

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
