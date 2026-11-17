# Qwen Code: un agente de programación con cualquier modelo

Qwen Code es un agente de programación de código abierto (licencia Apache 2.0) que funciona en la terminal, como Claude Code, pero puedes conectarlo con el modelo que quieras, también con uno que corra gratis en tu ordenador. Tiene más de 30.000 estrellas en GitHub.

Revisada el 18 de noviembre de 2026.

---

## Qué hace

- **Programa desde la terminal:** le pides cambios en tu proyecto y los hace.
- **Con el modelo que quieras:** OpenAI, Anthropic, Gemini, Qwen o cualquier otro proveedor, y cambias en cualquier momento.
- **En local:** con Ollama o vLLM usas un modelo en tu ordenador, sin pagar por uso.

## Cómo instalarlo

Con Node.js 22 o posterior:

`npm install -g @qwen-code/qwen-code@latest`

O en Mac con Homebrew: `brew install qwen-code`

Después, escribe `qwen` en la carpeta de tu proyecto y configura el proveedor con `/auth`.

## Lo que conviene saber

- Los modelos en local van más lentos y piden un ordenador con buena memoria.
- Con un proveedor de pago, el uso se cobra en tu cuenta de ese proveedor.
