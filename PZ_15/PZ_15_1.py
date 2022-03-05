# В матрице найти сумму и произведение элементов столбца N (N задать с
# клавиатуры)
from random import randint

matric = [[randint(0, 2) for i in range(1, 4)] for j in range(3)]  # создаём матрицу 3х3
print(*matric, sep='\n')
N = int(input('Введите номер столбца: '))

summa = 0
mult = 1

for i in range(0, len(matric)):  # находим элементы столбца
    p = (matric[i][N - 1])
    print('Элемент столбца:', p)
    summa += p  # суммируем элементы
    mult *= p   # перемножаем элементы

print('Сумма элементов столбца:', summa)
print('Произведение элементов столбца:', mult)