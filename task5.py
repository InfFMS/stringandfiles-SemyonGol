# Откройте текстовый файл task5.txt для чтения.
# Найдите самое длинное слово в тексте. Если таких слов несколько, выберите первое из них.
# Запишите это слово и его длину в новый файл в формате:
# Самое длинное слово: слово
# Его длина: длина
#
# Выведите это слово и длину в консоль.

with open('task5.txt', encoding='utf-8') as file:
    ln = file.read()
ln = ln.split()
maxw = ln[0]
maxv = len(ln[0])
for i in range(len(ln) - 1):
    for x in range(1, len(ln)):
        if len(ln[x]) > len(ln[i]):
            maxw = str(ln[x])
            maxv = str(len(ln[x]))
new = 'Самое длинное слово: ' + maxw + '\n'
new += 'Его длинна: ' + maxv
with open('fifth_task.txt', 'w',encoding='utf-8') as file:
    for s in [new]:
        file.write(s)