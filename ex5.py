# Реализуйте алгоритм перемешивания списка 
# (метод random.shuffle использовать нельзя, 
# но другие методы из библиотеки random - можно).
import random

lst = [1, 2, 3, 4, 5, 6, 7]

def shuffle(lst):
    for i in range(0, len(lst)):
        tmp = lst[i]
        r = random.randint(0, len(lst) - 1)
        lst[i] = lst[r]
        lst[r] = tmp
    return lst


print(f'{lst} => {shuffle(lst)}')
