import numpy as np
class Line:
    
    def __init__(self):
        self.x_0 = float(input('Введіть першу координату точки, що належить першій прямій: '))
        self.y_0 = float(input('Введіть другу координату точки, що належить першій прямій: '))
        self.m = float(input('Введіть перший коефіцієнт напрямного вектора першої прямої: '))
        self.n = float(input('Введіть другий коефіцієнт напрямного вектора першої прямої: '))
    def coef(self):
        return [self.x_0,self.y_0,self.m,self.n]
    def intersection(self):
        self.x_1 = float(input('Введіть першу координату точки, що належить другій прямій: '))
        self.y_1 = float(input('Введіть другу координату точки, що належить другій прямій: '))
        self.j = float(input('Введіть перший коефіцієнт напрямного вектора другої прямої: '))
        self.k = float(input('Введіть другий коефіцієнт напрямного вектора другої прямої: '))
        self.A = np.array([[self.m,-self.j],[self.n,-self.k]])
        self.Res = np.array([-self.x_0+self.x_1,-self.y_0+self.y_1])
        self.dot = np.linalg.solve(self.A,self.Res)
        return 'Точка перетину 2 прямих заданих канонічними рівняннями - {0}'.format(self.dot)
    def paralel(self):
        if self.m*self.j + self.n*self.k == 0:
            return 'Паралельні'
        else:
            return 'Не паралельні'
    def belongs(self):
        self.dot_x = float(input('Введіть першу координату точки: '))
        self.dot_y = float(input('Введіть другу координату точки: '))
        if ((self.dot_x - self.x_0)*self.n) == ((self.dot_y - self.y_0)*self.m):
            return 'Точка належить 1-ій прямій'
        elif ((self.dot_x - self.x_1)*self.k) == ((self.dot_y - self.y_1)*self.j):
            return 'Точка належить 2-ій прямій'
        else:
            return 'Точка не належить жодній прямій'
        
A = Line()
print(A.intersection())
print(A.belongs())
