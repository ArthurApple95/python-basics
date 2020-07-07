class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print(f'Сумма комплексных чисел:')
        return f'z = {self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        print(f'Произведение комплексных чисел:')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a}i'

    def __str__(self):
        return f'z = {self.a} + {self.b}i'


print('Пожалуйста, предоставьте два комплексных числа в формате a + bi \n')
a = int(input('Введите действительную часть первого комплексного числа: '))
b = int(input('Введите мнимую часть первого комплексного числа: '))
z_1 = ComplexNumber(a, b)
print(f'Комплексное число #1: {z_1} \n')
a2 = int(input('Введите действительную часть второго комплексного числа: '))
b2 = int(input('Введите мнимую часть второго комплексного числа: '))
z_2 = ComplexNumber(a2, b2)
print(f'Комплексное число #2: {z_2} \n')
print(f'{z_1 + z_2} \n')
print(z_1 * z_2)