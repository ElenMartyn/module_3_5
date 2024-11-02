def get_multiplied_digits(number):

    str_number = str(number) # строковое представление числа number

    if len(str_number) <= 1: #  проверяем больше ли 1 длина строки
        return int(str_number)

    first = int(str_number[0]) # отделение первой цифры в числе
    return first * get_multiplied_digits(int(str_number[1:])) # умножаем первую цифру числа на результат работы этой же функции с числом, но уже без первой цифры

result = get_multiplied_digits(40203)
print(result)
result = get_multiplied_digits(402033005)
print(result)
result = get_multiplied_digits(2300507901)
print(result)
