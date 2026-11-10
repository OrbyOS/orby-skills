# La palabra clave de Instagram, sin ManyChat

Alguien comenta una palabra en tu reel y le llega el enlace por privado. Es lo que hacen las herramientas de
mensajes automáticos con suscripción, pero Instagram tiene una conexión oficial que te deja hacerlo a ti. Con Claude
Code se monta en una tarde, sin saber programar.

Revisada el 30 de octubre de 2026 con la documentación oficial de Meta para desarrolladores (enlaces al final).

---

## 1. Qué consigues y qué te hace falta

Lo que hace, en orden:
1. Alguien comenta la palabra en tu reel.
2. Le contestas en público, con una frase distinta cada vez.
3. Le llega un mensaje privado con un botón: «Mándamelo».
4. Lo pulsa y le llega el enlace.
5. Una hora después, una pregunta para saber qué tal le ha ido.

Lo que hace falta:

| Qué | Por qué |
| --- | --- |
| **Una cuenta profesional de Instagram** (de empresa o de creador) | La conexión oficial no funciona con cuentas personales |
| **Una app en Meta for Developers** | Es la que pide permiso para leer comentarios y mandar mensajes. Crearla es gratis |
| **Un servidor con https** | Meta avisa de cada comentario a una dirección web tuya. Sirve un servidor pequeño de pocos euros al mes, o uno que ya tengas |
| **Que Meta dé la app por buena** | Mientras está en desarrollo, solo puedes escribir a cuentas que tengan un papel en la app (la tuya, para probar) |

> [!NOTE]
> «Gratis» quiere decir sin suscripción mensual. El servidor, si no lo tienes, sí tiene un coste pequeño.

## 2. Cómo funciona por dentro

- **El aviso (webhook):** cada vez que alguien comenta o te escribe, Meta manda los datos a una dirección de tu
  servidor. Antes de empezar, Meta comprueba que esa dirección es tuya con una palabra secreta que eliges tú.
- **La comprobación:** tu servidor mira si el comentario lleva la palabra (sin importar mayúsculas ni tildes) y en
  qué reel está.
- **Las respuestas:** contesta en público al comentario y manda el privado, las dos cosas por la conexión oficial.

Los permisos que pide la app son tres: leer la cuenta, gestionar los comentarios y gestionar los mensajes.

## 3. La trampa: un solo mensaje

Meta solo te deja mandar **un mensaje privado por comentario**, y en los 7 días siguientes al comentario. Después ya
no puedes volver a escribir a esa persona hasta que te conteste. Cuando contesta, tienes **24 horas** para escribirle.

Si el primer mensaje lleva el enlace, ahí se acaba la conversación. Por eso el primero no lleva el enlace, sino un
botón:

1. **Primer mensaje:** «¿Te lo mando?», con el botón **Mándamelo**.
2. **Lo pulsa:** pulsar el botón cuenta como una respuesta, así que se abren las 24 horas.
3. **Segundo mensaje:** el enlace.
4. **Una hora después:** una pregunta corta («¿Te ha servido?»), todavía dentro de las 24 horas.

Además de entregar el enlace, así empiezas una conversación con quien te ha comentado.

## 4. Los frenos, para que no parezca un robot

- **Nunca dos veces a la misma persona** por la misma palabra en el mismo reel, aunque comente cinco veces.
- **Un tope al día**, por ejemplo 100 mensajes. Si un reel se dispara, los demás comentarios esperan al día
  siguiente.
- **Respuestas públicas variadas:** cinco u ocho frases distintas, que se alternan. La misma frase cien veces seguidas
  es lo que más delata a un robot.
- **Si falla un envío, se apunta y no se repite en bucle.**

## 5. Montarlo con Claude Code

### Paso 1. La app de Meta (lo haces tú)

1. Entra en **developers.facebook.com** con tu cuenta y crea una app de empresa.
2. Añádele el producto **Instagram**, con la opción de inicio de sesión de Instagram.
3. Conecta tu cuenta profesional y genera el **token** de acceso de la cuenta.
4. Apunta la **clave secreta de la app**: sirve para comprobar que los avisos vienen de Meta.

