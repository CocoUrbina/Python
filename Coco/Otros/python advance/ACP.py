#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 09:44:15 2018

@author: oldemarrodriguez
"""

# ANÁLISIS EN COMPONENTES PRINCIPALES - ACP
# =========================================

import os
import pandas as pd
import prince # Para el ACP



# Ejemplo 1

os.chdir("/Users/oldemarrodriguez/Google Drive/MDCurso/Datos")
print(os.getcwd())
datos = pd.read_csv('EjemploEstudiantes.csv',delimiter=';',decimal=",",index_col=0)
print(datos)
datos.head()
datos.shape

# Declara una instancia de la clase PCA y llama en constructor
instancia_acp = prince.PCA(datos, n_components=4)
instancia_acp.plot_rows(show_labels=True,ellipse_fill=True)
instancia_acp.plot_correlation_circle()
instancia_acp.plot_cumulative_inertia(threshold=0.8)

# Ejemplo 2
iris = pd.read_csv('iris.csv',delimiter=';',decimal=".")
print(iris)
iris.head()
iris.shape

instancia_acp = prince.PCA(iris, n_components=4)
instancia_acp.plot_rows(ellipse_fill=True)
instancia_acp.plot_rows(color_by='tipo',ellipse_fill=True)
instancia_acp.plot_correlation_circle()
instancia_acp.plot_cumulative_inertia(threshold=0.8)

















