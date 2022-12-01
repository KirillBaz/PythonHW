# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19
a = [1.1, 1.2, 3.1, 10.01]

def max_part(list_):
    maximum=0
    for i in range(len(list_)):
        if list_[i]%1>maximum:
            maximum=list_[i]%1
    return maximum

def min_part(list_):
    minimum=1
    for i in range(len(list_)):
        if list_[i]%1<minimum:
            minimum=list_[i]%1
    return minimum

print(round(max_part(a)-min_part(a), 3))

