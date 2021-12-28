# Lab 19

Задано рядок символів, що містить слова розділені пробілами. Визначити скільки слів є числами.

Текстовий файл - https://github.com/Sklyar13OFF/LaboratorniPython/blob/master/Labkanineteen/mynumbers.txt
```python

'''
f - допоміжна змінна
line - перша лінія текстового файла
counter - лічильник
'''
f = open('mynumbers.txt') #відкриття файла
line = f.readline().split(' ') 
counter = 0
for i in line:
    if i.isdigit():
        counter += 1
print('Кількість чисел - ',counter)

```


**Результат**

Кількість чисел -  2

Process finished with exit code 0
