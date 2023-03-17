# HomeWork 1
 ##### Задача 2: 
 Найдите сумму цифр трехзначного числа. 

 *Пример:* 
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) 


*** Рассмотрите случай числа с плавающей точкой и не обязательно 3-х значного

```python
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
```
#### Задача 4: 
Петя, Катя и Сережа делают из бумаги журавликов.
Вместе они сделали S журавликов.
Сколько журавликов сделал каждый ребенок, если известно,
что Петя и Сережа сделали одинаковое количество журавликов,
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

*Пример:*
6 -> 1  4  1
24 -> 4  16  4
    60 -> 10  40  10


******Рассмотрите вариант, что он также делают журавлики
в момент подсчета и известно только число уже полностью готовых

```python
# -1-1-1-1  катя
# -0-0-0-1  петя
# -0-0-0-1  сережа
def inputInt(message):
    return int(input(message))

number = inputInt("Введите количество готовых журавликов: ")

if number % 6 == 0:
    nKatya = number // 6 * 4
    nPetya = nSerezha = number // 6
else:
    nKatya = number // 6 * 4 + number % 6
    nPetya = nSerezha = number // 6
print(f"Катя собрала {nKatya} штук. А Петя с Cережой по {nPetya} каждый.")
```
#### Задача 6: 
Вы пользуетесь общественным транспортом?
Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером,
где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no

 ******** Рассмотрите вариант разделения на правую и левую часть произвольно,
но не меняя порядок цифр.
```python
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
                print(f"Ваш билет счастливый пополам {num[0:6 - x:1]} | {num[6 - x::1]} ")
            else:
                print(f"Ваш билет счастливый по частям {num[0:6 - x:1]} | {num[6 - x::1]}  ")
    if not luck:
        print("Ваш билет оказался несчатливым")

number = input_int("Введите номер билета (6 знаков): ")
check_luck(number)
```
#### Задача 8: 
Требуется определить,
можно ли от шоколадки размером n × m долек отломить k долек,
если разрешается сделать один разлом по прямой между дольками
(то есть разломить шоколадку на два прямоугольника).

*Пример:*

3 2 4 -> yes
3 2 1 -> no
```python
def input_int(message):
    input_error: bool = True
    while input_error:
        try:
            temp = int(input(message))
        except ValueError:
            print("Вы ввели не число!")
        else:
            input_error = False
    return temp

a = input_int("Введите длинну (количество долек) шоколада: ")
b = input_int("Введите ширину (количество долек) шоколада: ")
c = input_int("Введите желаемое количество долек: ")

if a * b == c:
    print("Не нужно ломать - забирайте целиком")
elif a * b < c:
    print("В шоколадке нет столько долек =(")
elif c % a == 0 and c // a < b:
    print(f"Отломите после {c // a} долек по ширине")
elif c % b == 0 and c // b < a:
    print(f"Отломите после {c // b} долек по длинне")
else:
    print("Столько долек отломать не получится")
```