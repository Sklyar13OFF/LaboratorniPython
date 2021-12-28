import numpy as np
class Line:
    def __init__(self):
        self.x_0 = float(input('Введіть першу координату точки перетину першої прямої: '))
        self.y_0 = float(input('Введіть другу координату точки перетину першої прямої: '))
        self.m = float(input('Введіть перший коефіцієнт напрямного вектора першої прямої: '))
        self.n = float(input('Введіть другий коефіцієнт напрямного вектора першої прямої: '))
    def coef(self):
        return [self.x_0,self.y_0,self.m,self.n]
    def intersection(self):
        self.x_1 = float(input('Введіть першу координату точки перетину другої прямої: '))
        self.y_1 = float(input('Введіть другу координату точки перетину другої прямої: '))
        self.j = float(input('Введіть перший коефіцієнт напрямного вектора другої прямої: '))
        self.k = float(input('Введыть другий коефіцієнт напрямного вектора другої прямої: '))
        self.A = np.array([[self.m,-self.j],[self.n,-self.k]])
        self.Res = np.array([-self.x_0+self.x_1,-self.y_0+self.y_1])
        self.dot = np.linalg.solve(self.A,self.Res)
        return self.dot
    def paralel(self):
        if self.m*self.j + self.n*self.k == 0:
            return 'Паралельні'
        else:
            return 'Не паралельні'
    def belongs(self):
        self.dot_x = float(input('Введіть першу координату точки: '))
        self.dot_y = float(input('Введіть другу координату точки: '))
        if ((self.dot_x - self.x_0)/self.m) == ((self.dot_y - self.y_0)/self.n):
            return 'Точка належить 1-ій прямій'
        elif ((self.dot_x - self.x_1)/self.j) == ((self.dot_y - self.y_1)/self.k):
            return 'Точка не належить 2-ій прямій'
        else:
            return 'Точка не належить жодній прямій'
A = Line()
print(A.intersection())
print(A.belongs())
