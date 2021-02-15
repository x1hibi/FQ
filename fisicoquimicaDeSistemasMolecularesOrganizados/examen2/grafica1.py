#import matplot
import matplotlib.pyplot as plt
import math as m
import numpy as np

#FSMO Parameters
H=[390,250]
Cp=[3,6]
Tm=[330,340]
S=[H[0]/Tm[0],H[1]/Tm[1]]
size=250
R=8.31446261815324
#Define a matrix with values of G
G_unf=np.zeros((2,size))
#Define a matrix with values of H
H_unf=np.zeros((2,size))
#Define a matrix with values of H
TS_unf=np.zeros((2,size))
#Definen the fraction mol for unfolded protein
X_unf=np.zeros((2,size))
#Definen the fraction mol for unfolded protein
X_fold=np.zeros((2,size))


#Defnie a temperature intera
T=range(110,360)
#Define x axis
x=np.zeros(size)



# Iterare over T array to calculte G for the two proteins
for i in range(2):
    for j in range(size):
        # Ecuation for curve of stabilization 
        G_i=H[i]*(1-(T[j]/Tm[i]))-Cp[i]*(Tm[i]-T[j]+T[j]*np.log(T[j]/Tm[i]))
        # Add each value of G
        G_unf[i][j]=G_i

        # Ecuation for curve of stabilization 
        H_i=H[i]+Cp[i]*(T[j]-Tm[i])
        # Add each value of G
        H_unf[i][j]=H_i

        # Ecuation for curve of stabilization 
        TS_i=(S[i]+Cp[i]*np.log(T[j]/Tm[i]))*T[j]
        # Add each value of G
        TS_unf[i][j]=TS_i

        # Ecuation for fraction mol of unfolded
        expG=np.exp(-(G_i*1000)/(R*T[j]))
        X_i=expG/(1+expG)
        # Add each value of G
        X_unf[i][j]=X_i

        # Ecuation for fraction mol of folded
        X_fold[i][j]=1-X_i




print(X_unf[0])
print(np.exp(1))

# FSMO-1
plt.plot(T,G_unf[0],label="$\Delta G_{unf}$")
# FSMO-2
# plt.plot(T,G_unf[1])

# # FSMO-1 H_unf
plt.plot(T,H_unf[0],label="$\Delta H_{unf}$")
plt.plot(T,TS_unf[0],label="$\Delta TS_{unf}$")

# # FSMO-2 H_unf
# plt.plot(T,H_unf[1])
# plt.plot(T,TS_unf[1])

# # FSMO-1 X_unf
# plt.plot(T,X_unf[0],color="black")
# plt.plot(T,X_fold[0],color="yellow")

# # FSMO-2 X_unf
# plt.plot(T,X_unf[1],color="red")
# plt.plot(T,X_fold[1],color="blue")



## Rectas de Tm, Ts y Th FSMO-2
plt.plot([130.2,130.2],[-10,70],"--",label="$T_{m'}$")
plt.plot([330,330],[-10,70],"--",label="$T_{m}$")
plt.plot([200,200],[-10,70],"--",label="$T_{H}$")
plt.plot([222.6,222.6],[-10,70],"--",label="$T_{S}$")


## Rectas de Tm, Ts y Th FSMO-1
# plt.plot([263.2,263.2],[-5,17],"--",label="$T_{m'}$")
# plt.plot([340,340],[-5,17],"--",label="$T_{m}$")
# plt.plot([298.3,298.3],[-5,17],"--",label="$T_H$")
# plt.plot([300.7,300.7],[-5,17],"--",label="$T_S$")



# plot configuration style
plt.plot(T,x,'--',color="black")
plt.grid(True)
plt.title("Curva de estabilidad termodinámica de FSMO-1")
plt.xlim(120,350)
plt.ylim(-10,70)
plt.xlabel("T (K)")
plt.ylabel("$\Delta G$ (kJ/mol)")
plt.legend( loc=1)
plt.show()
