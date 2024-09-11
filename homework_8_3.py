class Car:

    def __init__(self, model, __vin_numbers, __numbers):
        self.model = model
        self.vin_numbers = __vin_numbers
        self.numbers = __numbers
        self.__is_valid_vin(self.vin_numbers)
        self.__is_valid_numbers(self.numbers)

    def __is_valid_vin(self, vin_numbers):
        if isinstance(vin_numbers, int):
            if vin_numbers >= 1000000 and vin_numbers <= 9999999:
                return True
            else:
                raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            raise IncorrectVinNumber('Некорректный тип vin номера')

    def __is_valid_numbers(self, numbers):
        if isinstance(numbers, str):
            if len(numbers) == 6:
                return True
            else:
                raise IncorrectCarNumbers('Неверная длина номера')
        else:
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')




class IncorrectVinNumber(Exception):

    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):

    def __init__(self, message):
        self.message = message


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')

