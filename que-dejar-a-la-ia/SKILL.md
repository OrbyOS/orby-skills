---
name: que-dejar-a-la-ia
description: Repasa las tareas de un negocio y decide, con criterios claros, cuáles puede hacer la IA sola, cuáles con revisión y cuáles no se le dejan nunca; lo deja escrito como reglas del negocio (REGLAS-IA.md) y, si usa Claude Code, como reglas que Claude respeta en cada sesión. Úsala cuando alguien pregunte qué puede delegar en la IA, tenga miedo de que la IA haga algo que no debe, quiera poner límites a sus agentes o a su equipo con la IA, o pida una política de uso de IA para su negocio.
---

# Qué dejar a la IA y qué no

La pregunta útil no es «¿la IA sabe hacer esto?», sino «¿qué pasa si lo hace mal y nadie lo ve?». Esta skill
repasa las tareas del negocio con esa pregunta y deja unas reglas escritas que se pueden dar a cualquier persona o
agente.

## Las cuatro preguntas

Para cada tarea:

1. **¿Se puede deshacer?** Un borrador se borra. Un pago, un correo enviado, un post publicado o un archivo borrado,
   no del todo.
2. **¿Toca dinero, precios o compromisos?** Cobrar, pagar, poner precio, aceptar condiciones, prometer un plazo.
3. **¿Hay una persona en una situación delicada al otro lado?** Un cliente enfadado, una queja, una baja, un tema de
   salud o personal.
4. **¿Hay datos personales o confidenciales?** De clientes, de pacientes, de empleados, contraseñas.

Con las respuestas:

| Resultado | Nivel |
| --- | --- |
| Se puede deshacer y no toca nada de las preguntas 2 a 4 | **La IA sola**: investigar, ordenar, resumir, preparar borradores para ti |
| No se puede deshacer, pero pasa por ti antes de salir | **La IA prepara, tú decides**: correos, publicaciones, propuestas, respuestas a clientes |
| Toca dinero o compromisos, o hay una persona delicada al otro lado | **Tuyo, con ayuda**: la IA te prepara la información; tú haces y dices |
| Datos personales sensibles, o pagos y borrados sin revisión | **Nunca a la IA sola**, y cuidado con qué datos le pasas |

Tres reglas que valen para casi cualquier negocio y que conviene proponer siempre:
- Nada que no se pueda deshacer sin que lo veas antes: pagar, borrar, publicar, enviar.
- A un cliente molesto le contesta una persona. La IA puede ayudarte a entender qué le pasa, pero no responde ella.
- El precio lo decides tú. La IA puede preparar la propuesta entera; la cifra no.

## Paso 1. Las tareas

Pide la lista de tareas en las que usa o quiere usar IA (o que haría alguien de su equipo con IA). Si no la tiene,
repasa con él estos grupos y que diga cuáles hace: contenido y redes, correo y mensajes, ventas y propuestas,
atención al cliente, facturas y pagos, documentos y contratos, datos de clientes.

Pregúntale también qué herramientas de IA usa y si alguna puede actuar sola (enviar, publicar, pagar): esas son las
que más necesitan reglas.

## Paso 2. Clasificar

Pasa cada tarea por las cuatro preguntas y enséñale la tabla con el nivel y una línea de por qué. Si duda en
alguna, que decida él; si su decisión deja algo irreversible sin revisión, díselo una vez, con el riesgo concreto,
y respeta lo que decida.

Si su sector tiene normas propias (salud, finanzas, legal, menores), añade como «nunca a la IA sola» cualquier texto
que pueda prometer resultados o dar un consejo profesional, y recomiéndale revisarlo con quien lleve ese tema.

## Paso 3. Escribir REGLAS-IA.md

Con la plantilla `plantilla-reglas.md` (en esta carpeta). Corto y en imperativo, para que lo entienda cualquiera de
su equipo y cualquier agente.

## Paso 4. Si usa Claude Code

Ofrécele dos cosas más, y haz solo las que acepte:
1. **Que Claude las lea siempre**: añadir al `CLAUDE.md` de su carpeta de trabajo la línea «Sigue las reglas de
   REGLAS-IA.md. Si una tarea choca con ellas, para y pregunta».
2. **Que algunas no dependan de que Claude se acuerde**: en el archivo de ajustes del proyecto
   (`.claude/settings.json`), reglas de permisos que piden confirmación o bloquean acciones concretas. Por ejemplo,
   pedir confirmación antes de cualquier comando que borre archivos. Escríbelas solo para acciones que él haya
   puesto en «nunca» o en «tú decides», enséñale el archivo antes de guardarlo y explícale cómo quitarlas.

## Revisión antes de entregar

- ¿Todo lo que no se puede deshacer está en «tú decides» o en «nunca»?
- ¿Las tres reglas generales están, salvo que él haya decidido otra cosa?
- ¿Cada regla se entiende sin explicación?
- ¿Hay alguna regla que él no haya aceptado? Fuera.
