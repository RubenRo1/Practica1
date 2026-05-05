#' ---
#' title: 'Práctica 3: Estadística descriptiva bivariante'
#' author: "Estadística"
#' date: "Grado en Inteligencia Artificial (UDC)"
#' output:
#'   html_document:
#'     toc: yes
#'     toc_float: yes
#'     pandoc_args: ["--number-offset", "2,0"]
#' ---
#' 
#' # Estadística descriptiva bivariante {#descriptiva2}
#' 
#' ## Variable estadística bidimensional
#' 
#' Como ya se comentó, cuando en el conjunto de datos contiene observaciones de
#' múltiples variables (normalmente características de los individuos de una muestra),
#' el análisis descriptivo suele comenzar con el análisis de estas variables de forma
#' individual, sin embargo, normalmente resulta de mayor interés analizar estas
#' variables de forma conjunta. Como las observaciones son características
#' correspondientes a un mismo individuo, es de esperar que haya relación entre ellas,
#' por lo que uno de los principales objetivos suele ser estudiar la posible relación
#' (asociación) entre variables.
#' 
#' En esta práctica nos centraremos en el análisis simultáneo de dos variables
#' estadísticas $X$ e $Y$, por tanto, supondremos que disponemos de una muestra
#' $\left\{(x_1,y_1),\ldots,(x_n,y_n)\right\}$.
#' 
#' El par $(X,Y)$ se denomina variable estadística bidimensional. En muchas ocasiones
#' una de las variables es de mayor interés, en esos casos la **variable de interés**
#' (o respuesta) se suele denotar por $Y$, y la otra variable $X$ se suele denominar
#' **variable explicativa** (o factor, si es cualitativa).  Además, en muchas de las
#' herramientas de R se suelen emplear fórmulas, del tipo `y ~ x`, para especificar
#' esta posible relación.
#' 
#' Las variables $X$ e $Y$ pueden ser cualitativas (nominales o ordinales) o
#' cuantitativas (discretas o continuas), dependiendo de la combinación de tipos de
#' ambas variables tienen sentido unos análisis u otros.  Al menos como punto de
#' partida, normalmente se emplean alguno de los siguientes métodos descriptivos:
#' 
#' - Si una de las variables es cuantitativa (continua o discreta con muchos valores 
#'   distintos) y la otra es categórica, se analizan las **distribuciones condicionadas** 
#'   de la variable numérica para los distintos valores de la variable cualitativa, 
#'   empleando:
#' 
#'     - Gráficos de cajas.
#' 
#'     - Medidas descriptivas.
#' 
#' - Si ambas variables son cualitativas (o cuantitativas discretas con pocos valores 
#'   distintos), se suelen emplear:
#' 
#'     - Gráficos de barras.
#' 
#'     - **Tablas de contingencia** y medidas de asociación.
#' 
#' - Si ambas variables son cuantitativas (continuas o discreta con muchos valores 
#'   distintos), se suelen emplear:
#' 
#'     - Gráficos de dispersión.
#' 
#'     - **Análisis de regresión** y correlación.
#' 
#' 
#' ## Análisis de una variable numérica y una categórica
#' 
#' En ocasiones interesar estudiar la distribución de una variable condicionada a que
#' la otra tome un determinado valor (o valores). En esta sección supondremos que
#' $(X,Y)$ es una variable estadística bidimensional, tal que:
#' 
#'  - $Y$ es una variable cuantitativa (valdría también para variables cualitativas).
#' 
#'  - $X$ es una variable cualitativa (o discreta) con $k$ modalidades $c_{1},c_{2},\ldots,c_{k}$.
#' 
#' Si sólo consideramos los individuos con $X=c_{i}$, hablaremos de la *distribución de
#' la variable* $Y$ *condicionada a* $X=c_{i}$. La variable condicionada se denotará
#' por $Y|X=c_{i}$ (esta definición es válida cualesquiera que sean los tipos de las
#' variables).
#' 
#' Se pueden emplear los métodos descritos en el tema anterior para estudiar las
#' distribuciones condicionadas (en este caso podemos realizar un análisis univariante
#' de la variable cuantitativa para cada modalidad de la variable cualitativa).
#' 
#' 
#' ### Gráficos de caja
#' 
#' Para analizar y comparar las distribuciones condicionadas son especialmente
#' recomendables los gráficos de cajas. Podemos generar un gráfico de cajas empleando
#' el método para `formula` (en lugar del método por defecto para vectores) de la
#' función genérica `boxplot()`: `boxplot(formula, data, ...)`.
#' 
#' Por ejemplo, continuando con los datos de móviles de la práctica anterior,
#' supongamos que nos interesa estudiar el `precio` dependiendo de la `marca` del
#' teléfono:
#' 

load("ecars2.RData")
load("movil.RData")
# str(movil)
# as.data.frame(attr(movil, "variable.labels")) # Etiquetas variables
boxplot(precio ~ marca, data = movil,
        ylab = "Precio (euros)", xlab = "Fabricante")

