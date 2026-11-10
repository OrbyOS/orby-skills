# Rehacer una app con Claude y arreglar lo que odian sus usuarios

Replica es un conjunto gratuito de 11 skills que estudia una app, rehace lo que hace con código nuevo, la prueba y lee las
quejas de sus usuarios para que la tuya las resuelva. Después le pone marca propia y la publica.

Revisada el 3 de noviembre de 2026 con su documentación (enlace al final). Ese día tenía 7,2k estrellas en GitHub y licencia MIT.
No hemos construido ninguna app con ella: lo que sigue viene de esa documentación.

> [!IMPORTANT]
> **Rehace funciones y flujos, no copia la app.** No se lleva su código, su marca, su logo, sus textos ni su contenido. Solo lee
> páginas públicas y tu propia cuenta. Exige cambiar de marca antes de publicar. Puedes rehacer el reproductor de una app de
> música, pero no su catálogo.

---

## Antes de instalar nada: ¿merece la pena?

Una de las skills, `replica-entrepreneur`, se puede usar sola. Es el mejor punto de partida: lee las reseñas de la app y te dice
qué odian sus usuarios, antes de que construyas nada. Si las quejas son pocas o flojas, seguramente no hay negocio ahí.

Piensa también en lo que no se copia. Si lo que hace valiosa a una app son sus usuarios, sus datos o sus acuerdos con otros,
rehacer las pantallas no te da nada de eso.

## Instalarla

Abre Claude Code (capítulo 3.2) en una carpeta nueva y pega estas líneas una a una:

```text
/plugin marketplace add Jakeschincariol/replica-skill
/plugin install replica-skill@replica-skill
```

Instalada así, las skills se llaman `/replica-skill:replica-recon`, y así con las demás. Si esas líneas no te funcionan en la
aplicación de escritorio, pégale a Claude la dirección `https://github.com/Jakeschincariol/replica-skill` y pídele que instale
las skills. Necesitan Python 3.8 o posterior.

Lee antes los archivos, como con cualquier skill de otra persona (capítulo 2.1).

## Las 11 skills, en orden

Cada una lee lo que dejó la anterior en una carpeta `replica/` de tu proyecto.

| Orden | Skill | Qué hace |
| --- | --- | --- |
| 1 | `recon` | Estudia la app: pantallas, flujos, componentes y datos. Con páginas públicas, capturas, su ficha en la tienda y tu cuenta |
| 2 | `architect` | Decide con qué se construye, la base de datos y la API |
| 3 | `design` | Saca colores, letras y medidas, y los rehace con tus recursos |
| 4 | `build` | Construye la app pantalla a pantalla |
| 5 | `backend` | Cuentas de usuario, base de datos, pagos e integraciones |
| 6 | `test` | Prueba cada flujo y apunta los fallos por gravedad |
| 7 | `diff` | Compara con el original: una nota y lo que falta |
| 8 | `entrepreneur` | Lee reseñas en App Store, Google Play, G2, Reddit y otros sitios, y convierte las quejas en mejoras y en un enfoque propio |
| 9 | `brand` | Le da nombre, colores y voz propios, y limpia cualquier rastro del original |
| 10 | `launch` | Página de venta, precios y ficha para la tienda |
| 11 | `deploy` | Comprueba que todo está limpio y la publica en tu dominio, cuando tú lo dices |

## Cómo usarla sin perderte

### 1. Empieza por las quejas

```text
Usa replica-entrepreneur con [nombre de la app]. Quiero saber qué odian sus usuarios, con cuántas reseñas y enlace a cada
cita. Si los datos son flojos, dímelo. Termina diciéndome si ves sitio para una versión mejor y para quién. No construyas nada.
```

### 2. Elige una parte pequeña

El propio proyecto avisa: una herramienta de reservas lleva semanas, y un motor de hojas de cálculo no es realista. Para tu
primera app, quédate con el flujo principal.

```text
Usa replica-recon con [dirección de la app]. Solo páginas públicas y mi cuenta, sin saltarte ningún acceso ni las condiciones
del servicio. Dime cuánto trabajo es, sin adornarlo. Marca como «fuera» todo lo que no sea el flujo principal: [qué tiene que
poder hacer alguien].
```

### 3. Sigue el orden y revisa cada paso

Lanza cada skill y lee lo que entrega antes de pasar a la siguiente. Hay tres paradas en las que manda tu criterio:

- **Después de `architect`:** qué servicios de pago necesita y cuánto te costarán.
- **Después de `diff`:** si le falta algo imprescindible, aún no está para publicar.
- **Antes de `deploy`:** prueba tú la app como lo haría un cliente, y sigue la lista del capítulo 3.7.

## Avisos

> [!CAUTION]
> **Esto no es asesoramiento legal.** Que una herramienta rehaga funciones con código nuevo no te garantiza nada. Comprueba
> antes de vender: que el nombre no sea una marca ya registrada, las condiciones de lo que hayas usado (también de tu cuenta en
> la app original, que pueden prohibir usarla para competir) y, si hay dinero en juego, habla con un abogado.

- **Tú pagas el resto.** Las skills son gratis, pero el alojamiento, el uso de la IA, los pagos y demás servicios corren de tu cuenta.
- **El mantenimiento es tuyo.** Publicarla es el principio: fallos, seguridad, copias de seguridad y clientes que escriben.
- **Los datos de tus usuarios son responsabilidad tuya.** Si guardas cuentas o pagos, tienes obligaciones de privacidad. Una
  revisión de seguridad hecha por alguien que sepa merece la pena antes de abrirla.
- **No hay clon perfecto.** Depende de lo compleja que sea la app.
- **No inventes reseñas.** La skill solo cuenta las que llevan enlace. Usa los datos tal como salen en tu página de venta.

## En resumen

- Empieza por `replica-entrepreneur`: dice si merece la pena antes de construir.
- Rehace funciones con código nuevo y marca propia. No copia código, logos, textos ni contenido.
- Para la primera app, solo el flujo principal, y revisa cada paso.
- Antes de vender, mira marcas y condiciones, y pregunta a un abogado si hay dinero en juego.
- El alojamiento, la IA y el mantenimiento los pagas tú.

---

## Fuentes

- Replica: [repositorio y documentación](https://github.com/Jakeschincariol/replica-skill) (las 11 skills, su orden, límites y
  letra pequeña). Licencia MIT.

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
