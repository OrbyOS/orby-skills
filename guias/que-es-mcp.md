# Qué es MCP, explicado sin tecnicismos

MCP es la forma estándar de conectar una IA con tus herramientas: tu correo, tu calendario o tu tienda. La documentación oficial lo compara con un puerto USB-C. Antes, cada aparato tenía su cable. Con USB-C, todo se enchufa igual. Aquí tienes qué es, cómo funciona con un ejemplo real y tres reglas antes de conectar nada.

Revisada el 3 de noviembre de 2026 con la documentación oficial de MCP (enlaces al final).

---

## Las cuatro palabras

| Palabra | Qué es | Con un ejemplo |
| --- | --- | --- |
| **MCP** | Las normas para que la IA y las herramientas se entiendan | El estándar USB-C |
| **Cliente** | La aplicación de IA que usas | Claude o ChatGPT |
| **Servidor** | El adaptador de cada herramienta, que le dice a la IA qué se puede hacer con ella | El servidor de tu tienda, con «ver pedidos» y «ver cliente» |
| **Llaves** | El permiso que le das para entrar y hasta dónde | «Puede leer pedidos, pero no devolver dinero» |

## Y entonces, ¿qué diferencia hay con una API?

Una API es la puerta que cada servicio abre a otros programas. Cada una tiene sus propias normas, y alguien tiene que programar la conexión.

MCP no sustituye a las API: muchas veces un servidor MCP las usa por detrás. Lo que añade es una forma común para que **la IA vea por sí misma qué puede hacer** con cada herramienta, sin que nadie programe una conexión distinta para cada combinación de aplicación y servicio.

En la práctica: con una API, un programador construye la conexión. Con MCP, si ya hay un servidor, lo conectas y le hablas a Claude con normalidad.

## Un ejemplo: pedidos y correos

Conectas dos servidores a Claude, el de tu tienda y el de tu correo. Le pides:

```text
Mira los pedidos que llevan más de cinco días sin enviarse. Prepara un borrador de correo a cada cliente, disculpándote y dándole una fecha. No envíes nada: enséñamelos primero.
```

Lo que ocurre por detrás:

1. Claude ve qué herramientas tiene cada servidor.
2. Pide al de la tienda los pedidos, y él se los devuelve.
3. Pide al del correo que cree los borradores.
4. Tú los revisas y decides.

No has copiado ni pegado nada, ni ha hecho falta programar.

## Dónde se conecta

- **En Claude:** en sus conectores, con botones (capítulo 3.1).
- **En Claude Code:** como plugin o con un comando (capítulo 3.15).

## Tres reglas antes de conectar nada

### 1. Solo de quien te fíes

Un servidor que se instala en tu ordenador es un programa con tus mismos permisos. La documentación oficial avisa de que uno malicioso puede ejecutar órdenes, leer tus archivos o borrar datos. Usa el del propio servicio, y lee antes de instalar lo que encuentres por ahí.

### 2. La llave más pequeña que sirva

Empieza solo leyendo y en una sola cuenta o proyecto. La documentación oficial recomienda dar el mínimo permiso e ir ampliando. Si roban una llave con permiso para todo, el daño es de todo.

### 3. Tú apruebas lo que no se puede deshacer

Enviar, pagar, borrar o publicar, siempre con tu aprobación. Un correo o un comentario de un cliente pueden traer instrucciones escondidas para la IA, y la IA no siempre las distingue de las tuyas. Por eso lees lo que va a hacer antes de decir que sí.

Para comprobarlo, pega esto en Claude antes de usar un conector nuevo:

```text
Dime qué puede hacer este conector, una por una, y cuáles de sus acciones no se pueden deshacer. Después dime qué permisos puedo quitarle para lo que quiero hacer: [tu tarea].
```

## En resumen

- MCP es el USB-C de la IA: una forma común de conectarla a tus herramientas.
- Cliente es tu IA; servidor, el adaptador de cada herramienta; llaves, tus permisos.
- No sustituye a las API: te ahorra programar la conexión.
- Solo servidores de fiar, el mínimo permiso y tu aprobación en lo irreversible.

---

## Fuentes

- Model Context Protocol: [qué es MCP](https://modelcontextprotocol.io/docs/getting-started/intro) y [buenas prácticas de seguridad](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices).

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
