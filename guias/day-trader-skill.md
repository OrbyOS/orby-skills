# Day Trader Skill: once skills de Claude para el trading intradía

Day Trader Skill son once skills gratis para Claude que te acompañan en una operación de principio a fin: buscan el gráfico, leen las noticias, marcan la entrada y la salida, y antes de arriesgar nada simulan la operación 10.000 veces. Ninguna puede lanzar una orden sola: todo va en simulado por defecto y nada sale sin tu «sí».

Revisada el 7 de noviembre de 2026 con el repositorio del proyecto (enlace al final). Ese día tenía 5.893 estrellas en GitHub y licencia MIT.

> [!CAUTION]
> **Esto no es una recomendación de inversión.** El trading intradía hace perder dinero a la mayoría de quienes lo practican. Las simulaciones te dicen las probabilidades, no te garantizan nada. Empieza siempre en simulado.

---

## 1. Instálala

Pega esto en Claude:

```text
https://github.com/Jakeschincariol/day-trader-skill

install skill
```

O, en Claude Code, como plugin:

```text
/plugin marketplace add Jakeschincariol/day-trader-skill
/plugin install day-trader-skill@day-trader-skill
```

Necesita Python 3.8 o posterior. Las herramientas que leen informes de la SEC te piden tu nombre y tu correo en `trader/config.json`.

## 2. Las once

| Comando | Qué hace |
| --- | --- |
| `/trader-scanner` | Busca entre miles de gráficos los que cumplen una pauta, como la rotura del rango de apertura |
| `/trader-news` | Sigue las noticias de los valores que vigilas |
| `/trader-entry` | Vigila la pauta vela a vela y te dice cuándo entrar |
| `/trader-exit` | Fija el stop y el objetivo antes de entrar |
| `/trader-timemachine` | Simula la sesión 10.000 veces y te da las probabilidades |
| `/trader-risk` | Comprueba cada operación contra tus límites |
| `/trader-budget` | Calcula cuánto comprar según tu presupuesto y tu pérdida máxima |
| `/trader-broker` | Manda la orden a tu bróker, en simulado por defecto y solo con tu «sí» |
| `/trader-alerts` | Te avisa del stop, del objetivo y del cierre |
| `/trader-analyst` | Resume los resultados de las empresas |
| `/trader-pelosi` | Lee las operaciones que declaran los congresistas de Estados Unidos |

## 3. Con una cuenta de fondeo

Pídele a Time Machine que simule con las reglas de tu cuenta: el objetivo, la pérdida máxima total y el límite diario. Mensaje:

```text
/trader-timemachine Simula esta entrada con las reglas de mi cuenta de fondeo: objetivo de 3.000 $, pérdida máxima de 2.000 $ y límite diario de 1.200 $. Dime qué probabilidad tengo de llegar al objetivo antes que al stop y cuántos días tardaría de media. Todo en simulado.
```

La idea: entrar solo en las operaciones con más probabilidad de acierto y descartar las que pueden quemar la cuenta. Menos operaciones, pero mejores. Los números del vídeo son un ejemplo ilustrativo.

## Fuentes

- [Repositorio de Day Trader Skill](https://github.com/Jakeschincariol/day-trader-skill).

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
