import matplotlib.pyplot as plt
import math as m
import numpy as np
energy=500
e=np.linspace(0,energy,energy+1)
p=[]
print("size",len(e))
k=1.38e-23
t=298
kt=k*t
Na=6.022e-23

for i in range(energy+1):
    frac=-e[i]*Na/kt
    exp=m.exp(frac)
    p.append(exp)

plt.title("Boltzman distribution")
plt.grid("true")
plt.xlim(0,energy)
plt.xlabel("Energy")
plt.ylim(0,1)
plt.ylabel("Probability")
plt.plot(e,p)






