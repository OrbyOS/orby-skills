# Free Claude Code: usa Claude Code con modelos gratis

Free Claude Code es un programa abierto que se pone entre Claude Code y los modelos: tú sigues trabajando igual, y por detrás responde
el modelo que elijas de entre 61 proveedores, muchos con plan gratuito. Si uno falla, salta al siguiente.

Revisada el 3 de noviembre de 2026 con su documentación (enlace al final). Ese día tenía 66k estrellas en GitHub y licencia AGPL-3.0.

> [!IMPORTANT]
> **Es la herramienta de Claude Code, pero no es Claude quien responde.** Salvo que conectes tu propia clave de pago de Anthropic, contesta
> otro modelo. No esperes los mismos resultados. Y el proyecto no es de Anthropic ni tiene su respaldo.

---

## ¿De verdad son 1.300 millones de tokens gratis?

Es la cifra que da el proyecto («más de 1.300 millones al mes»), pero no explica cómo sale y no hay ningún saco de tokens que te den
ellos. Lo gratis lo ponen los proveedores, cada uno con sus límites, y el proyecto avisa de que pueden cambiar en cualquier momento. Tómala como un máximo teórico al
sumar planes gratuitos, no como lo que vas a poder usar.

## Instalarlo

Con Claude Code instalado (capítulo 3.2), pega un solo comando en la terminal.

Mac o Linux:

```bash
curl -fsSL "https://raw.githubusercontent.com/Alishahryar1/free-claude-code/main/scripts/install.sh" | sh
```

Windows (PowerShell):

```powershell
& ([scriptblock]::Create((irm "https://raw.githubusercontent.com/Alishahryar1/free-claude-code/main/scripts/install.ps1")))
```

Cuando te pregunte, elige Claude Code como agente. Hay más proyectos con nombres parecidos: usa solo esta dirección.

## Ponerlo en marcha

1. **Ábrelo.** En Windows y Mac, desde el icono de Free Claude Code. En Linux, con `fcc-server`. Se abre su panel de administración.
2. **Consigue una clave gratuita** en [NVIDIA NIM](https://build.nvidia.com/settings/api-keys), el proveedor con el que arranca su guía.
3. **Pégala en el panel:** en **Providers**, abre NVIDIA NIM, pulsa **Add key** y guarda. Deja el modelo que viene y pulsa **Apply**.
4. **Arranca Claude Code con él:**

```bash
fcc-claude
```

Tu Claude Code normal, con el comando `claude`, sigue igual que antes.

## Que salte de modelo si uno se cae

En **Model Config**, añade **Fallback Models** en el orden en que quieras probarlos, y pulsa **+** en cada uno. Una misma petición que falla
puede gastar de más de un proveedor antes de salir bien.

Un orden sensato: primero el modelo con el que mejor te funcione, y después otro de un proveedor distinto, porque si un proveedor se cae, suelen caerse todos sus modelos a la vez.

## Para qué sí

Pruébalo con tareas que puedas revisar y comparar:

```text
Lee este proyecto y explícame qué hace cada carpeta. Después dime qué modelo estás usando y qué tres tareas de aquí harías con más riesgo de equivocarte.
```

Tiene sentido para aprender, para tareas repetitivas y para seguir trabajando cuando se te acaba el límite de tu plan. Para lo importante, compara el resultado con el de Claude.

> [!CAUTION]
> **Lo que escribes sale hacia cada proveedor que configures.** Los planes gratuitos pueden tener otras condiciones sobre tus datos, y quizá usarlos
> para entrenar. No le pases datos de clientes, contraseñas ni código privado sin leerlas.

## En resumen

- Claude Code con 61 proveedores y salto automático si uno falla.
- No responde Claude, salvo que pongas tu clave de pago de Anthropic.
- 1.300 millones es la cifra del proyecto, sin desglose: lo que uses depende de los límites de cada proveedor.
- Un comando, una clave gratuita de NVIDIA y `fcc-claude`.
- No le pases datos sensibles sin leer las condiciones del proveedor.

---

## Fuentes

- Free Claude Code: [repositorio y documentación](https://github.com/Alishahryar1/free-claude-code) (proveedores, cifra de tokens, salto de modelo, instalación y licencia).

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
