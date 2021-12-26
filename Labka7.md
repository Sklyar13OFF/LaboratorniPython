# Lab 7
**Завдання №1**

Визначити добуток додатних елементів матриці нижче головної діагоналі.

**Код**

```python
""""
n - кількість рядків матриці
m - кількість стовпців матриці
a - матриця
dob - добуток
counter - лічильник
"""
n = int(input('Введіть кількість рядків матриці :  ')) # ввід розмірності матриці
m = int(input('Введіть кількість стовпців матриці  :  '))
a=[
    [float(input('a[{0}] [{1}]  :  '.format(i, j))) for j in range(m)]  for i in range(n)
]
dob = 1
counter = 0
for el in range(len(a)):    #обчислення добутку
    for el2 in range(el):
        if a[el][el2] > 0:
            dob *= a[el][el2]
            counter += 1
if counter >= 0:
    print("Добуток додатніх елементів нижче головної діагоналі = {0}".format(dob))    #вивід результату
else:
    print('Нижче головної діагоналі немає додатніх елементів')
```
**Результат**

Введіть кількість рядків матриці :  3

Введіть кількість стовпців матриці  :  3

a[0] [0]  :  1

a[0] [1]  :  2

a[0] [2]  :  3

a[1] [0]  :  4

a[1] [1]  :  5

a[1] [2]  :  6

a[2] [0]  :  7

a[2] [1]  :  8

a[2] [2]  :  9

Добуток додатніх елементів нижче головної діагоналі = 224.0


Process finished with exit code 0

**Завдання №2**

Побудувати квадратну матрицю А, елементи якої задаються формулою:

![equations](http://www.sciweavers.org/upload/Tex2Img_1640510649/render.png)

**Код**

```python
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
```

**Результат**

Ввід розмірності матриці :  3

Найбільший за модулем елемент матриці  :  0.2804903282692988 , він знаходиться в 1 рядку та 0 стовпці  


Process finished with exit code 0

**Завдання №3**

Дано матрицю A. Знайти матрицю транспоновану до даної.

**Код**

```python
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
```

**Результат**
Введіть кількість рядків матриці  :  3

Введіть кількість стовпців матриці  :  3

Введіть значення для елемента в 0 рядку та 0 стовпці:   1

Введіть значення для елемента в 0 рядку та 1 стовпці:   2

Введіть значення для елемента в 0 рядку та 2 стовпці:   3

Введіть значення для елемента в 1 рядку та 0 стовпці:   4

Введіть значення для елемента в 1 рядку та 1 стовпці:   5

Введіть значення для елемента в 1 рядку та 2 стовпці:   6

Введіть значення для елемента в 2 рядку та 0 стовпці:   7

Введіть значення для елемента в 2 рядку та 1 стовпці:   8

Введіть значення для елемента в 2 рядку та 2 стовпці:   9

Транспонована матриця виглядатиме - [[1.0, 4.0, 7.0], [2.0, 5.0, 8.0], [3.0, 6.0, 9.0]]


Process finished with exit code 0


**Завдання №4**

Розмістити елементи непарних стовпців у порядку спадання.

**Код**

```python
'''
s -  кількість рядків матриці
l - кількість стовпців матриці
a - матриця
'''
s = int(input('Введіть кількість рядків матриці:  '))
l = int(input('Введіть кількість стовпців матриці:  '))
a = [[int(input('Введіть елемент матриці у {0} рядку та у {1} стовпці:  '.format(nn,n))) for n in range(l)] for nn in range(s)] #ввід елементів матриці
for i in range(0,len(a)):
    if i%2 == 1:
        a[i] = sorted(a[i],reverse = True)
print("Відсортована матриця:  ", a)
```

**Результат**

Введіть кількість рядків матриці:  3

Введіть кількість стовпців матриці:  3

Введіть елемент матриці у 0 рядку та у 0 стовпці:  1

Введіть елемент матриці у 0 рядку та у 1 стовпці:  2

Введіть елемент матриці у 0 рядку та у 2 стовпці:  3

Введіть елемент матриці у 1 рядку та у 0 стовпці:  4

Введіть елемент матриці у 1 рядку та у 1 стовпці:  5

Введіть елемент матриці у 1 рядку та у 2 стовпці:  6

Введіть елемент матриці у 2 рядку та у 0 стовпці:  7

Введіть елемент матриці у 2 рядку та у 1 стовпці:  8

Введіть елемент матриці у 2 рядку та у 2 стовпці:  9

Відсортована матриця:   [[1, 2, 3], [6, 5, 4], [7, 8, 9]]


Process finished with exit code 0


**Завдання №5**

Переставляючи стовпці даної цілочислової матриці, розташувати їх у відповідності з ростом характеристик. Характеристикою стовпця цілочислової матриці назвемо суму модулів його від’ємних непарних елементів.

**Код**

```python
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
```

**Результат**

Введіть кількість рядків матриці:  3

Введіть кількість стовпців матриці:  2

Введіть елемент матриці у 0 рядку та у 0 стовпці:  -1

Введіть елемент матриці у 0 рядку та у 1 стовпці:  2

Введіть елемент матриці у 1 рядку та у 0 стовпці:  -4

Введіть елемент матриці у 1 рядку та у 1 стовпці:  4

Введіть елемент матриці у 2 рядку та у 0 стовпці:  -2

Введіть елемент матриці у 2 рядку та у 1 стовпці:  6

(2, -1)
(4, -4)
(6, -2)

Process finished with exit code 0

**Завдання №6**


Знайти суму елементів в тих стовпцях, які містять хоча б один від’ємний елемент такі k, що k-й рядок матриці співпадає з k-м стовбцем
**Код** 

```python
'''
s -  кількість рядків матриці
l - кількість стовпців матриці
a - матриця
'''
s = int(input('Введіть кількість рядків матриці:  '))
l = int(input('Введіть кількість стовпців матриці:  '))
a = [[int(input('Введіть елемент матриці у {0} рядку та у {1} стовпці:  '.format(nn,n))) for n in range(l)] for nn in range(s)] #ввід елементів матриці
def sum_neg(matrix) :
    suma = 0
    for i in range(len(matrix)) :
        for j in range(len(matrix[i])) :
            if matrix[i][j] < 0 and i == j:
                suma += matrix[i][j]
    return suma
print('Сума:  ',sum_neg(a))
```

**Результат**

Введіть кількість рядків матриці:  2

Введіть кількість стовпців матриці:  2

Введіть елемент матриці у 0 рядку та у 0 стовпці:  -2

Введіть елемент матриці у 0 рядку та у 1 стовпці:  3

Введіть елемент матриці у 1 рядку та у 0 стовпці:  2

Введіть елемент матриці у 1 рядку та у 1 стовпці:  -2

Сума:   -4

Process finished with exit code 0
