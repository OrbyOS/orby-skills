# Sherlock: mira en qué redes existe un nombre de usuario

Sherlock es una herramienta gratuita y de código abierto que busca un nombre de usuario en más de 400 redes sociales y webs, y te dice en cuáles existe esa cuenta. Lo más útil es empezar por el tuyo: ver qué cuentas tuyas siguen abiertas por ahí.

Revisada el 13 de noviembre de 2026.

---

## Qué necesitas

- Un ordenador con Python (Mac, Windows o Linux).
- La terminal. Si nunca la has usado, pídele a Claude Code que lo haga por ti con el mensaje de abajo.

## Cómo instalarlo

```
pipx install sherlock-project
```

También vale `pip install sherlock-project` o, con Docker, `docker run -it --rm sherlock/sherlock`.

## Cómo usarlo

```
sherlock tu_usuario
```

Puedes buscar varios a la vez:

```
sherlock usuario1 usuario2
```

Al terminar te guarda la lista en un archivo con el nombre del usuario (`tu_usuario.txt`). Si la quieres en hoja de cálculo, añade `--csv` o `--xlsx`.

## Si prefieres que lo haga Claude Code

Abre Claude Code en una carpeta vacía y escribe:

> Instala Sherlock (sherlock-project) con pipx y búscame el usuario «tu_usuario». Enséñame la lista de webs donde aparece y guárdala en un archivo.

## Lo que conviene saber

- Que aparezca una cuenta no significa que sea de esa persona: otra gente puede usar el mismo nombre de usuario. Compruébalo antes de sacar conclusiones.
- Úsalo para lo tuyo o para lo que es público y legítimo (por ejemplo, ver si tu marca está libre en una red). No lo uses para vigilar a nadie.
- Algunos paquetes de terceros (Ubuntu 24.04, ParrotOS) dan problemas: usa pipx, pip o Docker.
- Código: github.com/sherlock-project/sherlock (licencia MIT).
