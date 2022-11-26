coordinates = ['x', 'y', 'z']
a=[]
for i in range(3):
    a.append(input(f'Введите значение {coordinates[i]}: '))
left = not (a[0] or a[1] or a[2])
right = not a[0] and not a[1] and not a[2]
if left == right:
    print("Утверждение истинно")
else:
    print("утверждение ложно")