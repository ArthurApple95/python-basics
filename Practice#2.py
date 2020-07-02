class Clothes:
    def __init__(self, v):
        self.v = v

    def __add__(self, other):
        return f'Общий расход ткани для изготовления пальто и костюма составит: {round(self.amount + other.amount)} ' \
               f'метров/-а '

class Abrigo(Clothes):
    @property
    def amount(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):
    @property
    def amount(self):
        return 2 * self.v + 0.3


a = int(input("Укажите размер для пальто: "))
b = int(input("Укажите рост для костюма: "))

coat = Abrigo(a)
suit = Suit(b)

print(coat+suit)