num = int(input('Введите число '))
fact = 1
for i in range(1, num+1):
   fact *= i
   print(f'{fact}', end = ' ')
