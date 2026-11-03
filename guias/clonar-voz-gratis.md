# Clonar tu voz gratis, en tu ordenador

VoiceStudio es un programa abierto que clona una voz a partir de una grabación limpia y genera audio en tu propio ordenador, sin
pagar por minuto y sin subir tu voz a ninguna nube. Aquí tienes cómo probarlo con tu voz y lo que debes mirar antes de usarlo en un
negocio, porque ahí está la letra pequeña.

Revisada el 3 de noviembre de 2026 con su documentación (enlaces al final). Ese día tenía 99,6k estrellas en GitHub y licencia AGPL-3.0, y
anunciaba 646 idiomas. No lo hemos probado: de la calidad en español no podemos decir nada. Juzga tú con tu propio oído.

> [!CAUTION]
> **Solo tu voz, o la de alguien que te haya dado permiso.** Es lo que pide el propio proyecto. Clonar la voz de otra persona sin
> permiso, para hacerla decir algo o para engañar a alguien, te puede traer problemas legales. Si es de un cliente o de alguien del
> equipo, pide el permiso por escrito y di para qué lo vas a usar.

> [!IMPORTANT]
> **Para probar es gratis. Para vender, mira la licencia del modelo.** El programa permite el uso comercial, pero cada modelo tiene sus
> condiciones. Según el inventario del propio proyecto, **el modelo que trae por defecto, OmniVoice, es de uso no comercial**. Más abajo
> te contamos qué hacer.

---

## Lo que hace falta

| Tu ordenador | Qué esperar |
| --- | --- |
| **Mac con Apple Silicon** | Compatible desde macOS 13.3 |
| **Windows 10 u 11 de 64 bits** | Con tarjeta NVIDIA o AMD, o solo con el procesador |
| **Linux de 64 bits** | Con NVIDIA, o solo con el procesador |
| **Mac con Intel** | Limitado: el programa se abre, pero el trabajo lo tiene que hacer otro ordenador |

Sin tarjeta gráfica se puede usar, pero va más lento. Reserva espacio en el disco para los modelos, que ocupan bastante. El programa te
pregunta antes de descargar cada uno.

## 1. Instálalo

Descárgalo de la [última versión](https://github.com/debpalash/VoiceStudio/releases/latest) en GitHub: el DMG si tienes Mac y el instalador
EXE si tienes Windows. Bájalo solo de ahí o de `voicestudio.sh`. El proyecto se llamó antes OmniVoice Studio, y hay copias con nombres parecidos.

Si el Mac dice que está dañado y no se puede abrir, el proyecto explica que es el sistema bloqueando la app, y tiene una
[guía](https://github.com/debpalash/VoiceStudio/blob/main/docs/install/macos.md) para ello. Léela antes de saltarte ese aviso: solo debes hacerlo con un
programa que hayas bajado de la fuente oficial.

## 2. Graba tu voz

Lo único que pide la documentación es una grabación limpia. El resto son consejos nuestros:

- Una habitación sin eco ni ruido, y el micrófono de siempre a la misma distancia.
- Habla como hablas de verdad, sin leer como un locutor.
- Solo tu voz, sin música de fondo.
- Prueba con unos 30 segundos, y compara con una toma distinta si no te convence.

No uses un audio descargado de otra persona, ni siquiera para probar.

## 3. Genera y compara

1. Abre **Voice cloning** y añade tu grabación.
2. Escribe un texto en español y elige el idioma. Deja el modelo por defecto para la primera prueba.
3. Genera, y escúchalo con los ojos cerrados al lado de tu voz real.

Texto de prueba que pone en apuros a cualquier clon:

```text
¿Sabes qué es lo primero que le pregunto a un cliente? Pues mira: cuánto paga hoy, 1.250 euros al mes, y qué pasaría si dejase de
pagarlos. Lo apuntas en una hoja de Excel, y en un rato lo tienes. ¡Ya verás!
```

Fíjate en las preguntas, las cifras, las palabras en inglés y si suena a acento español. Si falla, la solución suele ser probar otro modelo, y
la app te deja elegir entre varios en **Model Manager**.

## 4. Si es para tu negocio

Si vas a usar la voz en anuncios, en vídeos de tu marca o en un servicio, no te quedes en el modelo por defecto:

1. Abre **Model Manager** y mira la licencia que enseña cada modelo.
2. Descarta los que digan «no comercial» o NC.
3. Lee la licencia del que elijas en su página. El propio proyecto avisa de que **todavía no ha dado por revisado ningún modelo para uso
   comercial**. Lo que muestra es información de cada modelo, no un permiso suyo.

Otra opción para comparar es [Voicebox](https://github.com/jamiepine/voicebox) (59,3k estrellas, licencia MIT, 23 idiomas). Trae varios motores, entre
ellos Chatterbox Multilingual, que su creador publica con licencia MIT y con español entre sus idiomas. Comprueba la licencia del motor que elijas y pruébalo con el mismo texto. Según su creador, el audio de Chatterbox lleva una marca de agua.

Si tu voz te da de comer o el proyecto es importante, a veces compensa pagar un servicio con licencia clara. Pide consejo legal si hay dudas.

## Cuidados

- **Di que es sintética cuando toque.** Las plataformas y la ley pueden pedir que avises de que un audio está generado con IA. Compruébalo antes de publicar, y no lo hagas pasar por una grabación real.
- **Protege tu grabación.** Con tu voz, otros también pueden clonarte. No compartas la carpeta ni el audio. Y no uses la voz como contraseña en tu banco o en ningún sitio.
- **Escúchalo todo antes de publicar.** Un clon se puede equivocar en una cifra o en un nombre, y sonará igual de seguro.
- **Si abres su API,** su documentación da una clave para el acceso. Déjala en tu ordenador: no la expongas a internet.

## En resumen

- VoiceStudio clona voces en tu ordenador: gratis, sin nube y con muchas opciones de instalación.
- Solo tu voz, o la de alguien que te haya dado permiso.
- El modelo por defecto es de uso no comercial. Para probar vale; para vender, elige otro y lee su licencia.
- Juzga tú la calidad en español, con un texto difícil.
- Avisa cuando toque y escucha todo antes de publicar.

---

## Fuentes

- VoiceStudio: [repositorio y documentación](https://github.com/debpalash/VoiceStudio) (funciones, plataformas y uso responsable),
  [aviso de licencia](https://github.com/debpalash/VoiceStudio/blob/main/LICENSE-NOTICE.md) e [inventario de licencias de
  modelos](https://github.com/debpalash/VoiceStudio/blob/main/docs/licensing/model-inventory.md).
- [Voicebox](https://github.com/jamiepine/voicebox) y [Chatterbox](https://huggingface.co/ResembleAI/chatterbox) (licencia, idiomas y marca de agua).

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
