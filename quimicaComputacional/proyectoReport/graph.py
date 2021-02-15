#import matploy

import matplotlib.pyplot as plt

# x axis
x=[0,1,2,3,4,5]

# y axis

#DH

step1H=[0.000,0.000,7.936739828,7.936739828,-40.9393456,-40.9393456]
step2H=[0.000,0.000,-0.002903,-0.002903,-29.3084575,-29.3084575]
step3H=[0.000,0.000,-1.864958157,-1.864958157,1.955947031,1.955947031]
step4H=[0.000,0.000,-0.01027,-0.01027,-24.59460633,-24.59460633]

#G
step1G=[0.000,0.000,8.596252285,8.596252285,-31.40935921,-31.40935921]
step3G=[0.000,0.000,6.718743939,6.718743939,-38.35212404,-38.35212404]
step2G=[0.000,0.000,7.737191815,7.737191815,-5.545928732,-5.545928732]
step4G=[0.000,0.000,2.031248168,2.031248168,-31.47336518,-31.47336518]


#set axis labels and title
plt.xlabel("Reaction coordinate")
#plt.ylabel("$\Delta$G (kcal/mol)")
#plt.ylabel("$\Delta$H (kcal/mol)")
plt.ylabel("$\Delta$E (kcal/mol)")



#set settings, grid, size a file name 
plt.grid("true")
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
fig.savefig('reactioProfileG.png', dpi=100)
plt.rc('xtick', labelsize=25) 
plt.rc('ytick', labelsize=25)
plt.rcParams.update({'font.size': 27.5})

#make plot 
# plt.plot(x,M062XGMET,'r--',label="$\Delta$G Methane", linewidth=5,color="yellow")
# plt.plot(x,M062XHMET,'r--',label="$\Delta$H Methane", linewidth=5)
# plt.plot(x,M062XGET,label="$\Delta$G Ethene", linewidth=5)
# plt.plot(x,M062XHET,label="$\Delta$H Ethene", linewidth=5)


plt.plot(x,step1G,label="$\Delta$G Step 1", linewidth=5,color="red")
plt.plot(x,step2G,label="$\Delta$G Step 2", linewidth=5,color="blue")
plt.plot(x,step3G,label="$\Delta$G Step 3", linewidth=5,color="yellow")
plt.plot(x,step4G,label="$\Delta$G Step 4", linewidth=5,color="gray")

'''
plt.plot(x,step1H,label="$\Delta$H Step 1", linewidth=5,color="red")
plt.plot(x,step2H,label="$\Delta$H Step 2", linewidth=5,color="blue")
plt.plot(x,step3H,label="$\Delta$H Step 3", linewidth=5,color="yellow")
plt.plot(x,step4H,label="$\Delta$H Step 4", linewidth=5,color="gray")
'''


plt.plot(x,step1H,"r--",label="$\Delta$H Step 1", linewidth=5,color="red")
plt.plot(x,step2H,"r--",label="$\Delta$H Step 2", linewidth=5,color="blue")
plt.plot(x,step3H,"r--",label="$\Delta$H Step 3", linewidth=5,color="yellow")
plt.plot(x,step4H,"r--",label="$\Delta$H Step 4", linewidth=5,color="gray")



#plt.ylim(-42,10)
plt.xlim(0,5)
# settings of box label postion 
plt.legend(loc=3)
# show in script plot
plt.show()





