# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 0,56 -> 11

num = input('Введите вещественное число --> ')
left_right=num.split('.')
left = left_right[0]
right = left_right[1]
l_d=int(left)
r_d=int(right)
l_sum=0
r_sum=0
while l_d>0:
    l_sum+=l_d%10
    l_d=l_d//10
while r_d>0:
    r_sum+=r_d%10
    r_d=r_d//10
print(r_sum+l_sum)
