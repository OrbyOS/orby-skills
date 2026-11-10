# ¿Tu web la entiende la IA? Lista de comprobación

Cada vez más gente le pide a una IA que le recomiende un negocio: «recomiéndame un fisio en Valencia que trate
corredores». ChatGPT, Claude o Perplexity buscan en internet, leen unas cuantas webs y responden. No ven tus fotos ni
tu diseño: leen el texto. Si no entienden qué haces, para quién y dónde, no te recomiendan.

Esta lista se hace en una tarde, con tu web abierta. Empieza por la prueba y termina repitiéndola.

Revisada el 28 de octubre de 2026 con la documentación de OpenAI, Anthropic, Perplexity y Google (enlaces al final).

---

## 1. La prueba: pregúntaselo a la IA

Hazla antes de cambiar nada, y guarda las respuestas para comparar después. En ChatGPT, Claude y Perplexity, con la
búsqueda web activada:

1. «¿Qué hace [nombre de tu negocio] y dónde está?»
2. «¿Qué servicios ofrece [nombre de tu negocio] y cuánto cuestan?»
3. Sin decir tu nombre: «Recomiéndame [lo que vendes] en [tu ciudad o para tu tipo de cliente].»
4. «¿Qué opinan los clientes de [nombre de tu negocio]?»

Apunta para cada respuesta: ¿te encuentra?, ¿acierta qué haces?, ¿se inventa algo?, ¿qué fuentes cita? Las fuentes
que cita son las páginas que está leyendo: tu web, un directorio, unas reseñas. Ahí es donde hay que trabajar.

## 2. Que se pueda leer

> [!IMPORTANT]
> Es lo primero que hay que comprobar: si la IA no puede leer tu web, lo demás da igual.

- [ ] **El texto está en el HTML, no solo en JavaScript.** Los robots de ChatGPT y de Claude no ejecutan JavaScript:
      si tu web enseña el contenido solo después de cargar un script, para ellos está vacía. Prueba: abre tu web,
      haz clic derecho → «Ver código fuente» y busca la frase principal de tu portada. Si no está, pide a quien hizo
      tu web que la sirva ya escrita en la página (renderizado en el servidor o páginas estáticas).
- [ ] **El texto importante no está dentro de imágenes.** Servicios, precios, horarios y menús, en texto. Una carta
      en PDF o en foto no se lee bien.
- [ ] **No bloqueas a los buscadores de IA.** Mira `tudominio.com/robots.txt`. Si quieres salir en sus respuestas,
      no bloquees estos robots:
      - `OAI-SearchBot` (las búsquedas de ChatGPT);
      - `Claude-SearchBot` y `Claude-User` (las búsquedas de Claude);
      - `PerplexityBot` (las búsquedas de Perplexity).
      Los robots que recogen texto para entrenar modelos (`GPTBot`, `ClaudeBot`) son otra decisión: puedes
      bloquearlos y seguir saliendo en las búsquedas, porque cada uno se controla por separado.
- [ ] **Tu hosting no los bloquea por ti.** Algunos servicios de seguridad y CDN tienen una opción para bloquear los
      robots de IA, y a veces viene activada. Revisa la configuración de tu proveedor.

## 3. Que se entienda qué haces

- [ ] **La primera frase de tu portada dice qué haces, para quién y dónde**, sin adornos. «Fisioterapia para
      corredores en Valencia», no «Tu bienestar, nuestra pasión».
- [ ] **Una página por servicio**, con su nombre normal (el que buscaría tu cliente), qué incluye, para quién es, cuánto
      dura y cuánto cuesta.
- [ ] **Precios en texto.** Si no puedes poner un precio cerrado, pon «desde», un rango o de qué depende. Una IA a la
      que le preguntan «cuánto cuesta» prefiere una fuente que lo diga.
- [ ] **Dónde y cuándo:** dirección, zona a la que das servicio (o «solo online»), horario y cómo contactar, en texto y
      en el pie de todas las páginas.
- [ ] **Quién está detrás:** una página «Quiénes somos» con nombres, experiencia y desde cuándo. Ayuda a que la IA (y
      la persona) se fíe.

## 4. Que responda a lo que preguntan tus clientes

- [ ] **Preguntas frecuentes escritas como las haría un cliente**, no como titulares: «¿Cuántas sesiones necesito
      para una tendinitis?», «¿Atendéis los sábados?», «¿Trabajáis con mutuas?». Una respuesta clara de dos o tres
      frases para cada una.
