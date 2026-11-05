# Kimi K3 en 8 GB de RAM: qué es y cómo probarlo

Un programador ha escrito en C un motor de 176 KB que ejecuta Kimi K3, un modelo de 2,78 billones de parámetros, en una sola CPU y con 8,24 GB de RAM, sin tarjeta gráfica. No carga el modelo en memoria: lo va leyendo del disco y coge solo lo que hace falta en cada paso.

Comprobado el 5 de noviembre de 2026 en [FareedKhan-dev/kimi-k3-in-c](https://github.com/FareedKhan-dev/kimi-k3-in-c): más de 10.500 estrellas y licencia Apache 2.0. Las cifras son las que publica el proyecto.

---

## Lo que casi nadie te cuenta

| Con esta RAM | Segundos por token |
| --- | --- |
| 8 GB | 26,5 s |
| 32 GB | 24,2 s |
| 64 GB | 19,8 s |
| 128 GB o más | 5,6 s |

Un token es un trocito de palabra. Esas medidas son de una máquina de 124 núcleos con un disco muy rápido: en un portátil normal puede ir más lento. La respuesta es idéntica en todas; más memoria solo compra velocidad.

**Y el modelo ocupa 1,56 TB.** Necesitas unos 1,7 TB libres. Es una demostración impresionante, no un sustituto de tu chat de cada día.

## Pruébalo sin descargar el modelo

En un minuto compruebas que el motor funciona. Necesitas un compilador (GCC o Clang). Pégale esto a Claude Code:

```text
Clona https://github.com/FareedKhan-dev/kimi-k3-in-c, léeme qué vas a ejecutar y luego haz make -j y make test.
No descargues el modelo. Explícame sin tecnicismos qué demuestra cada prueba.
```

Si todo va bien, termina con «ENGINE MATCHES THE REFERENCE EXACTLY».

## Si quieres ir a por el modelo completo

Antes de descargar nada, deja que el proyecto mire tu ordenador:

```text
Ejecuta ./scripts/k3-doctor.sh y dime si mi ordenador puede con el modelo completo, cuánto disco necesito, cuánto tardaría la descarga
y cuánto tardaría en responder una pregunta corta. No descargues nada todavía.
```

## Lo que sí te puedes llevar

Si lo que quieres es usar IA en tu ordenador sin pagar, hay modelos pequeños mucho más prácticos. Para ti, esto es la prueba de hacia dónde va todo: cada vez hace falta menos máquina.

## Fuentes

- [Repositorio de kimi-k3-in-c](https://github.com/FareedKhan-dev/kimi-k3-in-c).

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
