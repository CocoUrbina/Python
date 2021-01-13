library(dplyr)
library(openxlsx)
library(ggplot2)
library(readxl)
options(scipen= 999)

data <- read_excel("C:/Users/pmontenegro/Desktop/PruebaTécnicaCD.xlsx")


#glimpse(data)
#table(data$`Desc Pais`)

data <- data %>% 
    mutate(val_num_dolar= ifelse(`Desc Pais`=="Costa Rica",`Valor Numeral`/601,
                          ifelse(`Desc Pais`=="El Salvador",`Valor Numeral`,
                          ifelse(`Desc Pais`=="Guatemala",`Valor Numeral`/7.58,
                          ifelse(`Desc Pais`=="Honduras",`Valor Numeral`/24.3522,
                          ifelse(`Desc Pais`=="Nicaragua",`Valor Numeral`/34.27,
                          ifelse(`Desc Pais`=="Panamá",`Valor Numeral`,"error"))))))) %>%
    mutate(val_num_dolar= as.numeric(val_num_dolar)) %>% 
    mutate(rangos= ifelse(val_num_dolar<0, "Menor $0",
                   ifelse(val_num_dolar>=0 & val_num_dolar< 5000, "$0 a $5K",
                   ifelse(val_num_dolar>=5000 & val_num_dolar< 50000, "$5K a $50K",
                   ifelse(val_num_dolar>=50000 & val_num_dolar< 100000, "$50K a $100K",
                   ifelse(val_num_dolar>=100000 & val_num_dolar< 500000, "$100K a $500K",
                   ifelse(val_num_dolar>=500000,"Más de $500K","otro")))))))

# table(data$val_num_dolar)
# table(data$rangos)


medidas <- data %>% 
    group_by(`Desc Pais`) %>% 
    summarise(Promedio= mean(val_num_dolar, na.rm = TRUE),
              Varianza= var(val_num_dolar),
              Mediana= median(val_num_dolar, na.rm = TRUE),
              sd= sd(val_num_dolar),
              Minimo= min(val_num_dolar),
              Maximo= max(val_num_dolar))
                              

