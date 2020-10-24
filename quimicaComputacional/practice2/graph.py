#import matploy library
import matplotlib.pyplot as plt

# x axis
x=[0,1,2,3,4,5]
# y axis arrays with data of of method for each thermodinamic potenctial 
# Free energy
HF=[0,0,31.816,31.816,-36.259,-36.259]
B3LYP=[0,0,6.098,6.098,-18.956,-18.956]
M062X=[0,0,10.076,10.076,-23.610,-23.610]
M062XTwo=[0,0,10.248,10.248,-24.554,-24.554]
# Enthalpy
#HF=[0,0,25.644,25.644,-28.247,-28.247]
#B3LYP=[0,0,-0.083,-0.083,-11.017,-11.017]
#M062X=[0,0,3.511,3.511,-15.257,-15.257]
#M062XTwo=[0,0,3.599,3.599,-16.123,-16.123]
#set axis labels and title
#plt.title("Graph 1 Free energy VS Reaction coordenate")
plt.xlabel("Reaction coordinate")
plt.ylabel("$\Delta G$ (kcal/mol)")

#set settings, grid, size a file name 
plt.grid("true")
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
fig.savefig('reactioProfileG.png', dpi=100)
plt.rc('xtick', labelsize=25) 
plt.rc('ytick', labelsize=25)
plt.rcParams.update({'font.size': 30})

#make plot 
plt.plot(x,HF,label="HF",linewidth=5)
plt.plot(x,B3LYP,label="B3LYP",linewidth=5)
plt.plot(x,M062X,label="M062X",linewidth=5)
plt.plot(x,M062XTwo,label="M062X*",linewidth=5)
plt.xlim(0,5)
# settings of box label postion 
plt.legend(loc=1, borderaxespad=1)
# show in script plot
plt.show()
