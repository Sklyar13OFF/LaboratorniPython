'''
n - кількість рядків матриці
m - кіліькість стовпців матриці
а - матриця
s  - транспонована матриця
'''
n = int(input('Введіть кількість рядків матриці  :  '))
m = int(input('Введіть кількість стовпців матриці  :  '))    #вводиться розмірність матриці
a = [
    [float(input('Введіть значення для елемента в {0} рядку та {1} стовпці:   '.format(i,j))) for j in range(m)] for i in range(n)]
s = []
for j in range(len(a[0])):
    s.append([])
    for i in range(len(a)):
        s[-1].append(a[i][j])
print('Транспонована матриця виглядатиме - {0}'.format(s))  #вивід транспонованої матриці