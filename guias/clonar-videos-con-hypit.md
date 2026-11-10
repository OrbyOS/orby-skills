# Hypit: convierte un vídeo que funcionó en tu propia receta

Hypit le da a tu agente (Claude Code, Codex) una forma de crear vídeo. Le pasas uno que ya haya funcionado y lo convierte en un flujo de trabajo: material, subtítulos, recursos y efectos, todo anclado a las palabras en lugar de a los segundos.

Comprobado el 5 de noviembre de 2026 en [hypit-ai/hypit](https://github.com/hypit-ai/hypit): más de 28.000 estrellas. Su licencia es «Apache 2.0 con condiciones»: léela si lo vas a usar en una empresa.

---

## Cuánto cuesta

Hypit es gratis. Lo que se paga es tu agente y, si los usas, los modelos que generan imagen, voz o vídeo. Puedes conectar tus propios servicios o modelos locales.

## 1. Instálalo

Necesitas Claude Code y Node 22.15 o superior. Con un solo comando:

```bash
npx skills add hypit-ai/hypit -g
```

Al usarlo por primera vez, tu agente comprueba si falta algo y te ayuda a prepararlo.

## 2. Pásale un vídeo y dile qué cambiar

```text
Con Hypit, analiza este vídeo: [ruta del vídeo]. Saca su estructura: gancho, ritmo, cortes, subtítulos, recursos y efectos.
Antes de generar nada, enséñame la receta y dime qué servicios harían falta y cuánto costarían.
```

Después, cámbialo por lo tuyo:

```text
Usa esa estructura con mi tema: [de qué va mi vídeo]. Mi público es [quién]. No copies sus frases ni sus imágenes.
Escríbeme el guion y espera a que lo apruebe.
```

## 3. Dale tu voz

```text
Usa esta grabación mía como voz del vídeo: [ruta del audio]. Si hay que clonarla, dime antes con qué servicio y cuánto cuesta.
```

Clona solo tu propia voz, o la de quien te haya dado permiso.

## 4. Corrige hablando

```text
Haz el gancho más grande y quita el efecto del segundo 12. No toques nada más.
```

---

## Copia la estructura, no el contenido

Un vídeo que funcionó te enseña el molde. Sus frases, imágenes y música son de quien las hizo. Pon tu tema, tu ejemplo y tu voz; además, es lo que hace que el vídeo sea tuyo.

## Fuentes

- [Repositorio de Hypit](https://github.com/hypit-ai/hypit) y [su guía de inicio](https://hypit.ai/quickstart/).

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
