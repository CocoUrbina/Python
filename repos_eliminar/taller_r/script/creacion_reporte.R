library(openxlsx)
library(tidyverse)
library(data.table)
library(magrittr)
library(lubridate)
library(dplyr)

# leer data table

rpt_porPais <- data.table(read.xlsx('datos/Pais.xlsx'))
dt_Unitedkingdom <- data.table(read.xlsx('datos/Unitedkingdom.xlsx'))
dt_porProducto <- data.table(read.xlsx('datos/Producto.xlsx'))
