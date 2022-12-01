# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
def binary_system(num):
    result=''
    while num>=1:
        result+=str(num%2)
        num//=2
    return result[::-1]

print(binary_system(143))

