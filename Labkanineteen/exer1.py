with open('mynumbers.txt') as file:
    line = file.readlines()
    num = []
    counter = 0
    for i in line:
        num.extend(map(int, i.split()))
    for el in range(len(num)):
        if type(num[el]) == float or type(num[el]) == int:
            counter += 1
    print('Кількість чисел: {0}'.format(counter))
