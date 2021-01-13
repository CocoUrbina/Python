####Función para corregir el problema de effects que tiene R


library(foreign)
library(car)
library(mlogit)

##setwd("C:/Users/Usuario/Documents/Gilbert/Documents/Documents/I Semestre 2016/categóricos 2016/05. Escogencia Discreta/")

setwd("L:/categóricos 2016/05. Escogencia Discreta/")




restaurant=as.data.frame(read.dta(file="restaurant.dta"))


####Logistica simple

rest=mlogit.data(restaurant,shape="long",choice="chosen", alt.var="restaurant", id.var="family_id")

summary(rest)

m1=mlogit(chosen~cost+rating+distance|0, data=rest)
summary(m1)

##Comparar distribuciones de frecuencias con los valores esperados del modelo

apply(fitted(m1,outcome=FALSE),2,mean)
round(cbind(m1$freq/sum(m1$freq),apply(fitted(m1,outcome=FALSE),2,mean)),3)


###El "intercambio" de costo económico por costo por distancia
##Se calcula la razón de ambos coeficientes

coef(m1)[1]/coef(m1)[3]


##La gente está dispuesta a pagar US$1.8 más por cada milla menos que tenga que recorrer


###Calculo de elasticidad

pred=predict(m1,data.frame(cost=tapply(rest$cost,rest$restaurant,mean),rating=tapply(rest$rating,rest$restaurant,mean),distance=tapply(rest$distance,rest$restaurant,mean)))
pred
medias=tapply(rest$cost,rest$restaurant,mean)
medias


elast.cost=m1$coef[1]*medias*(1-pred)
elast.cost



###Evaluar el supuesto de IIA
###Probar quitando cada uno


m1.a=mlogit(chosen~cost+rating+distance|0, data=rest, alt.subset=c("MamasPizza","CafeEccell","LosNortenos","WingsNmore","Christophers","MadCows"))

m1.b=mlogit(chosen~cost+rating+distance|0, data=rest, alt.subset=c("Freebirds","CafeEccell","LosNortenos","WingsNmore","Christophers","MadCows"))

m1.c=mlogit(chosen~cost+rating+distance|0, data=rest, alt.subset=c("Freebirds","MamasPizza","LosNortenos","WingsNmore","Christophers","MadCows"))

m1.d=mlogit(chosen~cost+rating+distance|0, data=rest, alt.subset=c("Freebirds","MamasPizza","CafeEccell","WingsNmore","Christophers","MadCows"))

m1.e=mlogit(chosen~cost+rating+distance|0, data=rest, alt.subset=c("Freebirds","MamasPizza","CafeEccell","LosNortenos","Christophers","MadCows"))

m1.f=mlogit(chosen~cost+rating+distance|0, data=rest, alt.subset=c("Freebirds","MamasPizza","CafeEccell","LosNortenos","WingsNmore","MadCows"))

m1.g=mlogit(chosen~cost+rating+distance|0, data=rest, alt.subset=c("Freebirds","MamasPizza","CafeEccell","LosNortenos","WingsNmore","Christophers"))

hmftest(m1,m1.a)
hmftest(m1,m1.b)
hmftest(m1,m1.c)
hmftest(m1,m1.d)
hmftest(m1,m1.e)
hmftest(m1,m1.f)
hmftest(m1,m1.g)





###Modelo con constantes para cada alternativa


m2=mlogit(chosen~cost+distance,data=rest, reflevel="MadCows")
summary(m2)

##Comparar distribuciones de frecuencias con los valores esperados del modelo

apply(fitted(m2,outcome=FALSE),2,mean)
round(cbind(m2$freq/sum(m2$freq),apply(fitted(m2,outcome=FALSE),2,mean)),3)

###Nótese que las frecuencisa esperadas y observadas son exactamente las mismas
###Por haber incluido una constante por cada categoría.

###Nótese que también hubo que excluir la variable rating, por colinealidad perfecta


