# Quita la publicidad de tu tele Android con Claude Code

Las teles con Android TV o Google TV traen filas patrocinadas, aplicaciones que no pediste y servicios que mandan datos de lo
que haces. CleanYourTV es un proyecto de código abierto que desactiva todo eso por Wi-Fi y cambia la pantalla de inicio por
una limpia. Claude Code hace el trabajo y tú decides qué se queda.

Revisada el 3 de noviembre de 2026 con la documentación del proyecto (enlaces al final). Ese día tenía 50,6k estrellas en
GitHub y listas para 427 modelos de 111 marcas. No lo hemos probado en una tele nuestra: lo que sigue viene de su documentación.

> [!CAUTION]
> **Puede dejar la tele sin arrancar.** Hay casos, y el último recurso es restablecerla de fábrica, que lo borra todo. Cambiar
> su software también puede afectar a la garantía. Hazlo solo en una tele tuya y bajo tu responsabilidad. Si está en garantía
> o no te la puedes jugar, no lo hagas.

---

## Primero: ¿funciona en tu tele?

| Tu tele | Qué puedes hacer |
| --- | --- |
| **Android TV o Google TV** | Todo: la limpieza y la pantalla de inicio nueva |
| **Fire TV** | Solo la limpieza, sin pantalla de inicio nueva. En la Fire TV Box de 2015, tampoco |
| **Samsung, LG, Roku, Vizio o Hisense con VIDAA** | No funciona. El proyecto explica cómo apagar el rastreo con el mando en [cleanyour.tv/not-android](https://cleanyour.tv/not-android) |

Busca tu modelo en [cleanyour.tv/tvs](https://cleanyour.tv/tvs). Si no sale, se puede intentar: Claude busca en tu tele qué
se puede desactivar y te pregunta. Pero nadie lo ha probado antes con ese modelo, así que el riesgo es mayor.

Las webs oficiales son `cleanyour.tv` y su repositorio de GitHub. El proyecto avisa de que otros dominios con un nombre
parecido no son suyos y de que no publica ninguna aplicación en las tiendas.

## Lo que hace y lo que no

- **Guarda antes una copia** de la lista de aplicaciones y de los ajustes de la tele.
- **Desactiva, no desinstala.** Usa `pm disable-user`, el mismo interruptor que Ajustes, Aplicaciones, Desactivar.
- **Se deshace** con `tools/restore.sh`.
- **No toca** el firmware, no necesita permisos de root y no salta ningún bloqueo.
- **Tus aplicaciones siguen igual.** Netflix y compañía se actualizan por Google Play, que no se toca.
- **No quita los anuncios de dentro de YouTube** ni de otras aplicaciones.

## Lo que hace falta

- **Claude Code** en tu ordenador (capítulo 3.2).
- **La tele y el ordenador en la misma Wi-Fi**, y la tele encendida.
- **Programas para montar la pantalla de inicio:** Python 3, un JDK de la versión 17 a la 22 y Android SDK 34. Claude puede
  instalarlos: pídele que te lo enseñe antes.

El proyecto calcula unos 15 minutos. Si tienes que instalar esos programas, cuenta con más. Hazlo de una sentada: en algunas
teles, el USB deja de funcionar mientras la depuración está encendida.

## 1. Activa la depuración en la tele

1. Ve a **Ajustes, Preferencias del dispositivo, Información**. El camino cambia un poco según la marca.
2. Pulsa OK sobre **Compilación** 7 veces, hasta que te avise de que ya tienes las opciones para desarrolladores.
3. Vuelve atrás, entra en **Opciones para desarrolladores** y activa **Depuración USB**. Si ves una opción de depuración por
   red o ADB, actívala también.

## 2. Descarga el proyecto en tu ordenador

Abre Claude Code y pídele esto:

```text
Clona https://github.com/Gathin23/cleanyourtv en una carpeta nueva y ábrela. Todavía no ejecutes nada. Dime qué necesito
tener instalado para seguir PROMPT.md y si me falta algo, y pídeme permiso antes de instalar.
```

Clonarlo importa: así Claude usa los programas del proyecto, que son los que guardan la copia, protegen la pantalla de inicio
y permiten deshacerlo, en lugar de escribir los suyos.

## 3. Pega PROMPT.md con tu modelo

Abre `PROMPT.md`, copia desde «I want to debloat my Android TV» hasta el final, cambia `<MODEL NAME HERE>` por tu modelo,
pégalo y añade esto debajo:

```text
Háblame en español. Antes de desactivar nada, enséñame la lista de lo que vas a tocar, para qué sirve cada cosa y qué
riesgo tiene, y espera mi OK. Hazlo por tandas pequeñas. Dime dónde queda la copia y cómo se deshace. No te saltes ningún
aviso del proyecto.
```

La tele te preguntará si permites la depuración desde tu ordenador: acepta. Después, Claude te pregunta qué aplicaciones
usas, cuáles quieres en el inicio y si mantienes el asistente de voz, Chromecast y las actualizaciones.

> [!TIP]
> Antes de aprobar la lista, piensa en lo que usas de vez en cuando: el asistente de voz, enviar vídeos desde el móvil, las
> entradas HDMI. Es lo que más se echa de menos después.

## 4. Al acabar, apaga la depuración

No te lo saltes. El puerto 5555 de la tele va sin cifrar y, en algunas teles, cualquier aparato de tu red podría entrar.

```text
Hemos terminado. Guíame para apagar en la tele la depuración USB, la de red y la inalámbrica, y para quitar las
autorizaciones. Después reinicia la tele y comprueba con tools/adb-closed.py que el puerto está cerrado. Enséñame el resultado.
```

La pantalla de inicio nueva sigue funcionando con la depuración apagada.

---

## Si algo sale mal

| Qué pasa | Qué hacer |
| --- | --- |
| **Echas de menos una función** | En Ajustes, Aplicaciones, vuelve a activar lo que desactivó. O pídele a Claude que lo haga |
| **Quieres dejarla como estaba** | Vuelve a encender la depuración y pídele a Claude que ejecute `tools/restore.sh` con tu lista. La pantalla de inicio nueva se queda instalada: se quita en Ajustes, Aplicaciones |
| **Una actualización lo ha devuelto todo** | Pasa: se instala por encima, y a veces trae aplicaciones nuevas. Vuelve a encender la depuración y pide que lo revise con `tools/check.py` |
| **La tele no llega a arrancar** | El último recurso es restablecerla de fábrica desde su menú de recuperación. Borra tus cuentas y tus ajustes. Mira antes la [guía de problemas](https://github.com/Gathin23/cleanyourtv/blob/main/docs/TROUBLESHOOTING.md) del proyecto |

Guarda la lista que aplicaste y la carpeta del proyecto: sin ellas, deshacerlo cuesta más.

## En resumen

- Solo Android TV y Google TV. En Fire TV, solo la limpieza. En Samsung, LG, Roku, Vizio y Hisense con VIDAA, no funciona.
- Desactiva y no desinstala, con copia previa y `tools/restore.sh` para deshacerlo.
- Revisa la lista antes de dar el OK, y ve por tandas.
- Puede dejar la tele sin arrancar y afectar a la garantía.
- Al terminar, apaga la depuración y comprueba que el puerto está cerrado.

---

## Fuentes

- CleanYourTV: [repositorio y documentación](https://github.com/Gathin23/cleanyourtv) (compatibilidad, cómo funciona, riesgos,
  garantía y puerto 5555), [PROMPT.md](https://github.com/Gathin23/cleanyourtv/blob/main/PROMPT.md) y
  [guía de problemas](https://github.com/Gathin23/cleanyourtv/blob/main/docs/TROUBLESHOOTING.md). Licencia MIT.

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
