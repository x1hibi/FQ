#import matplot
import matplotlib.pyplot as plt 
import math as m
import numpy as np 
import pandas as pd
import csv


size=20000
# jK-1
kb=1.3806488E-23
# energy in J of 
e=1E-20
T=range(1,size+1)
N=6.023E23

q=np.zeros(size)
x=np.zeros(size)

f=np.zeros(size)
E=np.zeros(size)

for i in range(size):
    x_i=e/(kb*T[i])
    ### two levels
    # q_i=1+np.exp(-x_i)
    #q_i=1+2*np.exp(-x_i)+3*np.exp(-2*x_i)
    #q[i]=q_i
    x[i]=1/x_i


    #E[i]=(-e*N*(np.exp(-1*x_i)+4*np.exp(-2*x_i)+9*np.exp(-3*x_i)))/(np.exp(-1*x_i)+2*np.exp(-2*x_i)+3*np.exp(-3*x_i))
    f[i]=-kb*T[i]*N*(np.log(np.exp(-1*x_i)+2*np.exp(-2*x_i)+3*np.exp(-3*x_i)))

print(f)

property=f
propertyName="Internal Energy"
propertyName="Heltmotz Energy"

titleName=propertyName+" vs kbt/e"

plt.plot(x,property)
#plt.plot(x,q)
# # plot configuration style
plt.grid(True)
plt.title(titleName)
# # plt.legend(loc=1, borderaxespad=1)
#plt.xlim(0,10)
#plt.ylim(1,3)
plt.ylabel(propertyName)
plt.xlabel("$k_bT/\epsilon$")
plt.show()
