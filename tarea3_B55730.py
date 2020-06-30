#!/usr/bin/env python
# coding: utf-8

# In[42]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import norm
import math


# In[43]:


#Lectura del archivo de datos.
address = 'xy.csv'
names = ['c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9',
         'c10', 'c11', 'c12', 'c13', 'c14', 'c15', 'c16', 'c17', 'c18', 'c19', 'c20']
data = pd.read_csv(address, names = names)
data


# In[59]:


#Inciso 1

#Definición de vectores del eje X para cada función de densidad marginal.
x_p = list(range(5,16))
y_p = list(range(5,26))

#Obtención de la función de densidad marginal de X.
#Par esto, primero se obtiene la suma de cada x_i del archivo de datos. Por ejemplo, para x_5 se suman todos
#los valores que le corresponden en y (todos los valores de esa fila).
#Luego, cada valor de x_i es almacenado en una lista llamada "xi" respectivamente; es decir, que en la posición
#0 de xi está la suma para x_5, en la posición 1, la de x_6 y así sucesivamente.

xi = list(range(0,11))

#Ciclo que hace la suma para cada x_i y lo almacena en la lista.
for i in range(0,11):
    sum = 0
    for j in range(len(names)):
        sum = sum+data.iloc[i][names[j]]
    xi[i] = sum
    
#Se imprime la lista para ver los resultados.
#print(xi)

#Obtención de la función de densidad marginal de Y.
#Se hace el mismo procedimiento anterior pero para cada y_i.

yi = list(range(0,21))

#Ciclo que hace la suma para cada y_i y lo almacena en la lista.
for j in range(0,21):
    sum = 0
    for i in range(0,11):
        sum = sum+data.iloc[i][names[j]]
    yi[j] = sum
    
#Se imprime la lista para ver los resultados.
#print(yi)

#Se grafican los resultados con x_p y y_p en el eje X y "xi", "yi" en el eje Y.
#plt.plot(x_p, xi)
#plt.title("Función de densidad marginal de X")
#plt.xlabel("Valores de los datos")
#plt.ylabel("Probabilidad")

#plt.plot(y_p, yi)
#plt.title("Función de densidad marginal de Y")
#plt.xlabel("Valores de los datos")
#plt.ylabel("Probabilidad")


#A partir de la información obtenida, se puede ver que las funciones de densidad marginales se comportan de
#forma similar a una distribución gaussiana. Entonces, se obtiene una curva de ajuste para cada función.

#Graficación de la curva de ajuste para X e Y.
#x_c = sns.distplot(xi, fit=stats.norm)
#plt.title("Curva de mejor ajuste para la función de densidad marginal de X")
#plt.xlabel("Valores de los datos")
#plt.ylabel("Probabilidad")

y_c = sns.distplot(yi, fit=stats.norm)
plt.title("Curva de mejor ajuste para la función de densidad marginal de Y")
plt.xlabel("Valores de los datos")
plt.ylabel("Probabilidad")

#Obtención de los parámetros asociados a las curvas de las funciones marginales.
#Definición de una función que retorne la expresión analítica de una distribución gaussiana.

def gaussiana(x, mu, sigma):
    return (1/(np.sqrt(2*np.pi*pow(sigma,2)))*(np.exp((-pow(x-mu,2))/(2*pow(sigma,2)))))

#Obtención de los parámetros asociados con cada función de densidad marginal.

param0,_ = curve_fit(gaussiana, x_p, xi)
param1,_ = curve_fit(gaussiana, y_p, yi)

#print(param0, param1)


# In[62]:


#Inciso 2.
#Debido a la independencia estadística de ambas funciones, la función de densidad conjunta se determina al hacer el
#producto de las funciones de densidad marginales. Esto puede hacerse de esta forma debido a que se conocen las 
#expresiones para estas funciones.

from mpl_toolkits.mplot3d import Axes3D
import pylab as pl

fig = pl.figure()
ax = Axes3D(fig)
X = np.arange(0, 30, 0.25)
Y = np.arange(0, 30, 0.25)
X, Y = np.meshgrid(X, Y)

c = (1/(np.sqrt(2*np.pi*pow(param0[1],2))))*(1/(np.sqrt(2*np.pi*pow(param1[1],2))))
arg = (-pow(X-param0[0],2))/(2*pow(param0[1],2)) - (-pow(Y-param1[0],2))/(2*pow(param1[1],2))
Z = c*np.exp(arg)

#Titulos.
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x,y)')
ax.set_title('Función de densidad probabilística conjunta')

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hot')


# In[46]:


#Inciso 3
#Correlación.
sum = 0
for i in range(0,11):
    for j in range(0,21):
        sum = sum+data.iloc[i][names[j]]*(i+5)*(j+5)
rxy = sum
print('La correlacion es: ', rxy)

#Covarianza.
sum = 0
for i in range(0,11):
    for j in range(0,21):
        sum = sum+(data.iloc[i][names[j]])*(i+5-param0[0])*(j+5-param1[0])
cov = sum
print('La covarianza es: ', cov)

#Coeficiente de correlación.
cor = (cov)/(param0[1]*param1[1])
print('El coeficiente de correlación es: ', cor)


# In[ ]:





# In[ ]:




