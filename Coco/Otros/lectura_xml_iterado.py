# -*- coding: utf-8 -*-
'''
Created on Tue Apr 18 17:09:05 2017

@author: rcastrillo

Programa para lectura de los XML de SUGEF. Utiliza iterparse para disminuir el
uso de memoria y  toma en cuenta listas. Utiliza pandas para generar csv

'''
# Indicar tipo de tabla que se quiere convertir a CSV y ubicación de escritura
# (PATH) y ubicación de archivos de muestra de SUGEF con estructura 
# (PATH_ESTRUCTURA)
TABLA = 'Crediticio_CuotasAtrasadas'
PATH = 'C:/Users/Public/Documents/Probabilidad de mora/Datos originales/Datos XML/' + TABLA + '/'
PATH_ESTRUCTURA = 'C:/Users/Public/Documents/Probabilidad de mora/Datos originales/Datos XML/Estructura XML/' + TABLA + '.xml'

import xml.etree.ElementTree as ET
import glob
import re
import pandas as pd

#%% Lectura de archivos de carpeta SUGEF XML/CREDITICIO. 

# El acceso debe ser solicitado de previo.
base_path = '//10.255.255.207/sugef xml/CREDITICIO'
files = [file for file in glob.glob(base_path + '/**/*.xml', recursive = True)]

#%% Funciones para leer los datos 

# Función para extraer datos de sublistas
def lectura_listas(node):
    val = ''
    for elem in node:
        if val != '': 
            val +='|'
        for child in elem:
            if val == '' or val[-1] == '|':
                val = val + str(child.tag) + ':' + str(child.text)
            else:
                val = val + '_' + str(child.tag) + ':' + str(child.text) 
    return val

def leer_xml(file, estructura):
    context = ET.iterparse(file, events = ('start', 'end')) 
    vals = []
    for event, elem in context:
        if event == 'end' and elem.tag == 'Encabezado':
            fecha = elem[4].text
        elif event == 'end' and elem.tag == 'Registro':
            datos = dict.fromkeys(estructura, '')
            datos['Fecha_XML'] = fecha
            for child in elem:
                if bool(re.search('^Lista', child.tag)):
                    datos[child.tag] = lectura_listas(child)
                else:
                    datos[child.tag] = child.text
            vals.append(datos)
            elem.clear()
            
    fecha = re.sub(pattern = "/", repl = "_", string = fecha)
    return vals, fecha

# Función para obtener estructura de XML de muestras otorgadas por SUGEF
def conseguirEstructura(path):
    estructura = []
    tree = ET.parse(path)
    root = tree.getroot()
    for elem in root[1][0]:
        estructura.append(elem.tag)
    return estructura


#%% Lectura de datos y conversión a CSV

estructura = conseguirEstructura(PATH_ESTRUCTURA)

for file in files:
    if re.findall(pattern = TABLA + '.xml', string = file):
        print('Parsing file: ', file, '\n')
        vals, fecha = leer_xml(file, estructura)
        df = pd.DataFrame(vals)
        csv_path = PATH + TABLA + '_' + fecha + '.csv'
        df.to_csv(csv_path, index_label = 'idx')
        