- [ ] **Saca las preguntas de tu bandeja de entrada:** las que te repiten por WhatsApp, por correo o en las llamadas
      son las que también le hacen a la IA.
- [ ] **Una pregunta, una respuesta.** Que cada respuesta se entienda sola, sin tener que leer el resto de la página.

## 5. Datos estructurados (opcional, pero ayudan)

Los datos estructurados son unas líneas de código invisibles que describen tu negocio de forma que una máquina no
pueda malinterpretar: nombre, tipo de negocio, dirección, horario, servicios. Google dice que no son obligatorios para
sus resultados con IA, pero siguen sirviendo para que te entiendan y para los resultados enriquecidos de Google.

- [ ] Un bloque `LocalBusiness` (o el tipo más concreto que exista para tu negocio) u `Organization` si no tienes local.
      Ejemplo para pegar en la portada, cambiando los datos:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "[Nombre del negocio]",
  "description": "[Qué haces, para quién y dónde, en una frase]",
  "url": "https://[tudominio.com]",
  "telephone": "[+34 …]",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[Calle y número]",
    "addressLocality": "[Ciudad]",
    "postalCode": "[Código postal]",
    "addressCountry": "ES"
  },
  "openingHours": "Mo-Fr 09:00-19:00",
  "sameAs": ["[enlace a tu perfil de Google]", "[enlace a tu Instagram]"]
}
</script>
```

- [ ] Compruébalo en el validador de schema.org (validator.schema.org) o en la prueba de resultados enriquecidos de
      Google.
- [ ] Los datos tienen que coincidir con lo que dice el texto de la página. Si no coinciden, no sirven.

## 6. Lo que dicen de ti fuera de tu web

Las IA no solo leen tu web: leen directorios, reseñas y otras webs que te mencionan. Muchas veces citan antes eso
que tu propia página.

- [ ] **Tu ficha de Google** (Perfil de Empresa) completa y al día: categoría, servicios, horario, fotos, web.
- [ ] **El mismo nombre, dirección y teléfono en todas partes:** web, ficha de Google, redes y directorios de tu sector.
      Si en un sitio pone una dirección antigua, la IA puede repetirla.
- [ ] **Reseñas:** pide reseñas a tus clientes y contéstalas. Son de lo primero que lee una IA cuando le preguntan
      qué opinan de ti.
- [ ] **Bing:** da de alta tu web en Bing Webmaster Tools y tu negocio en Bing Places. Es gratis y lo usan algunos
      asistentes de IA. OpenAI no ha confirmado qué buscador usa ChatGPT, así que tómalo como algo barato que puede
      ayudar, no como una garantía.

## 7. Lo que no hace falta (por ahora)

- **`llms.txt`:** es un archivo propuesto para resumir tu web a las IA. Google dice que no hace falta para sus
  resultados con IA, y los estudios que hay no encuentran que mejore las recomendaciones. Si ya lo tienes, no
  molesta; si no, hay cosas de esta lista que rinden más.
- **Trocear el texto o escribir «para la IA»:** escribe para personas, claro y concreto. Es lo que mejor entienden
  las dos.
- **Herramientas que prometen «posicionarte en ChatGPT»:** nadie controla lo que recomienda una IA. Lo que sí
  controlas es que tu información sea clara, esté en texto y diga lo mismo en todas partes.

## 8. Repite la prueba

Entre cuatro y seis semanas después de los cambios, vuelve a hacer las cuatro preguntas del paso 1 y compara. Los
buscadores de IA tardan en volver a leer tu web. Si sigue equivocándose en algo, mira qué fuente cita: ahí está lo
que hay que corregir.

---

## Fuentes

- OpenAI: [sus robots y qué controla cada uno](https://developers.openai.com/api/docs/bots).
- Anthropic: [sus robots y cómo controlarlos](https://support.claude.com/en/articles/8896518).
- Perplexity: [PerplexityBot](https://docs.perplexity.ai/docs/perplexitybot) y [sus robots](https://docs.perplexity.ai/docs/resources/perplexity-crawlers.md).
- Google: [guía para los resultados con IA en la Búsqueda](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide).
- Vercel: [los robots de IA no ejecutan JavaScript](https://vercel.com/blog/the-rise-of-the-ai-crawler).
- Search Engine Journal: [la postura de Google sobre llms.txt](https://www.searchenginejournal.com/googles-llms-txt-guidance-depends-on-which-product-you-ask/575431/).

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
