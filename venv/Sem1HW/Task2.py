# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |
# *** Рассмотрите случай числа с плавающей точкой и не обязательно 3-х значного

def input_num(message):
    input_error: bool = True
    while input_error:
        try:
            temp = float(input(message))
        except ValueError:
            print("Вы ввели не число!")
        else:
            input_error = False
    return temp


def Summa(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


number = input_num("Введите число: ")
print('Сумма цифр равна ', end=' ')
print(Summa(int(number)) + Summa(int(str(number).split(".")[1])))
