# Откройте текстовый файл для чтения task1.txt.
# Подсчитайте:
# Общее количество строк в файле.
# Общее количество слов во всем тексте файла.
# Общее количество символов (включая пробелы).
# Выведите полученную статистику на экран.

with open('task1.txt', encoding='utf-8') as f:
    ln = f.read()

def st(A):
    A = str(A.split('—'))
    i, n = 0, 1
    while A[i] != ']':
        if A[i] == '\\'  and A[i+1] == 'n':
            n += 1
        i += 1
    return n
ln = ln.split

print(st(ln), k, len(ln))