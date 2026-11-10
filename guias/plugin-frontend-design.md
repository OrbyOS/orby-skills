# Frontend Design: webs que no parecen hechas con IA

Si le pides una web a una IA sin más, sale la de siempre: el mismo degradado, el mismo titular centrado y las mismas tres tarjetas. Frontend Design es un plugin oficial de Anthropic para Claude Code que cambia eso: antes de escribir código, Claude elige una dirección visual (tipografía, colores, animaciones) y la lleva hasta el final.

Revisada el 9 de noviembre de 2026.

---

## 1. Instálalo

En Claude Code, una línea:

```text
/plugin install frontend-design@claude-plugins-official
```

Está en el marketplace oficial de Anthropic (github.com/anthropics/claude-plugins-official). Claude lo usa solo cuando le pides algo de diseño web.

## 2. Pídele algo concreto

Cuanto más le cuentes del negocio, mejor elige el estilo:

```text
Crea la página de inicio de [tu negocio]: [qué vendes, a quién y en qué ciudad]. Quiero que tenga personalidad y que no parezca una plantilla. Antes de programar, dime qué dirección visual eliges (tipografía, colores y animaciones) y por qué. Después hazla.
```

Otros ejemplos que funcionan: un panel con tus números del mes, una página de ventas para un curso o un formulario de reservas.

## 3. Corrige como lo harías con un diseñador

- «Más sobria», «más cálida», «que se lea mejor en el móvil».
- Pásale tu logo y tus colores si ya los tienes.
- Pide dos direcciones distintas y quédate con la que más se parezca a tu marca.

## Lo que conviene saber

- El plugin mejora el diseño, no el contenido: el texto, los precios y las fotos los tienes que revisar tú.
- Antes de publicar, comprueba la web en el móvil y que cargue rápido.
- Si quieres ir más allá, el capítulo «Una web que no huele a IA» te da la skill completa para tu web.
