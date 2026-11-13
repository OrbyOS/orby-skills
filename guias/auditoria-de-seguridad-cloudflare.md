# La auditoría de seguridad de Cloudflare: revisa tu app antes de publicarla

Cloudflare ha publicado gratis la skill con la que arranca su buscador interno de fallos de seguridad. Convierte a tu agente de programación en un auditor: mapea tu proyecto, busca fallos con varios agentes, intenta tumbar cada hallazgo y te deja un informe.

Revisada el 13 de noviembre de 2026.

---

## Para quién es

Si has hecho una app o una web con IA (Claude Code, Cursor…), pásasela antes de publicarla o de meter datos de clientes.

## Cómo instalarla

```
npx skills add https://github.com/cloudflare/security-audit-skill --skill security-audit
```

Para tenerla en todos tus proyectos, añade `--global`. Necesitas Node.js y un agente que use herramientas y subagentes (Claude Code, por ejemplo).

## Cómo usarla

Abre tu agente dentro del proyecto y escribe una de estas:

- «Audita la seguridad de este proyecto.»
- «Busca vulnerabilidades en ./src.»

## Qué hace, por fases

1. **Reconocimiento:** dibuja la arquitectura y por dónde entra cada dato.
2. **Búsqueda:** varios agentes aislados buscan cada tipo de fallo.
3. **Validación:** otro agente intenta desmentir cada hallazgo.
4. **Resultados:** separa lo confirmado, lo que hay que revisar y lo descartado.
5. **Verificación:** agentes nuevos comprueban lo que dice el informe.
6. **Informe:** te deja `REPORT.md` con todo explicado.

## Lo que conviene saber

- Para ejecutar tu código de verdad necesita un entorno aislado (sin internet y con límites). Sin él, deja los hallazgos como «por revisar» en lugar de probarlos.
- Varias pasadas encuentran más: según sus autores, una sola encuentra más o menos la mitad.
- No sustituye a una auditoría profesional si manejas pagos o datos sensibles.
- Gratis y de código abierto (MIT): github.com/cloudflare/security-audit-skill.
