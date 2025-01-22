with open('task3.txt', encoding='utf-8') as f:
    ln = f.read()
ln = ln.lower()
ln = ln.split()
print(ln)