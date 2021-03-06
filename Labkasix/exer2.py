"""""
A - масив, елементи якого задані формулою 
B - масив, який складається з порядкових номерів числа а
suma - кінцеве значення елемента, який заданий формулою
x - величина кута в радіанах
n - кількість елементів масиву
factorial - факторіал (коефіціент, на який домножується градус в cos(x) у елементах масиву А
result - кінцевий результат  
"""""
import math as m   #імпортуєм модуль math
A, B, suma = [], [], 0  #присвоєння значень змінним
x = float(input('Міра кута в радіанах :  '))  #введення значення кута в радіанах
n = int(input('Введіть кількість елементів массиву :  '))  #введення кількості елементів масиву
for s in range(1,n+1):
    i = int(input('Введіть значення і для {0} елемента масиву :  '.format(s)))    #наповнення масиву В
    B.append(i)
    for k in range (1, i+1):
        factorial = 1
        for j in range(1,k+1):     #обчислення факторіалу
            factorial *= j
        suma += m.sin(x*k) * m.cos(x*factorial) * ((-1)**(k+1))    #наповнення масиву А
    A.append(suma)
    suma = 0
result = A[B.index(min(B))]      #обчислення результату
print("Значення елемента в списку з найменшим порядковим номером:  {0} ".format(result))