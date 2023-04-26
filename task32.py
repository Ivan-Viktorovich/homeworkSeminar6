# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

from random import randint

arr = list(randint(-10, 10) for i in range(int(input("Введите размер массива: "))))
print(arr)
a = int(input("От: "))
b = int(input("До: "))
arr2 = []
for i in range(len(arr)):
    if arr[i] >= a and arr[i] <= b:
        arr2.append(i)
print(arr2)
