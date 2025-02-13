sp=[-1,3,-2,-7,-11,23,-12,56,-34]
for i in range(len(sp)-1):
    if ((sp[i])<0 and sp[i+1]<0) or (sp[i]>0 and sp[i+1]>0):
        print(sp[i],sp[i+1])
        break
