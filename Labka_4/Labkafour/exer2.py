"""
mini - мінімальне число
maxi - максимальне число
result - результат
"""
a = float(input('Введіть значення першої змінної :  '))
b = float(input('Введіть значення другої змінної :   '))
c = float(input('Введіть значення третьої змінної :   '))
if a <= b:
    mini = a
else:
    mini = b
if b >= c:
    maxi = b
else:
    maxi = c
result = mini + maxi**2
print('Результат - {0}'.format(result))