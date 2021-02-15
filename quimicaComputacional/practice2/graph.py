#import matploy

import matplotlib.pyplot as plt

# x axis
x=[0,1,2,3,4,5]
# y axis
HF=[0.000,0.000,26.668,26.668,-29.743,-29.743]
B3LYP=[0.000,0.000,0.925,0.925,-12.438,-12.438]
M062X=[0.000,0.000,4.564,4.564,-16.744,-16.744]
M062XTwo=[0.000,0.000,4.668,4.668,-17.620,-17.620]
#set axis labels and title
#plt.title("Reaction profile (Free energy)")
plt.xlabel("Reaction coordinate")
plt.ylabel("$\Delta$ZPE (kcal/mol)")

#set settings, grid, size a file name 
plt.grid("true")
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
fig.savefig('reactioProfileG.png', dpi=100)
plt.rc('xtick', labelsize=25) 
plt.rc('ytick', labelsize=25)
plt.rcParams.update({'font.size': 27.5})

#make plot 
plt.plot(x,HF,label="HF", linewidth=5)
plt.plot(x,B3LYP,label="B3LYP", linewidth=5)
plt.plot(x,M062X,label="M062X", linewidth=5)
plt.plot(x,M062XTwo,label="M062X*", linewidth=5)
plt.xlim(0,5)
# settings of box label postion 
plt.legend( loc=1)
# show in script plot
plt.show()
