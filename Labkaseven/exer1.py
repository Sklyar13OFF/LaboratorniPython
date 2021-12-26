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