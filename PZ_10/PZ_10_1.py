# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Максимальный элемент:
# Среднее арифметическое элементов первой трети:

lst = [10, 9, 2, 4, -3, 33, -32, 1, -6]  # последовательность из целых положительных и отрицательных чисел.

t = open('xml.txt', 'w', encoding='utf-8')  # открываю файл для записи и вношу последовательность
print(*lst, file=t)
t.close()

t1 = open('xml2.txt', 'w', encoding='utf-8')  # открываю файл для записи
t1.write(f'Исходные данные: {str(lst)}\n')
t1.write(f'Количество элементов: {len(lst)}\n')
t1.write(f'Максимальный элемент: {max(lst)}\n')
t1.write(f'Среднеее арифметическое элементов первой трети: {sum(lst[:3]) / len(lst[:3])}')
t1.close()