#' 
#' De estos gráficos se puede deducir mucha información:
#' 
#' 1. Comparando las medianas podemos estudiar si el factor (la variable cualitativa)
#' influye en la posición central de la respuesta (la variable cuantitativa).  En este
#' caso aparentemente hay grandes diferencias en el precio medio entre fabricantes,
#' especialmente entre *Apple* y el resto (abusando de la notación podríamos escribir
#' que mediana(precio|Apple) > mediana(precio|Xiaomi) > mediana(precio|Huawei)).
#' 
#' 2. Comparando las alturas de las cajas podemos estudiar si hay diferencias en la
#' variabilidad. En este caso, aparentemente la variabilidad del precio en *Huawei* es
#' mayor y no hay grandes diferencias en la variabilidad entre los otros fabricantes
#' (varibilidad(precio|Huawei > varibilidad(precio|Apple) =
#' varibilidad(precio|Xiaomi)).
#' 
#' 3. Analizando la forma de las cajas podemos estudiar la asimetría de las
#' distribuciones condicionadas. En este caso son bastante simétricas (quizás en
#' precio|Apple se observa una ligera asimetría positiva y en precio|Xiaomi una ligera
#' asimetría negativa).
#' 
#' 4. Finalmente podemos detectar la posible presencia de datos atípicos, que en este
#' caso no se observan.
#' 
#' 
#' ### Medidas descriptivas
#' 
#' Podemos completar la información gráfica mediante estadísticos descriptivos. Para
#' calcular medidas descriptivas de las distribuciones condicionadas podemos emplear la
#' función `tapply(X, INDEX, FUN, ...)`. Por ejemplo, para obtener el precio medio por
#' fabricante:
#' 

tapply(movil$precio, movil$marca, mean)

#' 
#' También se podría emplear^[Además de que la función `boxplot()` devuelve de forma
#' invisible los valores empleados en la construcción del gráfico.] las funciones
#' `by(data, INDICES, FUN, ...)` o `aggregate(formula, data, FUN, ...)` (que ademas
#' permiten operar sobre data.frames). Por ejemplo:

stat <- function(x) c(media = mean(x), mediana = median(x), sd = sd(x))
aggregate(precio ~ marca, movil, stat)

# by(movil$precio, movil$marca, summary)

#' 
#' 
#' ### Ejercicio
#' 
#' Empleando los datos (modificados) de vehículos eléctricos `ecars` de la práctica
#' anterior almacenados en el fichero *ecars2.RData*: 
#' 
#' a) Estudiar si la carga rápida (`cargarapida`) influye en la distancia recorrida con
#' carga completa (`dismax`).

load("ecars2.RData")

boxplot(dismax ~ cargarapida, data = ecars, 
        main = "Influencia de Carga Rápida en Distancia Máxima",
        ylab = "Distancia Máxima (km)", xlab = "Carga Rápida")

tapply(ecars$dismax, ecars$cargarapida, mean, na.rm = TRUE)

#' 
#' b) Analizar la velocidad máxima (`velmax`) dependiendo del tipo de tracción
#' (`traccion`).


boxplot(velmax ~ traccion, data = ecars, 
        col = "lightblue",
        main = "Velocidad Máxima por Tipo de Tracción",
        ylab = "Velocidad Máxima (km/h)", xlab = "Tracción")

# Resumen estadístico
summary(lm(velmax ~ traccion, data = ecars)) # Para ver si hay diferencias significativas




#' 
#' c) Estudiar la distribución del precio (`logprecio`) dependiendo del tipo de
#' vehículo (`carroceria2`).


# Opción 1: Boxplot (Excelente para comparar niveles de precio)
boxplot(logprecio ~ carroceria2, data = ecars, 
        las = 2, # Rota las etiquetas si son largas
        col = terrain.colors(5),
        main = "Distribución del log(Precio) por Carrocería")



#' 
#' ## Análisis de dos variables categóricas
#' 
#' Se pueden extender las herramientas para el análisis de una variable cualitativa al
#' caso bivariante. En este caso tendríamos tablas de frecuencias bidimensionales,
#' denominadas **tablas de contingencia**, que también podríamos obtener con la función
#' `table()` y podríamos representar mediante gráficos de barras con la función
#' `barplot()` (como ya se comentó, normalmente comenzaríamos por analizar los
#' gráficos).
#' 
#' 
#' ### Tablas de contingencia
#' 
#' Sea $(X,Y)$ una variable estadística bidimensional, tal que:
#' 
#' - $X$ es una variable cualitativa (o discreta) con $k$ modalidades
#'     $c_{1},c_{2},\ldots,c_{k}$.
#' 
#' - $Y$ es una variable cualitativa (o discreta) con $l$ modalidades
#'     $c_{1}^{\prime},c_{2}^{\prime},\ldots,c_{l}^{\prime}$.
#' 
#' Toda la información proporcionada por los sujetos de la muestra se puede resumir en
#' una **Tabla de contingencia**, una tabla de frecuencias bidimensional en la que las
#' filas se corresponden con una de las variable categóricas y las columnas con la otra
#' (la recomendación sería poner en columnas la variable con menor número de
#' modalidades).  Para cada combinación de filas y columnas se calcula la frecuencia de
#' la correspondiente combinación de modalidades (cada par de posibles valores
#' $(c_{i},c_{j}^{\prime})$ puede repetirse una o más veces en la muestra).  Al igual
#' que en el caso univariante podemos considerar frecuencias absolutas o relativas
#' (estás últimas también se suelen mostrar en escala de porcentajes):
#' 
#' - **Frecuencia absoluta** del par $(c_{i},c_{j}^{\prime})$
#'     $n_{ij}$ = número de individuos con $X=c_{i}$ e $Y=c_{j}^{\prime}$.
#' 
#' - **Frecuencia relativa** del par $(c_{i},c_{j}^{\prime})$ $=$
#'     $f_{ij}$$=\dfrac{n_{ij}}{n}$ = proporción de individuos con $X=c_{i}$
#'     e $Y=c_{j}^{\prime}$.
#' 
#' A partir de ellas podemos estudiar la **distribución conjunta** de ambas variables.
#' 
#' Como ya se comentó, podemos obtener la tabla de contingencia de frecuencias
#' absolutas con el comando `table(x, y)`. Por ejemplo:

