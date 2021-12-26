""""
n - розмірність матриці
a - матриця
max - максимальний елемент матриці
n1 - 1 index найбільшого за модулем елемента
n2 -  2 index набільшого за модулем елемента
"""
from math import*  #імпортування модуля
n = int(input('Ввід розмірності матриці :  '))
a = [
    [sin(i**2 - j**2)/n for j in range(n) ] for i in range(n)]
max = 0    #
for el in range(len(a)):   #прохід по елементам матриці
    for el2 in range(len(a)):
        if abs(a[el][el2]) >= abs(max):   #порівняння
            max = a[el][el2]
            n1 = el
            n2 = el2
print('Найбільший за модулем елемент матриці  :  {0} , він знаходиться в {1} рядку та {2} стовпці  '.format(max, n1, n2))