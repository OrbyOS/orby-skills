---
name: estudiar-videos-que-funcionan
description: Decide qué vídeos de otras cuentas merece la pena estudiar (los que funcionan mucho mejor de lo normal para su propia cuenta y le hablan al mismo cliente), los desmonta en tema, gancho y estructura, y los traduce a ideas para el negocio del usuario sin copiarlos. Úsala cuando alguien pida ideas de contenido, quiera saber qué funciona en su nicho, analizar la competencia o un vídeo viral, o no sepa de qué hablar esta semana.
---

# Estudiar los vídeos que funcionan

Empezar cada semana de cero, con un «hazme un post», da lo mismo que a todo el mundo. Es mejor empezar por lo que
ya ha demostrado que interesa a tu cliente. Pero no vale cualquier vídeo con muchas vistas: hay que elegir bien
cuál estudiar y copiar lo que lo hace funcionar, no el vídeo.

## Paso 1. Las cuentas

Pregunta:
1. ¿Qué vendes y a quién? (Si hay un CONTEXTO.md de la skill `lente-de-negocio`, léelo.)
2. De cinco a diez cuentas que le hablen a **tu mismo cliente**, aunque vendan otra cosa. Mejor cuentas hasta unas
   diez veces más grandes que la tuya que gigantes: lo que les funciona a ellas está a tu alcance.
3. De qué red.

Si no tiene cuentas, ayúdale a encontrarlas con búsquedas en la red que use (los temas que busca su cliente, los
hashtags de su sector) y que él confirme cuáles le hablan a su cliente.

## Paso 2. Los datos

De cada cuenta hacen falta sus últimos 12 a 30 vídeos con: enlace, vistas, fecha y, si se puede, la frase con la
que empieza. Opciones, de más fácil a más trabajosa:
- Que los apunte a mano en una hoja de cálculo mirando el perfil (las vistas salen en la cuadrícula de reels).
- Que use una herramienta de extracción que ya tenga.
No entres tú en cuentas de nadie ni uses su sesión. Guarda los datos en `videos.csv` con las columnas
`cuenta, enlace, vistas, fecha` y, si la tiene, `tema`.

Luego:

```bash
python3 SKILL/scripts/destacados.py videos.csv
```

(`SKILL` es la carpeta de esta skill.) Lista los vídeos que han tenido al menos tres veces las vistas normales de
su cuenta en los últimos 90 días. Si salen pocos, `--minimo 2`; si salen demasiados, `--minimo 5`.

## Paso 3. Las preguntas para decidir cuál estudiar

Pasa cada vídeo destacado por estas preguntas. Si falla en una de las tres primeras, se descarta:

1. **¿Le habla a mi cliente?** Si lo ve mi cliente, ¿se para? Un vídeo de otra audiencia no enseña nada sobre la mía.
2. **¿Ha funcionado por el contenido?** Descarta lo que destaca por algo que no se puede repetir: un invitado
   famoso, un sorteo, una colaboración con una cuenta enorme, una noticia que ya pasó o una polémica.
3. **¿Está a mi alcance?** ¿Lo podría grabar con lo que tengo, con mi cara, mi tiempo y mi material?
4. **¿Qué pregunta abre el gancho?** Si no sabes decir qué quiere saber quien sigue viendo, aún no lo has entendido.
5. **¿Se repite?** Si la misma idea o el mismo formato destaca en dos o más cuentas, es un patrón, no una casualidad:
   va primero.
6. **¿Es reciente?** Lo de las últimas semanas pesa más que lo de hace tres meses.

Enséñale al usuario la lista con lo que pasa y lo que no, en una línea por vídeo.

## Paso 4. Desmontar los elegidos

Para los tres a cinco mejores, pide al usuario que te pegue la transcripción o que te cuente qué pasa en el vídeo
(no lo inventes ni lo supongas por el título). Desmonta cada uno en:

| Parte | Qué apuntar |
| --- | --- |
| Tema | De qué habla, en una frase |
| Ángulo | Desde dónde lo cuenta: un error, una opinión contraria, un caso, un antes y un después, una lista |
| Gancho | La primera frase y qué tipo es: pregunta, promesa, algo que choca, un error común, una escena |
| Estructura | Los pasos del vídeo, en tres a cinco líneas |
| Formato | A cámara, voz en off, pantalla, texto en pantalla; duración |
| Cierre | Qué pide al final |

## Paso 5. Traducirlo a su negocio

Por cada vídeo desmontado, propón **una idea para su negocio** que use el mismo ángulo, el mismo tipo de gancho y
la misma estructura, pero con su tema y **un ejemplo suyo**. Pídele el ejemplo si no lo tienes; no lo inventes.
Escribe el gancho de su idea en una frase que pueda decir tal cual.

No copies frases del original, ni su guion, ni su imagen. Se aprende el porqué; el vídeo es otro.

Entrega `ideas-<fecha>.md` con: la tabla de destacados con su veredicto, los desmontajes y las ideas para su
negocio, ordenadas por cuál grabar primero (primero los patrones que se repiten en varias cuentas).

## Revisión antes de entregar

- ¿Cada vídeo elegido le habla a su cliente y ha funcionado por el contenido?
- ¿Los desmontajes salen de lo que el usuario ha visto o pegado, no de suposiciones?
- ¿Cada idea tiene un ejemplo real de su negocio o lo marca como pendiente?
- ¿Hay alguna frase copiada del original? Fuera.