frec <- table(movil$nsatisfa, movil$marca)
frec

#' A partir de la que podemos calcular las frecuencias relativas (proporciones) o los
#' porcentajes de las categorías, por ejemplo empleando la función `prop.table()`:

# Frecuencias relativas
prop.table(frec)   # frec/sum(frec)
# Porcentajes
porc <- 100*prop.table(frec)
porc

#' Es decir, hay 8 individuos con móviles de la marca Xiaomi y un nivel de satisfacción
#' alto (la combinación de categorías más frecuente, con un 16\% de las observaciones).
#' La combinación de categorías menos frecuente es un nivel de satisfacción bajo con un
#' móvil Apple con un 4\% de los individuos (2 casos).
#' 
#' Como también se comentó, podemos representar la distribución conjunta mediante un
#' gráfico de barras con la función `barplot()` (lo que en general permitiría detectar
#' con mayor comodidad las combinaciones de categorías más frecuentes y las menos
#' frecuentes). En este caso nos pueden interesar añadir los argumentos:
#' 
#' - `beside = TRUE`: para generar un gráfico de barras agrupado (si el número de 
#'    categorías es pequeño). Por defecto representa barras apiladas (`beside = FALSE`).
#' 
#' - `legend.text = TRUE` (o un vector de etiquetas de valores): para añadir una 
#'    leyenda (se pueden incluir argumentos adicionales con el parámetro `args.legend`).
#' 
#' Por ejemplo:

barplot(porc, ylab = "Porcentaje", beside = TRUE, legend.text = TRUE, 
        args.legend = list(x = "topleft", bty = "n"))

#' 
#' ### Ejercicio
#' 
#' Continuando con los datos (modificados) de vehículos eléctricos `ecars` del
#' ejercicio anterior: 
#' 
#' a) Obtener la tabla de contingencia y el gráfico de barras del tipo de tracción
#' (`traccion`) por carga rápida (`cargarapida`).

# 1. Tabla de contingencia
tabla_traccion <- table(ecars$traccion, ecars$cargarapida)
print(tabla_traccion)

# 2. Gráfico de barras agrupado (o apilado)
# Usamos 'beside = TRUE' para que las barras estén una al lado de la otra
barplot(tabla_traccion, 
        beside = TRUE, 
        legend = TRUE, 
        main = "Tracción según Carga Rápida",
        xlab = "Carga Rápida", 
        ylab = "Número de vehículos",
        col = c("steelblue", "orange", "darkgreen"))


#' 
#' b) Realizar un análisis descriptivo de la distribución conjunta de carga rápida
#' (`cargarapida`) y segmento de mercado (`segmento`).


# 1. Tabla de frecuencias conjuntas (en porcentajes sobre el total)
prop.table(table(ecars$cargarapida, ecars$segmento)) * 100

# 2. Gráfico de mosaico (Mosaic Plot)
# Es el mejor gráfico para "distribución conjunta" de dos variables cualitativas
mosaicplot(table(ecars$segmento, ecars$cargarapida), 
           main = "Relación entre Segmento y Carga Rápida",
           color = TRUE, 
           shade = TRUE)

#' 
#' 
#' ### Distribuciones marginales
#' 
#' En muchas ocasiones se suelen incluir en la tabla de contingencia los totales por
#' filas y columnas, denominadas **distribuciones marginales**.
#' Donde:
#' 
#' - $n_{i\cdot}=n_{i1}+n_{i2}+\ldots+n_{il}$ = número de individuos con $X=c_{i}$.
#' 
#' - $n_{{\cdot}j}=n_{1j}+n_{2j}+\ldots+n_{kj}$ = número de individuos con $Y=c_{j}^{\prime}$.
#' 
#' - $n$ = número (total) de individuos.
#' 
#' El caso de frecuencias relativas sería análogo:
#' 
#' - $f_{i\cdot}=\frac{n_{i\cdot}}{n}=f_{i1}+f_{i2}+\ldots+f_{il}$ 
#'   = proporción de individuos con $X=c_{i}$.
#' 
#' - $f_{{\cdot}j}=\frac{n_{{\cdot}j}}{n}=f_{1j}+f_{2j}+\ldots+f_{kj}$ 
#'   = proporción de individuos con $Y=c_{j}^{\prime}$.
#' 
#' - El total sería 1 en lugar de $n$.
#' 
#' Las distribuciones marginales son simplemente las distribuciones de frecuencias
#' unidimensionales de las variables $X$ e $Y$ (su nombre se debe a que se obtienen
#' añadiendo en los márgenes de la tabla las sumas de las frecuencias de la
#' distribución conjunta) y son de utilidad para estudiar las variables de forma
#' individual. Por tanto, a partir de la tabla de contingencia podemos realizar los
#' análisis descriptivos univariantes descritos en la práctica anterior.
#' 
#' Podemos obtener estas distribuciones con la función `addmargins()`. Por ejemplo:
#' 

