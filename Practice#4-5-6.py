class Warehouse:
    def __init__(self):
        self.my_warehouse = []

    def receipt(self, item):
        self.my_warehouse.append(item)

    def __str__(self):
        return f'{self.my_warehouse}'


class OrgStuff:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.unitInfo = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}


class Printer(OrgStuff):
    pass


class Scanner(OrgStuff):
    weight = "20 kg"


class Computer(OrgStuff):
    prodYear = 2015


# Готовим склад
listWH = Warehouse()

# Создаём товары
unit1 = Printer('HP', 2000, 1)
unit2 = Computer('Dell', 5500, 2)

# Добавляем товар на склад
listWH.receipt(unit1.unitInfo)
listWH.receipt(unit2.unitInfo)
print(listWH)

# Отправляем товар со склада по одной единице товара в офис
listWH.my_warehouse[0].update({'Количество': (listWH.my_warehouse[0].get('Количество') - 1)})
listWH.my_warehouse[1].update({'Количество': (listWH.my_warehouse[1].get('Количество') - 1)})

print(listWH)

# Очень долго не мог уловить  суть. Как понял (на часах 3:30), накидал каркас. Можно навести красоту,
# дать пользователю через циклы while выбирать, сколько товаров и в каком количестве закупать на склад в зависимости
# от значений в ветке if. Сколько каких товаров в каком количестве отправлять в какие места. Ну и седьмое задание
# можно, конечно, сделать, добавив try except во все инпуты. Но это всё мелочи, на которые, после понимания основных
# принципов, нет желания сейчас тратить время, зная, что Я могу их сделать. Так что справедливо согласен на оценку ниже.
# Благодарю за курс
