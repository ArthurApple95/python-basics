# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.

class Date():
    @classmethod
    def extraction(cls, param):
        day = int((param.split('-')[0]))
        month = int((param.split('-')[1]))
        year = int((param.split('-')[2]))
        return day, month, year

    @staticmethod
    def validation():
        if Date.extraction(userDate)[0] > 31 or Date.extraction(userDate)[0] == 0:
            print('day is wrong')
        else:
            if Date.extraction(userDate)[1] > 12 or Date.extraction(userDate)[1] == 0:
                print('month is wrong')
            else:
                print(
                    f'All good, day is {Date.extraction(userDate)[0]}, month is {Date.extraction(userDate)[1]}, year is {Date.extraction(userDate)[2]}')


userDate = input('Please input the date in DD-MM-YYYY format: ')
Date().extraction(userDate)
Date().validation()
