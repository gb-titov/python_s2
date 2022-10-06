# Задайте список из N элементов, 
# заполненных числами из промежутка [-N, N] (например, [-3, -2, 1, 0, 1, 2, 3]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

def fill_list(n):
    lst = []
    for i in range(-n, n+1):
        lst.append(i)
    return lst


def read_file(file_name):
    lst = []
    f = open('ex4.txt', 'r')
    for ln in f:
        lst.append(int(ln))
    f.close()
    return lst


def multiply_elements(lst_base, lst_index):
    m = 1
    for i in lst_index:
        m*=lst_base[i]
    return m


num = int(input('Введите N: '))

lst = fill_list(num)
idx = read_file('ex4.py')

print(f'{lst} => {idx} => {multiply_elements(lst, idx)}')
