# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 14:39:05 2021

@author: Pmontenegro
"""

# importar datos
#pip install hdbcli
### python -m pip install -U https://github.com/pypa/pip/archive/master.zip
#import pip
#pip3 install -U scikit-learn scipy matplotlib
#from hdbcli import dbapi
#python -m pip install --upgrade pip


import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import stats
import logging 
import warnings 
import os
import sys
print(sys.version)

# import sklearn

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from time import time
from operator import itemgetter 

# from sklearn import cross_validation
# from sklearn.grid_search import GridSearchCV
# from operator import itemgetter 


# warnings.filterwarnings("ignore", category= DeprecationWargning)

# Connection 

# connection = dbapi.connect(
#         address= "zeus.hana",
#         port= 21172,
#         encrypt= "true",
#         user= "pmontenegro",
#         password= "xxxx.xxxx")

# SQL

import pyodbc

# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
#driver={ODBC Driver 13 for SQL Server};server=AUSTRIA;database=PS-ODB;trusted_connection=yes
# server = 'AUSTRIA' 
#database = 'PS-ODB' 
#driver= '{ODBC Driver 13 for SQL Server}'

# cnxn = pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};Server='+server+';Database='+database+';Trusted_Connection=yes;')
# cnxn = pyodbc.connect('driver={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;)
# cursor = cnxn.cursor()

# Mysql, ORACLE, postgress, others

# pip install pymysql
# pip install mysqlclient
# !pip install pymysql

import pymysql

# Open database connection


#pconn <-
#  dbConnect(
#    RMySQL::MySQL(),
#    host = "prod-mysql-v1.cphh6upl16cf.us-east-1.rds.amazonaws.com",
#    user = "admin",
#    password = "rq6H%Mcey`^)H+2oWXeB{V",
#    port = 3306
#  )

# from mysqlclient import MySQLdb

#db = MySQLdb.connect(user="my-username",passwd="my-password",host="localhost",db="my-databasename")
#cursor = db.cursor()
#cursor.execute("SELECT * from my-table-name")
#data=cursor.fetchall()
#for row in data :
#    print (row)
#db.close()


#db = pymysql.connect("prod-mysql-v1.cphh6upl16cf.us-east-1.rds.amazonaws.com","admin","rq6H%Mcey`^)H+2oWXeB{V","3306" )
# prepare a cursor object using cursor() method
#cursor = db.cursor()

# execute SQL query using execute() method.

# cursor.execute('SELECT * FROM [PS-ODB].[dbo].[v_SPServicePayment]')

## Print results

for row in cursor:
    print(row)

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : %s " % data)
# disconnect from server
db.close()

print(1+1)
prueba = pd.read_sql_query('SELECT * FROM [PS-ODB].[dbo].[v_SPServicePayment]',cnxn)

prueba = pd.read_sql_query('SELECT * FROM db', connection)

#information

print("Information General")
prueba.info()
print("headers")
prueba.head()
print("data types")
prueba.dtypes

prueba.describe(include= "all")

print("Missing Values")
print(prueba.isnull.sum(), "\n")



fig, axes = plt.subplots(len(prueba.colums)//3, figsize =(12,48))

i = 0
for triaxis in axes:
    for axes in triaxis:
        prueba.hist(column= prueba.columns[i], bins = 100, ax= axis)
        i = i+1