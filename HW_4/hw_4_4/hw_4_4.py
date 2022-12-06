# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 10) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.
import random
path = r'C:\Users\Кирилл\Documents\Учеба\python\PythonHW\HW_4\hw_4_4\result.txt'
def polynomial(k):
    while k>0:
        with open(path, 'a') as data:
            data.write(f'{random.randint(1, 10)}*(x**{k})+')
        k-=1
    with open(path, 'a') as data:
        data.write(f'{random.randint(1,100)} = 0')
polynomial(4)

