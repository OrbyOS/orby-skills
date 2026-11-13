# Craft Anything: tu propia versión de una web o una app, con Claude Code

Craft Anything estudia una web, una aplicación o un juego que ya existe y le pide a tu Claude Code que construya un proyecto nuevo, tuyo, desde cero. Después compara el resultado con el original y te lo deja listo para abrir y retocar.

Revisada el 13 de noviembre de 2026.

---

## Qué necesitas

- Claude Code instalado y con tu sesión iniciada (Craft Anything usa el tuyo, sin tocarlo).
- Craft Anything: hay instaladores para Mac, Windows y Linux en la página de versiones del repositorio. Si prefieres compilarlo, necesitas Rust 1.97 o posterior.

## Cómo instalarlo

Lo más fácil: descarga el instalador de tu sistema en github.com/storytold/craft-anything (apartado Releases).

Desde el código:

```
git clone https://github.com/storytold/craft-anything && cd craft-anything
cargo run --release -p craft-anything
```

Para comprobar que todo está bien: `craft-anything-cli doctor`.

## Cómo usarlo

Con la aplicación, le das la dirección o el archivo y lo que quieres. Desde la terminal:

```
craft-anything-cli rebuild https://tu-ejemplo.com "Recrea esta web"
craft-anything-cli rebuild - "Un juego de la serpiente" --rounds 1
```

Funciona en cuatro pasos: estudia el original, construye un proyecto nuevo, lo compara con el original (en una web, a tres anchos de pantalla) y te lo deja listo.

Luego lo retocas pidiéndolo: «pon la cabecera en azul», «añade un formulario de contacto».

## Lo que conviene saber

- Está en una fase muy temprana: tendrá fallos.
- Crea tu versión, no copia el código del original. Aun así, no uses marcas, logos ni textos de otros: inspírate en la estructura y pon lo tuyo.
- Gasta de tu plan de Claude Code mientras construye.
- Es gratis y de código abierto (MIT o Apache 2.0).
