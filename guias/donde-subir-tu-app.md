# Dónde poner en internet una app hecha con Claude: Vercel, Railway o Hetzner

Tu app ya funciona en tu ordenador y quieres que la use otra gente. Hay tres sitios muy habituales para subirla y no sirven
para lo mismo: el que te sale gratis con una web puede costarte mucho con otro tipo de app. Esta guía explica cuándo usar
cada uno, qué cuesta y cuándo sale caro.

Precios comprobados el 1 de noviembre de 2026 en las páginas oficiales (enlaces al final), sin IVA. Cambian a menudo, y
Hetzner los ha subido varias veces este año: confírmalos antes de contratar.

---

## La respuesta corta

| Tu app es… | Empieza por | Por qué |
| --- | --- | --- |
| Una web o una app web sencilla, sin programas funcionando todo el tiempo | **Vercel** | Lo subes en minutos y aguanta picos de visitas sin tocar nada |
| Una app con servidor, base de datos o tareas de fondo, y no quieres administrar nada | **Railway** | Corre tu app tal cual y pagas por lo que usa |
| Una app que está siempre encendida, con cierto consumo, y sabes o puedes aprender a cuidarla | **Hetzner** | Precio fijo y bajo, pero el servidor es responsabilidad tuya |

No sabes cuál es la tuya: la sección «Que lo decida Claude» te lo resuelve con tu proyecto delante.

## Los tres, de un vistazo

| | Vercel | Railway | Hetzner |
| --- | --- | --- | --- |
| **Qué es** | Plataforma para webs y funciones que se ejecutan a demanda | Plataforma que corre tu app y sus servicios | Un servidor virtual entero para ti |
| **Plan más barato** | Hobby, gratis, solo uso no comercial | Hobby, 5 $/mes con 5 $ de uso incluidos | 6,49 €/mes (1 vCPU, 1 GB de RAM, 20 GB de disco) |
| **Para un negocio** | Pro, 20 $/mes con 20 $ de crédito | Pro, 20 $/mes con 20 $ de uso incluidos | 11,99 €/mes (1 vCPU, 2 GB, 40 GB) o 19,99 €/mes (2 vCPU, 4 GB, 80 GB) |
| **Cómo cobra** | Crédito incluido y, por encima, por uso | Por lo que consume cada minuto: 10 $ por GB de RAM al mes, 20 $ por vCPU al mes | Precio fijo al mes, con 20 TB de tráfico incluidos en la UE |
| **Límite de gasto** | Presupuesto de 200 $ por defecto, con opción de pausar los proyectos | Límite que para tus servicios, con un mínimo de 10 $ | El precio no cambia con el consumo mientras no pases del tráfico incluido |
| **Quién lo mantiene** | Ellos | Ellos | Tú: actualizaciones, seguridad y copias |

## Vercel

**Úsalo para:** webs, páginas de venta y aplicaciones web con poco trabajo en servidor. Conectas tu proyecto y cada cambio se
publica solo.

**Lo que no hace bien.** Cada función se ejecuta y termina. Vercel lo dice en su guía de migración: su sistema de archivos es
de solo lectura, salvo una zona temporal, y un programa que necesite estar siempre en marcha tiene que quedarse en otro sitio
o rediseñarse. Los archivos subidos y los datos van a servicios aparte, como una base de datos externa, cada uno con su coste.

> [!CAUTION]
> **El plan gratuito no vale para un negocio.** Vercel lo limita a uso personal no comercial. Cuenta como comercial, por
> ejemplo, cobrar a través de la web, anunciar la venta de un producto o servicio, o que te paguen por crearla o alojarla.
> Si tu web vende algo, necesitas Pro.

**Cuándo sale cara:** cuando la app hace mucho trabajo en sus funciones, procesa muchas imágenes o tiene mucho tráfico. Por
encima del crédito, en Pro se paga por uso y sin tope salvo tu presupuesto. Baja ese presupuesto de 200 $ a lo que estés
dispuesto a pagar y activa la pausa automática. Ojo: al llegar al límite, tu web se para.

## Railway

**Úsalo para:** una app con su servidor, su base de datos y tareas de fondo, sin administrar un servidor. Sus precios se
miden por lo que consumes de verdad, no por lo máximo que podrías usar.

**Lo que cuesta de verdad.** Una cuenta con sus precios, por mes encendida todo el tiempo:

| Consumo real | Coste de uso | Lo que pagas en Hobby |
| --- | --- | --- |
| Poca actividad: 0,25 GB de RAM y 0,1 vCPU | 2,50 $ + 2 $ = 4,50 $ | 5 $ (los cubre lo incluido) |
| Media: 1 GB de RAM y 0,5 vCPU | 10 $ + 10 $ = 20 $ | 20 $ |
| Alta: 2 GB de RAM y 1 vCPU | 20 $ + 20 $ = 40 $ | 40 $ |

