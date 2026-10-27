---
name: instalar-orbyos
description: Instala OrbyOS (el equipo de agentes de IA de contenido de código abierto de Orby) en el ordenador del usuario, lo arranca y le guía en los primeros pasos: cuenta, conectar Claude y onboarding. Úsala cuando alguien pida instalar, probar o arrancar OrbyOS u Orby en su ordenador.
---

# Instalar OrbyOS

OrbyOS es un programa web que corre en el ordenador del usuario (`http://localhost:8000`). Esta skill lo instala
paso a paso, explicando cada cosa en una línea, sin dar nada por sabido. La guía completa para leer está en
`guias/instalar-orbyos.md` del repositorio de Orby Skills.

Reglas:
- Explica qué vas a ejecutar antes de hacerlo y pide OK antes de instalar nada en el sistema (Homebrew, Python,
  ffmpeg) o de descargar el repositorio.
- Las claves del usuario no pasan por ti: se pegan en la propia app, en Conectores. Si te pega una en el chat,
  dile que no hace falta y que la pegue en la app.

## Paso 1. Comprobar el equipo

Mira el sistema y lo que hay instalado:

```bash
uname -s; python3 --version; for p in python3.13 python3.12 python3.11; do command -v $p; done; command -v ffmpeg git brew
```

- Windows sin WSL: OrbyOS no corre directamente. Explícale que necesita WSL (Ubuntu dentro de Windows) y para.
- Falta Python 3.11 o más reciente, o ffmpeg:
  - Mac con Homebrew: `brew install python@3.12 ffmpeg`.
  - Mac sin Homebrew: dile que lo instale desde [brew.sh](https://brew.sh) (es una línea que pega en la Terminal y le
    pedirá su contraseña del Mac: eso lo hace él) y vuelve a comprobar.
  - Linux: `sudo apt install python3.12 python3.12-venv ffmpeg git` (la contraseña la escribe él).
- Falta git: en Mac, `xcode-select --install` o `brew install git`; o descargar el ZIP desde GitHub.

## Paso 2. Descargar

Pregunta dónde lo quiere (por defecto, `~/Documents`) y:

```bash
cd ~/Documents && git clone https://github.com/OrbyOS/OrbyOs.git && cd OrbyOs
```

Si ya existe la carpeta, no la borres: pregunta si quiere actualizarla (`git pull`) o instalar en otra.

## Paso 3. Instalar y arrancar

`instalar.sh` instala las dependencias, crea el acceso directo y deja el servidor en marcha (no termina mientras la
app esté abierta). Lánzalo en segundo plano y guarda su salida:

```bash
cd RUTA/OrbyOs && bash instalar.sh > instalar.log 2>&1
```

La primera vez tarda varios minutos (descarga librerías de vídeo y transcripción). Comprueba cuándo responde:

```bash
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8000/
```

Un 200 o un 303 es que ya está. Si el registro muestra un error, léelo y resuélvelo con la tabla de abajo. Si el
puerto 8000 está ocupado, arranca en otro: `PORT=8001 ./arrancar.sh`.

## Paso 4. Primeros pasos

Dile que abra `http://localhost:8000` (en el Mac se abre solo) y acompáñale:
1. **Crear la cuenta**: nombre, correo y contraseña. La primera es la de administración. Te lleva al Onboarding.
2. **Conectar Claude** en Conectores → «Cómo usa Claude la app»:
   - Con su plan Pro o Max: `claude setup-token` en la Terminal, inicia sesión y pega el token en la app.
   - Con una clave de la API (pago por uso): se crea en console.anthropic.com y se pega en la app.
3. **Onboarding**: las ocho preguntas, luego de una a tres llamadas o audios contando su negocio y el kit visual.
4. Lo demás (Apify para investigar, Zernio para publicar, ManyChat para los mensajes, Telegram para el resumen) se
   conecta en Conectores cuando lo necesite.

Explícale cómo abrirlo otro día: en el Mac, doble clic en «Abrir Orby.command» dentro de la carpeta; en Linux,
`./arrancar.sh`. Funciona mientras esa ventana esté abierta.

## Si algo no va

| Error | Qué hacer |
| --- | --- |
| «Falta Python 3.11 o más reciente» | Paso 1 y repetir `bash instalar.sh` |
| «Falta ffmpeg» | Paso 1 y repetir |
| Falla `pip install` con un paquete de vídeo | Comprueba que usa Python 3.11, 3.12 o 3.13; con versiones más nuevas, algunas librerías aún no tienen paquete |
| «Address already in use» | `PORT=8001 ./arrancar.sh` y abrir `http://localhost:8001` |
| Los agentes no hacen nada | Conectores: la clave o el token de Claude, comprobados |

## Al terminar

Resume en tres líneas: dónde está instalado, cómo se abre otro día y qué tiene que conectar para empezar a
trabajar. Si quiere que funcione con el ordenador apagado, explícale que se instala en un servidor
(`INSTALAR.md` del repositorio) o que puede pedir la implementación en orbyos.es.
