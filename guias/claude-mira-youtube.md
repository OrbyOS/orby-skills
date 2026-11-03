# Que Claude aprenda de un vídeo de YouTube y lo convierta en skill

Claude no puede ver un vídeo de YouTube desde un enlace. Gemini, la IA de Google, sí. Esta guía los junta: una skill le pasa el
enlace a Gemini, Claude recibe lo que hay en el vídeo y, con varios vídeos del mismo tema, lo convierte en una skill que
usarás siempre.

Revisada el 3 de noviembre de 2026 con la documentación de Google y de Claude Code (enlaces al final). No lo hemos ejecutado de
principio a fin: necesita una clave de Google de cada persona. Pide siempre una prueba con un vídeo corto antes de fiarte.

---

## Las tres piezas

| Pieza | Para qué |
| --- | --- |
| **Una clave de Gemini** | Te identifica ante Google. Sale de Google AI Studio |
| **Una skill que llama a Gemini** | Le pasa el enlace y guarda en un archivo lo que devuelve |
| **El creador de skills** | Convierte lo aprendido en una skill tuya |

## Lo que cuesta y sus límites

Según la documentación de Google, a fecha de esta guía:

- Pasar enlaces de YouTube a la API de Gemini está **en vista previa y no tiene coste**. Google avisa de que los precios y los
  límites pueden cambiar.
- En el plan gratuito, **hasta 8 horas de vídeo al día**.
- **Solo vídeos públicos.** Ni privados ni ocultos.
- Con los modelos actuales, hasta 10 vídeos por petición.

## 1. Consigue la clave

1. Entra en [aistudio.google.com/apikey](https://aistudio.google.com/apikey) con tu cuenta de Google.
2. Pulsa **Create API key** y cópiala.

Trátala como una contraseña: no la pegues en el chat, ni la subas a GitHub, ni la metas en una web.

## 2. Pídele a Claude Code que monte la skill

Abre Claude Code (capítulo 3.2) y pega esto. Le pedimos que lea la documentación porque el nombre del modelo y la forma de
llamar a la API cambian.

```text
Crea una skill de Claude Code llamada ver-youtube, en ~/.claude/skills/ver-youtube/. Antes, lee
https://aistudio.google.com/docs/video-understanding y usa la forma actual de llamar a la API y un modelo vigente.

La skill recibe uno o varios enlaces de YouTube y una pregunta, llama a la API de Gemini con un script y guarda la respuesta en
un archivo de texto en la carpeta en la que estoy. Solo vídeos públicos. Si Google da un error o se pasa de un límite, me lo
dice y no se inventa el resultado.

La clave va en ~/.config/ver-youtube/clave.env, como GEMINI_API_KEY=. Crea ese archivo vacío, solo legible por mi usuario, y
ábremelo para que la pegue yo. Nunca me pidas la clave, no la leas, no la enseñes y no la metas en ningún otro archivo.
```

Pega la clave en el archivo que se abre, guárdalo y cierra Claude Code y vuelve a abrirlo. Después, pruébala con un vídeo corto
que conozcas:

```text
Usa ver-youtube con este vídeo: [enlace]. Resúmelo en cinco frases, con el minuto de cada una.
```

Compáralo con el vídeo. Si se inventa algo o los minutos no cuadran, corrígelo antes de seguir.

## 3. Saca lo que enseña cada vídeo

Elige **varios vídeos del mismo tema**, de gente distinta. De uno solo sacarás la opinión de una persona. Con varios, verás lo
que se repite y en qué no están de acuerdo.

```text
Usa ver-youtube con estos vídeos: [enlaces]. De cada uno, sácame en un archivo aparte:
- los pasos que enseña, en orden, con el minuto;
- lo que enseña en pantalla, porque eso no sale en lo que dice;
- las reglas y los errores que menciona;
- lo que afirma sin dar ninguna prueba.
Si no se entiende algo, márcalo como dudoso. No completes nada con lo que tú sepas. Escríbelo con tus palabras, sin copiar
frases largas del vídeo.
```

## 4. Conviértelo en una skill

El creador de skills es el plugin oficial `skill-creator`. Se instala en Claude Code desde la terminal con esta línea, o desde
el marketplace oficial si usas la aplicación de escritorio:

```text
/plugin install skill-creator@claude-plugins-official
```

Después, pídele esto:

```text
Con skill-creator, convierte lo que hay en estos archivos en una skill llamada [nombre], para que yo pueda [lo que quieres
conseguir]. Quédate con lo que se repite en varios vídeos. Lo que aparezca en uno solo, márcalo como dudoso o déjalo fuera. Donde
los vídeos no estén de acuerdo, pregúntame. Escríbela con tus palabras y apunta de qué vídeos sale cada parte. Hazme las
preguntas que te falten sobre mi caso y haz una prueba con una tarea real antes de darla por buena.
```

## 5. Revísala antes de fiarte

- **Léela entera.** Una skill es texto: si no entiendes una instrucción, pregunta para qué está.
- **Pruébala con un caso que sepas resolver.** Si no sabes juzgar el resultado, todavía no puedes fiarte de ella.
- **Comprueba lo importante.** Lo que afecte a dinero, salud o temas legales, míralo en una fuente oficial.
- **Cada corrección, una regla.** Lo que le cambies, que lo escriba en la skill.

## Cuidados

> [!CAUTION]
> **Un vídeo enseña, pero sigue siendo de quien lo hizo.** Aprender un método para tu trabajo es una cosa. Copiar el guion, las
> frases o los materiales de alguien para venderlos es otra. No conviertas un curso de pago en un producto tuyo, y respeta los
> derechos de lo que copies.

- **Lo que entiende una IA también falla.** Gemini se puede equivocar con lo que ve y con lo que oye. Por eso pedimos los minutos:
  para que puedas ir a comprobarlo.
- **Las preguntas que le haces también salen de tu ordenador.** Las condiciones del plan gratuito piden no enviar información
  sensible, confidencial o personal. Aquí basta con un enlace público y una pregunta general: no pegues datos de clientes.
- **Si lo montas para otros.** Las condiciones de Google solo permiten los servicios de pago cuando pones la herramienta a
  disposición de usuarios del Espacio Económico Europeo, Suiza o el Reino Unido. Para una app con clientes en España, cuenta con pagar.

## En resumen

- Claude no ve YouTube por sí solo: una skill le pide a Gemini que vea el vídeo y le devuelve el resultado.
- Con el plan gratuito, hasta 8 horas de vídeo al día, solo públicos. En vista previa: puede cambiar.
- La clave, en un archivo solo tuyo. Nunca en el chat.
- Varios vídeos del mismo tema, y luego el creador de skills.
- Revísala y pruébala con un caso que sepas juzgar antes de fiarte.

Para saber si una tarea merece una skill, mira el capítulo 2.1.

---

## Fuentes

- Google: [vídeo en la API de Gemini](https://aistudio.google.com/docs/video-understanding) (enlaces de YouTube, vista previa, sin
  coste, 8 horas al día, solo públicos y 10 vídeos por petición), [claves de la API](https://aistudio.google.com/docs/api-key) y
  [condiciones](https://aistudio.google.com/docs/terms).
- Claude Code: [skills y `skill-creator`](https://code.claude.com/docs/en/skills).

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