addmargins(frec)
addmargins(porc, margin = 2, FUN = list(Total = sum))

#' 
#' 
#' ### Distribuciones condicionadas
#' 
#' Para estudiar si hay relación (asociación) entre las variables nos interesará
#' comparar las distribuciones condicionadas (que se definen como en la sección
#' anterior, aunque en este caso son cualitativas).  Si sólo consideramos los
#' individuos con $Y=c_{j}^{\prime}$, hablaremos de la distribución de la variable $X$
#' condicionada a $Y = c_j^{\prime}$ (que denotaremos por $X|Y = c_j^{\prime}$).
#' 
#' La tabla de frecuencias absolutas de $X$ condicionada a $Y=c_{j}^{\prime}$, será:
#' 
#'  $X|Y=c_{j}^{\prime}$    $c_{1}$    $\cdots$    $c_{i}$    $\cdots$   $c_{k}$
#' ---------------------- ----------- ---------- ----------- ---------- -----------
#'                         $n_{1/j}$   $\cdots$   $n_{i/j}$   $\cdots$   $n_{k/j}$
#' 
#' donde $n_{i/j}=n_{ij}$. Es decir, es simplemente la columna $j$ de la tabla de
#' contingencia de frecuencias absolutas. Análogamente obtendríamos la tabla de
#' frecuencias absolutas de $Y|X=c_{i}$.
#' 
#' Por ejemplo:

# Tabla de frecuencias absolutas del nivel de satisfacción condicionada a fabricante Apple
frec[, "Apple"]
# Tabla de frecuencias absolutas de fabricante condicionada a nivel de satisfacción alto
frec["Alto", ]

#' 
#' A partir de estos valores podríamos obtener las frecuencias relativas. Por ejemplo
#' la tabla de frecuencias relativas de $X$ condicionada a $Y=c_{j}^{\prime}$, será de
#' la forma:
#' 
#'    $X|Y=c_{j}^{\prime}$    $c_{1}$    $\cdots$    $c_{i}$    $\cdots$   $c_{k}$
#'   ---------------------- ----------- ---------- ----------- ---------- -----------
#'                           $f_{1/j}$   $\cdots$   $f_{i/j}$   $\cdots$   $f_{k/j}$
#' 
#' donde $f_{i/j}=\frac{n_{ij}}{n_{\cdot j}}=\frac{f_{ij}}{f_{\cdot j}}$. De forma
#' análoga se obtendrían las frecuencias relativas de cada modalidad de $Y$
#' condicionadas a una modalidad de $X$.
#' 
#' Para calcular de forma simultánea las tablas de frecuencias relativas de las
#' distribuciones condicionadas podemos emplear el argumento `margin` (índice sobre el
#' que se condiciona) de la función `prop.table()`.
#' 
#' Por ejemplo, podemos obtener y representar las distribuciones del nivel de
#' satisfacción condicionadas a los distintos fabricantes:

# Distribución del nivel de satisfacción según fabricante
porc.cond <- 100*prop.table(frec, 2)
porc.cond
# Gráfico de barras apilado
barplot(porc.cond, ylab = "Porcentaje", legend.text = TRUE)
# La suma por columnas es el 100%
addmargins(porc.cond, 1)

#' 
#' Si no hay relación (asociación) entre las variables las distribuciones condicionales
#' deberían ser similares a la correspondiente distribución marginal. A efectos
#' ilustrativos podemos repetir el ejemplo anterior pero añadiendo la distribución
#' marginal del nivel de satisfacción:

frec2 <- addmargins(frec, 2)
# frec2 <- addmargins(frec, margin = 2, FUN = list(Total = sum))
100*prop.table(frec2, 2)


#' 
#' ### Medidas de asociación
#' 
#' Para cuantificar el grado de asociación nos interesaría calcular medidas
#' descriptivas que, por ejemplo, tomen el valor 0 cuando el nivel de asociación sea
#' nulo y el valor 1 cuando el nivel de asociación sea máximo.
#' 
#' Si no hay ninguna asociación entre las variables las tablas de frecuencias relativas
#' de $Y|X=c_{1},\ldots,Y|X=c_{k}$ serán iguales (a las frecuencias relativas
#' marginales de $Y$). Es decir: $$f_{i/j}=\frac{f_{ij}}{f_{\cdot j}}=f_{i.}\text{ para
#' todo }i,j.$$ De donde se deduce que $f_{ij}=f_{i.}f_{.j}$, o equivalentemente:
#' $$n_{ij}=\dfrac{n_{i.}n_{.j}}{n}$$ para todo $i$, $j$. Los valores:
#' $$e_{ij}=\dfrac{n_{i.}n_{.j}}{n}$$ se denominan **frecuencias esperadas bajo
#' independencia**.
#' 
#' Las medidas de asociación más simples (válidas para todo tipo de variables
#' cualitativas) están basadas en el estadístico chi-cuadrado de Pearson (1900):
#' $$\chi^2=\sum_{i,j}\frac{(n_{ij} - e_{ij})^2}{e_{ij}}$$ Este estadístico mide la
#' distancia entre las frecuencias observadas y las esperadas bajo independencia, y
#' toma el valor 0 cuando no hay asociación entre las variables (estudiaremos con mayor
#' profundidad este estadístico en la parte de inferencia estadística).
#' 
#' Podemos obtener medidas de asociación reescalando esta distancia de forma que tome
#' valores entre 0 y 1. Las más conocidas son:
#' 
#' - El coeficiente de contingencia:
#'   $$C=\sqrt{\frac{ \chi^2}{ \chi^2 +n}}$$
#'   (su valor máximo puede ser menor de 1).
#' 
#' - La V de Cramer:
#'   $$V=\sqrt{\frac{ \chi^2}{ n \cdot (m-1)}}$$
#'   donde $m$ es el mínimo del número de filas y de columnas
#'   (puede tomar el valor 1, asociación completa, en tablas de cualquier dimensión).
#' 
#' Podemos calcular estas medidas a partir de los resultados de la función
#' `chisq.test()` del paquete base de R, pero puede resultar más cómodo emplear la
#' función `assocstats()` del paquete `vcd`:

