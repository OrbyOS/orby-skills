# SolidCraft: Claude te diseña piezas en 3D

SolidCraft es un programa de diseño 3D gratis y de código abierto. Trae un servidor MCP: conectas a Claude y diseña dentro del programa mientras tú miras. Cuando cambias una medida, la pieza se recalcula entera.

Comprobado el 5 de noviembre de 2026 en su repositorio, [tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft): más de 13.800 estrellas y licencia Apache 2.0.

---

## Lo que puedes esperar

El propio proyecto dice que está al principio y que ya sirve para piezas sencillas. Soportes, cajas, escuadras y tapas: bien. Para una pieza de la que dependa algo importante, mide y comprueba antes de usarla.

## 1. Instala SolidCraft

Descárgalo en [solidcraft.io/download](https://solidcraft.io/download), para Windows, Mac o Linux. También puedes [probarlo en el navegador](https://solidcraft.io/app), sin instalar nada, pero para conectar a Claude necesitas la versión de escritorio.

## 2. Conéctalo a Claude Code

Con un solo comando, en la Terminal:

```bash
claude mcp add solidcraft -- solidcraft-cli mcp
```

Si la Terminal no encuentra `solidcraft-cli`, pídele a Claude que lo localice en tu instalación y use la ruta completa. Abre la aplicación antes de empezar: así ves cómo modela en la pantalla.

## 3. Pide tu primera pieza

```text
Con SolidCraft, diséñame una escuadra de 72 mm de alto, 50 de ancho y 60 de fondo, con 5 mm de grosor y un agujero de 4 mm en cada ala.
Deja las medidas como parámetros, para poder cambiarlas después. Cuando acabes, dime qué has hecho y qué tendría que comprobar antes de imprimirla.
```

## 4. Cámbiala sin empezar de nuevo

```text
Hazla de 80 mm de ancho y deja el resto igual. Comprueba que los agujeros siguen centrados.
```

## 5. Expórtala

```text
Expórtala en 3MF y en STL para mi impresora 3D, en esta carpeta. Dime el tamaño final de la pieza.
```

---

## Dos cuidados

- **Mide antes de fiarte.** La IA puede equivocarse con una medida. Mira las dimensiones en la pantalla antes de gastar plástico.
- **Nada que aguante peso sin comprobarlo.** Para una pieza de seguridad, hace falta alguien que sepa calcularla.

## Fuentes

- [Repositorio de SolidCraft](https://github.com/tangency-labs/solidcraft) y [su guía de MCP](https://github.com/tangency-labs/solidcraft/blob/main/docs/mcp.md).

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
