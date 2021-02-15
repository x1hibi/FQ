#import matplot
import matplotlib.pyplot as plt 
import math as m
import numpy as np 
import pandas as pd
import csv

# Por medio de excel se consiguieron los parametros de de las líneas de tendencia para la aproximación
# Linea infeior (en forma nativa), esta se calculo tomando el intervalo de 300.05-330.15
# Se obtuvo un coeficiente de correlacion de 0.788

m1=3.19E-4
b1=0.146

# Linea superior (en forma desplegada), esta se calculo tomando el intervalo de 370.05-341.55
# Se obtuvo un coeficiente de correlacion de 0.488

m2=2.37E-4
b2=0.229

results = []

with open("data.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        results.append(row)

psi=np.zeros(len(results))
T=np.zeros(len(results))
rectUnfold=np.zeros(len(results))
rectNative=np.zeros(len(results))
X=np.zeros(len(results))


rectTmX=[[300,370],[0.5,0.5]]
rectTmY=[[339.087,339.087],[0,1]]

lnK=[]
Tinv=[]

sumX=0
sumY=0
sumXY=0
sumXX=0

for i in range(len(results)):
    T[i]=results[i][0]
    psi[i]=results[i][1]
    # Esta fue creada despues de determinar el valor de Tm

    # Construimos la recta inferior 
    rectNative[i]=m1*T[i]+b1
    # Construimos la recta superior
    rectUnfold[i]=m2*T[i]+b2

    # Calculo de fraccion mol 
    X[i]=(psi[i]-rectNative[i])/(rectUnfold[i]-rectNative[i])


    if T[i]>=330 and T[i]<=350 and X[i] > 0 and X[i]<=1:
        # Calculo de la constante de equilibrio
        keq=(X[i])/(1-X[i])
        print("keq",keq)
        print("x",X[i])
        # Se calcula el logaritomo de keq y la temperatura inversa
        lnK.append(np.log(keq))
        Tinv.append(1/T[i])




for i in range(len(lnK)):
    # Se calculan los parametros para calcular la pendiente y la ordenada al origen 
    sumY+=lnK[i]
    sumX+=Tinv[i]
    sumXY+=lnK[i]*Tinv[i]
    sumXX+=Tinv[i]**2

R=8.31446261815324
n=len(lnK)

print(sumY,sumX,sumXY,sumXX)

# Se calcula la pendiente
m=((n*sumXY)-(sumX*sumY))/((n*sumXX)-sumX**2)
b=(sumY-m*sumX)/n

lnk2=[]


for i in range(len(lnK)):
    lnk2.append(m*Tinv[i]+b)


print("m",m,"b",b)

#Se calculan los valores de H y S
H_vh=-m*R
S_vh=b*R
G_vh298=H_vh-298*S_vh

print("H",H_vh,"S",S_vh,"G",G_vh298)




# plt.plot(T,rectNative,"--",label="Recta secmento nativo \n $y_{eq}=3.19E-4*T+0.146$")
# plt.plot(T,rectUnfold,"--",label="Recta secmento desplegado \n $lnK_{eq}=2.37*E-4T+0.229$")
# plt.plot(T,psi)
# plt.plot(T,X)

#Rectas de aproximacion 


plt.plot(Tinv,lnk2,"--",label="$lnK_{eq}=-56900.78T^{-1}+(168.39)$")
plt.plot(Tinv,lnK)
#plt.plot(T,psi,label="$\psi$")
# plt.plot([339.08,339.08],[0,1],"--",label="$T_{m}$")
# plt.plot([290,370],[0.5,0.5],"--",label="$50\%$ de proteína nativa")

# plot configuration style
plt.grid(True)
plt.title("Gráfica de Van't Hoff")
# plt.title("Desplegamiento térmico de la proteína XYZ con aproximaciones")
# plt.legend(loc=1, borderaxespad=1)
# plt.xlim(290,370)
# plt.ylim(-0.1,1.1)
# plt.ylim(0.24,0.32)
plt.legend(loc=1, borderaxespad=1)


# plt.ylabel("$\psi$")    
plt.xlabel("1/T ($K^{-1}$)")
plt.ylabel("$lnK_{eq}$ ($M^{-1}$)")
plt.show()
