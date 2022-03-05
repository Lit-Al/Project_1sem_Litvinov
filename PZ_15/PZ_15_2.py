# В матрице найти отрицательные элементы, сформировать из них новый массив.
# Вывести размер полученного массива
from random import randint

matric = [[randint(-2, 2) for i in range(1, 4)] for j in range(3)]  # создаём матрицу 3х3
print(*matric, sep='\n')
p = []

for i in range(len(matric)):
    for j in range(len(matric[0])):  # ищем отрицательные элементы
        if matric[i][j] < 0:
            p.append(matric[i][j])  # вносим отрицательные элементы в список
print('Отрицательные элементы:', p)
print('Кол-во отрицательных элементов:', len(p))