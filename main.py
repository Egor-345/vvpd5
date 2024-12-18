import math


def my_input(value_type, input_message, error_message):
    while True:
        value = input(input_message)
        if value.startswith("-") and value_type not in (int, float):
            print('Ошибка: введённое значение не может быть отрицательным.')
            continue
        try:
            value = value_type(value)
            if (value_type == int or value_type == float) and value < 0:
                print('Ошибка: введённое значение должно быть больше или равно нулю.')
                continue
            break
        except (ValueError, TypeError):
            print(error_message)
            continue
    return value


def sin(x):
    sinx = 0
    for i in range(50):
        sinx += ((-1) * i) * (x * (2 * i + 1)) / math.factorial(2 * i + 1)
    return round(sinx, 2)


def ln(x):
    if x <= -1 or x > 1:
        return "Ошибка: x должно быть в интервале (-1, 1]"
    lnx = 0
    for i in range(1, 50):
        lnx += ((-1) * (i + 1)) * (x * i) / i
    return round(lnx, 2)


def arctg(x):
    if x < -1 or x > 1:
        return "Ошибка: x должно быть в интервале [-1, 1]"
    arctgx = 0
    for i in range(50):
        arctgx += ((-1) ** i) * (x ** (2 * i + 1)) / (2 * i + 1)
    return round(arctgx, 2)


def menu():
    while True:
        print('\n---Меню---')
        print('1. Функция sinx')
        print('2. Функция ln(1+x)')
        print('3. Функция arctgx')
        print('0. Выход.')
        choice = input('Сделайте выбор: ')

        if choice == '0':
            break

        if choice in ('1', '2', '3'):
            while True:
                x = my_input(float, 'Введите x: ', 'Неверный тип данных.')
                if choice == '2' and (x <= -1 or x >= 1):  # исправлено условие
                    print('Ошибка: Для ln(1+x) x должен быть в интервале (-1; 1]')
                    continue
                if choice == '3' and (x < -1 or x > 1):
                    print('Ошибка: Для arctg(x) x должен быть в интервале [-1; 1]')
                    continue
                break

            if choice == '1':
                result = sin(x)
                print(f"sin({x}) = {result}")
            elif choice == '2':
                result = ln(x)
                print(f"ln(1 + {x}) = {result}")
            elif choice == '3':
                result = arctg(x)
                print(f"arctg({x}) = {result}")
        else:
            print('Неверный выбор.')


if __name__ == "__main__":
    menu()
