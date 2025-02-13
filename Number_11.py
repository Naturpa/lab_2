A=[12,11,34,23,43,54,563,255]
for i in range(0,len(A)-1,2):
    A[i],A[i+1]=A[i+1],A[i]
print(A)