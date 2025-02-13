sp=[12,4,12,7,7,5,6,4,12,3]
sp1=[]
for i in range(len(sp)):
    if sp.count(sp[i])==1:
        sp1.append(sp[i])
print (sp1)