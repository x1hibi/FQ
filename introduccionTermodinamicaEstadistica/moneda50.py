#import matploy library
import matplotlib.pyplot as plt
import numpy as np
import math as m

# x axis
nc=[6,12]
# y axis arrays with data of of method for each thermodinamic potenctial 
# Volumen
v=[0.2185531487,0.3778053109]

x=range(50)

y=[]
p=0.5

for i in x:
    # define the combination
    c=m.factorial(50)/(m.factorial(i)*m.factorial(50-i))
    pi=c*(p**i)*((1-p)**(50-i))
    y.append(pi)


#set axis labels and title
plt.xlabel("Tiros")
plt.ylabel("Probabilidad")

#set settings, grid, size a file name 
plt.grid("true")
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
fig.savefig('reactioProfileG.png', dpi=100)
plt.rc('xtick', labelsize=25) 
plt.rc('ytick', labelsize=25)
plt.rcParams.update({'font.size': 20})


#make plot 
plt.plot(x,y,'o',label="Probabilidad",markersize=15)
plt.ylim(0,1)
plt.xlim(0,50)
# settings of box label postion 
plt.legend(loc=1, borderaxespad=1)
# show in script plot
plt.show()
