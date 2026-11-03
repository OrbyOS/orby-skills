# Cómo aparecer en las respuestas de IA de Google

Google ha publicado su propia guía para salir en AI Overviews y en AI Mode, y lo que dice ahorra mucho trabajo: la mayoría de los
trucos que se venden no hacen falta. Lo que cuenta es tener contenido que solo podrías haber escrito tú. Aquí tienes lo que
dice y un método para aplicarlo con Claude a tu web.

Revisada el 3 de noviembre de 2026 con la documentación oficial de Google (enlaces al final).

> [!IMPORTANT]
> **Nadie puede garantizarte que salgas.** La propia guía dice que cumplir todo no asegura aparecer. Y desconfía de quien lo
> prometa o diga tener acceso a datos internos de Google: la guía también avisa de esas herramientas.

---

## Lo que dice Google

### Lo que sí cuenta

- **Contenido propio.** Una visión tuya, como tu experiencia de primera mano. No un resumen de lo que ya hay por ahí.
- **Que se pueda indexar.** La página tiene que estar en Google y poder mostrarse con fragmento.
- **Que esté ordenado para quien lee.** Párrafos claros, secciones y títulos, con imágenes y vídeos que aporten.
- **Lo básico de siempre.** Que Google pueda rastrearla, que la página funcione bien y que no haya contenido duplicado.
- **Datos del negocio.** Si vendes productos o tienes un local, Merchant Center y tu Perfil de Empresa.

### Lo que dice que NO hace falta

| Lo que te venden | Lo que dice Google |
| --- | --- |
| **Crear un `llms.txt`** | Búsqueda de Google no lo usa. Ni ayuda ni perjudica |
| **Trocear el contenido** | No hace falta partirlo en piezas pequeñas, ni hay una longitud ideal |
| **Reescribir para la IA** | No hace falta una forma especial de escribir ni añadir búsquedas larguísimas: entiende sinónimos y significado |
| **Datos estructurados especiales** | No son necesarios para esto. Siguen sirviendo para los resultados enriquecidos |
| **Conseguir menciones falsas** | No ayuda |

> [!CAUTION]
> **No crees decenas de páginas con la IA para cada variante de una búsqueda.** La guía avisa de que publicar páginas en masa para
> manipular los resultados puede incumplir su política contra el abuso de contenido a escala.

Todo esto se refiere a Google. Para que ChatGPT, Claude o Perplexity entiendan tu web, mira el capítulo 5.9: algunas de sus
recomendaciones son distintas porque son otros sistemas.

---

## El método

Lo que hace falta: acceso a tu web y una cuenta de [Search Console](https://search.google.com/search-console) con tu web
verificada. Se hace en una tarde, y sirve mejor cuanto más tráfico tengas: con muy pocos datos, empieza por lo que te preguntan
tus clientes.

## 1. Comprueba lo básico

En Search Console:

1. Con la **Inspección de URLs**, mira si tus páginas importantes están indexadas.
2. En los **Ajustes**, mira que no hayas apagado la opción de aparecer en las funciones de IA generativa.
3. Abre el informe **Rendimiento de IA generativa** y descárgalo, para poder comparar más adelante. Cuenta las veces que los enlaces
   a tu web se han mostrado en esas funciones, por páginas, países, fechas y dispositivos. Si sale vacío, puede que aún no tengas
   suficientes impresiones.

Pídele a Claude que mire también lo que no se ve:

```text
Revisa estas páginas de mi web: [direcciones]. Dime si hay algo que impida a Google indexarlas o mostrar un fragmento, como
noindex, nosnippet o un bloqueo en robots.txt, y si el texto importante está en la página y no solo dentro de imágenes. No cambies
nada: dame la lista de lo que hay que arreglar.
```

## 2. Descarga tus búsquedas

El informe de IA generativa no enseña las búsquedas. Están en el informe normal:

1. Entra en **Rendimiento, Resultados de búsqueda**.
2. Elige los últimos 3 meses y activa clics, impresiones y posición.
3. Pulsa **Exportar** y descarga el archivo. Trae una pestaña de consultas y otra de páginas.

## 3. Que Claude marque las que no respondes con claridad

Abre Claude con el archivo y las direcciones de tu web:

```text
Te paso las búsquedas por las que me encuentra Google. Mi web es [dirección] y lo que vendo es [qué haces y para quién].

1. Quédate con las búsquedas que tienen que ver con lo que vendo. Agrupa las que preguntan lo mismo.
2. Lee mis páginas y marca cada grupo como: «lo respondo con claridad», «lo respondo a medias» o «no lo respondo». Cita la frase
   de mi web en la que te basas.
3. Ordénalos por impresiones, y deja arriba los que tienen muchas impresiones y no están bien respondidos.

No me propongas páginas nuevas para cada variante. Si no puedes leer una página, dímelo. No inventes datos.
```

## 4. Reescríbelas con tu experiencia real

Aquí está el trabajo que no puede hacer la IA sola. Elige los tres primeros grupos:

```text
Vamos a mejorar la respuesta a [búsqueda] en esta página: [dirección]. Antes de escribir, hazme preguntas de dos en dos para sacar lo
que solo sé yo: un caso real, qué falla casi siempre, qué le digo a un cliente, qué haría de otra forma y cuánto cuesta o tarda de
verdad. Después, propón el cambio con mis respuestas: primero la respuesta clara y luego mi experiencia. Si un dato no me lo has
oído a mí o no tiene fuente, márcalo como [PENDIENTE]. Respeta mi manera de hablar y no toques el resto de la página.
```

Si no tienes experiencia real que contar sobre esa búsqueda, seguramente no te toca responderla.

Quita los datos de clientes si no tienes su permiso, y revisa el resultado antes de publicar. Para que no suene a IA, usa el capítulo 1.6.

## 5. Mira qué ha pasado

Vuelve a descargar los informes pasadas unas semanas, y compara las mismas páginas. Es un plazo aproximado: el cambio no es
inmediato, y una subida o bajada también puede venir de otras cosas.

```text
Te paso los informes de Search Console de antes y de ahora, y estas son las páginas que cambié: [lista]. Dime qué ha cambiado en esas
páginas y en las demás, para comparar. Si los datos no bastan para sacar una conclusión, dímelo.
```

## En resumen

- Lo que cuenta es tu experiencia de primera mano, en una página que Google pueda indexar y mostrar con fragmento.
- Según Google, no hacen falta `llms.txt`, trocear, reescribir para la IA ni datos estructurados especiales.
- Descarga tus búsquedas, que Claude marque las que no respondes bien y reescríbelas con lo que solo sabes tú.
- Mide en Search Console, y no te fíes de quien te garantice salir.

---

## Fuentes

- Google: [guía para las funciones de IA generativa de la Búsqueda](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide),
  [informe de rendimiento de IA generativa](https://support.google.com/webmasters/answer/16984139) y
  [control de IA generativa de la Búsqueda](https://support.google.com/webmasters/answer/16908024).

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
