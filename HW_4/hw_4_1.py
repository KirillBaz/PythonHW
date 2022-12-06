import math
acc = float(input('Введите точность отображения числа пи (отрицательная целая степень десятки) '))
acc1 = 0
while acc < 1:
    acc*=10
    acc1+=1
print(round(math.pi, acc1))

