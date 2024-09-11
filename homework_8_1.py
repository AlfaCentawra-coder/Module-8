def add_everything_up(a, b):
    try:
        c = a + b
        return c
    except TypeError:
        if type(a) == int or type(a) == float:
            a = str(a)
        if type(b) == int or type(b) == float:
            b = str(b)
        result = a + b
        return result
    finally:
        print('Программа выполнена! Хорошего дня!')

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))