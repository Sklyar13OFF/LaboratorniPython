'''
s -  кількість рядків матриці
l - кількість стовпців матриці
a - матриця
suma - сума
sum_neg - функція знаходженння суми
'''
s = int(input('Введіть кількість рядків матриці:  '))
l = int(input('Введіть кількість стовпців матриці:  '))
a = [[int(input('Введіть елемент матриці у {0} рядку та у {1} стовпці:  '.format(nn,n))) for n in range(l)] for nn in range(s)] #ввід елементів матриці
def sum_neg(matrix) : #функція
    suma = 0
    for i in range(len(matrix)) :
        for j in range(len(matrix[i])) :
            if matrix[i][j] < 0 and i == j:
                suma += matrix[i][j]
    return suma
print('Сума:  ',sum_neg(a))