> [!CAUTION]
> El token y la clave secreta dan acceso a tu cuenta. No los pegues en el chat ni en el código: guárdalos en un
> archivo `.env` en el servidor y dile a Claude que los lea de ahí. Nunca los subas a un repositorio público.

### Paso 2. El servidor (lo hace Claude)

Abre Claude Code en una carpeta nueva y pídeselo así:

```text
Móntame un servidor pequeño para responder por privado a quien comente una palabra en mis reels de Instagram, con
la API oficial de Instagram (inicio de sesión de Instagram). Lee el token y la clave secreta de un archivo .env.
Tiene que:
1. Tener la dirección de avisos de Meta: responder a la comprobación con mi palabra secreta y comprobar la firma de
   cada aviso con la clave secreta.
2. Suscribir la cuenta a los avisos de comentarios y de mensajes.
3. Si un comentario lleva la palabra [PALABRA] (sin importar mayúsculas ni tildes), contestar en público con una de
   estas frases, alternándolas: [frases]. Y mandar una respuesta privada al comentario con el texto [mensaje] y un
   botón de respuesta rápida «Mándamelo».
4. Cuando la persona pulse el botón o conteste, mandarle [enlace]. Una hora después, si siguen dentro de las 24
   horas, preguntarle [pregunta].
5. No escribir nunca dos veces a la misma persona por la misma palabra en el mismo reel, y no pasar de 100 mensajes
   al día.
6. Guardar cada envío y cada error en una base de datos pequeña.
Explícame cada paso antes de hacerlo y dime al final qué tengo que pegar en el panel de Meta.
```

### Paso 3. Conectar los avisos (lo haces tú, con lo que te diga Claude)

En el panel de tu app, en la configuración de Instagram, pega la **dirección de avisos** de tu servidor y la
**palabra secreta**. Meta la comprueba al guardar. Después, activa los avisos de **comentarios** y **mensajes**.

### Paso 4. Probar

Mientras la app está en desarrollo, prueba con una cuenta que tenga un papel en la app: comenta la palabra en un reel
tuyo y mira que llegue todo, en orden. Si algo falla, pásale a Claude el error que haya guardado.

### Paso 5. Que Meta apruebe la app

Para que funcione con cualquier persona y no solo en pruebas, la app tiene que salir del modo de desarrollo y
publicarse. Según tu caso, Meta te pedirá antes una **revisión** de los permisos de comentarios y mensajes: explicar
para qué los usas y, normalmente, un vídeo corto de la app funcionando. Si la app va a servir a cuentas de otros (las
de tus clientes, por ejemplo), además necesita el acceso avanzado. Claude te puede ayudar a redactar la explicación.

## 6. Si no llega el mensaje

- **Mira en las solicitudes de mensajes:** si la persona no te sigue, el privado llega ahí.
- **¿Han pasado más de 7 días desde el comentario?** Meta ya no deja contestarlo por privado.
- **¿La app sigue en modo de desarrollo?** Solo llega a cuentas con un papel en la app.
- **El token caduca a los 60 días:** pídele a Claude que lo renueve solo antes de que caduque.

## 7. En resumen

- Instagram te deja responder por privado a un comentario con su conexión oficial, sin suscripción.
- Un solo mensaje por comentario: el primero lleva un botón, y el enlace llega cuando lo pulsan.
- Frenos: una vez por persona y reel, y un tope al día.
- Hace falta una cuenta profesional, una app de Meta publicada y un servidor con https.

---

## Fuentes

- Meta for Developers: [respuestas privadas](https://developers.facebook.com/docs/instagram-platform/private-replies),
  [API de Instagram con inicio de sesión de Instagram](https://developers.facebook.com/docs/instagram-platform/instagram-api-with-instagram-login),
  [avisos (webhooks)](https://developers.facebook.com/docs/instagram-platform/webhooks) y
  [mensajes](https://developers.facebook.com/docs/instagram-platform/instagram-api-with-instagram-login/messaging-api).

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
