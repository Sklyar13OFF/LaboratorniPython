import numpy
class Line:
    def __init__(self):
        self.a = float(input('Введіть перший коефіцієнт канонічного рівняння прямої:  '))
        self.b = float(input('Введіть другий коефіцієнт канонічного рівняння прямої:  '))
        self.a_1 = float(input('Введіть перший коефіцієнт канонічного рівняння другої прямої:  '))
        self.b_1 = float(input('Введіть другий коефіцієнт канонічного рівняння другої прямої:  '))
    def coef(self):
        return [self.a,self.b]
    def crossing(self):
        self.a_1 = float(input('Введіть перший коефіцієнт канонічного рівняння другої прямої:  '))
        self.b_1 = float(input('Введіть другий коефіцієнт канонічного рівняння другої прямої:  '))
        self.m1 = numpy.array([[self.a, self.b], [self.a_1, self.b_1]])
        self.v1 = numpy.array([1,1])
        return numpy.linalg.solve(self.m1, self.v1)
    def paralel(self):
        if self.a*self.a_1 + self.b*self.b_1 == 0:
            return ("Паралельні")
        else:
            return ("Не паралельні")
    def belong(self):
        self.x = float(input('Введіть першу координату точки :  '))
        self.y = float(input('Введіть другу координату точки  :  '))
        if self.x/ self.a + self.y/self.b == 1:
            return 'Належить'
        else:
            return 'Не належить'
A  = Line()
print(A.paralel())