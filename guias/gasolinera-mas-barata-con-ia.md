# La gasolinera más barata de tu ruta, con IA

El Ministerio publica cada día el precio de todas las gasolineras de España, actualizado varias veces al día y en abierto. Dentro de una misma ciudad la diferencia entre la más barata y la más cara puede pasar de 15 € por depósito. Un asistente de IA con acceso a internet puede leer esos datos por ti y decirte dónde llenar en tu ruta.

Revisada el 9 de noviembre de 2026. Ese día, a las 13:39, había 11.487 gasolineras en los datos. En Madrid, la gasolina 95 iba de 1,529 a 1,844 €/l (15,75 € en 50 litros). En Sevilla, de 1,419 a 1,895 €/l (23,80 €).

---

## 1. El prompt

Para Claude con búsqueda web activada, o cualquier asistente que pueda consultar internet:

```text
Consulta los precios oficiales de carburantes del Ministerio para España (el Geoportal de Gasolineras o su servicio de datos abiertos «PreciosCarburantes»).
Mi coche usa [gasolina 95 / diésel] y el depósito es de [50] litros.
Voy de [origen] a [destino] y no me quiero desviar más de [3] km.
Dame las 5 gasolineras más baratas de mi ruta, con dirección, precio por litro, a qué hora se actualizó el precio y cuánto me ahorro llenando ahí frente a la media de la zona.
```

## 2. Para tu zona de siempre

```text
Con los mismos datos, dime las 5 gasolineras más baratas para [gasolina 95] a menos de [5] km de [tu dirección o código postal], y cuánto me ahorro al año si lleno [una vez por semana] en la más barata en lugar de en la más cara de la zona.
```

## 3. Que te avise

Si tu asistente puede programar tareas, añade: «Repite esta consulta cada lunes a las 8:00 y mándame solo la más barata».

## Lo que conviene saber

- Pide siempre la hora del precio: cambian varias veces al día.
- Comprueba el precio en el surtidor antes de llenar.
- La web oficial para mirarlo tú es geoportalgasolineras.es.
