num = int(input("Введите номер координатной четверти (1-4) "))
str = "x от {} до {}, y от {} до {}"
a = [0, "-infinity", "+infinity"]
if num == 1:
   print(str.format(a[0],a[2],a[0],a[2]))
elif num == 2:
    print(str.format(a[0],a[1],a[0],a[2]))
elif num == 3:
    print(str.format(a[0],a[1],a[0],a[1]))
else:
    print(str.format(a[0],a[2],a[0],a[1]))