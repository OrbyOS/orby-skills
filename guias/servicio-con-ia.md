# Vende el resultado, no el software: cómo montar un servicio hecho con IA

Montar una aplicación de IA y venderla es lo que está haciendo todo el mundo. El problema es que tu cliente no quiere
otra herramienta: no tiene tiempo de aprender a usarla ni ganas de pelearse con ella. Quiere que le llegue hecho.

La alternativa: por fuera, un servicio que entrega un resultado; por dentro, agentes de IA que hacen la mayor parte
del trabajo y una persona que revisa antes de que salga nada. Esta guía lo monta paso a paso.

---

## Paso 1. Elige el resultado que vas a vender

Un buen servicio con IA cumple estas cinco condiciones. Si una falla, busca otro resultado.

| Condición | Por qué | Pregunta para comprobarlo |
| --- | --- | --- |
| **El cliente ya paga por esto** (a alguien o con su tiempo) | No tienes que convencerle de que lo necesita | ¿A quién le paga hoy, o cuántas horas le dedica? |
| **Se repite** (cada semana o cada mes) | Lo repetido es lo que los agentes hacen bien, y te da ingresos recurrentes | ¿Lo necesita otra vez el mes que viene? |
| **Se puede revisar antes de entregarlo** | La revisión humana es lo que hace fiable el servicio | ¿Puedo ver el resultado antes que el cliente? |
| **Se ve si está bien hecho** | El cliente renueva lo que puede comprobar | ¿Cómo sabría el cliente que ha funcionado? |
| **Lo conoces** | Para revisar con criterio tienes que saber cómo es «bien hecho» | ¿Sabría hacerlo yo a mano? |

Ejemplos de resultados que encajan (inventados, para que veas la forma):
- Una gestoría que entrega a cada cliente autónomo un resumen mensual claro de sus números, con lo que tiene que
  hacer ese mes.
- Una agencia que contesta todas las reseñas de Google de sus restaurantes cada semana, en su tono.
- Una consultora que entrega cada lunes a sus clientes un informe de lo que ha hecho la competencia.
- Un editor que entrega cada semana los reels montados a partir de lo que el cliente graba.

Escribe tu resultado en una frase con esta forma: **«Cada [frecuencia], [quién] recibe [qué], sin [lo que hoy le
cuesta]»**. Si no cabe en una frase, aún es demasiado grande.

## Paso 2. Empaquétalo

Un servicio que se explica en una página se vende; uno que necesita una llamada para entenderse, cuesta. Define:

1. **Nombre:** lo que consigue el cliente, no cómo lo haces. «Reseñas contestadas», no «Gestión de reputación con IA».
2. **Qué incluye:** la lista exacta de lo que se entrega, con su cantidad y su frecuencia.
3. **Qué no incluye:** igual de importante. Lo que queda fuera evita discusiones después.
4. **Lo que pone el cliente:** accesos, materiales, una persona que responda. Si el cliente tiene que hacer mucho, ya
   no es un servicio hecho.
5. **Plazos:** cuándo empieza, cuándo se entrega cada vez y cuánto tarda en estar en marcha.
6. **Cómo se revisa:** cuándo ve el cliente el trabajo y cuántas correcciones entran.

No hace falta decirle al cliente que lo hacen agentes de IA si no lo pregunta, pero tampoco lo escondas si lo
pregunta: lo que vende es el resultado y que tú respondes por él.

## Paso 3. Reparte el trabajo: agentes y revisión humana

Haz una tabla con cada paso del servicio, de principio a fin, y decide quién lo hace:

| Paso | Lo hace | Revisa |
| --- | --- | --- |
| Recoger lo que manda el cliente | Agente | |
| Investigar o preparar la información | Agente | |
| Preparar el borrador | Agente | |
| Comprobar datos, tono y que no se promete nada de más | Agente con una lista de comprobación | Tú, por muestreo al principio |
| **Aprobar antes de que salga** | **Tú** | |
| Entregar | Agente (o tú) | |
| Hablar con el cliente cuando algo va mal | **Tú** | |

> [!IMPORTANT]
> **Nada sale sin que lo vea una persona**, al menos hasta que lleves semanas sin corregir nada en ese paso. La
> revisión humana no es un coste que hay que quitar: es lo que hace que el cliente se fíe del servicio.

Otras reglas que sostienen el servicio:
- **Cada corrección se convierte en una regla** escrita para el agente, para que no la repita.
- **El trato con el cliente es tuyo:** la IA te prepara la información, tú hablas.
- Lo que no se puede deshacer (publicar, enviar, pagar) siempre con tu OK.

