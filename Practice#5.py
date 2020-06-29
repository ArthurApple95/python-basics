# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
# (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
# классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.


class Stationery:
    title = "зачем он здесь нужен?"

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Чиркаем ручкой")


class Pencil(Stationery):
    def draw(self):
        print("Обводим карандашом")


class Handle(Stationery):
    def draw(self):
        print("Закрашиваем маркером")


item1 = Pen()
item1.draw()

item2 = Pencil()
item2.draw()

item3 = Handle()
item3.draw()
