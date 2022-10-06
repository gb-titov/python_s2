#Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

def get_sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += (1 + 1 / i)**i
    return sum


num = int(input('Введите целое число: '))

print(f'{num} => {get_sum(num)}')
