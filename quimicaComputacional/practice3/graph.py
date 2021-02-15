#import matploy

import matplotlib.pyplot as plt

# x axis
x=[0,1,2,3,4,5]
# y axis
#ZPE
"""
HF=[0.000,0.000,11.131,11.131,-24.279,-24.279]
B3LYP=[0.000,0.000,-2.986,-2.986,-23.011,-23.011]
M052X=[0.000,0.000,-1.607,-1.607,-27.674,-27.674]
M062X=[0.000,0.000,-0.519,-0.519,-29.142,-29.142]
"""

### H

"""
HF=[0.000,0.000,10.059,10.059,-24.418,-24.418]
B3LYP=[0.000,0.000,-3.991,-3.991,-23.171,-23.171]
M052X=[0.000,0.000,-2.636,-2.636,-27.819,-27.819]
M062X=[0.000,0.000,-1.613,-1.613,-29.235,-29.235]
"""
#G
"""
HF=[0.000,0.000,18.294,18.294,-23.650,-23.650]
B3LYP=[0.000,0.000,4.335,4.335,-22.575,-22.575]
M052X=[0.000,0.000,5.690,5.690,-27.283,-27.283]
M062X=[0.000,0.000,6.901,6.901,-28.793,-28.793]
"""

#Compartion

M062XGET=[0.000,0.000,6.901,6.901,-28.793,-28.793]
M062XHET=[0.000,0.000,-1.613,-1.613,-29.235,-29.235]
M062XGMET=[0.000,0.000,10.076,10.076,-23.610,-23.610]
M062XHMET=[0.000,0.000,3.511,3.511,-15.257,-15.257]


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
plt.rcParams.update({'font.size': 27.5})

#make plot 
plt.plot(x,M062XGMET,'r--',label="$\Delta$G Methane", linewidth=5,color="yellow")
plt.plot(x,M062XHMET,'r--',label="$\Delta$H Methane", linewidth=5)
plt.plot(x,M062XGET,label="$\Delta$G Ethene", linewidth=5)
plt.plot(x,M062XHET,label="$\Delta$H Ethene", linewidth=5)
plt.xlim(0,5)
# settings of box label postion 
plt.legend( loc=1)
# show in script plot
plt.show()
