lst1 = list(map(int, input().split()))
lst2 = input().lower().split()
print(' '.join(lst2[i - 1] for i in lst1).capitalize())