###El "intercambio" de costo económico por costo por distancia

coef(m2)[1]/coef(m2)[3]

###Calculo de elasticidad


pred=predict(m2,data.frame(cost=tapply(rest$cost,rest$restaurant,mean),rating=tapply(rest$rating,rest$restaurant,mean),distance=tapply(rest$distance,rest$restaurant,mean)))
pred

###REVISAR
elast.cost=m2$coef[1]*medias*(1-pred)
elast.cost

###Estas elasticidades no tienen lógica


###MODELO CON INTERACCIONES CON VARIABLES INDIVIDUALES

##La lógica sería interactuar ingreso con costo
##Una forma elegante es dividir el costo entre el ingreso, 
###por lo que se interpretaría como costo por ingreso disponible
###Además, se interpretaría como una relación inversa entre ingreso y selección de restaurante


m3=mlogit(chosen~cost+distance+rating+I(cost/income)|0,data=rest, reflevel="MadCows")
summary(m3)


###Otro modelo similar


m4=mlogit(chosen~distance+rating+I(cost/income)|0,data=rest)
summary(m4)

###Comparar coeficientes

cbind(coef(m4),coef(m1))



###Otro modelo con interacción en las constantes

m5=mlogit(chosen~distance+cost|income,data=rest, reflevel="MadCows")
summary(m5)


###Como casi todos los coeficientes de las interacciones son significativos
###entonces, cuanto mayor es el ingreso, menor la probabilidad de escoger
###cualquiera de las alternativas sobre MadCows (excepto quizá Christopher´s)

###Una prueba de razón de verosimilitudes confirma la importancia de las interacciones

lrtest(m2,m5)



###MODELO ANIDADO

###Se tienen las siguientes categorías de restaurantes:

###Baratos: Freebirds y MamasPizza
###Especializados: CafeEccell, Los Nortenos, WingsNMore
###Caros: Christophers y MadCows

m10=mlogit(chosen~cost+rating+distance|0, data=rest, nests=list(baratos=c('Freebirds','MamasPizza'),especial=c('CafeEccell','LosNortenos','WingsNmore'),caros=c('Christophers','MadCows')),un.nest.el=TRUE)
summary(m10)

###Noten la prueba de hipótesis para la "variable" iv.  Este es el lambda del que hablábamos

###Comparando valores predichos

round(cbind(m10$freq/sum(m10$freq),apply(fitted(m10,outcome=FALSE),2,mean)),3)

###Vean como los predichos por el anidado son más parecidos a la realidad.

###Ahora un anidado con interacciones con los nidos

rest$baratos=(rest$restaurant=='Freebirds' | rest$restaurant=='MamasPizza')
rest$especial=(rest$restaurant=='CafeEccell' | rest$restaurant=='LosNortenos' | rest$restaurant=='WingsNMore')
rest$caros=(rest$restaurant=='Christophers' | rest$restaurant=='MadCows')


rest$inc.baratos=0
rest$inc.especial=0
rest$inc.caros=0

rest$inc.baratos[rest$baratos==1]=rest$income[rest$baratos==1]
rest$inc.especial[rest$especial==1]=rest$income[rest$especial==1]
rest$inc.caros[rest$caros==1]=rest$income[rest$caros==1]

m11=mlogit(chosen~cost+rating+distance+inc.baratos+inc.especial+inc.caros|0, data=rest, nests=list(baratos=c('Freebirds','MamasPizza'),especial=c('CafeEccell','LosNortenos','WingsNmore'),caros=c('Christophers','MadCows')),un.nest.el=TRUE)
summary(m11)



####PROBIT MULTINOMIAL

###Todavía no me corre y no sé por qué no?  Creo que 

m20=mlogit(chosen~cost+distance, data=rest,seed=20,  R=100, probit=TRUE, start=c(m1$coef[1],m1$coef[3]))
summary(m20)








