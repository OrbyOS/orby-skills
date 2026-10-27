#!/bin/bash
# Instala las skills de Orby en Claude Code (~/.claude/skills).
#
#   Todas:        curl -fsSL https://raw.githubusercontent.com/OrbyOS/orby-skills/main/instalar.sh | bash
#   Solo una:     curl -fsSL https://raw.githubusercontent.com/OrbyOS/orby-skills/main/instalar.sh | bash -s editar-reels-con-claude
#   Desde la carpeta descargada:   bash instalar.sh [nombre de la skill]
#
# Solo copia carpetas a ~/.claude/skills. No instala programas ni toca nada más. Si ya tenías una skill con el mismo
# nombre, la actualiza (lo que hayas instalado dentro de ella, como su .venv, se conserva).
set -e

ORIGEN_URL="${ORBY_SKILLS_URL:-https://github.com/OrbyOS/orby-skills/archive/refs/heads/main.tar.gz}"
DESTINO="${HOME}/.claude/skills"
QUIERO="$1"

# 1. De dónde salen las skills: de esta carpeta si el script está dentro del repositorio; si no, se descargan.
AQUI=""
if [ -n "${BASH_SOURCE[0]:-}" ] && [ -f "${BASH_SOURCE[0]}" ]; then  # ejecutado como archivo, no por tubería
  AQUI="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
fi
if [ -n "$AQUI" ] && ls "$AQUI"/*/SKILL.md >/dev/null 2>&1; then
  ORIGEN="$AQUI"
else
  TMP="$(mktemp -d)"
  trap 'rm -rf "$TMP"' EXIT
  echo "Descargando las skills de Orby…"
  curl -fsSL "$ORIGEN_URL" | tar -xz -C "$TMP"
  ORIGEN="$(dirname "$(ls "$TMP"/*/*/SKILL.md | head -1)")/.."
fi

# 2. Copiarlas.
mkdir -p "$DESTINO"
instaladas=()
for skill in "$ORIGEN"/*/; do
  nombre="$(basename "$skill")"
  [ -f "$skill/SKILL.md" ] || continue
  [ -z "$QUIERO" ] || [ "$QUIERO" = "$nombre" ] || continue
  mkdir -p "$DESTINO/$nombre"
  (cd "$skill" && tar --exclude .venv --exclude __pycache__ -cf - .) | (cd "$DESTINO/$nombre" && tar -xf -)
  instaladas+=("$nombre")
done

if [ ${#instaladas[@]} -eq 0 ]; then
  echo "No he encontrado la skill «$QUIERO». Estas son las que hay:"
  for skill in "$ORIGEN"/*/; do [ -f "$skill/SKILL.md" ] && echo "  $(basename "$skill")"; done
  exit 1
fi

echo
echo "Instaladas en $DESTINO:"
for nombre in "${instaladas[@]}"; do echo "  $nombre"; done
echo
echo "Abre Claude Code (o ciérralo y vuelve a abrirlo) y pídele lo que quieras en tus palabras,"
echo "por ejemplo: «edítame este reel» o «prepárame una estructura para grabar»."
