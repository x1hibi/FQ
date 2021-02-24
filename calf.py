## sum of sinatures

# np=8
# rep=9
# sem=9

np=10 # comunicacion y analitica 3
rep=10 #1 analitica
sem=10 #1 seminario

## semestrers 
s1=[6,6,9,8,8]
s2=[6,10,10,7,7,8]
s3=[6,7,8,8,8]
s4=[7,8,7,8,6]
s5=[8,9,7,6]
s6=[9,7,np,7]
s7=[np,9,7,9]
s8=[9,10,10]
s9=[10,sem]
s10=[8,rep,7,8,9]
#s11=[8,8,10,rep,np,rep,8,7,5]
s11=[8,8,10,10,7,10,8,7,rep]

semesters=[s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11]


s=[5,6,5,5,4,4,4,3,1,5]

sum2=0
total=0

sizeArrays=0

for i in semesters:
    print(len(i))
    sizeArrays+=len(i)
    for j in i:
        total+=j

for i in range(10):
    sum2+=s[i]

print("obligatorias",sum2+1)
print("socio",2)
print("optativas A",1)
print("optativas B",5)
print("total number",sizeArrays)
print("total sum",total)

print("promedio",total/(sizeArrays))
