class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Автомобиль {self.name} начал движение')

    def stop(self):
        print(f'Автомобиль {self.name} остановился')

    def turn(self, direction):
        self.direction = direction
        print(f'Автомобиль {self.name} повернул {self.direction}')

    def show_speed(self):
        print(f'Скорость автомобиля: {self.speed} км/час')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Вы превышаете допустимую скорость на {self.speed - 60} км/час')
        else:
            print(f'Скорость автомобиля: {self.speed} км/час')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Вы превышаете допустимую скорость на {self.speed - 40} км/час')
        else:
            print(f'Скорость автомобиля: {self.speed} км/час')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


bmw = TownCar(80, 'white', 'X5')
print(vars(bmw))
bmw.go()
bmw.stop()
bmw.turn('направо')
bmw.show_speed()
print()

ferrari = SportCar(180, 'red', 'enzo')
print(vars(ferrari))
ferrari.go()
ferrari.stop()
ferrari.turn('налево')
ferrari.show_speed()
print()

mazda = WorkCar(80, 'blue', 'six')
print(vars(mazda))
mazda.go()
mazda.stop()
mazda.turn('направо')
mazda.show_speed()
print()

volkswagen = PoliceCar(100, 'white', 'polo')
print(vars(volkswagen))
volkswagen.go()
volkswagen.stop()
volkswagen.turn('налево')
volkswagen.show_speed()
