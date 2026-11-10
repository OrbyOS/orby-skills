# Ordenar tu Google Drive con Claude

Facturas sueltas, contratos con nombres como «documento (3)», tres copias de la misma propuesta… Ordenar un Drive a
mano lleva una tarde entera. Con Claude en Chrome, Claude lo revisa contigo: propone una estructura de carpetas,
marca los duplicados, te enseña el plan y solo mueve o renombra cuando le das el visto bueno.

Revisada el 30 de octubre de 2026 con la ayuda oficial y el blog de Claude (enlaces al final).

---

## 1. Qué te hace falta

- **Google Chrome** en el ordenador. Claude en Chrome no funciona en otros navegadores ni en el móvil.
- **Un plan de pago de Claude** (Pro, Max, Team o Enterprise). En el gratuito no está.
- **La extensión Claude en Chrome**, instalada desde la Chrome Web Store, con tu cuenta de Claude. Fíjala en la barra
  para tenerla a mano.

**El panel lateral es una sesión de Cowork** desde el 12 de agosto de 2026: la conversación se guarda en tu historial,
puedes usar tus skills y conectores, y lo que empiezas en Chrome lo puedes seguir en la aplicación de escritorio, la
web o el móvil. Max y Team ya lo tienen, y a Pro le va llegando poco a poco. Si prefieres el panel de antes, en el
panel pulsa los tres puntos de arriba a la derecha y elige **Switch back to classic** (volver al clásico).

Claude en Chrome ve la página que tienes abierta y puede leer, hacer clic, escribir y moverse por ella, igual que
harías tú. Por eso sirve para Drive: abre carpetas, mira qué hay en cada archivo, mueve y renombra.

> [!NOTE]
> Si solo quieres buscar o leer documentos, el conector de Google Drive (capítulo 3.1) es más rápido y está en todos
> los planes. Para revisar carpetas enteras, moverlas y renombrar archivos uno a uno viendo lo que hace, mejor Claude
> en Chrome.

## 2. Antes de empezar: dos avisos

> [!IMPORTANT]
> **Prueba primero con una carpeta pequeña o con una copia.** Elige una carpeta de unos veinte archivos y comprueba
> que el resultado te convence antes de pasar a todo el Drive.

> [!CAUTION]
> **Cuidado con las carpetas compartidas.** Si mueves o renombras algo dentro de una carpeta compartida, cambia
> también para las personas con las que la compartes, y a lo mejor dejan de encontrarlo. Déjalas fuera la primera
> vez o díselo a Claude en el mensaje.

Además:
- **Revisa cada acción antes de aprobarla.** Claude en Chrome empieza en un modo en que aprueba solo las acciones que
  considera seguras y para a preguntarte las demás. Si prefieres aprobar una a una, cambia al modo de aprobación
  manual.
- **Nada de borrar.** Los mensajes de esta guía piden que no borre nada: lo que sobre lo decides tú.

## 3. Abre Drive y Claude

1. Abre **drive.google.com** en Chrome y entra en la carpeta que quieres ordenar.
2. Abre el panel de **Claude en Chrome** con el icono de la extensión.

## 4. Que revise la carpeta y proponga la estructura

Pega este mensaje en el panel de Claude:

```text
Revisa esta carpeta de Google Drive y todo lo que tiene dentro, sin mover, renombrar ni borrar nada todavía.
Quiero ordenarla en estas carpetas: Clientes (una subcarpeta por cliente), Proveedores, Facturas, Contratos y
Marketing. Mira el contenido de cada archivo, no solo el nombre, y dime a qué carpeta iría cada uno. Marca aparte los
archivos que parezcan duplicados (y de qué otro archivo) y los que no sepas identificar. Deja fuera las carpetas
compartidas. No borres nada.
```

## 5. Que te enseñe el plan antes de mover nada

Antes de tocar un solo archivo, pídele el plan completo:

```text
Antes de mover nada, enséñame el plan completo en una tabla: nombre actual del archivo, qué es, carpeta de origen,
carpeta de destino y por qué. Pon al final, aparte, los duplicados y los que no has identificado, que se quedan
donde están. No hagas ningún cambio hasta que te diga que sí.
```

Lee la tabla con calma. Corrige lo que no te cuadre («el archivo X es de Proveedores, no de Clientes») y pídele que
la actualice.

## 6. Aplicar el plan

Cuando el plan te convenza:

```text
Aplica el plan tal como lo hemos dejado: crea las carpetas que falten y mueve cada archivo a la suya. Los duplicados
y los que no has identificado, déjalos donde están. No borres nada. Al terminar, dime qué has movido y si algo ha
fallado.
```

Revisa el resultado en Drive. Si algo no está donde debía, díselo y lo arregla.

## 7. Renombrar por contenido

Con todo en su sitio, que cada archivo diga qué es. El formato **fecha_tipo_cliente** (por ejemplo,
`2026-10-15_factura_cliente-ejemplo`) ordena solo por fecha y se encuentra con el buscador:

```text
Renombra los archivos de esta carpeta según su contenido, con el formato AAAA-MM-DD_tipo_cliente: la fecha del
documento (no la de subida), el tipo (factura, contrato, propuesta, presupuesto…) y el cliente o proveedor, en
minúsculas y con guiones en lugar de espacios. Antes de cambiar nada, enséñame una tabla con el nombre viejo y el
nuevo, y espera a que te diga que sí. Si no sabes la fecha o el cliente de un archivo, déjalo como está y márcalo.
```

## 8. En resumen

- Claude en Chrome ordena tu Drive viendo lo que hay en cada archivo, como lo harías tú.
- Primero el plan, luego mover, luego renombrar. Cada paso, con tu visto bueno.
- Una carpeta pequeña o una copia la primera vez, las compartidas fuera y nada de borrar.

---

## Fuentes

- Ayuda de Claude: [empezar con Claude en Chrome](https://support.claude.com/en/articles/12012173-getting-started-with-claude-in-chrome)
  y [usar Claude en Chrome con seguridad](https://support.claude.com/en/articles/12902428-use-claude-in-chrome-safely).
- Blog de Claude: [el panel lateral de Claude en Chrome, ahora con Cowork](https://claude.com/blog/cowork-chrome-side-panel)
  (12/08/2026).

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
