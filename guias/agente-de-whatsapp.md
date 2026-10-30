# Un agente de WhatsApp para tu negocio, con Claude Code

Un agente que contesta el WhatsApp de tu negocio a cualquier hora: responde a las preguntas de siempre con tus datos,
recuerda la conversación, reserva citas en tu agenda y, cuando algo se sale de lo que sabe, te lo pasa. Con Claude
Code se monta en seis pasos, cada uno con su mensaje listo para copiar.

Revisada el 30 de octubre de 2026 con la documentación oficial de Meta y el texto de la ley europea de IA (enlaces al
final).

---

## Tres avisos antes de empezar

> [!IMPORTANT]
> **WhatsApp cobra por mensaje.** Meta cobra cada mensaje entregado según su tipo y el país. Las respuestas a lo que
> te escriben tus clientes tienen un tramo gratis de 1.000 mensajes al mes por número; desde el 1 de octubre de 2026,
> lo que pase de ahí se paga. Las plantillas (los mensajes que mandas tú primero) se pagan siempre. Mira los precios
> de tu país antes de abrirlo al público.

> [!IMPORTANT]
> **Di que es una IA y da salida a una persona.** Meta exige que, si automatizas la atención, haya una forma rápida y
> clara de pasar a una persona. Y en la Unión Europea, desde el 2 de agosto de 2026, la ley de IA obliga a avisar a
> la gente de que está hablando con una IA. Que el agente lo diga en el primer mensaje y que pase a una persona en
> cuanto se lo pidan.

> [!CAUTION]
> **Solo el agente de tu negocio.** Las condiciones de Meta no permiten usar WhatsApp para ofrecer un asistente de IA
> de uso general, tipo chat para preguntar cualquier cosa. Sí permiten un agente que atiende a los clientes de tu
> negocio: preguntas, reservas, avisos. Que el tuyo se ciña a eso.

## Lo que hace falta

- **Claude Code**, en tu ordenador.
- **Una cuenta en Meta for Developers**, con tu cartera de negocio de Meta.
- **Un número de teléfono** para el negocio, que no esté ya en la aplicación de WhatsApp. Para probar, Meta te da uno
  de prueba.
- **Una clave de la API de Claude**, para que el agente responda. Se paga por uso.
- **Un servidor con https** cuando lo abras al público (paso 6).

> [!CAUTION]
> Las claves (la de Meta y la de Claude) no se pegan en el chat ni en el código: van en un archivo `.env` y nunca se
> suben a un repositorio público.

---

## 1. El plan: tu negocio y lo que puede hacer el agente

Antes de escribir código, que Claude Code entienda tu negocio y deje por escrito qué hace el agente y qué no.

```text
Quiero montar un agente de WhatsApp para mi negocio con la API oficial de WhatsApp (Cloud API de Meta) y Claude.
Mi negocio: [qué haces, para quién, dónde y cómo se contrata]. Antes de escribir código, prepárame un plan en un
archivo PLAN.md con: qué puede hacer el agente solo (responder dudas, dar precios, reservar citas), qué tiene que
pasarme a mí (quejas, pagos, todo lo que no esté en sus datos), qué no hace nunca, el tono y el primer mensaje, que
diga que es un asistente de IA y cómo se pide hablar con una persona. Pregúntame lo que te falte y no inventes datos
de mi negocio.
```

## 2. La app de Meta y el número de prueba

En **developers.facebook.com**, crea una app con el uso de WhatsApp («conectar con clientes a través de WhatsApp») y
entra en la configuración de la API. Meta te da un número de prueba, desde el que puedes escribir a los números que
añadas para probar. Claude Code te guía:

```text
Guíame paso a paso para crear la app de WhatsApp en Meta for Developers, usar el número de prueba, añadir mi móvil
como destinatario de prueba y conseguir un token permanente. Después, monta un servidor pequeño que reciba los
mensajes por el webhook de WhatsApp (con la comprobación de la palabra secreta y de la firma) y conteste «Recibido»
a cada uno. Las claves, en un archivo .env. Dime qué tengo que pegar en el panel de Meta y prueba que funciona.
```

