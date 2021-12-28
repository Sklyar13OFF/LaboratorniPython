# Lab 19

Задано рядок символів, що містить слова розділені пробілами. Визначити скільки слів є числами.

Текстовий файл - https://github.com/Sklyar13OFF/LaboratorniPython/blob/master/Labkanineteen/mynumbers.txt
```python
f = open('mynumbers.txt')
line = f.readline().split(' ')
counter = 0
for i in line:
    if i.isdigit():
        counter += 1
print(counter)

```


**Результат**

Кількість чисел:  8


Process finished with exit code 0
