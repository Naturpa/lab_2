sp=[1,3,2,7,11,23,12,56,34]
for i in range(len(sp)-1):
    if sp[i]<sp[i+1]:
        print(sp[i+1])