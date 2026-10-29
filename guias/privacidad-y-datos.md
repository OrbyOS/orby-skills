# Privacidad y datos de clientes

Para que la IA trabaje bien hay que darle contexto, y parte de ese contexto son datos de tus clientes. Esta guía
explica qué hace Claude con lo que le das según el plan, cómo configurar tu cuenta y qué no deberías pegar nunca.

Revisada el 29 de octubre de 2026 con la ayuda oficial de Claude y la página de condiciones de Anthropic (enlaces al
final). Los ajustes cambian: comprueba siempre los de tu cuenta.

---

## 1. Qué pasa con tus conversaciones, según el plan

| Plan | ¿Se usan tus conversaciones para entrenar? | Dónde se decide |
| --- | --- | --- |
| Free, Pro y Max (personales) | Solo si lo permites en tus ajustes de privacidad | Tú, en tu cuenta |
| Team y Enterprise (empresas) | No, por defecto | Las condiciones comerciales |
| La API (para desarrolladores) | No, por defecto | Las condiciones comerciales |

En los planes personales, según Anthropic:
- Si permites que se usen para mejorar Claude, se guardan hasta **cinco años**.
- Si no lo permites, se guardan **30 días**.
- Las conversaciones que borras no se usan para entrenar.

## 2. Configura tu cuenta en cinco minutos

1. **Entrenamiento:** en Claude, ve a los ajustes de privacidad (`claude.ai/settings/data-privacy-controls`) y
   decide si permites que tus conversaciones se usen para mejorar Claude. Se puede cambiar cuando quieras.
2. **Memoria:** en los planes personales viene activada. En **Settings → Your Claude** puedes pausarla, borrarla o
   desactivar que busque en tus conversaciones anteriores. Los temas sensibles, como la salud, no se guardan en la
   memoria salvo que lo actives, y los números de documentos de identidad y de cuentas bancarias no se guardan nunca.
3. **Chats de incógnito:** para algo puntual y delicado, usa un chat de incógnito. No se guarda en tu historial ni en
   la memoria y no se usa para entrenar. Se borra a los 30 días. No funciona dentro de un proyecto.
4. **Borrar:** si pegaste algo que no debías, borra esa conversación. Ojo: borrarla no borra lo que la memoria haya
   apuntado de ella; revísalo en los ajustes de memoria.

> [!IMPORTANT]
> Si en tu negocio trabajan varias personas con datos de clientes, mira los planes de empresa (Team o Enterprise):
> tus conversaciones no se usan para entrenar por defecto y la cuenta la administra tu negocio, no cada persona.

## 3. Qué no pegar nunca

- **Contraseñas, claves de acceso y códigos.** Nunca, en ningún plan.
- **Números de tarjeta y cuentas bancarias** de nadie.
- **Documentos de identidad** de clientes.
- **Datos de salud** de pacientes con nombre, si no tienes un acuerdo que lo cubra.
- **Lo que firmaste no compartir:** contratos o documentos con cláusula de confidencialidad.

## 4. Cómo usar datos de clientes sin exponerlos

La mayoría de las tareas no necesitan saber quién es el cliente, sino qué le pasa.
- **Quita nombres y datos que identifiquen:** «Cliente A, clínica dental de tres sillones en una ciudad mediana»
  sirve igual que el nombre y la dirección.
- **Resume en lugar de pegar:** en vez del historial completo de correos, lo que se pidió y lo que quedó pendiente.
- **Pega solo lo necesario:** para contestar una queja no hace falta la ficha entera del cliente.
- **Pregúntate:** ¿se lo enviaría por correo a un proveedor externo? Si no, no lo pegues tal cual.

> **Antes:** «Contesta a este correo de Laura Gómez, DNI…, que se queja de su tratamiento de ortodoncia…».
>
> **Después:** «Contesta a esta queja de una paciente de ortodoncia: está molesta porque el tratamiento se ha
> retrasado un mes. Tono cercano, sin admitir culpas médicas; propón una cita para revisarlo».

## 5. Tus obligaciones con tus clientes

Si tratas datos personales de clientes, tu negocio sigue siendo responsable de ellos aunque los procese una
herramienta de IA. En España y en la Unión Europea eso significa cumplir el RGPD: usar los datos solo para lo que
tus clientes saben y con herramientas que ofrezcan garantías. Si manejas datos sensibles (salud, por ejemplo),
consúltalo con quien lleve la protección de datos de tu negocio. Esta guía no es asesoramiento legal.

## 6. En resumen

- Decide en tus ajustes si tus conversaciones sirven para entrenar.
- Usa el incógnito para lo puntual y delicado.
- Nunca contraseñas, cuentas, documentos de identidad ni lo confidencial.
- Con clientes: quita lo que les identifica y pega solo lo necesario.

---

## Fuentes

- Anthropic: [actualización de las condiciones y la política de privacidad](https://www.anthropic.com/news/updates-to-our-consumer-terms)
  (28/08/2025).
- Ayuda de Claude: [chats de incógnito](https://support.claude.com/en/articles/12260368-use-incognito-chats),
  [memoria y búsqueda en conversaciones](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context)
  y [datos sensibles en las conversaciones](https://support.claude.com/en/articles/8325621-i-would-like-to-input-sensitive-data-into-my-chats-with-claude-who-can-view-my-conversations).

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
