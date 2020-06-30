# Tarea3
Repositorio que contiene la solución de la tarea 3 del curso Modelos probabilísticos de señales y sistemas.

Estudiante: Jonathan Ramírez Hernández; carné: B55730.
Correo: jon231996@gmail.com
Grupo: 02.

Solución.

	Primeramente, se importaron las bibliotecas necesarias parala solución de la tarea. Entre ellas, “pandas”, “numpy”, “matplotlib”, “scipy” y “math”. Posteriormente, se importó el archivo de datos .csv que se llamaba “xy”. Se le asignaron nombres a las columnas, en los que, por ejemplo, “c0” significa la primera columna, y así sucesivamente. A los datos importados se les asignó el nombre  “data”.

Inciso 1
	La idea para resolver este inciso es obtener las funciones de densidad marginales de X e Y. Para la función de X, se toma cada fila de los datos y se suman todas las probabilidades que corresponden a esa fila (las asociadas a cada “y”); de esta forma, se obtiene un valor de probabilidad para cada fila de “x”, es decir, “x5” tiene una probabilidad asociada, también “x6”, “x7” y así sucesivamente. Luego, se muestra la gráfica de las probabilidades de cada “x” junto con su valor del eje X asociado, por ejemplo, “x5” tiene una probabilidad P (que se muestra en el eje Y) y en el eje X es 5 (por “x5”), y así con el resto. Este mismo procedimiento se hace para la función de Y, pero al obtener la suma de cada “y” se hace columna por columna. Las gráficas obtenidas están en el repositorio.
	Luego de ver las formas de las gráficas (función de densidad marginal) se puede ver que tienen una forma conocida, en este caso ambas se parecen a una distribución gaussiana. Entonces, se supone una curva de ajuste que tenga forma normal y se grafica para ver la aproximación. Las gráficas de las curvas de ajuste se adjuntan en el repositorio. 
	Finalmente, para obtener los parámetros del modelo probabilístico asociado con las curvas de ajuste, se define una función que recibe de entrada tres parámetros: “x” que es el conjunto de valores del eje X, “mu” y “sigma” que son los coeficientes de la expresión análitica de una distribución normal. La función retorna la expresión de una distribución normal. Luego, se obtienen los parámetros asociados a cada curva usando la función “curve_fit”, estos se almacenan en vectores llamados “param0” para la función de X y “param1” para la de Y. Solo contienen dos valores en los que el primero se refiere  a “mu” y el segundo a “sigma”.

NOTA: en el código la mayoría de los comandos para graficar vienen en comentario debido a que si se dejan, la figura que se quiera ver no se grafica de forma correcta, por lo que lo mejor es graficarlas una a la vez.

Inciso 2
	Al asumir la independencia estadística de ambas funciones se tiene que la función de probabilidad conjunta se obtiene al hacer el producto de las funciones de densidad marginales de X e Y. Estas expresiones se conocen por los resultados del inciso anterior. Luego, con el uso de los comandos para gráficas en 3D de mathplot se grafica la función de distribución conjunta. La gráfica se adjunta. El coeficiente de la función conjunta es el producto de los coeficientes de cada función marginal y el argumento de la exponencial es la suma de los argumentos de la exponencial de cada función marginal, por las propiedades de la función exponencial.


Inciso 3
	Para calcular la correlación, se utilizó la propia definición que muestra que éste valor se obtiene de la suma total del producto de los valores de “x” e “y” con la probabilidad de ambos, es decir f(x,y). Es decir, que se suman x5*y5*f(x5,y5), x6*y5*f(x6,y5) y así sucesivamente hasta acabar la tabla. La suma de todo eso es el valor de la correlación. Para ello, simplemente se utilizó un ciclo “for” anidado para recorrer toda la tabla y hacer lo especificado. Este valor de la correlación indica la medida en la que las funciones de X e Y están correlacionadas una con la otra. La correlación se entiende como la medida en la que la variación de los parámetros de una variable aleatoria afectan la variación de los parámetros de la otra.
	Para calcular la covarianza se procedió de forma similar al inciso anterior, pero esta vez se utilizaron los valores de “x” e “y” (5, 6, 7, …, 15, 16, 17, etc…) menos el valor medio de la función respectiva, que ya se conoce pues es el valor de “mu”, es decir: 5-mu, 6-mu, 7-mu, etc. Esto es lo que indica la definición de la covarianza. La covarianza muestra la variación que sufren dos variables al tomar como referencia la media, por ejemplo, la forma en la que la variación de los valores más altos de una variable afectan los más bajos de la otra.
	El coeficiente de correlación se calcula con la fórmula: CCOR = Cxy/(sigma_x*sigma_y). Es decir, es la división de la covarianza entre el producto de las desviaciones estándar de las funciones de X e Y. Este coeficiente también se usa para medir la variación de una variable con respecto a la otra, pero, a diferencia de la covarianza, no toma como referencia la media para hacerlo. Mide la relación entre dos variables que son cuantitativas y continuas.
	Los valores obtenidos son:
1. Correlación: 149.54281000000012
2. Covarianza: 0.06669156992289262
3. Coeficiente de correlación: 0.00335377268083899

Inciso 4
	Las gráficas de las funciones marginales de X e Y y la de distribución conjunta se realizaron en los incisos anteriores, y se adjuntan en el repositorio, por lo que se resuelve este inciso.