Hobby está pensado para proyectos personales, según su propia descripción; para producción en un negocio, ellos dirigen a
Pro, que incluye 20 $ de uso. Comprueba sus condiciones si vas a usarlo para vender.

**Cuándo sale cara:** cuando la app está siempre encendida y consume mucha memoria. En la última fila ya pagas unas tres veces lo
que cuesta un servidor con 2 GB en Hetzner. Pon un límite duro en **Set Usage Limits**: al llegar, Railway para tus
servicios. Y si la app se usa poco, activa **Serverless**, que la detiene cuando no hay actividad.

## Hetzner

**Úsalo para:** una app que está encendida todo el mes con un consumo estable, o varias apps en un mismo servidor. Por 11,99 € al
mes tienes 2 GB de RAM y una vCPU que no suben por mucho que los uses.

**Lo que no te cuentan.** Te dan un servidor vacío. Sus condiciones lo dejan claro: administrarlo y protegerlo corren de tu
cuenta. Claude Code te ayuda a montarlo, pero **sigue siendo responsabilidad tuya** tener al día las actualizaciones, el
cortafuegos, las copias de seguridad y qué pasa si se cae de madrugada.

**Cuándo sale cara:** en dinero, casi nunca. Sale cara en tiempo y en riesgo: una mala configuración puede dejar tus datos
expuestos. Si la app guarda datos de clientes y no sabes lo que estás mirando, empieza por Railway. Suma además las copias de
seguridad, desde 1,20 € al mes.

> [!NOTE]
> Los planes más baratos de Hetzner (Cost-Optimized) salen como no disponibles en su web. Y en internet aún circulan muchos
> precios antiguos: mira siempre su propia página.

## Que lo decida Claude

Abre tu proyecto en Claude Code y pega esto. Te responde con tu app delante, no con una regla general:

```text
Quiero poner esta app en internet. Antes de cambiar nada, lee el proyecto y dime: qué partes tiene (web, servidor, base de
datos, tareas de fondo), si guarda archivos en disco y si necesita algún programa siempre en marcha. Después, compara Vercel,
Railway y Hetzner para ESTA app, con precios mirados hoy en sus páginas oficiales y una estimación de cuánto me costaría con
[número] usuarios al mes. Es [personal / para un negocio que cobra]. Dime también qué tendría que cambiar en el código para cada
una, cuál me recomiendas y por qué. Marca lo que sea una estimación y no contrates ni subas nada.
```

## Súbela con estos cuidados

```text
Vamos a subirla a [Vercel / Railway / Hetzner]. Guíame paso a paso y explícame cada paso antes de hacerlo. Antes de subir nada,
revisa que no haya claves en el código ni en el repositorio: tienen que ir en las variables de entorno del servicio. Dime qué
tengo que crear yo en su web (cuenta, plan, forma de pago), porque eso lo hago yo. Ayúdame a poner el límite de gasto, a tener
copias de seguridad de la base de datos y a probar que todo funciona antes de darle la dirección a nadie.
```

Antes de dar la dirección a nadie, comprueba estas cinco cosas:

- **Claves:** ninguna en el código. Si alguna se subió a un repositorio, cámbiala: borrarla no basta.
- **Límite de gasto:** puesto, y con un aviso antes de llegar. El uso de la API de Claude se paga aparte: ponle su propio límite.
- **Copias de seguridad:** hechas y probadas. Una copia que no has restaurado nunca es una esperanza.
- **Datos de clientes:** sabes dónde se guardan y qué pasa si se borran.
- **Una prueba real:** entra desde el móvil, sin haber iniciado sesión, y haz lo que haría un cliente.

## En resumen

- Web o app sencilla: Vercel. Si vendes algo, en Pro: el gratis es solo para uso no comercial.
- App con servidor, base de datos o tareas de fondo, sin administrar nada: Railway, con su límite puesto.
- Siempre encendida, con consumo estable y alguien que la cuide: Hetzner.
- Vercel sale cara con mucho trabajo y tráfico; Railway, con mucha memoria siempre encendida; Hetzner, en tiempo y en riesgo.

---

## Fuentes

- Vercel: [precios](https://vercel.com/pricing), [uso justo y qué se considera uso comercial](https://vercel.com/docs/limits/fair-use-guidelines)
  y [guía de migración desde Railway](https://vercel.com/kb/guide/migrate-a-python-api-from-railway-to-vercel) (archivos,
  procesos y bases de datos).
- Railway: [planes y precios](https://docs.railway.com/reference/pricing/plans) y
  [control de costes](https://docs.railway.com/pricing/cost-control).
- Hetzner: [precios de Regular Performance](https://www.hetzner.com/cloud/regular-performance/), [precios de la nube](https://www.hetzner.com/cloud)
  y [condiciones](https://www.hetzner.com/legal/terms-and-conditions/) (la administración y la seguridad corren por tu cuenta).

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
