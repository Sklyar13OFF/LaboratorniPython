'''''
 n  - змінна 
 y - результат
'''''
n = float(input('Введіть значення змінної  :   '))   #Ввід змінної n
if 0 <= n < 5:
    y = 0
elif 5 <=  n < 10:
    y = 1                     #порівняння змінної n з літералами та присвоєння значення змінній у
elif  10 <= n < 15:
    y = 2
else:
    y = 3
print("Значення, яке приймає у :  {0}".format(y))
