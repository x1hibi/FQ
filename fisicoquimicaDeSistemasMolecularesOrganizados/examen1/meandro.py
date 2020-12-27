#import matploy library
import matplotlib.pyplot as plt
import numpy as np

# x axis
nc=[6,12]
# y axis arrays with data of of method for each thermodinamic potenctial 
# Volumen
v=[0.2185531487,0.3778053109]

x=range(26, -1, -1)
y=range(26, -1, -1)
x2=[25,24,24,24,23,23,22,22,21,21,20,19,18,13,13,14,14,15,15,15,16,4,4,5,5,6,6,12,11,10,9]
y2=[17,18,17,16,18,19,19,20,20,13,13,12,12,12,11,11,10,10,9,8,8,3,2,2,1,1,0,6,6,5,4]

#set axis labels and title
plt.xlabel("Residuos")
plt.ylabel("Residuos")

#set settings, grid, size a file name 
plt.grid("true")
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
fig.savefig('reactioProfileG.png', dpi=100)
plt.rc('xtick', labelsize=25) 
plt.rc('ytick', labelsize=25)
plt.rcParams.update({'font.size': 20})

#make plot 
plt.plot(x,y,'o',label="Diagonal",markersize=15)
plt.plot(x2,y2,'o',label="Contactos",markersize=15)
plt.xlim(26,0)
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.ylim(0,26)
plt.yticks(np.arange(min(y), max(y)+1, 1.0))
# settings of box label postion 
plt.legend(loc=1, borderaxespad=1)
# show in script plot
plt.show()
