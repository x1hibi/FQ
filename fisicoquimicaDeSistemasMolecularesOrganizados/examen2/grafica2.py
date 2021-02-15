#import matplot
import matplotlib.pyplot as plt 
import math as m
import numpy as np 

R=8.31446261815324
T=range(290,320,5)
Keq=np.linspace(1.2,1.7,6)
lnK=np.zeros(6)
Tinv=np.zeros(6)
for i in range(6):
    lnK[i]=np.log(Keq[i]*10**5)
    Tinv[i]=1/T[i]
print(lnK)

sumX=0
sumY=0
sumXY=0
sumXX=0
n=6

# Se hace una regresión lineal 
for i in range(6):
    #sum x,y,xy and x**2
    sumY+=lnK[i]
    sumX+=Tinv[i]
    sumXY+=lnK[i]*Tinv[i]
    sumXX+=Tinv[i]**2

m=((n*sumXY)-(sumX*sumY))/((n*sumXX)-sumX**2)
b=(sumY-m*sumX)/n

H_vh=-m*R
S_vh=b*R
### Solo la energía libre depende de temperatura
G_vh=np.zeros(6)

for i in range(6):
    G_vh[i]=H_vh-T[i]*S_vh

print("m",m,"b",b)

G_vh[i]=H_vh-T[i]*S_vh

print("H",H_vh)
print("S",S_vh)
print("G",G_vh,H_vh-298*S_vh)


# plot configuration style
plt.scatter(Tinv,lnK,label="$lnK_{eq}=-1271.4932T^{-1}+16.0841$")
plt.plot(Tinv,lnK,"--")
plt.grid(True)
plt.title("Gráfico de Van't Hoff")
plt.legend(loc=1, borderaxespad=1)
#plt.xlim(120,350)
# plt.ylim(0,70)
plt.xlabel("1/T ($K^{-1}$)")
plt.ylabel("$lnK_{eq}$ ($M^{-1}$)")
plt.show()
