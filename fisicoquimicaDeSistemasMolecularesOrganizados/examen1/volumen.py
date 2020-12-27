#import matploy library
import matplotlib.pyplot as plt

# x axis
nc=[6,12]
# y axis arrays with data of of method for each thermodinamic potenctial 
# Volumen
v=[0.2185531487,0.3778053109]

#set axis labels and title
plt.xlabel("Número de carbonos")
plt.ylabel("Volumen del hidrocarburo")

#set settings, grid, size a file name 
plt.grid("true")
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
fig.savefig('reactioProfileG.png', dpi=100)
plt.rc('xtick', labelsize=25) 
plt.rc('ytick', labelsize=25)
plt.rcParams.update({'font.size': 30})

#make plot 
plt.plot(nc,v,label=" $v=0.0265n_c+0.0593$",linewidth=5)
#plt.xlim(0,5)
# settings of box label postion 
plt.legend(loc=2, borderaxespad=1)
# show in script plot
plt.show()
