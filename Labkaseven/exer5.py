'''
s -  кількість рядків матриці
l - кількість стовпців матриці
a - матриця
'''
s = int(input('Введіть кількість рядків матриці:  '))
l = int(input('Введіть кількість стовпців матриці:  '))
a = [[int(input('Введіть елемент матриці у {0} рядку та у {1} стовпці:  '.format(nn,n))) for n in range(l)] for nn in range(s)] #ввід елементів матриці

a = list(zip(*sorted(list(zip(*a)),  #сортування матриці
                          key=lambda column: sum(abs(el) for el in column
                                                 if el < 0 and el % 2))))

print(*a, sep="\n")