# OpenMAIC: convierte un PDF en una clase con profesores de IA

OpenMAIC es una plataforma de código abierto de la Universidad de Tsinghua (licencia MIT, más de 40.000 estrellas en GitHub). Le das un tema o tus materiales y te monta una clase completa: diapositivas, exámenes, simulaciones y profesores de IA que te la explican.

Revisada el 14 de noviembre de 2026.

---

## Qué hace

- **Acepta tus materiales:** PDF, Word, PowerPoint, hojas de cálculo, texto e imágenes. También le vale describir un tema.
- **Monta la lección en minutos:** primero el índice y después cada parte, con diapositivas, preguntas tipo examen y simulaciones que se pueden tocar.
- **Profesores y compañeros de IA:** hablan en voz alta, pintan en la pizarra y responden a lo que preguntas.
- **Se exporta:** a un PowerPoint que puedes editar, a una página HTML que funciona sin internet o a un paquete para moverla a otra instalación.
- La interfaz está en español, entre otros doce idiomas.

## Para qué sirve en tu negocio

- Convertir tu manual, tu curso o tus apuntes en una clase interactiva para tus alumnos o tu equipo.
- Preparar la formación de un empleado nuevo a partir de los documentos que ya tienes.
- Sacar un PowerPoint de partida para una charla o un taller.

## Cómo probarlo

Sin instalar nada: tiene una demo en open.maic.chat.

En tu ordenador (necesitas Node.js 22 o superior, pnpm y PostgreSQL; el comando `pnpm db:up` te levanta una base de datos de prueba). En la terminal:

`git clone https://github.com/THU-MAIC/OpenMAIC.git`

`cd OpenMAIC && pnpm install`

`cp .env.example .env.local && cp openmaic.example.yml openmaic.yml`

Abre `.env.local`, pon tu clave de OpenAI en `OPENAI_API_KEY` (o cambia a otro proveedor del que tengas clave) y quita el `#` de la línea `DATABASE_URL`. Después:

`pnpm db:up`

`pnpm dev`

Y abre http://localhost:3000 en el navegador. La forma más cómoda: abre Claude Code en esa carpeta y pídele «Instala OpenMAIC siguiendo su Quick Start y ábremelo».

## Lo que conviene saber

- El programa es gratis, pero el modelo de IA que le conectes cobra por uso según tu proveedor.
- Una clase larga con muchos materiales gasta más; prueba primero con un documento corto.
- Revisa siempre el contenido antes de dárselo a nadie: la IA puede equivocarse en datos concretos.
