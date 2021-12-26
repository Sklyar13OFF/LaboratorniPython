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
import numpy
class Line:
    def __init__(self):
        self.a = 0
        self.b = 0
    def coef(self):
        self.a = float(input('Введіть перший коефіцієнт канонічного рівняння прямої:  '))
        self.b = float(input('Введіть другий коефіцієнт канонічного рівняння прямої:  '))
        return [self.a,self.b]
    def crossing(self):
        self.a_1 = float(input('Введіть перший коефіцієнт канонічного рівняння другої прямої:  '))
        self.b_1 = float(input('Введіть другий коефіцієнт канонічного рівняння другої прямої:  '))
        self.m1 = numpy.array([[self.b, self.a], [self.b_1, self.a_1]])
        self.v1 = numpy.array([1,1])
        return numpy.linalg.solve(self.m1, self.v1)
    def paralel(self):
        if self.a*self.a_1 + self.b*self.b_1 == 0:
            return "Паралельні"
        else:
            return "Не паралельні"
    def belong(self):
        self.x = float(input('Введіть першу координату точки :  '))
        self.y = float(input('Введіть другу координату точки  :  '))
        if self.x/ self.a + self.y/self.b == 1:
            return 'Належить'
        else:
            return 'Не належить'
```
**Результат** 

Введіть перший коефіцієнт канонічного рівняння прямої:  2

Введіть другий коефіцієнт канонічного рівняння прямої:  2

Введіть перший коефіцієнт канонічного рівняння другої прямої:  3

Введіть другий коефіцієнт канонічного рівняння другої прямої:  3


Не паралельні


Process finished with exit code 0

**завдання №2**

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


