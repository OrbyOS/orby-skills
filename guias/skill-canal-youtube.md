# Skills de Claude para llevar un canal de YouTube

`claude-youtube` es un paquete gratuito con 14 comandos para Claude Code: revisa tu canal, te escribe guiones, te prepara el calendario, analiza lo que funciona a tu competencia y te deja listo lo que hay que rellenar al subir. Aquí tienes cómo instalarlo, un flujo para cada vídeo y lo que no hace: el montaje.

Revisada el 3 de noviembre de 2026 con su documentación (enlace al final). Ese día tenía 644 estrellas en GitHub y licencia MIT. Está en beta y su último cambio es de abril de 2026.

---

## Instalarlo

Con Claude Code instalado (capítulo 3.2), pega esto en la terminal:

```bash
git clone https://github.com/AgriciDaniel/claude-youtube.git
cp -r claude-youtube/skills/claude-youtube ~/.claude/skills/claude-youtube
```

Vuelve a abrir Claude Code. Sin más, ya te da guiones, ideas y estrategia. Para que mire los datos reales de tu canal, necesita una clave gratuita de la API de YouTube, y para tus estadísticas privadas, una autorización de Google. Su documentación lo explica.

## Los comandos, por trabajo

| Trabajo | Comando | Qué te da |
| --- | --- | --- |
| **Plan** | `/youtube strategy` | Posicionamiento, temas e hitos a 30, 60 y 90 días |
| | `/youtube calendar` | Calendario del mes, con los Shorts |
| | `/youtube ideate` | 10 ideas ordenadas, con su gancho y su miniatura |
| **Analizar virales** | `/youtube competitor` | Vídeos destacados de otros y huecos que puedes ocupar |
| | `/youtube audit` | Revisión completa de tu canal |
| | `/youtube analyze` | Qué dicen tus estadísticas y qué hacer primero |
| **Guion** | `/youtube script` | Guion para que no se vayan, con gancho y llamada a la acción |
| | `/youtube hook` | 5 aperturas distintas |
| **Publicar** | `/youtube seo` | 3 títulos, descripción, etiquetas y capítulos |
| | `/youtube thumbnail` | Indicaciones para 3 miniaturas |
| | `/youtube metadata` | Todo lo que hay que rellenar al subir |
| **Reutilizar** | `/youtube shorts` y `/youtube repurpose` | Shorts y versiones para otras redes |
| **Ingresos** | `/youtube monetize` | Vías de ingresos y plan a 90 días |

**El montaje no está:** ninguno edita el vídeo. Para eso, sigue el capítulo 5.14, que te monta el proceso con Claude Code, y el 5.12 para sacar los clips.

## El flujo de un vídeo

### 1. Una vez: tu canal

```text
/youtube strategy Mi canal es [dirección o tema] y le hablo a [a quién]. Mi objetivo es [objetivo]. Antes de recomendarme nada, dime lo que has podido comprobar con datos y lo que es opinión general.
```

### 2. Cada semana: la idea

```text
/youtube competitor Estos son tres canales que le hablan a mi mismo público: [canales]. Dime qué vídeos les han funcionado mucho más que su normal y por qué crees que ha sido. Después, con /youtube ideate, dame ideas que yo pueda contar con mi experiencia. No me propongas copiar ninguno.
```

### 3. El guion, con lo tuyo

```text
/youtube script Sobre [idea]. Antes de escribir, pregúntame de dos en dos lo que solo sé yo: casos reales, errores y datos. Si un dato no me lo has oído a mí o no tiene fuente, márcalo como [PENDIENTE]. Respeta mi manera de hablar. Y dame cinco ganchos con /youtube hook.
```

### 4. Para subirlo

```text
/youtube metadata Este es el guion final: [pégalo]. El título no puede prometer nada que el vídeo no cumpla.
```

Después, con unas semanas de datos, usa `/youtube analyze` y apunta lo que aprendas como regla.

> [!CAUTION]
> **Sus referencias son orientativas.** Los datos de CTR, retención o ingresos por nicho van dentro de la skill, y YouTube cambia. Fíate más de tus propias estadísticas. Y si un guion trae una cifra, compruébala antes de decirla a cámara.

## En resumen

- `claude-youtube`: 14 comandos gratis para plan, guion, publicación y análisis.
- No monta el vídeo: para eso, capítulo 5.14.
- Con la clave de YouTube, trabaja con los datos de tu canal.
- Métele tu experiencia antes de escribir, y marca lo que no tenga fuente.
- Tus estadísticas mandan más que sus referencias.

---

## Fuentes

- claude-youtube: [repositorio y documentación](https://github.com/AgriciDaniel/claude-youtube) (comandos, instalación, requisitos y estado).

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
