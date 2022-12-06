# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def deliteli(num):
    dltl = []
    for i in range(1, num+1):
        if num % i == 0:
            dltl.append(i)
    return(dltl)
    
def simple_del(num1):
    prostie_deliteli = []
    dlt = deliteli(num1)
    for j in dlt:
        if deliteli(j) == [1] or deliteli(j)==[1,j]:
            prostie_deliteli.append(j)
    return prostie_deliteli
print(simple_del(42))