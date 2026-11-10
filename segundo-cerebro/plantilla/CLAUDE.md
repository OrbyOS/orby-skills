# [Nombre del negocio] · cómo está montado todo

Esta carpeta es el segundo cerebro del negocio. Léela entera antes de hacer nada. Si algo de lo que te piden choca
con estas reglas, pregunta antes de seguir.

**Qué hacemos:** [una frase: qué vendemos y a quién].
**Quién trabaja aquí:** [nombre del dueño o la dueña] y los agentes de IA que lean este archivo.
**Idioma:** [español de España, de tú…].

## Mapa

```
[carpeta del negocio]/
├── CLAUDE.md          Este archivo: cómo está montado todo
├── entrada/           Lo que llega sin ordenar (notas, audios, capturas). Se vacía cada semana
├── clientes/          Una carpeta por cliente
│   └── <cliente>/
│       ├── ficha.md       Quién es, qué ha comprado, qué le importa, cómo habla
│       ├── historial.md   Una línea por cada contacto, la más reciente arriba
│       ├── llamadas/      AAAA-MM-DD.md con las notas o la transcripción de cada llamada
│       └── entregas/      Lo que le hemos entregado, con fecha
├── contenido/
│   ├── ideas/         Una idea por archivo o una lista en ideas.md
│   ├── guiones/       AAAA-MM-DD_tema.md
│   └── publicado/     Lo publicado, con fecha, enlace y cómo funcionó
├── oferta/            Qué vendemos, precios, garantías, preguntas frecuentes y objeciones
├── estrategia/        Objetivos, a quién nos dirigimos, competencia, decisiones importantes
├── operaciones/       Procesos, plantillas, herramientas y proveedores
└── archivo/           Lo terminado o superado. No se edita
```

## Dónde va cada cosa nueva

- Algo que no sabes dónde va → `entrada/`, y avisa.
- Un cliente nuevo → copia `clientes/_plantilla-cliente/` a `clientes/<nombre-del-cliente>/` y rellena la ficha.
- Una llamada o una reunión → `clientes/<cliente>/llamadas/AAAA-MM-DD.md` y una línea en su `historial.md`.
- Una propuesta o una entrega → `clientes/<cliente>/entregas/AAAA-MM-DD_que-es.md`.
- Una idea de contenido → `contenido/ideas/`. Un guion → `contenido/guiones/`.
- Un cambio de precio o de oferta → `oferta/` y una línea en `estrategia/decisiones.md` con la fecha y el porqué.
- Una versión superada → `archivo/`, nunca se borra sin preguntar.

## Nombres

- Fechas siempre como `AAAA-MM-DD`, al principio del nombre, para que se ordenen solas.
- Nombres de carpeta en minúsculas, con guiones y sin tildes: `clientes/clinica-dental-sol/`.
- Un archivo por cosa. Si un archivo pasa de dos pantallas, probablemente son dos.

## Reglas para la IA

1. **Antes de trabajar para un cliente, lee su `ficha.md` y su `historial.md`.** No le preguntes al dueño lo que ya
   está escrito ahí.
2. **Después de cada trabajo, deja rastro:** una línea en el historial del cliente o en el archivo que toque, con la
   fecha.
3. **No inventes.** Si un dato no está en la carpeta, pregúntalo o márcalo como `[PENDIENTE]`.
4. **No borres nada.** Lo superado va a `archivo/`. Borrar solo con permiso expreso.
5. **Nada sale hacia fuera** (correos, mensajes, publicaciones) sin el OK del dueño.
6. **Datos sensibles:** contraseñas y claves no se guardan en esta carpeta. Los datos de salud, bancarios o de
   menores de los clientes, tampoco: si hacen falta, se indica dónde están, no se copian.
7. **Si algo está desordenado** (un archivo en el sitio equivocado, una fecha mal puesta), dilo y propón moverlo; no
   lo muevas sin avisar.

## Encargos frecuentes

- «Prepárame la llamada con [cliente]» → lee su ficha, su historial y su última llamada, y entrega: quién es en dos
  líneas, de qué hablamos la última vez, qué quedó pendiente, qué le ofrecimos y tres preguntas para esta llamada.
- «Resume la llamada de hoy con [cliente]» → guarda las notas en `llamadas/`, actualiza `historial.md` y la ficha si
  ha cambiado algo, y lista lo que queda pendiente y de quién.
- «¿Qué tengo esta semana?» → repasa los historiales con tareas pendientes y `entrada/`.
- [Añade aquí los tuyos.]

## Lo que he aprendido
(Cada vez que el dueño corrija cómo se hace algo, apúntalo aquí con la fecha. Estas reglas mandan sobre las de arriba.)
