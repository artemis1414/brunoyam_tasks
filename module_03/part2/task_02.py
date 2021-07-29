from random import randint

n = int(input('Введите размер матрицы целым числом: '))
m = [[randint(0, 100) for i in range(n)] for j in range(n)]
max_number = m[0][0]
for row in m:
    for element in row:
        max_number = max(element, max_number)
print(m)  # check result
print('Максимальный элемент матрицы:', max_number)
