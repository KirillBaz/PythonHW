x = int(input("Введите абсциссу точки "))
y = int(input("Введите ординату точки "))
if y>0:
    if x>0:
        print("точка находится в первой четверти")
    else:
        print("Точка находится во второй четверти")
if y<0:
    if x>0:
        print("точка находится в четвертой четверти")
    else:
        print("Точка находится в третьей четверти")