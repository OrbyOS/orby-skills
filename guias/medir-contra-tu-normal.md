# Medir cada reel contra tu normal

Un reel con 10.000 visualizaciones puede ser un fracaso, y uno con 2.000, el mejor que has hecho. Depende de lo que
suele hacer tu cuenta. Esta guía explica cómo medir cada reel contra tu normal, cómo saber cuáles han funcionado de
verdad y cómo sacar con Claude qué repetir. Sin herramientas de analítica de pago.

Revisada el 30 de octubre de 2026 con la documentación oficial de Meta para desarrolladores (enlaces al final).

---

## 1. Por qué las visualizaciones sueltas engañan

Las visualizaciones de un reel dependen de muchas cosas que no son el reel: cuántos seguidores tienes, cómo va tu
cuenta esa semana o si otro vídeo tuyo acaba de arrastrar gente. Si una cuenta suele hacer 20.000 por reel, 10.000 es
la mitad de lo normal: ha ido mal. Si otra suele hacer 800, 2.000 es más del doble: ha ido muy bien.

Las cifras sueltas te dicen si has tenido suerte. Compararlas con tu normal te dice si has mejorado.

## 2. Tu normal y la x de cada reel

**Tu normal** es la mediana de visualizaciones de tus últimos reels: pon las cifras de tus últimos 30 en orden y
quédate con la del medio. Mejor la mediana que la media: un reel que se dispara sube mucho la media y no cambia la
mediana.

Cada reel nuevo se mide así:

```text
x = visualizaciones del reel ÷ tu normal
```

| x | Qué quiere decir |
| --- | --- |
| **2 o más** | Ha funcionado: el doble de lo normal o más. Hay que saber por qué |
| **Entre 0,6 y 2** | Lo normal. No saques conclusiones de uno solo |
| **Menos de 0,6** | No ha funcionado. También hay que saber por qué |

Ejemplo inventado: tus últimos 30 reels tienen una mediana de 1.500 visualizaciones. Uno nuevo hace 4.200: x = 2,8,
ha funcionado. Otro hace 700: x = 0,47, no ha funcionado.

> [!TIP]
> Compara siempre reels con el mismo tiempo publicados: las cifras de un reel de ayer no se comparan con las de uno
> de hace un mes. Mira cada reel, por ejemplo, a los 7 días de publicarlo.

## 3. El análisis de cada reel que se sale

Cada reel que pasa de x 2, y cada uno que baja de 0,6, se abre entero con Claude. Para cada uno, apunta:
- **El gancho:** la primera frase y lo que se ve en pantalla en ese momento.
- **Los 3 primeros segundos:** si la gente se queda o se va. Instagram da el porcentaje de quien lo salta.
- **La duración.**
- **La hora y el día** de publicación.
- **El tema y el formato:** a cámara, voz en off, pantalla.
- **La llamada a la acción del final.**

Lo que enseña es la comparación: qué tienen en común los que funcionaron y qué les falta a los que no. Así sabes qué
repetir, no solo qué ha ido bien.

> [!NOTE]
> Con un solo reel no hay conclusión. Busca lo que se repite en varios: si tres de tus cuatro mejores reels abren con
> una situación vivida y ninguno de los flojos lo hace, ahí tienes algo.

## 4. Dos medidas más, si quieres afinar

- **Envíos:** compartidos más guardados, dividido entre visualizaciones. Mide si el reel es tan útil que alguien lo
  manda o lo guarda para luego. A menudo dice más que los me gusta.
- **Seguidores por cada mil visualizaciones:** cuántas personas te siguen por cada mil que ven el reel. Mide si el reel
  hace que quieran ver más de ti.

Se miden igual que las visualizaciones: contra tu normal.

## 5. De dónde salen los datos

**Sin programar:** en la aplicación de Instagram, en cada reel, pulsa **Ver estadísticas**. Copia en una hoja de
cálculo, por cada reel, la fecha y la hora, las visualizaciones, los compartidos, los guardados, los seguidores que te
ha traído y el porcentaje de salto. Pásale la hoja a Claude.

**Automático, con la conexión oficial de Instagram:** si tienes una cuenta profesional, Instagram deja leer las
estadísticas de tus propios reels con su conexión oficial, sin pagar nada. Hace falta una app en Meta for Developers
(gratis) con el permiso de estadísticas. Da las visualizaciones, los compartidos, los guardados, el alcance, el tiempo
medio de visualización y el porcentaje de salto de cada reel. Dos cosas que saber:
- Los datos pueden tardar hasta 48 horas en estar al día.
- Los seguidores que trae cada reel no salen por la conexión para los reels: cópialos de la aplicación si los
  quieres.

> [!CAUTION]
> El token de la app da acceso a tu cuenta. No lo pegues en el chat ni en el código: guárdalo en un archivo `.env` y
> dile a Claude que lo lea de ahí.

## 6. Pedírselo a Claude

Con la hoja de cálculo, en cualquier conversación con Claude:

```text
Te paso las estadísticas de mis últimos reels: [adjunta la hoja]. Calcula mi normal (la mediana de visualizaciones
de los últimos 30) y la x de cada reel (visualizaciones ÷ mi normal). Dime cuáles pasan de 2 y cuáles bajan de 0,6.
Después compara los que funcionaron con los que no: gancho, primeros 3 segundos, duración, hora, tema y formato.
Dime qué se repite en los buenos y falta en los flojos, y qué haría en los próximos tres reels. Si con los datos que
hay no se puede concluir algo, dilo en vez de adivinar.
```

Con la conexión oficial, en Claude Code:

```text
Móntame un script que lea con la API oficial de Instagram (inicio de sesión de Instagram) las estadísticas de mis
reels: visualizaciones, compartidos, guardados, alcance y porcentaje de salto. El token está en el archivo .env.
Guárdalas en una hoja de cálculo, calcula mi normal (la mediana de visualizaciones de mis últimos 30 reels) y la x de
cada reel, y márcame los que pasan de 2 y los que bajan de 0,6. Explícame cada paso antes de hacerlo.
```

## 7. En resumen

- Las visualizaciones sueltas engañan: mide cada reel contra tu normal, la mediana de tus últimos reels.
- x = visualizaciones ÷ tu normal. Desde 2, ha funcionado; por debajo de 0,6, no.
- Abre con Claude los que se salen, por arriba y por abajo, y busca lo que se repite.
- Afina con los envíos y los seguidores por cada mil visualizaciones.

---

## Fuentes

- Meta for Developers: [estadísticas de una publicación de Instagram](https://developers.facebook.com/docs/instagram-platform/reference/instagram-media/insights)
  y [API de Instagram con inicio de sesión de Instagram](https://developers.facebook.com/docs/instagram-platform/instagram-api-with-instagram-login).

---

Hecha por [Orby](https://orbyos.es). Más guías y skills gratuitas en este mismo repositorio.
