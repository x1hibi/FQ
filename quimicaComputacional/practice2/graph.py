#import matplot
import matplotlib.pyplot as plt

# x axis array
x=[0,1,2,3,4,5]

# y axis arrays
HF=[0.000,0.000,31.816,31.816,-36.259,-36.259]
B3LYP=[0.000,0.000,6.098,6.098,-18.956,-18.956]
M062X=[0.000,0.000,10.076,10.076,-23.610,-23.610]
M062XTwo=[0.000,0.000,10.248,10.248,-24.554,-24.554]

#set axis labels and title
plt.title("Reaction profile (Free energy)") # plot title
plt.xlabel("Reaction coordinate") # x axis label 
plt.ylabel("Free energy (kcal/mol)") # y axis label 

#set settings, grid, size a file name 
fig = plt.gcf() #conf of plot
fig.set_size_inches(18.5, 10.5) #size of the plot
fig.savefig('reactioProfileG.png', dpi=100) #name of file to save

#set another configurations 
plt.grid("true") #set grid 
plt.rc('xtick', labelsize=15) #font size x axis label
plt.rc('ytick', labelsize=15) #font size y axis label
plt.rcParams.update({'font.size': 20}) # font size title, labels and legend 
plt.legend(loc=1, borderaxespad=1) # position of box with legend and border

#make plot 
plt.plot(x,HF,label="HF") # plot y array of HF method 
plt.plot(x,B3LYP,label="B3LYP")
plt.plot(x,M062X,label="M062X")
plt.plot(x,M062XTwo,label="M062X*")
plt.xlim(0,5) # plot rang to show in x axis 

# show in script plot
plt.show()
