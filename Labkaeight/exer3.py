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
