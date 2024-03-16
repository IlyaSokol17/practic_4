a = input('Введите счет игры через разделитель(:) - ')
t_1 = int(a[0])
t_2 = int(a[2])
if t_1 > t_2:
    print(1)
elif t_1 < t_2:
    print(2)
elif t_1 == t_2:
    print(0)