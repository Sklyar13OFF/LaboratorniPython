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

