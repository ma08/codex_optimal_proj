words = []

while True:
    line = input()
    words.extend(line.split())
unique = []
for word in words:
    if word.lower() not in unique:
        unique.append(word.lower())
        print(word, end=' ')
    else:
        print('.', end=' ')
print()
