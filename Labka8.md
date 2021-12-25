# Lab 8 

**Завдання №1**

Дано дійсні числа x,y,z . Обчислити

![equations](http://www.sciweavers.org/upload/Tex2Img_1640440394/render.png)

```python
""""
x - 1 дійсне число
у - 2 дійсне число
z - 3 дійсне число
max - функція
u - результат
"""
x = float(input('Введіть 1 дійсне число :  '))
y = float(input('Введіть 2 дійсне число :  '))    #ввід значень
z = float(input('Введіть 3 дійсне число :  '))
def max(a,b):
    if a >= b:
        return a     #функція
    else:
        return b
u = (max(x,max(y,z)) + max(x+y,max(x*y,4*z)))/max((max(max(x+y,x*y),x**2))**2,max(7,z**2))  #обчислення результату
print('Результат : {0}'.format(u))
```

**Результат**

Введіть 1 дійсне число :  3

Введіть 2 дійсне число :  2

Введіть 3 дійсне число :  3

Результат : 0.18518518518518517


Process finished with exit code 0

**Завдання №3**
Нехай ![equations](http://www.sciweavers.org/upload/Tex2Img_1640440676/render.png). Визначити ![equatoins](http://www.sciweavers.org/upload/Tex2Img_1640440723/render.png).

```python
""""
n - кількість доданків
recurssion - рекурсивна функція
result - результат
"""
n = int(input('Введіть кількість доданків :  '))   #введення кількості доданків
def  recurssion(n):    #рекурсія
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 9
    else:
        return recurssion(n-1) + 4*recurssion(n-3)    #обчислення рекурсії
result = recurssion(n)  #результат
print('Результатом буде : {0}'.format(result))
```
**Результат**

Введіть кількість доданків :  4

Результатом буде : 45


Process finished with exit code 0


