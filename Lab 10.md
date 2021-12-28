# Lab 10
**Завдання №1**

Об’єкт “Пряма на площині ”

Поля:

*для зберігання коефіцієнтів канонічного рівняння прямої*

Методи:  

  *введення та виведення коефіцієнтів;*
  
  *знаходження точки перетину з іншою прямою;*
  
  *встановлення паралельності з іншою прямою;*
  
  *встановлення належності деякої точки прямій.*
  
**Код**

```python
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
        return self.dot
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
```
**Результат** 

>>> A = Line()


Введіть першу координату точки, що належить першій прямій: 1

Введіть другу координату точки, що належить першій прямій: 2

Введіть перший коефіцієнт напрямного вектора першої прямої: 3

Введіть другий коефіцієнт напрямного вектора першої прямої: 4

>>> print(A.intersection())


Введіть першу координату точки, що належить другій прямій: -4

Введіть другу координату точки, що належить другій прямій: -3

Введіть перший коефіцієнт напрямного вектора другої прямої: 3

Введіть другий коефіцієнт напрямного вектора другої прямої: 0

[-1.25        0.41666667]

>>> print(A.belongs())


Введіть першу координату точки: 2

Введіть другу координату точки: 3

Точка не належить жодній прямій



**Завдання №2**

Об’єкт -  “Монітор”

Поля:

*фірма виробник;*

*дата виробництва;*

*дата купівлі;*

*вартість;*

*тип монітора;*

*розміри монітора*

**Код**

```python

from datetime import date
class Monik:
    def __init__(self):
        self.firm = input('Введіть назву фірми виробника: ')
        self.date1 = int(input('Введіть число дати виробництва:  '))
        self.date2 = int(input('Введіть місяць дати виробництва:  '))
        self.date3 = int(input('Введіть рік дати виробництва :  '))
        self.date_1 = int(input('Введіть число дати купівлі:  '))
        self.date_2 = int(input('Введіть місяць дати купівлі:  '))
        self.date_3 = int(input('Введіть рік дати купівлі :  '))
        self.price = int(input('Введіть вартість в гривнях:  '))
        self.type = input('Введіть тип монітора:  ')
        self.height = int(input('Введіть довжину монітора в пікселях:  '))
        self.width = int(input('Введіть ширину монітора в пікселях:  '))
    def calculate_age(self):
        today = date.today()
        return today.year - self.date3 - ((today.month, today.day) < (self.date2, self.date1))
    def pic(self):
        self.pic_h =  int(input('Введіть довжину картинки : '))
        self.pic_w = int(input('Введіть ширину картинки : '))
        if self.pic_h >= self.height and self.pic_w >= self.width:
            return "Можна"
        else:
            return "Не можна"
    def coef(self):
        if self.pic_h >= self.height and self.pic_w >= self.width:
            self.coef.h = self.height/self.pic_h
            self.coef.w = self.width/self.pic_w
        return [self.coef.h,self.coef.w]
A = Monik()
print(A.pic())
```
**Результат**

Введіть назву фірми виробника: Lipton

Введіть число дати виробництва:  13

Введіть місяць дати виробництва:  05

Введіть рік дати виробництва :  2004

Введіть число дати купівлі:  13

Введіть місяць дати купівлі:  13

Введіть рік дати купівлі :  23

Введіть вартість в гривнях:  23

Введіть тип монітора:  Large

Введіть довжину монітора в пікселях:  1920

Введіть ширину монітора в пікселях:  1080

Введіть довжину картинки : 32

Введіть ширину картинки : 32

Не можна

Process finished with exit code 0


