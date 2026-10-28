# Las reglas

Cada regla tiene un número que se puede comprobar, su porqué y un antes y un después. Los números son puntos de
partida sensatos, no leyes: si rompes una, que sea a propósito y sepas decir por qué.

---

## 1. Tipografía

### 1.1 Una familia, dos como mucho
**Regla.** Una familia para todo. Si hay dos, una para titulares y otra para texto, y que se diferencien de verdad.
**Por qué.** Cada familia es una voz. Tres voces en una página parecen tres empresas.
**Antes:** Titulares en una serif decorativa, subtítulos en una geométrica, botones en una tercera.
**Después:** Una sans bien hecha (o la del sistema) para todo; la jerarquía la hacen el tamaño y el peso.

### 1.2 Dos pesos, tres como mucho
**Regla.** Normal (400) y uno fuerte (600 o 700). Un tercero solo si hay una razón.
**Por qué.** Si todo tiene un peso distinto, nada destaca. El contraste de peso funciona cuando es escaso.
**Antes:** 300 en el texto, 400 en los subtítulos, 500 en el menú, 600 en los botones, 800 en el titular.
**Después:** 400 en el texto y el menú, 600 en titulares y botones.

### 1.3 Una escala, no tamaños sueltos
**Regla.** De 5 a 6 tamaños en toda la página, sacados de una proporción fija (entre 1,2 y 1,333). Por ejemplo, con
1,25 y base 17: 14 · 17 · 21 · 27 · 33 · 42 px.
**Por qué.** Los tamaños de una escala se relacionan entre sí y el ojo lo nota como orden. Diez tamaños parecidos
(15, 16, 17, 18, 20, 22…) se leen como un error.
**Antes:** 13, 14, 15, 16, 18, 20, 22, 24, 28, 36, 48, 72 px.
**Después:** 14, 17, 21, 27, 33, 42 px.

### 1.4 Texto que se lee sin esfuerzo
**Regla.** Cuerpo de texto entre 16 y 20 px. Interlineado de 1,5 a 1,65 en el texto y de 1,1 a 1,25 en los
titulares. Líneas de 60 a 75 caracteres (`max-width: 65ch` o parecido).
**Por qué.** Un texto pequeño o con líneas de lado a lado cansa, y quien se cansa se va sin leer la oferta.
**Antes:** Texto de 14 px a todo el ancho de una pantalla de 1.440 px.
**Después:** Texto de 18 px en una columna de 65 caracteres.

### 1.5 El titular, grande por jerarquía, no por efecto
**Regla.** El titular principal mide entre 2 y 3 veces el cuerpo. Más de 96 px casi siempre es un efecto.
**Por qué.** Un titular enorme grita, pero no dice más. La jerarquía viene de la diferencia, no del tamaño absoluto.

---

## 2. Color

### 2.1 Neutros más un acento
**Regla.** Una gama de grises (de 3 a 5) más **un** color de acento. Como mucho 7 colores en toda la página, contando
blancos y negros. El acento ocupa menos del 10 % de la superficie: botones, enlaces y poco más.
**Por qué.** El acento solo funciona si es raro. Si hay cinco colores fuertes, ninguno señala dónde pulsar.
**Antes:** Azul, morado, rosa, verde para los «éxitos» y naranja para los avisos, todos a la vez.
**Después:** Blanco roto, tres grises, casi negro para el texto y un verde para los botones.

### 2.2 Sin degradados por defecto
**Regla.** Colores planos. Un degradado solo si representa algo (luz, profundidad de una foto) y nunca en botones ni
en textos.
**Por qué.** El degradado azul a morado es la firma de lo hecho con prisa por una IA. Lo plano y bien elegido parece
decidido.

### 2.3 Contraste que se lee
**Regla.** Texto normal con contraste de 4,5:1 o más con su fondo; texto grande (24 px o 19 px en negrita) de 3:1
o más. Nada de gris claro sobre blanco para «parecer elegante».
**Por qué.** Si no se lee al sol con el móvil, no se lee. Y es la norma de accesibilidad (WCAG AA).
**Antes:** `#9ca3af` sobre `#ffffff` (2,5:1).
**Después:** `#4b5563` sobre `#ffffff` (7,6:1).

### 2.4 Fondos tranquilos
**Regla.** Fondo blanco, blanco roto o gris muy claro (o muy oscuro si toda la marca es oscura). Nada de negro puro
con texto blanco puro en bloques largos: usa casi negro (`#111` a `#1a1a1a`) y blanco roto.