Para escribir las reglas de cada agente puedes usar la skill `reglas-de-un-agente`, y para repartir un equipo
entero, `equipo-de-contenido`, de este mismo repositorio.

## Paso 4. Lo mínimo para empezar

No construyas una aplicación. Para los primeros clientes basta con:
- una carpeta por cliente con su contexto (qué vende, cómo habla, qué no se dice), que los agentes leen antes de
  trabajar (la plantilla `segundo-cerebro` de este repositorio sirve);
- tus agentes en Claude Code o en Proyectos de Claude, con sus reglas escritas;
- una forma sencilla de entregar (una carpeta compartida, un correo) y de cobrar cada mes.

Construye algo más solo cuando un paso manual te frene de verdad con varios clientes a la vez.

## Paso 5. Ponle precio

No hay una cifra correcta para todos, y desconfía de quien te dé una sin conocer tu mercado. Hay un método:

1. **Lo que le cuesta hoy al cliente.** Las horas que dedica él o su equipo multiplicadas por lo que vale su hora, o
   lo que paga ahora a una agencia o a un profesional por lo mismo. Pregúntaselo a tres clientes posibles; no lo
   supongas.
2. **Lo que te cuesta a ti.** Tus horas de revisión y de trato con el cliente, más las herramientas (el plan de
   Claude, las conexiones que uses) repartidas entre tus clientes.
3. **El precio va entre los dos:** por debajo de lo que le cuesta hoy al cliente (si no, no le compensa) y bastante
   por encima de lo que te cuesta a ti (si no, no te compensa a ti).
4. **Cobra por el resultado y por mes**, no por horas: si los agentes te hacen más rápido, el beneficio es tuyo, no
   un descuento para el cliente.
5. **Empieza con un piloto pagado** de un mes, con un objetivo claro, y revisa el precio con lo que has aprendido.

Si al hacer la cuenta el precio que necesitas es más alto de lo que le cuesta hoy al cliente, el problema no es el
precio: es el resultado que has elegido. Vuelve al paso 1.

## Paso 6. Los primeros clientes

- Empieza por tres personas que ya conozcas y que tengan el problema. Ofrece el piloto, entrega, mide.
- Apunta todo lo que corriges: es tu manual y lo que hará que el décimo cliente te cueste mucho menos que el primero.
- Pide permiso para contar el resultado: el primer caso real vale más que cualquier anuncio.

## Un ejemplo de principio a fin

Un caso inventado para ver los seis pasos juntos: una persona que lleva años de recepcionista en clínicas dentales
y conoce bien cómo se pierden pacientes.

1. **El resultado:** «Cada lunes, la clínica recibe la lista de pacientes que no han vuelto a su revisión, con un
   mensaje preparado para cada uno, sin que nadie de recepción tenga que buscarlos.» Se repite, se revisa antes de
   enviarse, se ve si funciona (cuántos piden cita) y ella lo conoce.
2. **El paquete:** «Pacientes recuperados». Incluye la lista semanal y los mensajes listos para enviar. No incluye
   llamar por teléfono ni gestionar la agenda. La clínica pone el acceso de solo lectura a su programa de citas y
   una persona que apruebe los mensajes.
3. **El reparto:** un agente saca la lista, otro escribe cada mensaje con el tono de la clínica y una lista de lo
   que no se dice (precios, diagnósticos). Ella revisa todos los mensajes las primeras semanas y luego por muestreo.
   La clínica aprueba y envía.
4. **Lo mínimo:** una carpeta por clínica con su tono y sus reglas, los dos agentes con sus reglas escritas y un
   documento compartido para entregar la lista.
5. **El precio:** pregunta a tres clínicas cuántas horas dedica recepción a esto (si es que lo hace) y cuánto deja
   un paciente que vuelve. Pone el precio por debajo de ese valor y por encima de lo que le cuestan sus horas de
   revisión. Primer mes, piloto pagado.
6. **Los primeros clientes:** tres clínicas en las que ha trabajado. Al mes, cuenta con permiso cuántos pacientes
   han vuelto a pedir cita.

## Errores que se repiten

- Vender «IA» en lugar de un resultado. Al cliente le da igual cómo lo haces.
- Prometer que no hay revisión humana para parecer más barato. Es lo que hace fiable el servicio.
- Elegir algo que cada cliente quiere distinto. Los agentes rinden con lo que se repite.
- Construir la plataforma antes de tener clientes.
- Bajar el precio porque «lo hace la IA». El cliente paga por no tener el problema, no por tus horas.

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
