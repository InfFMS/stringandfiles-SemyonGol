# Откройте текстовый файл task3.txt для чтения.
# Извлеките все уникальные слова из файла (слова разделяются пробелами и знаками пунктуации).
# Подсчитайте, сколько раз каждое уникальное слово встречается в тексте.
# Запишите результаты в новый файл в формате:
# слово1: количество
# слово2: количество
#
# Убедитесь, что слова записаны в алфавитном порядке.
import numpy as np
with open('task3.txt', encoding='utf-8') as f:
    ln = f.read()
ln = ln.lower()
ln = ln.split()
ln = np.array(ln)
unic = np.unique(ln, return_counts=True)
words = unic[0]
numb = unic[1]
lnew = ''
for i in range(len(words)):
    lnew = (lnew + words[i] + ': ' + str(numb[i])) + '\n'
with open('third_task.txt', 'w', encoding='utf-8') as f:
    for s in [lnew]:
        f.write(s)