---

## 3. Espacio

### 3.1 Una escala de espacios
**Regla.** Todos los márgenes, rellenos y huecos salen de una escala de 4 px: 4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 ·
96 · 128.
**Por qué.** Con una escala, los espacios se repiten y la página respira con ritmo. Con valores sueltos (13, 18,
27 px) todo parece un poco descolocado aunque nadie sepa decir por qué.

### 3.2 Lo que va junto, junto
**Regla.** El espacio dentro de un grupo es como mucho la mitad del espacio entre grupos. Entre secciones, de 64 a
128 px en escritorio.
**Por qué.** El ojo agrupa por cercanía. Si el titular está igual de lejos de su texto que de la sección anterior,
no se sabe a qué pertenece.
**Antes:** 24 px entre título y párrafo, 24 px entre secciones.
**Después:** 12 px entre título y párrafo, 96 px entre secciones.

### 3.3 Más aire del que crees
**Regla.** Si dudas, más espacio. Una sección con una sola idea y mucho aire comunica más que tres ideas apretadas.

---

## 4. Jerarquía y composición

### 4.1 Una cosa principal por pantalla
**Regla.** En cada pantalla (lo que se ve sin desplazarse), una idea y una acción principal. Un solo botón primario
por vista; el resto, secundarios (borde o texto).
**Por qué.** Dos botones iguales obligan a pensar. Quien piensa, duda; quien duda, se va.

### 4.2 Un eje de alineación
**Regla.** El texto largo, alineado a la izquierda. Centrado solo para titulares cortos y piezas sueltas. Todos los
bloques comparten los mismos bordes de una rejilla (12 columnas, o una sola columna de ancho fijo).
**Por qué.** Todo centrado es lo fácil y lo que menos se lee. Los bordes compartidos dan orden sin añadir nada.

### 4.3 Menos componentes repetidos
**Regla.** Si una sección es «tres tarjetas iguales con icono, título y texto», pregúntate si eso se puede decir con
una lista o con una frase. Como mucho una sección de tarjetas por página.
**Por qué.** Es la composición por defecto de las plantillas y de la IA. No dice nada de tu negocio.

---

## 5. Detalles

### 5.1 Radios
**Regla.** Uno o dos radios en todo el diseño (por ejemplo, 8 px para botones y campos, 12 px para tarjetas). O
ninguno. Nunca todo con el máximo redondeo.

### 5.2 Sombras
**Regla.** Ninguna, o una sola sombra sutil para lo que flota (un menú desplegable, una ventana). Nada de resplandor
(«glow») ni sombras de colores.

### 5.3 Botones
**Regla.** Color plano de acento, texto en el peso fuerte, al menos 44 px de alto para el dedo. Texto con un verbo
concreto: «Reservar una llamada», no «Empezar» ni «Descubrir más». Sin brillos, sin degradados, sin iconos de
cohete.

### 5.4 Iconos e imágenes
**Regla.** Fotos reales (del producto, del equipo, del cliente con permiso) antes que ilustraciones genéricas. Iconos
de un mismo set y del mismo grosor, o ninguno. Nunca emojis como iconos.

### 5.5 Contenido de verdad
**Regla.** Textos reales desde el principio. Nada de «Revoluciona tu flujo de trabajo», cifras inventadas («+10.000
clientes felices»), logos de clientes que no lo son ni testimonios inventados. Si falta un dato, se marca como
pendiente.
**Por qué.** El diseño sirve al contenido. Un diseño perfecto con textos vacíos sigue oliendo a plantilla.

---

## 6. Correos

Además de lo anterior:
- **Una columna** de 560 a 640 px de ancho. Nada de varias columnas: en el móvil se rompen.
- **Fuentes del sistema** (las de cada dispositivo). Las fuentes web no cargan en muchos programas de correo.
- **Texto real, no imágenes con texto.** Muchos correos se abren con las imágenes bloqueadas.
- **Un solo botón** y que sea un enlace con estilo (funciona en todos los programas), con el mismo texto concreto.
- **Estilos en línea** (`style=""` en cada elemento): muchos programas ignoran la etiqueta `<style>`.
- Que se lea bien en modo oscuro: nada de texto gris claro sobre blanco ni logos negros sin fondo.
- Pie con quién lo envía y cómo darse de baja.