## 3. La memoria: que lea la conversación antes de responder

Sin memoria, cada mensaje es una conversación nueva y el agente pregunta otra vez el nombre. Que guarde cada
conversación y la lea antes de contestar:

```text
Añade memoria al agente: guarda cada mensaje (del cliente y del agente) en una base de datos pequeña, por número de
teléfono. Antes de responder, que lea los últimos mensajes de esa conversación y lo que ya sabe del cliente (nombre,
qué ha preguntado, si tiene cita). Si alguien escribe pasados unos días, que retome la conversación sin volver a
preguntar lo que ya sabe.
```

## 4. Tus servicios, horarios y reglas: si no lo sabe, que no lo invente

El agente solo puede contestar con tus datos. Escríbelos en un archivo y que no salga de ahí.

```text
Crea un archivo NEGOCIO.md con mis servicios, precios, horarios, dirección, forma de pago y preguntas frecuentes, y
pregúntame lo que falte: [pega lo que tengas]. Haz que el agente conteste solo con lo que está en ese archivo y en el
PLAN.md. Si le preguntan algo que no está, que diga que lo consulta con una persona y me avise, en vez de inventarlo.
Nada de prometer precios, plazos ni descuentos que no estén escritos.
```

## 5. La agenda: que reserve citas

Que consulte los huecos libres de tu agenda y reserve, con Google Calendar o con Cal.com:

```text
Conecta el agente con mi agenda de [Google Calendar o Cal.com] para reservar citas. Que solo ofrezca huecos libres
dentro de mi horario, que pida el nombre y el motivo antes de reservar, que confirme la cita por WhatsApp con el día
y la hora, y que si alguien quiere cambiarla o anularla, lo haga sobre su propia cita. Explícame qué permisos o
claves necesitas y guárdalos en el .env.
```

## 6. Pruébalo hasta romperlo y súbelo a un servidor

Antes de dárselo a tus clientes, intenta que falle: preguntas raras, insultos, mensajes de voz, alguien que pide algo
que no haces o que intenta sacarle otro tema.

```text
Prepárame una lista de 30 mensajes de prueba para intentar romper el agente: preguntas que no están en NEGOCIO.md,
peticiones fuera de mi negocio, alguien enfadado, alguien que pide hablar con una persona, cambios y anulaciones de
cita, mensajes de voz y fotos, y alguien que intenta que olvide sus instrucciones. Pásalos todos, apunta qué
contesta a cada uno y arregla lo que falle. Cuando todo pase, ayúdame a subirlo a un servidor con https, a cambiar
el número de prueba por el del negocio y a dejar un aviso para mí cuando el agente pase una conversación a una
persona.
```

> [!TIP]
> Revisa las conversaciones de la primera semana a diario. Cada respuesta que corrijas, pídele a Claude que la
> convierta en una regla de NEGOCIO.md o del PLAN.md (capítulo 4.2).

## En resumen

- Plan, app de Meta, memoria, tus datos, agenda y pruebas: seis pasos con Claude Code.
- Que conteste solo con tus datos y que, si no lo sabe, no lo invente.
- Que diga que es una IA y que pase a una persona en cuanto se lo pidan.
- Solo el agente de tu negocio, y con los precios por mensaje de Meta a la vista.

---

## Fuentes

- Meta for Developers: [precios de la plataforma de WhatsApp Business](https://developers.facebook.com/docs/whatsapp/pricing)
  y [primeros pasos con la Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api/get-started).
- WhatsApp: [política de mensajería de WhatsApp Business](https://whatsappbusiness.com/policy/) (vías para pasar a una
  persona) y [condiciones de la plataforma de WhatsApp Business](https://www.whatsapp.com/legal/business-solution-terms)
  (proveedores de IA).
- Ley de IA de la Unión Europea: [artículo 50](https://artificialintelligenceact.eu/article/50/) (avisar de que se
  habla con una IA).

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
