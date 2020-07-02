import numpy as np


class Matrix:
    def __init__(self, *args):
        self.args = args
        self.args = np.array(self.args)

    def __str__(self):
        return f"{self.args}"

    def __add__(self, other):
        return Matrix(self.args + other.args)


readyMatrix = Matrix([10, 2, 30], [3, 40, 50], [50, 60, 7])
readyMatrix2 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
readyMatrix3 = readyMatrix + readyMatrix2
print(readyMatrix3)
