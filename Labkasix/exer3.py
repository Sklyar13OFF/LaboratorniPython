"""
n - вимірність простору
sklyar_ab - скалярний добуток векторів a i b
sklyar_ac - скалярний добуток векторів a i c
result - результат обчислення
"""
n = int(input('Введіть вимірність простору :  '))  #ввід вимірності простору
sklyar_ab = 0    #початкові значення скалярних добутків
sklyar_ac = 0
a = [float(input('Введіть {0} - ий елемент вектора a:  '.format(i))) for i in range(1,n+1)]
b = [float(input('Введіть {0} - ий елемент вектора b:  '.format(j))) for j in range(1,n+1)]
c = [float(input('Введіть {0} - ий елемент вектора c:  '.format(k))) for k in range(1,n+1)]
for i in range(n):
    sklyar_ab += a[i] * b[i]
    sklyar_ac += a[i] * c[i]
result = 2*sklyar_ab - 3*sklyar_ac
print('Результатом буде :  {0}'.format(result))