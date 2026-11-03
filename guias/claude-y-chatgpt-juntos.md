# Claude y ChatGPT juntos: que Codex revise lo que hace Claude Code

OpenAI ha publicado un plugin oficial para usar Codex, su agente de programación, sin salir de Claude Code. Sirve sobre todo para
tener una segunda opinión: que un modelo de otra empresa revise lo que ha hecho Claude, o que se encargue de un problema en el que
Claude se ha atascado.

Revisada el 3 de noviembre de 2026 con su documentación (enlaces al final). Ese día tenía 34,8k estrellas en GitHub y licencia
Apache-2.0. No lo hemos instalado: lo que sigue viene de esa documentación.

> [!IMPORTANT]
> **No te da un plan de 200 dólares gratis.** El plugin es gratis, pero todo lo que hace gasta de tu límite de Codex. El plan
> gratuito de ChatGPT está pensado para tareas rápidas. Y es una segunda opinión, no una verdad: revisa lo que proponga igual que
> revisas lo de Claude.

---

## Lo que hace falta

- **Claude Code** en tu ordenador (capítulo 3.2).
- **Node.js 18.18 o posterior.**
- **Una cuenta de ChatGPT** (el plugin admite también la gratuita) o una clave de la API de OpenAI.

## Instalarlo

Pega estas líneas en Claude Code, una a una:

```text
/plugin marketplace add openai/codex-plugin-cc
/plugin install codex@openai-codex
/reload-plugins
/codex:setup
```

`/codex:setup` comprueba si Codex está listo y, si falta, te ofrece instalarlo. Si te falta iniciar sesión:

```text
!codex login
```

Si usas una clave de API, trátala como una contraseña: nunca en el chat (capítulo 2.5).

## Los comandos

| Comando | Para qué | ¿Cambia algo? |
| --- | --- | --- |
| `/codex:review` | Revisa los cambios que tienes a medias | No, solo lee |
| `/codex:adversarial-review` | Cuestiona las decisiones: lo que se ha dado por hecho y lo que puede fallar. Le puedes decir en qué fijarse | No, solo lee |
| `/codex:rescue` | Le pasa una tarea a Codex: investigar un fallo o intentar arreglarlo | **Sí, puede tocar archivos** |
| `/codex:transfer` | Continúa esta conversación dentro de Codex | Copia la conversación a Codex |
| `/codex:status`, `/codex:result` y `/codex:cancel` | Ver cómo va, ver el resultado y cancelar | No |

## Tres formas de usarlo

### 1. Revisión antes de publicar

Revisar lleva un rato, así que mándalo en segundo plano y sigue a lo tuyo:

```text
/codex:review --background
/codex:status
/codex:result
```

### 2. Que le busque las pegas a una decisión

```text
/codex:adversarial-review Comprueba si este formulario de pago puede cobrar dos veces y qué pasa si se corta la conexión.
```

### 3. Cuando Claude se atasca

```text
/codex:rescue Investiga por qué falla el envío del formulario. De momento no cambies nada: dime qué has encontrado.
```

Y cuando vuelva con su respuesta, no la apliques a ciegas:

```text
Esto es lo que dice Codex: [pega lo que ha dicho]. No te fíes solo porque lo diga: comprueba cada punto en el código. Dime en cuáles
tiene razón, en cuáles no y por qué. No cambies nada hasta que te lo diga.
```

## Qué consumo sale de cada plan

Precios y límites de la página oficial de Codex, en dólares y sin contar impuestos:

| Plan | Precio al mes | Qué tiene |
| --- | --- | --- |
| **Free** | 0 $ | Tareas rápidas, y la página no da cifras de límite |
| **Go** | 8 $ | Tareas ligeras, y tampoco da cifras |
| **Plus** | 20 $ | Mensajes cada 5 horas: de 15 a 160 con GPT-6.1 Sol y de 350 a 3.000 con GPT-6 Luna |
| **Pro** | 100, 200 o 500 $ | Ahora mismo sin límite cada 5 horas |
| **Clave de API** | Lo que uses | A precio de API, sin funciones en la nube |

Tres cosas que conviene saber:

- **Son estimaciones, no límites fijos.** Puede haber además un límite semanal, también en Pro. Lo que te queda se ve en el panel de uso de Codex.
- **Comprueba el plan gratuito.** El plugin dice admitirlo, pero la página de precios describe ese acceso en la aplicación de
  escritorio y sujeto a despliegue. `/codex:setup` y una revisión pequeña te sacan de dudas.
- **El uso de Claude también corre.** Claude Code gasta de tu plan de Claude como siempre. Este plugin no lo sustituye.

## Avisos

> [!CAUTION]
> **La revisión automática puede vaciarte el límite.** El plugin tiene un modo (`--enable-review-gate`) que hace revisar a Codex cada
> respuesta de Claude y le obliga a arreglar lo que encuentre. Su documentación avisa de que puede crear un bucle largo. Déjalo apagado
> salvo que estés mirando.

- **Tu código también va a otra empresa.** Lo que revisa Codex lo lee OpenAI, además de Anthropic. Si hay datos de clientes o claves,
  mira antes sus condiciones (capítulo 0.5).
- **Dos modelos también se equivocan.** Que estén de acuerdo no prueba nada. Lo que importa se prueba de verdad, y si no sabes
  juzgarlo, pide a alguien que sepa.
- **Pensado para código.** Necesita un proyecto con cambios que revisar. Para una segunda opinión sobre un texto, basta con pegarlo en otro chat.
- **El nombre de los modelos cambia.** El plugin elige solo si no le dices nada, así que no hace falta que elijas tú.

## En resumen

- Plugin oficial de OpenAI, gratis, para usar Codex desde Claude Code.
- `/codex:review` y `/codex:adversarial-review` solo leen. `/codex:rescue` puede tocar archivos.
- Gasta de tu límite de Codex: con el plan gratis no tendrás el uso de un plan de pago.
- Pide a Claude que compruebe lo que dice Codex antes de aplicarlo.
- Deja la revisión automática apagada, y ten en cuenta que tu código lo lee también OpenAI.

---

## Fuentes

- OpenAI: [repositorio y documentación del plugin](https://github.com/openai/codex-plugin-cc) (requisitos, instalación, comandos y
  avisos) y [precios y límites de Codex](https://learn.chatgpt.com/docs/pricing).

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
