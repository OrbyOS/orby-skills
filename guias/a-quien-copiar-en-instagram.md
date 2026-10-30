# A quién copiar en Instagram, sin buscar por hashtags

Copiar lo que ya funciona es la forma más rápida de acertar con el contenido. Pero solo sirve si copias a cuentas que
le hablan a tu mismo cliente, y eso no lo da un hashtag. Esta guía explica el método para encontrarlas con Claude
Code: partir de las cuentas que ya sigues, seguir sus conexiones, filtrar y, en las cuentas grandes, quedarte solo con
los vídeos que se salen de lo normal.

Revisada el 30 de octubre de 2026.

---

## 1. Por qué buscar por hashtag falla

Un hashtag junta a todo el que habla de un tema, le hable a quien le hable. Si buscas un tema de marketing, te salen
agencias que venden a empresas grandes, cursos para principiantes, gente que vende plantillas y cuentas de humor.
Todas hablan de lo mismo, pero casi ninguna le habla a tu cliente. Si copias a esas cuentas, el contenido le acaba
gustando a su público y no al tuyo.

Lo que importa no es de qué habla una cuenta, sino **a quién le habla**.

## 2. El método: de las cuentas que sigues a sus conexiones

### Las semillas

Empieza por las cuentas que ya sigues y que sabes que le hablan a tu cliente: entre cinco y quince. Son las
**semillas**. Las eliges tú, y de ellas sale todo lo demás.

### Sus conexiones

De cada semilla, se miran tres cosas:
- **Con quién colabora:** las publicaciones que firma junto a otra cuenta.
- **A quién menciona o etiqueta** en sus publicaciones.
- **Qué cuentas le pone Instagram como parecidas**, las que salen en «cuentas sugeridas» de su perfil.

### Las que se repiten

Si una cuenta aparece en las conexiones de varias semillas, vale más: varias cuentas que le hablan a tu cliente la
han traído, cada una por su lado. Ordena los candidatos por cuántas semillas los traen y empieza por arriba.

## 3. Los filtros

Antes de estudiar una cuenta, comprueba que pasa estos filtros. Si falla uno, fuera.

| Filtro | Qué se mira |
| --- | --- |
| **Publica con regularidad** | Al menos 1 publicación en los últimos 14 días y 8 en los últimos 60. Una cuenta parada no te dice qué funciona hoy |
| **Tiene interacción** | Que la gente comente y dé me gusta en proporción a sus seguidores. Por ejemplo, al menos 5 interacciones de media por cada 1.000 seguidores |
| **Hace vídeo corto** | Si casi no publica reels, no te sirve para aprender a hacerlos |
| **Le habla a tu mismo cliente** | Lee su biografía, sus textos y a quién vende. Si su cliente no es el tuyo, fuera, aunque tenga muy buen contenido |

Apunta por qué cae cada cuenta. Si casi todas caen por lo mismo (por ejemplo, porque no le hablan a tu cliente), el
problema suele estar en las semillas: cámbialas.

## 4. Las cuentas grandes: solo sus outliers

Una cuenta mucho más grande que la tuya no se descarta, pero se mira de otra manera. Muchas de sus visitas vienen de
su marca: la gente ve sus vídeos porque es quien es, no por cómo están hechos. Eso no lo puedes copiar.

Por eso, de una cuenta grande solo se estudian sus **outliers**: los reels que han tenido muchas más visitas de lo
normal **en esa misma cuenta**. Por ejemplo, al menos el triple de lo que suele tener. Si en una cuenta que siempre
hace 200.000 visitas un reel hace 2 millones, ahí no ha sido la marca, sino el contenido.

> [!TIP]
> Esta comparación sirve para cualquier cuenta, no solo para las grandes: un vídeo con el triple de lo normal en su
> cuenta dice más que uno con muchas visitas a secas. El capítulo 5.1 explica cómo encontrarlos y desmontarlos.

## 5. Después: copiar lo que ya ha funcionado

Con las cuentas que quedan y sus mejores vídeos, el trabajo es el del capítulo 5.1: desmontar cada vídeo (el gancho,
la pregunta que deja abierta, cada paso) y sacar una plantilla con tu tema y un ejemplo tuyo. Se copia por qué
funcionó, no las frases.

Las cuentas que te convenzan pásalas a tus semillas. Así, cada vuelta parte de mejores cuentas que la anterior.

## 6. Montarlo con Claude Code

### Lo que hace falta

- **Claude Code**, en tu ordenador.
- **Una cuenta de Apify**, un servicio que descarga los datos públicos de perfiles de Instagram. El plan gratuito da 5
  dólares de saldo cada mes y no pide tarjeta. Descargar 60 perfiles cuesta unos céntimos, así que una vuelta cabe de
  sobra.

> [!CAUTION]
> Apify te da una clave para usarlo. No la pegues en el chat ni en el código: guárdala en un archivo `.env` y dile a
> Claude que la lea de ahí. Descarga solo datos públicos y úsalos para estudiar, no para publicarlos.

### El prompt

Abre Claude Code en una carpeta nueva y pídeselo así:

```text
Quiero encontrar cuentas de Instagram que le hablen a mi mismo cliente, para estudiar su contenido. Mi negocio: [qué
vendes y a quién]. Usa Apify (la clave está en el archivo .env) y sigue este método:
1. Semillas: estas cuentas que ya sigo: [lista]. Descarga sus perfiles.
2. Conexiones: de cada semilla, saca las cuentas con las que colabora, las que menciona o etiqueta en sus
   publicaciones y las que Instagram le pone como parecidas. Cuenta cuántas semillas traen a cada candidata.
3. Descarga hasta 60 candidatas, empezando por las que traen más semillas.
4. Filtros: que publique al menos 1 vez en 14 días y 8 en 60, que tenga interacción, que haga reels y que le hable a
   mi cliente (léelo en su biografía y sus textos). Apunta por qué descartas cada una.
5. Cuentas mucho más grandes que la mía: no las descartes, pero de ellas quédate solo con los reels que tengan al
   menos el triple de las visitas normales de esa cuenta.
6. Entrégame una tabla con las que pasan: cuenta, cuántas semillas la traen, a quién le habla (con una frase de su
   perfil) y sus reels destacados con el enlace.
Antes de descargar nada, dime cuántos perfiles vas a pedir y cuánto costará aproximadamente.
```

## 7. En resumen

- Busca por a quién le habla una cuenta, no por de qué habla.
- Parte de tus semillas y sigue sus colaboraciones, menciones y cuentas parecidas. Las que traen varias semillas,
  primero.
- Filtra por regularidad, interacción, vídeo corto y cliente.
- De las cuentas grandes, solo sus outliers.
- Copia por qué funcionaron sus vídeos, con tu tema y tus ejemplos.

---

## Fuentes

- Apify: [precios y plan gratuito](https://apify.com/pricing) y
  [descargador de perfiles de Instagram](https://apify.com/apify/instagram-profile-scraper).

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
