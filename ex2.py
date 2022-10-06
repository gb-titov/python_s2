# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def MultiplyDigits(digit):
    lst = []
    tmp = 1
    for i in range(1,digit+1):
        tmp *= i
        lst.append(tmp)
    return lst


num = int(input("Введите число: "))

print(f'{num} => {MultiplyDigits(num)}')
