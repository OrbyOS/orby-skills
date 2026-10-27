# Instala OrbyOS en tu ordenador

OrbyOS es el código abierto de [Orby](https://orbyos.es): un equipo de siete agentes de IA que lleva el contenido
de una marca personal. Investiga tu nicho, planifica la semana, prepara lo que hay que grabar, edita, publica y
atiende los mensajes. Tú apruebas; ellos trabajan.

Esta guía lo deja funcionando en tu ordenador en unos veinte minutos, sin saber programar. Si usas Claude Code, hay
un atajo: la skill [`instalar-orbyos`](../instalar-orbyos) hace estos pasos contigo.

---

## Lo que necesitas

| Qué | Para qué | Cuánto cuesta |
| --- | --- | --- |
| Un Mac o un ordenador con Linux (en Windows, dentro de WSL) | Donde corre OrbyOS | |
| Python 3.11 o más reciente | El programa | Gratis |
| ffmpeg | Editar los vídeos | Gratis |
| Claude: tu plan Pro o Max, o una clave de la API | Que el equipo piense y escriba | Tu plan, o pago por uso |
| Apify (opcional al principio) | Leer los posts de tu cuenta y de tu competencia | Tiene saldo gratis para empezar |
| Zernio (opcional) | Publicar y ver métricas | Gratis para las dos primeras cuentas |
| ManyChat Pro (opcional) | Palabras clave y mensajes de Instagram | El plan Pro de ManyChat |
| Telegram (opcional) | El resumen de cada mañana en el móvil | Gratis |

Para probarlo basta con lo de las cuatro primeras filas. Lo demás se conecta cuando lo necesites.

---

## Paso 1. Python y ffmpeg

Abre la **Terminal** (en el Mac: `Cmd + espacio`, escribe «Terminal» y pulsa Intro).

**En un Mac**, con [Homebrew](https://brew.sh) (si no lo tienes, la página dice cómo instalarlo con una línea):

```bash
brew install python@3.12 ffmpeg
```

**En Linux** (Ubuntu o Debian):

```bash
sudo apt install python3.12 python3.12-venv ffmpeg git
```

## Paso 2. Descargar OrbyOS

Elige una carpeta (por ejemplo, Documentos) y descarga el código:

```bash
cd ~/Documents
git clone https://github.com/OrbyOS/OrbyOs.git
cd OrbyOs
```

Si no tienes `git`, entra en [github.com/OrbyOS/OrbyOs](https://github.com/OrbyOS/OrbyOs), pulsa el botón verde
**Code → Download ZIP**, descomprímelo y abre esa carpeta en la Terminal (escribe `cd ` y arrastra la carpeta a la
ventana).

## Paso 3. Instalar y abrir

```bash
bash instalar.sh
```

Comprueba que tienes Python y ffmpeg, instala lo que necesita (la primera vez tarda unos minutos: descarga las
librerías de vídeo y de transcripción) y abre OrbyOS en el navegador, en `http://localhost:8000`.

En el Mac te deja además un acceso directo, **«Abrir Radar.command»**: para abrirlo otro día, doble clic ahí.
OrbyOS trabaja mientras esa ventana esté abierta.

## Paso 4. Tu cuenta y tu negocio

1. **Crea tu cuenta** con tu nombre, tu correo y una contraseña. La primera que se crea es la de administración.
   Todo se queda en tu ordenador.
2. Te lleva directamente al **Onboarding** de tu negocio, que empieza con ocho preguntas. Puedes rellenarlas ya o
   después.
3. Ve a **Conectores** (en el menú de tu negocio). En «Cómo usa Claude la app», elige tu plan o una clave:
   - **Con tu plan Pro o Max:** instala [Claude Code](https://code.claude.com), ejecuta en la Terminal
     `claude setup-token`, inicia sesión y pega el token que te da.
   - **Con una clave de la API:** créala en [console.anthropic.com](https://console.anthropic.com) y pégala.
     Pagas por uso.
   Las demás claves (Apify, Zernio, ManyChat, Telegram) van en la misma página, cuando quieras conectarlas.

Las claves se guardan en tu ordenador. No las pegues nunca en un chat ni en un archivo que vayas a compartir.

## Paso 5. Primeros pasos dentro

En este orden, y aprobando cada cosa cuando el agente te la proponga:

1. **Onboarding**: tus datos y redes, de una a tres llamadas o audios en los que cuentas tu negocio (de ahí sale tu
   ficha, tu voz, tus temas y tus límites) y tu kit visual.
2. **Investigación**: Lupi mira qué destaca en tu nicho (necesita Apify).
3. **Plan y guiones**: Plani propone la semana y Escri prepara qué grabar.
4. **Graba** y sube las tomas: Monti las edita.
5. **Publicación** y **Comunidad**, cuando conectes Zernio y ManyChat.

Nada se publica ni se envía sin tu visto bueno, salvo que tú le des más autonomía a un agente.

---

## Si algo no va

| Ves | Haz |
| --- | --- |
| «Falta Python 3.11 o más reciente» | Repite el paso 1 y vuelve a ejecutar `bash instalar.sh` |
| «Falta ffmpeg» | `brew install ffmpeg` (Mac) o `sudo apt install ffmpeg` (Linux) |
| El navegador no se abre solo | Abre tú `http://localhost:8000` |
| «Address already in use» | Ya hay algo abierto en ese puerto: cierra la otra ventana de OrbyOS o arranca con `PORT=8001 ./arrancar.sh` |
| Los agentes no responden | Revisa en Conectores que la clave de Claude o el token están pegados y comprobados |
| Al cerrar la ventana deja de funcionar | Es lo normal en tu ordenador. Para que trabaje siempre, se instala en un servidor: lo explica `INSTALAR.md` del repositorio |

## Para que trabaje aunque apagues el ordenador

OrbyOS se puede publicar en un servidor pequeño con un solo comando (`./desplegar.sh`). Los pasos están en
`INSTALAR.md` y `README.md` del repositorio.

Si prefieres que te lo dejemos montado y adaptado a tu negocio, escríbenos desde [orbyos.es](https://orbyos.es).
