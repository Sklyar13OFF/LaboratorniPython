f = open('mynumbers.txt')
line = f.readline().split(' ')
counter = 0
for i in line:
    if i.isdigit():
        counter += 1
print(counter)
