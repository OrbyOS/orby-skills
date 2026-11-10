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

## Paso 4. Ver el vídeo de verdad: transcripción y capturas

Con la transcripción sola te pierdes la mitad: en un vídeo corto, lo que sale en pantalla (el texto, lo que se
enseña, cuándo cambia el plano) cuenta tanto como lo que se dice. Para los tres a cinco mejores, consigue las dos
cosas. No las inventes ni las supongas por el título.

**La transcripción.** De más fácil a más trabajosa:
- Que el usuario la copie de la propia red, si la muestra (muchas enseñan los subtítulos automáticos o la
  transcripción del vídeo).
- Si tiene el archivo del vídeo, transcríbelo tú. Si está instalada la skill `editar-reels-con-claude`, usa su
  script `transcribir.py`.
- Si no, que te cuente qué dice, con sus palabras.

**Las capturas.** Una cada dos segundos basta para ver qué sale en pantalla. Dos maneras:
- **Con el archivo del vídeo:** sácalas tú con ffmpeg (si no está instalado, pide permiso antes de instalarlo):

  ```bash
  mkdir -p capturas
  ffmpeg -i video.mp4 -vf "fps=1/2,scale=720:-2" capturas/%03d.jpg
  ```

  En un vídeo de 30 segundos salen unas 15 imágenes. Míralas todas, en orden, junto a la transcripción.
- **Sin el archivo:** que el usuario vea el vídeo en el móvil, lo pause cada pocos segundos, haga una captura de
  pantalla y te las pase en orden.

Usa solo vídeos que el usuario pueda ver; no entres en cuentas de nadie. Las capturas y el vídeo son para estudiarlo:
al terminar, bórralos si ya no hacen falta.

Con las dos cosas delante, apunta por cada tramo: qué se dice, qué sale en pantalla y cuándo cambia.

## Paso 5. Desmontar los elegidos

Desmonta cada uno en:

| Parte | Qué apuntar |
| --- | --- |
| Tema | De qué habla, en una frase |
| Ángulo | Desde dónde lo cuenta: un error, una opinión contraria, un caso, un antes y un después, una lista |
| Gancho | La primera frase, lo que se ve a la vez en pantalla y qué tipo es: pregunta, promesa, algo que choca, un error común, una escena |
| Pregunta abierta | Qué quiere saber quien sigue viendo después del gancho, y en qué segundo se responde |
| Estructura | Cada paso del vídeo, en una línea: qué se dice y qué se ve |
| Formato | A cámara, voz en off, pantalla, texto en pantalla; duración |
| Cierre | Qué pide al final |

## Paso 6. Una plantilla con su tema

Por cada vídeo desmontado, saca **una plantilla**: la estructura del vídeo con huecos (el gancho, la pregunta que
abre, cada paso y el cierre), sin una sola frase del original. Luego rellénala con **su tema y un ejemplo suyo**:
mismo ángulo, mismo tipo de gancho y misma estructura. Pídele el ejemplo si no lo tienes; no lo inventes.
Escribe el gancho de su idea en una frase que pueda decir tal cual.

No copies frases del original, ni su guion, ni su imagen. Se aprende el porqué; el vídeo es otro.

Entrega `ideas-<fecha>.md` con: la tabla de destacados con su veredicto, los desmontajes, las plantillas y las
ideas ya rellenadas, ordenadas por cuál grabar primero (primero los patrones que se repiten en varias cuentas).

## Revisión antes de entregar

- ¿Cada vídeo elegido le habla a su cliente y ha funcionado por el contenido?
- ¿Los desmontajes salen de la transcripción y de las capturas, no de suposiciones?
- ¿Cada idea tiene un ejemplo real de su negocio o lo marca como pendiente?
- ¿Hay alguna frase copiada del original? Fuera.
