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
        return 'Вік моніка - {0}'.format(2021 - self.date3)

    def pic(self):
        self.pic_h = int(input('Введіть довжину картинки : '))
        self.pic_w = int(input('Введіть ширину картинки : '))
        if self.pic_h == self.height and self.pic_w == self.width:
            return "Можна без масштабування"
        else:
            return "Не можна без масштабування"

    def coef(self):
        self.pic_h = int(input('Введіть довжину картинки в пікселях: '))
        self.pic_w = int(input('Введіть ширину картинки в пікселях: '))
        self.woutprop1 = self.height / self.pic_h
        self.woutprop2 = self.width / self.pic_w
        if self.pic_h > self.pic_w:
            self.wprop = self.width / self.pic_w
        else:
            self.wprop = self.height / self.pic_h
        return 'Без збереження пропорцій, коефіцієнт: {0}. Із збереженням пропорцій, коефіцієнт: {1}'.format([self.woutprop1, self.woutprop2],
                                                                                     [self.wprop, self.wprop])


A = Monik()
print(A.calculate_age())
print(A.pic())
print(A.coef())
