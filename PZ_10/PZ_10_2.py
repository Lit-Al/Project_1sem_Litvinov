# Из предложенного текстового файла (text18-12.txt) вывести на экран его содержимое,
# количество пробельных символов. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно вставив после каждой строки строку из символов
# «*».
f = open('text18-12.txt', 'r', encoding='utf-8')  # открываю файлы через кодировку ютф-8, чтобы избежать проблем
# вывожу содержимое файла
print(*f)
f = open('text18-12.txt', 'r', encoding='utf-8')
# находим пробелы
count = f.read().count(' ')
print('')
print('Количество пробелов в файле:', count)
f.close()
# открываю один для чтения, другой для записи(файлы)
f = open('text18-12.txt', 'r', encoding='utf-8')
f1 = open('my_file.txt', 'w', encoding='utf-8')
f1.write(f.read())  # переношу текст в другой файл

with open('my_file.txt', 'r', encoding='utf-8') as f:
    with open('my_file.txt', 'w', encoding='utf-8') as f1:
        count1 = 0
        for line in f:
            count1 += 1
            if count1 < 7:
                f1.write(line)
                f1.write('*** \n')
            else:
                f1.write(line)
                f1.write('\n***')






