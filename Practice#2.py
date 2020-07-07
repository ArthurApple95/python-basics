# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.


class OwnNullError(Exception):
    def __init__(self, txt):
        self.txt = txt


a = int(input('Give number #one: '))
b = int(input('Give number #two: '))

try:
    if b == 0:
        raise OwnNullError("Can't divide by 0")
    res = a / b
except OwnNullError as lol:
    print(lol)
else:
    print(f"Results is {res}")
finally:
    print("Good bye")
