# 1.	Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
#	6782 -> 23
#	0,56 -> 11

def get_digit_sum(number):
    number = number.replace(".", "", 1).replace(",","",1)
    sum = 0
    for i in range(len(number)):
        sum += int(number[i])
    return sum


num = input("Введите число: ")
digits_sum = get_digit_sum(num)

print(f'{num} -> {digits_sum}')
