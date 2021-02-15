import numpy as np

e=2E-20

n=6.023E23


kb=1.380649E-23

T=range(1000)

U=np.zeros(len(T))

u=2000
#T=-e/(kb*np.log((3*u)/(2*n*e-2*u)))
T=-e/(kb*np.log((2*u)/(3*n*e-3*u)))

print("T",T)

print("all ok")
