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
        return 2021 - self.date3
    def pic(self):
        self.pic_h =  int(input('Введіть довжину картинки : '))
        self.pic_w = int(input('Введіть ширину картинки : '))
        if self.pic_h >= self.height and self.pic_w >= self.width:
            return "Можна"
        else:
            return "Не можна"
    def coef(self):
        if self.pic_h == self.height and self.pic_w == self.width:
            self.coef.h = self.height/self.pic_h
            self.coef.w = self.width/self.pic_w
            return [self.coef.h,self.coef.w]
A = Monik()
print(A.pic())

