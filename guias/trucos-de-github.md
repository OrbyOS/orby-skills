# Cuatro trucos de GitHub cambiando la dirección web

Cada vez que veas un proyecto en GitHub, cambia unas letras de la dirección y lo tienes listo para entenderlo con IA:
entero en un texto para pegar en Claude, en un diagrama, convertido en un mensaje para construir algo parecido, o conectado
a Claude como fuente. No hay que instalar nada ni saber programar, y se usan sin pagar ni crear una cuenta.

Probados el 1 de noviembre de 2026 con proyectos públicos. Son servicios de terceros: pueden cambiar o dejar de funcionar.

---

## Los cuatro, de un vistazo

Parte de la dirección de cualquier proyecto público, por ejemplo `github.com/usuario/proyecto`, y cambia el principio:

| Cambia por | Y tienes | Para qué |
| --- | --- | --- |
| `gitingest.com/usuario/proyecto` | Todo el proyecto en un solo texto | Pegarlo en Claude y preguntarle lo que quieras |
| `gitdiagram.com/usuario/proyecto` | Un diagrama de cómo está hecho | Entender de un vistazo qué partes tiene |
| `gitreverse.com/usuario/proyecto` | Un mensaje para construir algo parecido | Dárselo a Claude Code como punto de partida |
| `gitmcp.io/usuario/proyecto` | Una dirección para conectarlo a Claude | Que Claude consulte el proyecto cuando lo necesite |

En los tres primeros, el truco es cambiar **hub** por otra palabra: git**hub** pasa a git**ingest**, git**diagram** y
git**reverse**. En el cuarto, cambia `github.com` por `gitmcp.io`.

## 1. Gitingest: el proyecto entero en un texto

Convierte todos los archivos del proyecto en un solo texto, con un resumen de lo que ocupa. Tarda unos segundos: si se
queda vacío, recarga la página.

Copia el resultado, pégalo en Claude y pregúntale:

```text
Te paso un proyecto de GitHub entero. Explícame, sin tecnicismos: qué hace, para quién es, qué necesita para funcionar y
cuánto cuesta usarlo. Dime también qué datos míos manejaría y si ves algo que me deba preocupar antes de instalarlo.

[pega aquí el texto de Gitingest]
```

Si el proyecto es muy grande, el texto no cabrá en una conversación. Gitingest te dice cuánto ocupa («Estimated tokens») y deja
excluir archivos antes de generar.

## 2. GitDiagram: el mapa del proyecto

Dibuja las partes del proyecto y cómo se conectan. Puedes pulsar en cada parte y descargar la imagen. Sirve para saber de qué
va algo antes de leerlo y para enseñárselo a otra persona.

El propio servicio avisa de que es un resumen hecho con IA: míralo como un mapa, no como la verdad. Para confirmar algo,
pregúntale a Claude con el texto de Gitingest delante.

## 3. GitReverse: el mensaje para hacer algo parecido

Lee el proyecto y escribe un mensaje en lenguaje normal, como si le pidieras a un agente que lo construyera. Lo probamos con un
proyecto nuestro en español y nos lo devolvió en español.

Úsalo como borrador. Pásalo a Claude Code cambiando lo que no sea tuyo:

```text
Quiero construir algo parecido a este proyecto, pero para mi caso: [qué quieres y para quién]. Este es el mensaje que describe
el original: [pega aquí el de GitReverse]. Quédate con lo que me sirve y quita lo que no. Antes de escribir nada, hazme las
preguntas que te falten y dame un plan corto.
```

> [!IMPORTANT]
> **Inspirarte no es copiar.** Si vas a usar código de otro o venderlo, mira antes el archivo `LICENSE` del proyecto. Si no tiene
> licencia, no des por hecho que puedes reutilizarlo.

## 4. GitMCP: conectar el proyecto a Claude

Con los anteriores, le pasas el proyecto una vez. Con este, Claude lo tiene como fuente y consulta su documentación y su código
cuando hace falta, sin que pegues nada. Sirve sobre todo cuando trabajas con una herramienta que cambia a menudo y Claude
responde con datos antiguos.

**En Claude (web y aplicación de escritorio):** ve a **Customize → Connectors**, pulsa **+ Add → Add custom connector**, ponle un
nombre y pega `https://gitmcp.io/usuario/proyecto`.

**En Claude Code:**

```bash
claude mcp add --transport http nombre-del-proyecto https://gitmcp.io/usuario/proyecto
```

Después, pregúntale:

```text
Busca en la documentación de [proyecto] cómo se hace [lo que quieres], y dime en qué archivo o apartado lo has visto.
```

No pide cuenta, y solo funciona con proyectos públicos. Más sobre cómo se añaden conectores, en el capítulo 3.1.

---

## Tres cuidados

> [!CAUTION]
> **Lo que hay en un proyecto lo ha escrito un desconocido.** Un archivo puede llevar instrucciones escondidas para que la IA haga
> algo que no has pedido. Revisa lo que Claude quiere hacer antes de aprobarlo, y no instales ni ejecutes nada de un proyecto
> solo porque un resumen diga que está bien.

- **Tu clave de GitHub, para ti.** Gitingest y GitDiagram permiten ver proyectos privados si les das una clave de GitHub.
  Para los trucos de esta guía no hace falta. Un proyecto privado de tu empresa no lo mandes a un servicio que no conoces.
- **Comprueba lo que te digan.** Los resúmenes y diagramas salen de una IA y se pueden equivocar. Si vas a tomar una decisión, mira
  la fuente: que Claude te diga en qué archivo lo ha visto.

## Si alguno deja de funcionar

Son servicios gratuitos de terceros. Si uno cae, Claude Code puede hacer lo mismo en tu ordenador, y además te queda una copia:

```text
Descarga este proyecto público en una carpeta nueva, sin ejecutar ni instalar nada de lo que trae: [dirección de GitHub]. Léelo
y explícame qué hace, qué partes tiene y cómo se conectan, con un diagrama si ayuda. Dime en qué archivo has visto cada cosa.
```

## En resumen

- Gitingest: el proyecto entero en un texto, para preguntarle a Claude.
- GitDiagram: el mapa del proyecto, para entenderlo de un vistazo.
- GitReverse: el mensaje para construir algo parecido, adaptado a lo tuyo.
- GitMCP: el proyecto conectado a Claude, para que lo consulte cuando le haga falta.
- Solo proyectos públicos, sin darles tu clave, y comprobando lo que te digan.

---

## Fuentes

- [Gitingest](https://github.com/coderamp-labs/gitingest), [GitDiagram](https://github.com/ahmedkhaleel2004/gitdiagram),
  [GitReverse](https://www.gitreverse.com) y [GitMCP](https://github.com/idosal/git-mcp): páginas oficiales de cada proyecto.
- Claude: [conectores personalizados](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp).

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
