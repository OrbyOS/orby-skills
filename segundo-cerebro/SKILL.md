---
name: segundo-cerebro
description: Monta el «segundo cerebro» de un negocio en una carpeta que Claude entiende: una carpeta por área (clientes, contenido, oferta, estrategia, operaciones), un archivo CLAUDE.md que le explica a la IA cómo está todo y dónde va cada cosa, y fichas e historiales por cliente para que encargos como «prepárame la llamada de mañana» salgan sin explicar nada. También ordena lo que el usuario ya tiene disperso. Úsala cuando alguien quiera organizar su negocio para trabajar con IA, montar un segundo cerebro, que Claude «sepa» de sus clientes, o tenga la información repartida entre notas, chats y documentos.
---

# Segundo cerebro del negocio

Las ideas en las notas del móvil, los clientes en el chat, los guiones en diez documentos. Cuando hace falta algo, no
está. Esta skill lo junta en una sola carpeta, ordenada para que la lea la IA y no solo la persona: cada cosa en su
sitio, con su fecha, y un archivo que explica a Claude cómo está montado todo.

La plantilla está en `plantilla/` (en esta carpeta). El corazón es `plantilla/CLAUDE.md`.

## Paso 1. Dónde y para qué

Pregunta:
1. **Dónde lo quiere:** una carpeta nueva (por ejemplo, `~/Documents/<nombre-del-negocio>`). Si ya tiene una carpeta
   del negocio, pregunta si se monta dentro o al lado. Nunca muevas ni borres lo que ya tiene sin enseñarle antes el
   plan.
2. **Qué negocio es**, en una frase: qué vende y a quién.
3. **Qué áreas necesita.** Las de la plantilla sirven para casi todos (clientes, contenido, oferta, estrategia,
   operaciones). Quita las que no use y añade las que falten (por ejemplo, `formacion/` si da cursos o `proyectos/`
   si trabaja por proyectos).
4. **Los tres encargos que más repite** («prepárame la llamada», «escribe el correo de seguimiento», «¿qué tengo esta
   semana?»). Van en el CLAUDE.md para que salgan siempre igual.

## Paso 2. Montarlo

1. Copia `plantilla/` a la carpeta elegida.
2. Rellena `CLAUDE.md` con lo que te ha contado: la frase del negocio, las áreas que se quedan, los encargos
   frecuentes y cualquier regla suya («los presupuestos siempre en PDF», «a los clientes se les habla de usted»).
   Quita lo que no aplique. Que no pase de dos pantallas.
3. Si el usuario no usa Claude Code en esa carpeta, explícale cómo conectarla: abrir Claude Code dentro de la carpeta
   (el `CLAUDE.md` se lee solo) o, en Claude.ai, crear un Proyecto y subir el `CLAUDE.md` y las fichas.

## Paso 3. Llenarlo con lo que ya tiene

Pídele lo que tenga disperso y ordénalo con él:
- **Clientes:** para cada cliente activo, una carpeta copiada de `clientes/_plantilla-cliente/`, con su ficha y su
  historial. Si pega notas o chats, saca de ahí la ficha y las líneas del historial, y enséñaselas para que las
  confirme. No inventes lo que no esté.
- **Contenido:** las ideas en `contenido/ideas/`, los guiones con su fecha en `contenido/guiones/`.
- **Oferta:** lo que vende, sus precios y las preguntas que le hacen siempre.
- **Lo que no sepas dónde va:** a `entrada/`, y lo decidís juntos.

No hace falta llenarlo todo el primer día. Basta con los clientes activos y la oferta: lo demás se va llenando al
trabajar, porque cada encargo deja rastro.

## Paso 4. Probarlo

Haz con él uno de sus encargos frecuentes, por ejemplo «prepárame la llamada con [cliente]», leyendo solo lo que hay
en la carpeta. Si te falta algo para hacerlo bien, eso es lo que hay que añadir a la ficha o al CLAUDE.md. Repite
hasta que el encargo salga sin preguntarle nada.

## Mantenerlo vivo

- Después de cada trabajo, deja rastro: una línea en el historial del cliente o en el archivo que toque.
- Una vez a la semana, vacía `entrada/` repartiendo cada cosa en su sitio.
- Cuando el usuario corrija cómo se hace algo, apúntalo en «Lo que he aprendido» del CLAUDE.md con la fecha.
- Lo superado va a `archivo/`. No se borra nada sin preguntar.
- Nada de contraseñas ni claves en la carpeta. Datos sensibles de clientes (salud, banca, menores): se indica dónde
  están, no se copian.

## Cómo pedírselo a Claude

- «Monta el segundo cerebro de mi negocio en Documentos.»
- «Te pego mis notas de clientes: ordénalas en sus fichas.»
- «Prepárame la llamada de mañana con [cliente].»
