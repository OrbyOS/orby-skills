# Limpia tu móvil Android con Claude Code

Los móviles Android traen de fábrica aplicaciones del fabricante y de la operadora que no se pueden desinstalar desde los ajustes. Con un cable y ADB, la herramienta oficial de Android para desarrolladores, sí se pueden quitar, sin root y sin instalar nada en el móvil. Claude Code hace el trabajo pesado: lista lo que hay, te explica qué es cada cosa y quita solo lo que apruebes.

Revisada el 9 de noviembre de 2026.

---

## Antes de empezar

- Haz una copia de seguridad de tus fotos y datos.
- Necesitas un ordenador con Claude Code y el cable USB del móvil.
- Lo que se quita así se puede recuperar (te explicamos cómo abajo), y un restablecimiento de fábrica lo devuelve todo.

## 1. Activa la depuración USB

1. En el móvil: Ajustes → Información del teléfono → toca 7 veces «Número de compilación». Se activan las opciones para desarrolladores.
2. Ajustes → Sistema → Opciones para desarrolladores → activa **Depuración USB**.
3. Conecta el móvil al ordenador. Cuando salga «¿Permitir la depuración USB?», pulsa **Permitir**.

## 2. El mensaje para Claude Code

```text
Quiero limpiar mi móvil Android de aplicaciones de fábrica que no uso, con ADB y sin root.
1. Si no tengo ADB (Android platform-tools), instálalo y comprueba con «adb devices» que ve el móvil.
2. Lista todos los paquetes instalados y clasifícalos: sistema imprescindible, fabricante, operadora, rastreo o publicidad, y apps que he instalado yo.
3. Para cada paquete que se pueda quitar, dime en una línea qué hace y si es seguro quitarlo. Marca como «no tocar» todo lo que sea del sistema, de llamadas, mensajes, cámara, actualizaciones o Google Play.
4. No quites nada hasta que yo te diga cuáles. Cuando te los diga, usa «pm uninstall -k --user 0» y guarda en un archivo la lista de lo que has quitado.
```

Claude te enseñará la lista. Revísala, quita solo lo que reconozcas y ve poco a poco: mejor cinco aplicaciones hoy que cincuenta a ciegas.

## 3. Si algo deja de funcionar

Pídele a Claude que lo recupere desde el archivo que guardó, o usa este comando con el nombre del paquete:

```text
adb shell cmd package install-existing nombre.del.paquete
```

Funciona en Android 6 o posterior. Si no sabes cuál ha sido, recupéralos todos desde la lista y vuelve a probar.

## La alternativa sin escribir nada

Universal Android Debloater Next Generation es un programa gratuito y de código abierto (en GitHub, con casi 10.000 estrellas) que hace lo mismo con botones. Tiene listas de paquetes por fabricante y marca cada uno según el riesgo de quitarlo. Puedes usar sus listas para comprobar lo que te proponga Claude.

## Lo que conviene saber

- No quites nada que no sepas qué es. Si una app del sistema falta, el móvil puede fallar en algo concreto (notificaciones, cámara, actualizaciones).
- Las actualizaciones grandes del sistema pueden reinstalar algunas apps. Guarda la lista y repite el proceso.
- Usarlo es responsabilidad tuya: es una herramienta oficial, pero el móvil es tuyo.
