# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
def fibonacci_full(num):
    fib = [1, 1]
    for i in range(2,num):
        fib.append(fib[i-2]+fib[i-1])
    neg_fib = fib[::-1]
    for j in range(0, len(neg_fib), 2):
        neg_fib[j] *= -1
    neg_fib.append(0)
    return neg_fib+fib
print(fibonacci_full(8))