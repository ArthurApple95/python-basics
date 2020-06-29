# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep


class TrafficLight:
    count = 0

    def __init__(self):
        self.__colour = ["Red", "Yellow", "Green"]

    def running(self, count):
        print(self.__colour[int(count)])
        if int(count) % 2 == 0:
            sleep(7)
        else:
            sleep(2)


a = TrafficLight()
i = 0
timesLimit = int(input('How many colour changes would you like? '))
times = 0
while times < timesLimit:
    a.running(i)
    i += 1
    if i == 3:
        i = 0
    times += 1
