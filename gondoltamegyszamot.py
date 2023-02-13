import random

gondoltszam=random.randint(1,5)

szam=int(input('A gondoltam egy számt! 1 és 5 között. Ki tudod találni? '))


if gondoltszam == szam:
    print('Eltaláltad!')
    
elif gondoltszam > szam:
    print('A számom nagyobb!')
    
else:
    print('A számom kisebb!')