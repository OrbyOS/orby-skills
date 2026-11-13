# Cinco plugins para Claude Code que conviene tener antes de nada

Cinco añadidos para Claude Code: uno le deja ver y probar lo que hace en el navegador, otro evita que se pare cuando llegas a tu límite, otro le hace gastar menos, otro le da memoria entre sesiones y el último hace que lo que diseña no parezca una plantilla.

Revisada el 13 de noviembre de 2026. Todos son gratis; algunos usan cuentas o modelos que pueden tener su propio coste.

---

## 1. Playwright: que Claude vea y pruebe lo que hace

Sin él, Claude escribe tu web o tu formulario y da por hecho que funciona. Con él, abre un navegador, entra, hace clic, rellena campos y comprueba el resultado.

Cómo instalarlo, en la terminal:

```
claude mcp add playwright npx @playwright/mcp@latest
```

También está en el marketplace oficial: dentro de Claude Code escribe `/plugin` y búscalo.

Prueba: «Abre mi web en el navegador, rellena el formulario de contacto y dime si llega bien».

## 2. OmniRoute: que la tarea no se pare cuando llegas a tu límite

Es una pasarela gratuita y de código abierto (licencia MIT) que se pone entre Claude Code y los modelos. Si un modelo se queda sin cuota o falla, pasa al siguiente de tu lista.

```
npm install -g omniroute
omniroute
```

Se abre un panel en `http://localhost:20128`. Ahí conectas tus cuentas (tu suscripción, tus claves y, si quieres, modelos gratuitos) y montas el orden de respaldo. Para lanzar Claude Code a través de OmniRoute:

```
omniroute run claude
```

Ojo: OmniRoute no regala modelos. Usa las cuentas que tú conectes, cada una con sus límites y sus condiciones.

## 3. Headroom: menos tokens por la misma respuesta

Recorta lo que Claude no necesita leer (resultados repetidos, registros, datos en bloque) antes de mandárselo al modelo. Código abierto, licencia Apache 2.0.

```
uv tool install --python 3.13 "headroom-ai[all]"
headroom wrap claude
```

Para ver cuánto te ahorra con tu uso real: `headroom savings`. Para quitarlo: `headroom unwrap claude`.

Cuánto ahorra depende de lo que hagas: en sus pruebas, entre un 21 % y un 57 % en tareas de agente, y muy poco en texto normal.

## 4. MemPalace: una memoria de tu proyecto que no se borra

Cada sesión nueva de Claude empieza de cero. MemPalace guarda tus conversaciones y lo que vas decidiendo, ordenado por proyectos y temas, en tu ordenador. Nada sale de tu equipo salvo que tú lo actives. Licencia MIT.

La forma más sencilla es dejar que Claude te guíe:

```
npx skills add MemPalace/mempalace
```

Después pídele a Claude que termine la instalación con la skill de configuración. Si prefieres hacerlo a mano: `pipx install mempalace`.

## 5. Frontend Design: diseños que no parecen una plantilla

Es el plugin oficial de Anthropic para que lo que Claude diseña (webs, páginas, pantallas) tenga criterio de diseñador y no el aspecto genérico de siempre.

Dentro de Claude Code:

```
/plugin install frontend-design@claude-plugins-official
```

Prueba: «Rediseña la portada de mi web con el plugin de diseño. Primero enséñame dos direcciones distintas».

## Lo que conviene saber

- Instálalos de uno en uno y prueba cada uno antes de añadir el siguiente.
- Instala solo desde el repositorio oficial de cada proyecto: hay copias con el mismo nombre.
- Ninguno de estos proyectos nos paga ni tiene relación con nosotros.