library(vcd)
assocstats(frec)

# Empleando chisq.test:
chisq.stat <- chisq.test(frec)$statistic
chisq.stat # Estadístico chi-cuadrado
names(chisq.stat) <- NULL
# Coeficiente de contingencia
sqrt(chisq.stat / (chisq.stat + sum(frec)))
# V de Cramer
sqrt(chisq.stat / (sum(frec) * (min(dim(frec)) - 1)))

#' En este caso el grado de asociación entre satisfacción y fabricante es bastante
#' bajo.
#' 
#' En el caso de variables ordinales (o discretas) podemos emplear medidas de
#' asociación que aprovechen la información adicional que proporciona la ordenación. En
#' la siguiente sección se mostrarán como ejemplo el coeficiente de correlación de
#' Spearman y la tau-b de Kendall (que aparecen como alternativa al coeficiente de
#' correlación lineal de Pearson).
#' 
#' ### Ejercicio
#' 
#' Continuando con los datos (modificados) de vehículos eléctricos `ecars` de
#' ejercicios anteriores: 
#' 
#' a) Estudiar la distribución de carga rápida (`cargarapida`) condicionada al tipo de
#' tracción (`traccion`).


# 1. Creamos la tabla de contingencia
tabla_ac <- table(ecars$traccion, ecars$cargarapida)

# 2. Calculamos las frecuencias relativas por FILAS (condicionada a tracción)
# margin = 1 indica que cada fila sumará 100% (o 1)
prop.table(tabla_ac, margin = 1)

# 3. Visualización con gráfico de barras apiladas al 100%
barplot(t(prop.table(tabla_ac, margin = 1)), 
        legend = TRUE, 
        main = "Carga Rápida condicionada al tipo de Tracción",
        col = c("tomato", "skyblue"),
        ylab = "Proporción")


#' 
#' b) Realizar un análisis descriptivo completo (incluyendo medidas de asociación) de
#' tipo de tracción (`traccion`) y tipo de vehículo (agrupado) (`carroceria2`).

# Tabla de contingencia
tabla_conjunta <- table(ecars$traccion, ecars$carroceria2)
print(tabla_conjunta)

# Gráfico de Mosaico (el mejor para ver la distribución conjunta)
mosaicplot(tabla_conjunta, main = "Asociación: Tracción vs Carrocería", 
           shade = TRUE, color = TRUE)


# Test de Chi-cuadrado
prueba_chi <- chisq.test(tabla_conjunta)
print(prueba_chi)


# Necesitas la librería 'vcd' o calcularla manualmente
# install.packages("vcd")
library(vcd)
assocstats(tabla_conjunta)


#' 
#' ## Análisis de dos variables numéricas
#' 
#' En esta sección nos centraremos en el caso de dos variables numéricas, y supondremos
#' que $Y$ es la variable de interés o respuesta (también denominada variable
#' dependiente en este contexto) y $X$ es la variable explicativa (también denominada
#' predictor, variable regresora o variable independiente).  Nos interesa estudiar la
#' posible relación entre estas dos variables (si la distribución de $Y$ depende de $X$
#' y en caso afirmativo, cuál es la relación funcional entre ellas).
#' 
#' Es importante tener en cuenta que relación no implica causalidad, es lo que se
#' conoce como [relación espuria](https://es.wikipedia.org/wiki/Relaci%C3%B3n_espuria)
#' (o correlación espuria). La aparente relación puede ser debida a la casualidad o a
#' otras variables que no se tienen en cuenta (denominadas *factores de confusión* o
#' *variables ocultas*)^[Ver por ejemplo el blog
#' [spurious-correlations](https://tylervigen.com/spurious-correlations) o [Chocolate
#' creates Nobel prize winners](https://www.confectionerynews.com/Article/2012/10/11/Chocolate-creates-Nobel-prize-winners-says-study).].
#' 
#' 
#' ### Gráfico de dispersión
#' 
#' Como primer paso la recomendación es generar un gráfico de dispersión de $Y$ sobre
#' $X$, en el que se representa cada par de observaciones $(x_i , y_i)$ como un punto
#' en el plano cartesiano.  Si se observa alguna forma concreta en la nube de puntos,
#' indicaría que hay algún tipo de relación entre las variables.  Si los puntos de la
#' nube se agrupan en torno a una recta, diremos que las variables parecen estar
#' relacionados linealmente (la relación es lineal, aparentemente).
#' 
#' En R podemos generar este gráfico con el comando `plot(x, y)`. Por ejemplo:

