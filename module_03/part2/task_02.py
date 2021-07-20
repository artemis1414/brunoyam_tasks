from random import randint

n = int(input('Введите размер матрицы целым числом: '))
m = [[randint(0, 100) for i in range(n)] for j in range(n)]
max_number = 0
for i in m:
    for j in i:
        if j > max_number:
            max_number = j
print(m)  # check result
print('Максимальное элемент матрицы:', max_number)
