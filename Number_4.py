s=input("Введите строку: ")
if s.count('f')==1:
    print(s.index('f'))
if s.count('f')>=2:
    print(s.index('f'),s.rindex('f'))