plot(movil$peso, movil$precio, xlab = "Peso (gramos)", ylab = "Precio (euros)")

#' En este caso aparentemente hay una relación lineal negativa, al aumentar el peso
#' disminuye el precio (de forma lineal).
#' 
#' 
#' ### Medidas descriptivas
#' 
#' Podemos emplear los estadísticos descriptivos univariantes descritos en la práctica
#' anterior para analizar las variables por separado.
#' 
#' Por ejemplo, podemos calcular las medias $\overline{x}$ e $\overline{y}$ de ambas
#' variables. El vector: $$\left( \begin{array}[c]{c} \overline{x}\\ \overline{y}
#' \end{array} \right)$$ se denomina **vector de medias** de la variable $(X,Y)$.
#' 
#' Análogamente podemos calcular las varianzas $s_X^2$ y $s_Y^2$. En este caso además
#' nos interesará una medida de la variabilidad conjunta de ambas variables, la
#' **covarianza** de $(X,Y)$:
#' $$s_{XY}=\frac{1}{n}\sum_{i=1}^{n}(x_{i}-\overline{x})(y_{i}-\overline{y})
#' =\frac{1}{n}\sum_{i=1}^{n}x_{i}y_{i}-\overline{x}\, \overline{y}$$
#' 
#' Podemos obtener la covarianza con la función `cov()`.  Por ejemplo:

cov(movil$peso, movil$precio)

#' 
#' Se denomina matriz de varianzas-covarianzas de la variable $(X,Y)$ a la matriz:
#' $$S=\left( \begin{array}[c]{cc} 
#' s_{X}^{2} & s_{XY}\\ s_{XY} & s_{Y}^{2} 
#' \end{array} \right)$$
#' 
#' La función `cov()` devuelve esta matriz cuando el primer argumento es un data.frame
#' o una matriz:

cov(movil[c("peso", "precio")])

#' 
#' La covarianza es una medida del grado de relación lineal
#' Sin embargo, el valor de la covarianza depende de la escala de las variables (por lo
#' que resulta complicado saber cuando es grande o próxima a cero).  Para medir el
#' grado de dependencia o relación (lineal) entre las variables es preferible reescalar
#' este valor (por ejemplo de forma que su valor máximo sea conocido).
#' 
#' ### El coeficiente de correlación lineal
#' 
#' El coeficiente de correlación lineal de Pearson: $$r=\frac{s_{XY}}{s_{X}s_{Y}}$$ es
#' una medida adimensional de la **relación lineal** entre dos variables cuantitativas
#' (no depende de las unidades de medida). Siempre toma valores entre -1 y 1: $$-1 \leq
#' r \leq 1$$
#' 
#' Si $r = \pm 1$ hay una relación lineal exacta entre las dos variables.
#' 
#' Si $r=0$ no hay relación lineal entre las variables (puede haber una relación no
#' lineal) y se dice que las variables son **incorreladas**.
#' 
#' Podemos obtener el coeficiente de correlación con la función `cor()`.  Por ejemplo:

# Coeficiente de correlación
cor(movil$peso, movil$precio)
# Matriz de correlaciones
cor(movil[c("peso", "precio")])

#' 
#' Además, el coeficiente de correlación lineal:
#' 
#' - No se ve afectado por transformaciones lineales.
#' 
#' - No es una medida robusta, puede verse seriamente afectado por observaciones atípicas.
#' 
#' También hay modificaciones de este coeficiente más adecuadas para el caso de
#' distribuciones asimétricas, o si hay observaciones atípicas, o si alguna de las
#' variables es discreta o incluso solo ordinal, como el coeficiente de correlación por
#' rangos de Spearman (transforma las variables a rangos) o la tau-b de Kendall (mide
#' la concordancia entre pares de observaciones). También podemos obtener estas medidas
#' la función `cor()`, estableciendo el parámetro `method = "spearman"` o `method =
#' "kendall"`, respectivamente.
#' 
#' 
#' ### Ejercicio
#' 
#' Continuando con los datos (modificados) de vehículos eléctricos `ecars` de
#' ejercicios anteriores:
#' 
#' a) Generar el gráfico de dispersión de la eficiencia (`eficiencia`) sobre la
#' velocidad de carga (`velcarga`). Calcular la covarianza y la correlación entre ambas
#' variables (Nota: si hay datos faltantes se puede emplear `use = "complete.obs"` al
#' llamar a `cov()` o `cor()` para no tenerlas en cuenta en los cálculos).


#' 
#' b) Estudiar si el precio (`logprecio`) es de utilidad para explicar la velocidad
#' máxima (`velmax`).



