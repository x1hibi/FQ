#import matploy

import matplotlib.pyplot as plt

# x axis
x=[0,1,2,3,4,5]
# y axis
g=[0,0,20.662,20.662,-20.026,-20.026]
#set axis labels and title
#plt.title("Reaction profile (Free energy)")
plt.xlabel("Reaction coordinate")
plt.ylabel("$\Delta$G (kcal/mol)")

#set settings, grid, size a file name 
plt.grid("true")
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
fig.savefig('reactioProfileG.png', dpi=100)
plt.rc('xtick', labelsize=25) 
plt.rc('ytick', labelsize=25)
plt.rcParams.update({'font.size': 28})

#make plot 
plt.plot(x,g,label="$\Delta G$ $HAT$", linewidth=5)
plt.plot([2,3],[4.240238719,4.240238719],"--",label="$\Delta G$ $SET$", linewidth=5)

plt.xlim(0,5)
# settings of box label postion 
plt.legend( loc=1)
# show in script plot
plt.show()
