# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no
# ******** Рассмотрите вариант разделения на правую и левую часть произвольно,
# но не меняя порядок цифр.


def input_int(message):
    input_error: bool = True
    while input_error:
        try:
            str_temp = input(message)
            temp = int(str_temp)
        except ValueError:
            print("Вы ввели не число!")
        else:
            if len(str_temp) == 6:
                input_error = False
            else:
                print('Введите 6 значное число')
    return str_temp


def Summa(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return s


def check_luck(num):
    luck = False
    for x in range(1, 5):
        if Summa(int(num) // 10 ** x) == Summa(int(num) % 10 ** x):
            luck = True
            if x == 3:
                print(f"Ваш билет счастливый пополам {num[0:6-x:1]} | {num[6-x::1]} ")
            else:
                print(f"Ваш билет счастливый по частям {num[0:6-x:1]} | {num[6-x::1]}  ")
    if not luck:
        print("Ваш билет оказался несчатливым")

number = input_int("Введите номер билета (6 знаков): ")
check_luck(number)
