# Codex Security: los fallos de seguridad de tu código, encontrados y arreglados

Codex Security es la herramienta de OpenAI para buscar fallos de seguridad en tu código, comprobar que son reales y proponerte el arreglo. Es de código abierto (licencia Apache 2.0) y tiene casi 14.000 estrellas en GitHub.

Revisada el 17 de noviembre de 2026.

---

## Qué hace

- **Revisa tu proyecto entero**, una carpeta o solo los últimos cambios.
- **Comprueba cada hallazgo** antes de avisarte, para no llenarte de falsas alarmas.
- **Propone el parche** y verifica que el arreglo funciona.
- Puede escribir tu política de seguridad y llevar los fallos a GitHub, Jira o Linear.

## Cómo usarlo

Necesitas Node.js (22.13 o posterior) y Python 3.10 o posterior. En la terminal:

`npm install --global @openai/codex-security`

`cs login`

Y dentro de tu proyecto:

`cs scan .`

## Lo que conviene saber

- Necesitas iniciar sesión con tu cuenta de OpenAI o poner una clave, y el uso cuenta en tu plan.
- Revisa cada parche antes de aplicarlo: una herramienta de seguridad no sustituye a una revisión cuando hay datos de clientes de por medio.
