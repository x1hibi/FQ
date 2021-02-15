#import matploy library
import matplotlib.pyplot as plt
import numpy as np
import math as m


pka=9.95

size=141

ph=np.linspace(0,14,size)

a0=np.zeros(size)
a1=np.zeros(size)

for i in range(size):
    a0_i=(10**-ph[i])/(10**-ph[i]+10**-pka)
    a1_i=(10**-pka)/(10**-ph[i]+10**-pka)
    a0[i]=a0_i
    a1[i]=a1_i
    print(ph[i],a0_i,a1_i)

x=0.002810461973210197
x2=0.9971895380267898



#make plot 
plt.plot([pka,pka],[0,1.1],"--",label="$pka$")
plt.plot([0,14],[x,x],"--",label="$\chi_{A^-}=0.002810$")
plt.plot([0,14],[x2,x2],"--",label="$\chi_{HA}=0.997189$")
plt.plot(ph,a0,label="$HA$")
plt.plot(ph,a1,label="$A^-$")
# # settings of box label postion 
plt.legend(loc=6, borderaxespad=1)
plt.grid(True)
plt.xlim(-0,14)
plt.ylim(-0.1,1.1)
# # show in script plot
plt.show()
