# Напишите программу, которая просит пользователя ввести несколько предложений (например, 5, каждое предложение с новой строки).
# Каждое введенное предложение записывается в файл, но:
# Слова во всех предложениях должны быть приведены к верхнему регистру.
# Между словами вместо пробела ставится символ "_".
# После записи откройте этот файл, считайте содержимое и выведите его на экран.
print('Enter one sentence:', end=' ')
sentence = input()
while sentence != '':
    sentence = sentence.upper()
    sentence = sentence.split()
    new = ''
    for i in range(len(sentence)):
        new += sentence[i] + '_' + '\n'
    with open('forth_task.txt', 'a', encoding='utf-8') as file:
        for s in [new]:
            file.write(s)
    print('Enter one sentence: (enter empty string if you want to end)', end=' ')
    sentence = input()
print('Thanks for using that program!')