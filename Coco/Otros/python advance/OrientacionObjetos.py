#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 15:20:00 2018

@author: oldemarrodriguez
"""

# Clase vacía
class Punto:
    pass

p1 = Punto()
p2 = Punto()
p1.x = 5
p1.y = 4
p2.x = 3
p2.y = 6
print(p1.x, p1.y)
print(p2.x, p2.y)

# Método resetear traslada un punto al origen
# Aquí se declaran de forma implícita dos atributos
class Punto:
    def resetear(self):
        self.x = 0
        self.y = 0

p = Punto()
p.x = 5
p.y = 4
print(p.x, p.y)       
p.resetear()
print(p.x, p.y)

import math

# Clase Punto
class Punto:
    def __init__(self, x = 0, y = 0): # Constructor
        self.x = x
        self.y = y      
    def cambiar(self, x, y):
        self.x = x
        self.y = y
    def inicializar(self):
        self.cambiar(0, 0)
    def calcular_distancia(self, otro_Punto):
        return math.sqrt(
                (self.x - otro_Punto.x)**2 +
                (self.y - otro_Punto.y)**2)


# ¿Cómo usarla?
Punto1 = Punto(2,3)
Punto2 = Punto(-2,9)
print(Punto1.x)
print(Punto1.y)
print(Punto2.x)
print(Punto2.y)

Punto1.inicializar()
Punto2.cambiar(5,0)
print(Punto1.x)
print(Punto1.y)
print(Punto2.x)
print(Punto2.y)
print(Punto2.calcular_distancia(Punto1))
Punto1.cambiar(3,4)
print(Punto1.calcular_distancia(Punto2))
print(Punto1.calcular_distancia(Punto1))

Punto3 = Punto() # Se invoca el constructor
print(Punto3.x)
print(Punto3.y)


# Ejemplo de conducta de clase
class Perro():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad        
    def sentarse(self):
        print(self.nombre.title() + " está ahora sentado.")
    def levantarse(self):
        print(self.nombre.title() + " se levantó!")
        

mi_Perro = Perro('Puppy', 14)
su_Perro = Perro('Negro', 3)

print("El nombre de mi perro es " + mi_Perro.nombre.title() + ".")
print("Mi perro tiene " + str(mi_Perro.edad) + " de edad.")
mi_Perro.sentarse()

print("El nombre de su perro es " + su_Perro.nombre.title() + ".")
print("Su perro tiene " + str(su_Perro.edad) + " de edad.")
su_Perro.sentarse()

mi_Perro.levantarse()
su_Perro.levantarse()

# HERENCIA y Relaciones de Componente-Compuesto
class Bateria():
    def __init__(self, capacidad = 70, marca = "LTH"):
        self.capacidad = capacidad
        self.marca = marca
    def describe(self):
        print("Este carro tiene una batería marca " + self.marca + " de capacidad " + str(self.capacidad) + "-kWh.")

mi_bateria = Bateria(90, "Hitachi")
mi_bateria.describe()

# Clase Base
class Carro():
    def __init__(self, fabricante, modelo, anno):
        self.fabricante = fabricante
        self.modelo = modelo
        self.anno = anno
        self.kilometraje = 0       
    def obtener_nombre_completo(self):
        nombre_completo = self.fabricante + ' ' + str(self.anno) + ' ' + self.modelo
        return nombre_completo.title()   
    def lee_kilometraje(self):
        print("Este carro tiene " + str(self.kilometraje) + " kilometros recorridos.")      
    def modifica_kilometraje(self, kilometros):
        if kilometros >= self.kilometraje:
            self.kilometraje = kilometros
        else:
            print("Usted no puede modificar para atrás el kilometraje!")
    def incrementa_kilometraje(self, kilometros):
        self.kilometraje += kilometros

# Clase derivada o clase hija, tiene el carro y otra cosa que son otro objetos como la bateria
class Carro_Electrico(Carro):
    def __init__(self, fabricante, modelo, anno, capacidad_bateria, marca_bateria):
        super().__init__(fabricante, modelo, anno)
        self.bateria = Bateria(capacidad_bateria, marca_bateria)        
        
mi_tesla = Carro_Electrico('tesla', 'modelo S', 2018, 65, "Hitachi")
print(mi_tesla.obtener_nombre_completo())
mi_tesla.bateria.describe()

# Encapsulación en Python
# Atributos y Métodos privados
# Métodos GETTERS AND SETTERS (Obtener y Modificar)

class Prueba(object):
        def __init__(self):
            self.__dato = 1
        @property
        def dato(self):
            print("Pasó por obtener")
            return self.__dato
        @dato.setter
        def dato(self, nuevo_dato):
            print("Pasó por modificar")
            if nuevo_dato > 100:
                raise ValueError("El dato debe ser menor o igual a 100")
            self.__dato = nuevo_dato
 
tempo = Prueba()
tempo.dato

tempo.dato = 3
tempo.dato
tempo.dato = 200 # Da error controlado

# MÉTODOS PRIVADOS
# Los métodos pueden hacerse privados de la misma manera, 
# nombrándolos con dos guiones bajos principales y sin guiones bajos posteriores.
# Un método privado se puede usar solamente dentro de otro método de la misma clase.
# Versión Usando property al verdadero estilo Python

class Celsius:
    def __init__(self, temperatura = 0):
        self.__temperatura = temperatura
    def convierte_fahrenheit(self):
        return (self.temperatura * 1.8) + 32
    @property
    def temperatura(self):
        print("Obteniendo el valor")
        return self.__temperatura
    @temperatura.setter
    def temperatura(self, nuevo_valor):
        if nuevo_valor < -273:
            raise ValueError("Una temperatura por debajo de -273 no es posible")
        print("Retornando el valor")
        self.__temperatura = nuevo_valor

c = Celsius()
c.temperatura
c.temperatura = 37
c.temperatura
c.convierte_fahrenheit()

# EJEMPLO: Mi propio Data Frame usando Componente-Compuesto 

import pandas as pd
import numpy as np

class mi_DF():
    def __init__(self, DF = pd.DataFrame()):
        self.__num_filas = DF.shape[0]
        self.__num_columnas = DF.shape[1]
        self.__DF = DF
    @property
    def num_filas(self):
        return self.__num_filas
    @property
    def num_columnas(self):
        return self.__num_columnas
    @property
    def DF(self):
        return self.__DF  
    def maximo(self):
        max = self.DF.iloc[0,0]
        for i in range(self.num_filas):
            for j in range(self.num_columnas):
                if self.DF.iloc[i,j] > max:
                    max = self.DF.iloc[i,j]
        return max
    def valores(self):
        min = self.DF.iloc[0,0]
        max = self.DF.iloc[0,0]
        total_ceros = 0
        total_pares = 0
        for i in range(self.num_filas):
            for j in range(self.num_columnas):
                if self.DF.iloc[i,j] > max:
                    max = self.DF.iloc[i,j]
                if self.DF.iloc[i,j] < min:
                    min = self.DF.iloc[i,j]
                if self.DF.iloc[i,j] == 0:
                    total_ceros = total_ceros+1
                if self.DF.iloc[i,j] % 2 == 0:
                    total_pares = total_pares+1
        return {'Maximo' : max, 'Minimo' : min, 'Total_Ceros' : total_ceros, 'Pares' : total_pares}
    def estadisticas(self,nc):
        media = np.mean(self.DF.iloc[:,nc])
        mediana = np.median(self.DF.iloc[:,nc])
        deviacion = np.std(self.DF.iloc[:,nc])
        varianza = np.var(self.DF.iloc[:,nc])
        maximo = np.max(self.DF.iloc[:,nc])
        minimo = np.min(self.DF.iloc[:,nc])
        return {'Variable' : self.DF.columns.values[nc],
                'Media' : media,
                'Mediana' : mediana,
                'DesEst' : deviacion,
                'Varianza' : varianza,
                'Maximo' : maximo,
                'Minimo' : minimo}
      

datos = mi_DF(pd.DataFrame([[4,1,-3],[2,4.4,0],[-5,9,198],[2,4,-5]]))
print(datos.num_filas)
print(datos.num_columnas)
print(datos.DF)
print(datos.maximo())
print(datos.valores())
print(datos.estadisticas(1))

import pandas as pd
import os

# Cambia la carpeta de trabajo
os.chdir("/Users/oldemarrodriguez/Google Drive/MDCurso/Datos")
print(os.getcwd())

# Leyendo un archivo CSV
datos_est = pd.read_csv('EjemploEstudiantes.csv',delimiter=';',decimal=",",index_col=0)
datos = mi_DF(datos_est)
print(datos.num_filas)
print(datos.num_columnas)
print(datos.DF)
print(datos.maximo())
print(datos.valores())
print(datos.estadisticas(3))