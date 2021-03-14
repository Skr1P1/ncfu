print('Составьте линейное уравнение ax+b=0')
a = float(input('Введите a -->'))
b = float(input('Введите b -->'))
if a != 0:
    x = (b*-1)/a
    print('Корень уравнения:', x)
else:
    print('Нет корней')