t = int(input('Введите время: '))
u = int(input('Введите скорость: '))
s = 109
s1 = u * t
if s1 >= s:
    s1 = s1 % s
print('Искомое расстояние: ', s1, ' км')
