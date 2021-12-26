infile = open('mynumbers.txt','r')
lines = infile.readlines()
a=[]
for line in lines:
    if line < 0:
        a.append(line)
for el in a:
    el = abs(el)
print(min(a))