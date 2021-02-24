## sum of sinatures

# np=8
# rep=9
# sem=9

np0=0 #analitica 3
np1=0 #comunicación cientifica 
sem=0 #seminario (pass)
rep0=5 #analitica instrumental
rep1=5 #termo estadistica (pass)
np2=0 #prop de los solidos 
rep2=5 #terno irreversible no lineal 


np0=0 #analitica 3
np1=0 #comunicación cientifica 
rep0=5 #analitica instrumental

np2=0 #prop de los solidos 
rep2=5 #terno irreversible no lineal 


## semestrers 
s1=[6,6,9,8,8]
s2=[6,10,10,7,7,8]
s3=[6,7,8,8,8]
s4=[7,8,7,8,6]
s5=[8,9,7,6]
s6=[9,7,np0,7]
s7=[np1,9,7,9]
s8=[9,10,10]
s9=[10,9] # semn
s10=[8,rep0,7,8,9]
s11=[8,8,10,10,7,np2,10,rep2,8,7]

semesters=[s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11]


s=[5,6,5,5,4,4,4,3,1,5]

total=0
np=0
rep=0
sizeArrays=0

for i in semesters:
    print(len(i))
    sizeArrays+=len(i)
    for j in i:
        if(j==0):
            print("np")
            np+=1
        if(j<6):
            print("reprobada")
            rep+=1
        total+=j

print("total number",sizeArrays)
print("total np",np)
print("total rep",rep)
print("total sum",total)

print("promedio",total/(sizeArrays-np))
