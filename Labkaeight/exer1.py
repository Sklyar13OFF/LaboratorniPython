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