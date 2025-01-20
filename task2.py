# Откройте текстовый файл task2.txt для чтения.
# Считайте его содержимое в строку.
# Найдите и замените все вхождения слова "Python" на слово "Питон" (регистр учитывать).
# Запишите обновленный текст в новый файл с другим именем.
# Выведите на экран сообщение о количестве произведённых замен.

with open('task2.txt', encoding='utf-8') as f:
    ln = f.read()
ln = ln.split()
c = 0
for i in range(len(ln)):
    if ln[i] == 'python':
        ln[i] = 'питон'
    elif ln[i] == 'Python':
        ln[i] = 'Питон'
        c += 1
lnew = ''
for i in range(len(ln)):
    lnew += ln[i]
    lnew += ' '
with open('second_task.txt', 'w', encoding='utf-8') as f:
    for s in [lnew]:
        f.write(s)
print(c)