#' 
#' ### Regresión y correlación
#' 
#' El análisis de **regresión** (1889, Francis Galton, Natural inheritance) es una
#' técnica estadística centrada en el estudio de las posibles relaciones entre
#' variables con el propósito de establecer una relación funcional entre ellas (un
#' modelo matemático que relacione una respuesta con un conjunto de variables
#' explicativas).  Por **correlación** se entiende el grado de asociación entre dos (o
#' más) variables. En este apartado nos centraremos únicamente en regresión simple (dos
#' variables numéricas), desde un punto de vista descriptivo (se volverá a tratar más
#' adelante en la parte de inferencia estadística).
#' 
#' Nos interesará especialmente estudiar si hay una relación lineal entre las dos
#' variables (la relación más simple).  Si suponemos que la variable respuesta $Y$ y la
#' variable explicativa $X$ están relacionadas linealmente podemos obtener la *recta de
#' regresión mínimo cuadrática* (aproximación de la relación entre ambas variables) y
#' estudiar la *bondad del ajuste* (tratar de medir lo adecuada que es la recta
#' ajustada para explicar la respuesta; en este caso será una medida del grado de
#' relación lineal).
#' 
#' En general tendríamos tres posibles situaciones:
#' 
#' -   **Relación exacta** (o **funcional**): la variable explicativa
#'     determina totalmente el valor de la respuesta:
#'     $$Y = m(X)$$
#' 
#' -   **Independencia:** la variable explicativa no aporta ninguna
#'     información sobre la respuesta.
#' 
#' -   **Relación estadística** o **estocástica**: la variable explicativa
#'     permiten predecir en mayor o menor grado el valor de la respuesta:
#'     $$Y = m(X) + \varepsilon$$
#' 
#' Se puede explicar la respuesta mediante una función de la **variable explicativa**,
#' más un **término de error** $\varepsilon$ (que recogería el efecto conjunto de otras
#' variables no consideradas).
#' 
#' Consideraremos el caso más simple, lo que se conoce como **regresión lineal
#' simple**. Supondremos que la variable respuesta $Y$ y la variable explicativa $X$
#' están relacionadas linealmente: $$Y = a + bX + \varepsilon$$
#' 
#' El **objetivo principal** es, a partir de los valores observados: $$\{ (x_i, y_i) :
#' i = 1, \cdots, n \},$$ $$y_i = a + bx_i + \varepsilon_i,$$ **aproximar la recta de
#' regresión:** $$y = a + bx$$ (es decir, aproximar los parámetros $a$ y $b$).
#' 
#' Como criterio de ajuste (para buscar la recta con la que se predice mejor la
#' respuesta) se empleará el método de mínimos cuadrados.
#' 
#' 
#' ### Recta de regresión mínimo cuadrática
#' 
#' Es la recta $\hat{y}=\hat{a}+\hat{b}x$ que **minimiza la suma de los cuadrados de
#' los errores**: 
#' $$\min_{a, b} \sum \limits_{i=1}^{n}(y_i- (a + bx_i))^2 
#' = \min_{a, b} \sum \limits_{i=1}^{n}e_i^2$$
#' Puede verse fácilmente^[Calculando las derivadas parciales de la suma de cuadrados,
#' igualando a cero y resolviendo el sistema.] que: $$\begin{array}[c]{l} \hat{a} =
#' \overline{y} - \hat{b} \overline{x}\\ \hat{b}=\dfrac{s_{XY}}{s_X^{2}} \end{array}$$
#' 
#' Entonces la ecuación de la recta de regresión mínimo cuadrática de $Y$ sobre $X$
#' puede expresarse como: $$\hat{y}=\bar{y}+\dfrac{s_{XY}}{s_X^{2}}(x-\bar{x})$$
#' 
#' NOTAS:
#' 
#' -   La recta de regresión mínimo cuadrática siempre pasa por el punto
#'     $\left(  \bar{x},\bar{y}\right)$.
#' 
#' -   La recta de regresión de $Y$ sobre $X$ ($Y|X$) no coincide con la
#'     recta de regresión de $X$ sobre $Y$ ($X|Y$), salvo relación lineal
#'     perfecta.
#' 
#' En R podemos realizar un ajuste de un modelo lineal con la función `lm()`. Por
#' ejemplo:

fit <- lm(precio ~ peso, data = movil)
plot(movil$peso, movil$precio,
     xlab = "Peso (en gramos)", ylab = "Precio (en euros)")
abline(fit, col = "blue")
fit

#' En este caso, la recta de regresión mínimo cuadrática para explicar el precio a
#' partir del peso es: $$\widehat{precio} = 2515.65 - 12.11 \cdot peso$$.
#' 
#' Podemos interpretar los coeficientes:
#' 
#' - $\hat{a}$: predicción de $Y$ cuando $X = 0$ (no suele ser de gran interés).
#' 
#' - $\hat{b}$: Incremento en (la predicción de) $Y$ cuando $X$ aumenta una unidad.
#' 
#' En este caso, por cada incremento de un gramo de peso, la predicción del precio
#' disminuye en 12.11 euros.
#' 
#' Sustituyendo en la recta ajustada la variable explicativa por un valor obtendríamos
#' la correspondiente predicción de la respuesta. Podemos obtener estas predicciones
#' con la función genérica `predict()`. Por defecto se obtienen las predicciones para
#' los valores observados: 
#' $$\hat{y}_i = \hat{a} + \hat{b}x_i$$

pred <- predict(fit)
# Gráfico de predicciones frente a observaciones
plot(pred, movil$precio, xlab = "Predicciones", ylab = "Observaciones")
abline(a = 0, b = 1, lty = 2) # recta x = y

#' Podemos obtener predicciones para nuevos valores empleando el parámetro `newdata`
#' (que debe ser un data.frame; ver `?predict.lm`):

predict(fit, newdata = data.frame(peso = c(150, 200)))

