class TypeDigitError(Exception):
    def __init__(self, txt):
        self.txt = txt


userList = []
a = None
while a != "stop":
    a = input('Введите число для списка или введите stop для завершения: ')
    try:
        for i in a:
            if ord(i) > 57 or ord(i) < 48:
                raise TypeDigitError("Not a digit, can't add it")
        b = int(a)
        userList.append(b)
    except TypeDigitError as lol:
        print(lol)
print(userList)
