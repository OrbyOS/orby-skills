# Reels de prueba con Claude: diez ideas al día, sin quemar tu cuenta

Los reels de prueba de Instagram se enseñan primero a gente que no te sigue. Si funcionan, puedes compartirlos con tus seguidores; si no, no los ve nadie de tu público. Son la forma más barata de probar ideas: publicas muchas, miras cuáles enganchan y haces más de esas. Con Claude puedes publicarlos por ti, hasta diez al día, y que lea los datos de cada uno.

Revisada el 7 de noviembre de 2026 con la documentación de Meta para desarrolladores (enlace al final). Es lo que hacemos en @orbyos desde el 3 de noviembre.

---

## 1. A mano, para empezar hoy

Hace falta una cuenta profesional (de creador o de empresa).

1. Sube un reel como siempre.
2. Antes de publicar, activa **Reel de prueba**.
3. Elige si se comparte solo con tus seguidores cuando vaya bien o si lo decides tú.

## 2. Con Claude, para publicar cada día

Instagram deja publicar reels de prueba con su API oficial. Claude Code te monta el programa que los sube a la hora que le digas. Necesitas:

- Una cuenta profesional de Instagram conectada a una página de Facebook.
- Una app de Meta para desarrolladores con permiso para publicar contenido.
- Un sitio donde dejar el programa encendido: tu ordenador o un servidor pequeño.

Mensaje para empezar:

```text
Quiero publicar reels de prueba en mi Instagram con la API oficial de Meta (Instagram Graph API, publicación de contenido con trial_params).
Primero explícame, paso a paso y sin tecnicismos, qué tengo que crear en Meta y qué permisos hacen falta. No me pidas claves en el chat: dime dónde guardarlas.
Después escríbeme un programa que lea una lista de vídeos con su texto y publique uno a cada hora que yo marque, y que apunte el enlace de cada uno.
```

**Lo que importa:** las claves de Meta dan acceso a tu cuenta. Guárdalas en un archivo que no se suba a ningún sitio y no las pegues en un chat.

## 3. Que aprenda de cada reel

Mensaje para cuando ya tengas unos cuantos publicados:

```text
Lee las métricas de mis últimos reels de prueba con la API (vistas, alcance, tiempo medio de visionado, guardados, compartidos y comentarios).
Ordénalos de mejor a peor y dime qué tienen en común los tres primeros: el gancho, el tema y la duración.
Con eso, propónme diez ideas para mañana que sigan lo que funciona.
```

La API da el tiempo medio de visionado de cada reel. La gráfica segundo a segundo de dónde se va la gente solo está en la app: haz una captura y pásasela a Claude para que te diga dónde se cae.

## 4. Cuando uno funcione

Cuando un reel pase de unas cien mil vistas, promociónalo como anuncio con un presupuesto pequeño, unos veinte euros al día, y mira si te trae seguidores o clientes antes de subirlo.

## Lo que conviene saber

- Meta limita cuántas publicaciones puedes hacer al día por la API. Diez reels caben de sobra.
- No publiques diez veces el mismo vídeo: prueba ideas distintas.

## Fuentes

- [Meta para desarrolladores: publicación de contenido en Instagram](https://developers.facebook.com/docs/instagram-platform/content-publishing).

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