#' 
#' ### Bondad del ajuste
#' 
#' Las diferencias entre valores observados y predicciones:
#' $$y_i-(\hat{a}+\hat{b}x_i)=y_i-\hat{y}_i=e_i$$ se denominan **residuos** (de media
#' $0$). Su varianza: $$s_{R}^2=\dfrac{1}{n}\sum
#' \limits_{i=1}^{n}(y_i-\hat{y}_i)^2=\dfrac {1}{n}\sum \limits_{i=1}^{n}e_i^2$$ es una
#' medida de la variabilidad de los datos respecto a la recta, denominada **varianza
#' residual** (aunque también depende de la escala de la respuesta).
#' 
#' Una medida de la bondad del ajuste (evaluación global de la recta de regresión) es
#' **el coeficiente de determinación**: $$R^2
#' =\frac{\sum_{i=1}^{n}(\hat{y}_i-\bar{y})^2}{\sum_{i=1}^{n}
#' (y_i-\bar{y})^2}=\frac{s_{E}^2}{s_Y^2}
#'  =1-\frac{\sum_{i=1}^{n}(y_i-\hat{y}_i)^2}{\sum_{i=1}^{n}(y_i-\bar
#' {y})^2}=1-\frac{s_{R}^2}{s_Y^2}$$ que se puede interpretar como la **proporción de
#' variabilidad** (de la respuesta) **explicada por la regresión**.
#' 
#' Se verifica que $0 \leq R^2 \leq 1$:
#' 
#' -   Si $R^2=1$ todas las observaciones están en la recta de regresión
#'     (lo explica todo)
#' 
#' -   Si $R^2=0$ la recta de regresión no explica nada
#' 
#' Podemos obtener este coeficiente empleando la función `summary()`. Por ejemplo:

summary(fit)$r.squared

#' La recta ajustada explicaría un 69\% de la variabilidad del precio, por lo tanto el
#' ajuste es regular/bueno.
#' 
#' En el caso de regresión lineal simple, se puede interpretar del coeficiente de
#' determinación a partir del coeficiente de correlación lineal de Pearson. Teniendo en
#' cuenta que $$\hat{y}_i=\bar{y}+\hat{b}(x_i-\bar{x}),$$ se puede expresar el
#' coeficiente de determinación como:
#' $$R^2=\hat{b}^2\frac{s_X^2}{s_Y^2}=\frac{s_{XY}^2}{s_X^2 s_Y^2},$$ que resulta ser
#' el cuadrado del coeficiente de correlación lineal de Pearson $r=\frac{s_{XY}}{s_X
#' s_Y}$.
#' 
#' Por ejemplo:

cor(movil$peso, movil$precio)^2

#' 
#' NOTA: $$r=0 \Leftrightarrow s_{XY}=0 \Leftrightarrow \hat{b}=0$$
#' 
#' 
#' ### Ejercicio
#' 
#' Continuando con los datos (modificados) de vehículos eléctricos `ecars` de
#' ejercicios anteriores:
#' 
#' a) Obtener la recta de regresión mínimo cuadrática de velocidad máxima (`velmax`)
#' sobre el precio en escala logarítmica (`logprecio`), representarla gráficamente y
#' estudiar la bondad del ajuste. Emplearla para predecir la velocidad máxima de un
#' coche eléctrico con un precio de 50000 euros.


#' 
#' b) Estudiar si la distancia máxima con carga completa (`dismax`) es de utilidad para
#' explicar la velocidad de carga (`velcarga`). En caso afirmativo emplearla para
#' predecir los datos faltantes de `velcarga`.

load("ecars2.RData")
index <- which(is.na(ecars$velcarga))
ecars[index, ]
# Nota: son los 5 sin carga rápida (cuidado)

#' 
#' 
#' ## Estadística descriptiva multivariante
#' 
#' Los métodos descriptivos anteriores se pueden extender al caso multivariante (aunque
#' se han desarrollado métodos específicos para analizar simultáneamente muchas
#' variables). A continuación se muestran algunos ejemplos solo con fines ilustrativos.
#' 
#' Por ejemplo, en el caso de más de dos variables numéricas podemos emplear un gráfico
#' de dispersión matricial:

plot(movil[5:7])

#' y calcular la matriz de correlaciones:

mcor <- cor(movil[c(5:7)])
print(mcor, digits = 2)

#' 
#' En el caso de una variable numérica (respuesta) y varias variables categóricas
#' (factores), podemos generar gráficos de cajas agrupados^[En el caso de tres factores
#' se recomendaría generar uno por cada nivel del tercer factor. En los análisis
#' gráficos no se suelen considerar más de tres factores simultáneamente.]:

boxplot(precio ~ sexo + marca, data = movil, col = gray.colors(2),
        ylab = "Precio (euros)", xlab = "Fabricante")

#' También podemos obtener estadísticos descriptivos de la respuesta para cada
#' combinación de niveles de los factores:

aggregate(precio ~ sexo + marca, movil, mean)

#' También es habitual representar gráficamente estos estadísticos:

with(movil, interaction.plot(marca, sexo, precio))

#' 
#' En el caso de múltiples variables categóricas podemos generar tablas de contingencia
#' multidimensionales y, por ejemplo, gráficos de barras agrupados con las frecuencias
#' de dos variables categóricas para cada combinación de categorías de las demás. Por
#' ejemplo:

# Distribución conjunta de sexo, nsatisfa y marca
frec <- with(movil, table(sexo, nsatisfa, marca))
frec
# Distribución de nsatisfa condicionada a sexo y marca:
porc.cond <- 100*prop.table(frec, c(1,3))
round(porc.cond, 1)

