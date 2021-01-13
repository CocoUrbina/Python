#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 14:08:02 2018

@author: oldemarrodriguez
"""

# Se debe instalar el paquete "mglearn" con -> pip install mglearn

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from   math import pi
# Import the dendrogram function and the ward clustering function from SciPy
from scipy.cluster.hierarchy import dendrogram, ward, linkage, fcluster
from scipy.spatial.distance import pdist



# Ejemplo 1. Datos de Estudiantes

os.chdir("/Users/oldemarrodriguez/Google Drive/MDCurso/Datos")
print(os.getcwd())
datos = pd.read_csv('EjemploEstudiantes.csv',delimiter=';',decimal=",",index_col=0)
print(datos)
datos.head()
datos.shape

# Agregación de:
# Declara instancias de la clase ward
ward_res = ward(datos)         


# Plotea el dendograma
plt.figure(figsize=(13,10))
dendrogram(ward_res,labels= datos.index.tolist())


# Agrega cortes con 2 y 3 clústeres
ax = plt.gca()
limites = ax.get_xbound()
ax.plot(limites, [7.25, 7.25], '--', c='k')
ax.plot(limites, [4, 4], '--', c='k')

ax.text(limites[1], 7.25, ' dos clústeres', va='center', fontdict={'size': 15})
ax.text(limites[1], 4, ' tres clústeres', va='center', fontdict={'size': 15})
plt.xlabel("Orden en el eje X")
plt.ylabel("Distancia o Agregación")

# Interpretación 
def centroide(num_cluster, datos, clusters):
  ind = clusters == num_cluster
  return(pd.DataFrame(datos[ind].mean()).T)


grupos = fcluster(linkage(pdist(datos), method='ward'),3,criterion='maxclust')
centros = np.array(pd.concat([centroide(1,datos,grupos),centroide(2,datos,grupos),centroide(3,datos,grupos)]))


# RADAR PLOT para interpretar
# ===========================
centros_trans = centros.T
centros_trans

df = pd.DataFrame()
for i in range(datos.shape[1]):
    df = pd.concat([df,pd.DataFrame({datos.columns[i]:centros_trans[i,:].tolist()})],axis = 1)

df =  pd.concat([df,pd.DataFrame({'grupo': ['Cluster-1','Cluster-2','Cluster-3']})],axis = 1)
df

# Variables y Número de Variables
variables=list(df)[0:5]
variables
N = len(variables)
N
 
# Ángulo de los ejes 
angulos = [n / float(N) * 2 * pi for n in range(N)]
angulos+= angulos[:1]
 
# Inicializa el Radar
ax = plt.subplot(111, polar=True)
 
# En primer eje en la parte de arriba
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)
 
# Dibuja los ejes por variables + las etiquetas
plt.xticks(angulos[:-1], variables)
 
# Dibuja las etiquetas en Y
ax.set_rlabel_position(0)
plt.yticks([1,2,3,4,5,6,7,8,9,10], ["1","2","3","4","5","6","7","8","9","10"], color="grey", size=7)
plt.ylim(0,10)
 
# Plotea cada cluster (grupo) = una línea de datos
 
# Cluster 1
valores=df.loc[0].drop('grupo').values.flatten().tolist()
valores += valores[:1]
ax.plot(angulos, valores, linewidth=1, linestyle='solid', label="Cluster-1")
ax.fill(angulos, valores, 'b', alpha=0.1)
 
# Cluster 2
valores=df.loc[1].drop('grupo').values.flatten().tolist()
valores += valores[:1]
ax.plot(angulos, valores, linewidth=1, linestyle='solid', label="Cluster-2")
ax.fill(angulos, valores, 'r', alpha=0.1)
 
# Cluster 3
valores=df.loc[2].drop('grupo').values.flatten().tolist()
valores += valores[:1]
ax.plot(angulos, valores, linewidth=1, linestyle='solid', label="Cluster-3")
ax.fill(angulos, valores, 'b', alpha=0.1)
 
# Agrega la leyenda
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))