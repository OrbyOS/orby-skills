# Founder: prueba tu negocio dentro de Claude antes de abrirlo

Founder es un paquete gratuito de 11 skills para Claude que pone a prueba una idea de negocio antes de gastar dinero en ella. Un consejo que la puntúa, un financiero que hace las cuentas, un director de marketing, y un panel de 100 clientes simulados que te dicen quién compraría, quién no y por qué. Es de código abierto (licencia MIT) y está en GitHub: github.com/Jakeschincariol/founder-skill.

Revisada el 11 de noviembre de 2026.

---

## Las 11 skills, en una línea cada una

| Skill | Qué hace |
|---|---|
| founder-board | Tu consejo: tres agentes puntúan la idea con los marcos de *$100M Offers* (Hormozi), *Zero to One* (Thiel) y la biografía de Steve Jobs, y votan si invertir. |
| founder-competitors | Busca a tu competencia directa e indirecta, sus precios y de qué se quejan sus clientes, con fuentes. |
| founder-consumer | El panel: crea clientes iguales a tu público, cada uno con su ingreso, sus hábitos y su objeción, y cuenta quién compra. |
| founder-pricing | Saca un rango de precio a partir de lo que dice el panel y lo compara con la competencia y tu margen. |
| founder-offer | Monta una oferta que responde a las objeciones del panel y la vuelve a probar. |
| founder-cfo | Tu financiero: coste por cliente, punto de equilibrio, previsión del primer año y cuánto dinero necesitas. |
| founder-marketing | Posicionamiento, canales, una campaña de lanzamiento de 30 días y cuánto puedes pagar por cliente. |
| founder-brand | Nombres, con comprobación de marca, dominio y redes, más tono y promesa. |
| founder-ops | Proveedores, personas, rutinas, herramientas, permisos y riesgos. |
| founder-launch | Primero una prueba barata en el mundo real; después, el lanzamiento con fechas. |
| founder-plan | Junta todo en un plan de negocio con un veredicto final. |

## 1. Instálala

La forma más sencilla: abre Claude, pega esto y envíalo.

```text
https://github.com/Jakeschincariol/founder-skill

install skill
```

Si usas Claude Code, también puedes instalarla como plugin:

```text
/plugin marketplace add Jakeschincariol/founder-skill
/plugin install founder-skill@founder-skill
```

Con el plugin, cada skill se llama con el prefijo del paquete, por ejemplo `/founder-skill:founder-board`.

## 2. Úsala en orden

Cada skill guarda lo que descubre en una carpeta `founder/` de tu proyecto y la siguiente lo lee. El orden recomendado:

```text
/founder-board
/founder-competitors
/founder-consumer
/founder-pricing
/founder-offer
/founder-cfo
/founder-marketing
/founder-brand
/founder-ops
/founder-launch
/founder-plan
```

Empieza contándole tu idea con detalle: qué vendes, a quién, a qué precio y dónde. Cuanto mejor la describas, mejores serán las respuestas.

Si solo quieres ver qué opina tu público, puedes lanzar el panel solo: `/founder-consumer --quick`.

## 3. Cómo leer el panel de clientes

- Son clientes simulados, no personas reales. Sirven para encontrar objeciones rápido y gratis, no para predecir ventas.
- Los modelos de IA tienden a ser amables: toma el porcentaje de compra como un techo, no como lo que va a pasar.
- Las objeciones son lo valioso. Si diez clientes dicen «está caro» o «no me fío», ahí tienes trabajo antes de abrir.
- Lo que digan nunca son testimonios. No los uses como tales.

## Lo que conviene saber

- El consejo aplica ideas publicadas en libros de Hormozi, Thiel y la biografía de Jobs. No habla en su nombre ni tiene relación con ellos.
- Las cifras del financiero dependen de los datos que le des. Confirma costes con tus proveedores y los impuestos con tu gestor.
- No es asesoramiento financiero, legal ni fiscal. Permisos y marcas dependen de dónde estés.
- Antes de invertir de verdad, habla con diez clientes reales. Founder te dice qué preguntarles.
