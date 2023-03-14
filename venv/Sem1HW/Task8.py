# # Задача 8: Требуется определить,
# # можно ли от шоколадки размером n × m долек отломить k долек,
# # если разрешается сделать один разлом по прямой между дольками
# # (то есть разломить шоколадку на два прямоугольника).
# #
# # *Пример:*
# #
# # 3 2 4 -> yes
# # 3 2 1 -> no
#
# def input_int(message):
#     input_error: bool = True
#     while input_error:
#         try:
#             temp = int(input(message))
#         except ValueError:
#             print("Вы ввели не число!")
#         else:
#             input_error = False
#     return temp
#
#
# a = input_int("Введите длинну (количество долек) шоколада: ")
# b = input_int("Введите ширину (количество долек) шоколада: ")
# c = input_int("Введите желаемое количество долек: ")
#
# if a * b == c:
#     print("Не нужно ломать - забирайте целиком")
# elif a * b < c:
#     print("В шоколадке нет столько долек =(")
# elif _ in (a, b) % c == 0 or c % _ in (a, b) == 0:
#     print("Да - можно")
# #
# # elif c % a == 0 and c // a < b:
# #     print(f"Отломите после {c // a} долек по длинне")
# # elif a >= c:
# #     if a % c == 0:
# #         print(f"Отломите после {a // c} долек по длинне")
# #
# # elif a % c == 0 and a // c < b:
# #     print(f"Отломите после {a // c} долек по длинне")
# # elif c % b == 0 and c // b < a:
# #     print(f"Отломите после {c // b} долек по ширине")
# # elif b % c == 0 and b // c < a:
# #     print(f"Отломите после {b // c} долек по ширине")
# else:
#     print("Столько долек отломать не получится")

n, m, k = [int(input()) for _ in '123']
print('YES' if k < n * m and ((k % n == 0) or (k % m == 0)) else 'NO')
