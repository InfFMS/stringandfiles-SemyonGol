with open('task3.txt', encoding='utf-8') as f:
    ln = f.read()
ln = ln.lower()
ln = ln.split()
print(ln[5])
if ln[5].endswith('.'):
    ln[5] = ln[5].replace('.', '')
print(ln[5])