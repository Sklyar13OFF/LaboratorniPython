# Lab 19

Задано рядок символів, що містить слова розділені пробілами. Визначити скільки слів є числами.

Текстовий файл - https://github.com/Sklyar13OFF/LaboratorniPython/blob/master/Labkanineteen/mynumbers.txt
```python
with open('mynumbers.txt') as file:
    line = file.readlines()
    num = []
    counter = 0
    for i in line:
        num.extend(map(int, i.split()))
    for el in range(len(num)):
        if type(num[el]) == float or type(num[el]) == int:
            counter += 1
    print('Кількість чисел:  {0}'.format(counter))
```
Текстовий файл:

**Результат**

Кількість чисел:  8


Process finished with exit code 0
