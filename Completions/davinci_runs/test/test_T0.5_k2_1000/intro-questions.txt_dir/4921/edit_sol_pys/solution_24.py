
words = []

while True:
    try:
        line = input()
        words.extend(line.split())
    except EOFError:
        break

unique = []
for word in words:
    if word not in unique:
        unique.append(word)
        print(word, end=' ')
    else:
        print('.', end=' ')
print()
