def maximum(queue): # функция для нахождения максимального элемента
  m = next(queue) # след. элемент очереди (первый)
  for i in queue: # проход по очереди
    if i > m:
      m = i
  return m

def edit(arr): # функция для форматирования элементов столбца
    for i in range(len(arr[0])): #  проход по столбцам матрицы
        max_len = maximum(map(lambda x: len(x[i]), arr)) # нахождение длины самого длинного элемента в столбце
        for r in arr: # проход по всем строкам матрицы
            r[i] = '| ' + r[i].center(max_len) + " " # выравнивание элемента массива по самому длинному элементу

journal = [row.replace('|', ' ').split() for i, row in enumerate(open('/Users/skooff/Projects/py_practice/j.txt', 'r')) if i % 2 == 1]
# ^ проход по всем нечётным строкам таблицы и запись их в виде матрицы
print('Таблица была считана')
journal_edited = input("Введите название предмета и оценки всех учеников по нему через пробел (23 ученика): ").split()
# ^ массив с новыми данными
position = int(input("Введите номер позиции, на которой должен распологаться предмет: ")) + 1
# ^ позиция нового столбца
for i in range(len(journal)): # проход по всем строкам матрицы
    journal[i].insert(position, journal_edited[i]) # вставка эллементов по индексу-позиции
edit(journal) # форматирование добавленного столбца
with open('journal_edited.txt', 'w') as new: # создание новой таблицы
    row = ''.join(journal[0]) # преобразуем массив обратно в строку
    print('-' * len(row) + '-', file = new, sep = '') # добавление верхнего горизонтального разделителя
    for i in journal: # проход по всем строкам таблицы
        row = ''.join(i) + '|' # преобразуем массив в строку таблицы
        print(row, file = new) # печатаем её
        print('-' * len(row), file = new, sep = '') # добавляем горизонтальный разделитель снизу