# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 09:14:08 2017

@author: rcastrillo
"""
import glob

path = r'C:\Users\Public\Documents\Probabilidad de mora\Datos originales\Datos XML\Crediticio_OperacionesDirectasIndirectas'

files = glob.glob(path + r'\**\*.csv', recursive = True)

first = True

newfile = path + r'\Crediticio_OperacionesDirectasIndirectas_todos.csv'
i = 0
total = len(files)

fout = open(newfile, 'a')

for line in open(files[0]):
    fout.write(line)

for file in files[1:]:
    f = open(file)
    next(f)
    for line in f:
        fout.write(line)
    f.close()

fout.close()


