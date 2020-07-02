class Cell:
    def __init__(self, num=0):
        self.cells_num = num

    def __str__(self):
        return f'Кол-во ячеек новой клетки: {self.cells_num}'

    def __add__(self, other):
        new_cell = Cell()
        new_cell.cells_num = self.cells_num + other.cells_num
        return new_cell

    def __sub__(self, other):
        new_cell = Cell()
        new_cell.cells_num = self.cells_num - other.cells_num
        if self.cells_num > other.cells_num:
            return new_cell
        else:
            return f'Нельзя разделить клетки'

    def __mul__(self, other):
        new_cell = Cell()
        new_cell.cells_num = self.cells_num * other.cells_num
        return new_cell

    def __truediv__(self, other):
        new_cell = Cell()
        new_cell.cells_num = self.cells_num // other.cells_num
        return new_cell

    def make_order(self, row):
        result = ''
        for i in range(int(self.cells_num/row)):
            result += f'{"*" * row}\n'
        result += f'{"*" * (self.cells_num % row)}'
        return result


a = 15
a = Cell(a)

b = 3
b = Cell(b)

c = 2
c = Cell(c)

d = a + b + c
print(d)

d = a - b - c
print(d)

d = a * b * c
print(d)

d = a / b / c
print(d)

print()
print(a.make_order(4))