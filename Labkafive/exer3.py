"""""
x - значення кута синуса в радіанах
eps - задана точність
n - кількість множників
sinus - наближена формула
"""""
import  math as m  #
x = float((input('Введіть значення для кута в радіанах:   ')))   #ввід значення кута в радіанах
eps = float(input("Введіть значення для точності {0}:     ".format('\u03B5')))   #ввід значення для точності
n = int(input('Введіть кількість множників:  '))    #ввід кількості множників
sinus = x       #початкове значення змінної наближеної формули
for i in range(1, n):
    sinus *= (1 - (x**2)/ ( (m.pi**2) * (i**2) ))
if abs(m.sin(x)-sinus) <= eps:       #порівняння точності із заданою користувачем
    print("Рівність справедлива при заданій точності")
else:
    print("Рівність несправедлива при заданій точності")
