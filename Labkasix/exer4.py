import random as ran
n = int(input('Введіть довжину масиву (більше 5) :  '))
ask = int(input('Ви бажаєте самі ввести список (введіть 0) чи бажаєте рандомно згенерувати його (введіть 1)?  '))
if ask == 0:
    b = [float(input('Введіть {0} - ий елемент масиву : '.format(i))) for i in range(1,n+1)]
    print("Ваш список - {0}".format(b))
else:
    b  = [ran.uniform(1,100) for i in range(1,3)]+ [ran.uniform(-1,1) for i in range(3,n)]
    print("Ваш список - {0}".format(b))
b = [i  for i in b if abs(i) < 1] + [i for i in b if abs(i) >= 1]
print("Відсортований список -  {0}".format(b))
