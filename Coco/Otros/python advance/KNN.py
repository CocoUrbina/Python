#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 11:20:54 2018

@author: oldemarrodriguez
"""

# Paquetes necesarios
import os
import pandas as pd
import numpy as np
import mglearn
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix

# Los K Vecinos Más Cercanos - KNN Method

# Ilustración del KNN
mglearn.plots.plot_knn_classification(n_neighbors=1)
mglearn.plots.plot_knn_classification(n_neighbors=3)

# Índices de Calidad del Modelo
# Índices para matrices NxN

def indices_general(MC, nombres = None):
    precision_global = np.sum(MC.diagonal()) / np.sum(MC)
    error_global = 1 - precision_global
    presicion_categoria  = pd.DataFrame(MC.diagonal()/np.sum(MC,axis = 1)).T
    if nombres!=None:
        presicion_categoria.columns = nombres
    return {"Matriz de Confusion":MC, 
            "Precision Global":precision_global, 
            "Error Global":error_global, 
            "Precisión por categoria":presicion_categoria}

# Ejemplo 1. Datos de Iris

os.chdir("/Users/oldemarrodriguez/Google Drive/MDCurso/Datos")
print(os.getcwd())
datos = pd.read_csv('iris.csv',delimiter=';',decimal=".")
datos.shape
datos.head()
datos.info()

# Elimina la variable catégorica, deja las variables predictoras en X
X = datos.iloc[:,:4] 
X.head()
# Deja la variable a predecir en y
y = datos.iloc[:,4:5] 
y.head()

# Con el 70% de los datos para entrenamiento
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=0)
# Mediante el cosntructor inicializa el atributo n_neighbors=3
instancia_knn = KNeighborsClassifier(n_neighbors=3)
# Entrena el modelo llamando al método fit
# Observe que no hay variable que guarde el modelo como en R
# Esto se debe a que al ser Python orientado a Objetos,
# el modelo queda en un atributo de la instancia "instancia_knn"
instancia_knn.fit(X_train,y_train)

# Imprime las predicciones en testing
print("Las predicciones en Testing son: {}".format(instancia_knn.predict(X_test)))
# Porcentaje de predicción global
print("Precisión en Testing: {:.2f}".format(instancia_knn.score(X_test, y_test)))
# Matriz de confusión
prediccion = instancia_knn.predict(X_test)
MC = confusion_matrix(y_test, prediccion)
print("Matriz de Confusión:\n{}".format(MC))

indices = indices_general(MC,list(np.unique(y)))

for k in indices:
    print("\n%s:\n%s"%(k,str(indices[k])))

# Ejemplo 3. Scoring de Crédito

os.chdir("/Users/oldemarrodriguez/Google Drive/MDCurso/Datos")
print(os.getcwd())
datos = pd.read_csv('MuestraCredito5000.csv',delimiter=';',decimal=".")
datos.shape
datos.head()
datos.info()
# Está tomando erroneamente los datos como numéricos
# En este caso se deben convertir a variables ccategóricas
# porque en realidad estos numéros son códigos
# NO es que siempre se deban convertir las variables numéricas a categórica 
datos['MontoCredito'] = datos['MontoCredito'].astype('category')
datos['IngresoNeto'] = datos['IngresoNeto'].astype('category')
datos['CoefCreditoAvaluo'] = datos['CoefCreditoAvaluo'].astype('category')
datos['MontoCuota'] = datos['MontoCuota'].astype('category')
datos['GradoAcademico'] = datos['GradoAcademico'].astype('category')
datos.head()
datos.info()

# Elimina la variable catégorica, deja las variables predictoras en X
X = datos.iloc[:,:5] 
X.head()
# Deja la variable a predecir en y
y = datos.iloc[:,5:6] 
y.head()

# Con el 75% de los datos para entrenamiento
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.75, random_state=0)
# Mediante el constructor inicializa el atributo n_neighbors=3
instancia_knn = KNeighborsClassifier(n_neighbors=3)
# Entrena el modelo llamando al método fit
# Observe que no hay variable que guarde el modelo como en R
# Esto se debe a que al ser Python orientado a Objetos,
# el modelo queda en un atributo de la instancia "instancia_knn"
instancia_knn.fit(X_train,y_train)

# Imprime las predicciones en testing
print("Las predicciones en Testing son: {}".format(instancia_knn.predict(X_test)))
# Porcentaje de predicción global
print("Precisión en Testing: {:.2f}".format(instancia_knn.score(X_test, y_test)))
# Matriz de confusión
prediccion = instancia_knn.predict(X_test)
MC = confusion_matrix(y_test, prediccion)
print("Matriz de Confusión:\n{}".format(MC))

indices = indices_general(MC,list(np.unique(y)))

for k in indices:
    print("\n%s:\n%s"%(k,str(indices[k])))










