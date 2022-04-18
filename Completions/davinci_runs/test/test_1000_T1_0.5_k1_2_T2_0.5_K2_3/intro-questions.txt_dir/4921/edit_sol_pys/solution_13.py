

words = []

while True:
    try:
        line = input()
        words.extend(line.split())
    except EOFError:
        break

unique = []
for word in words:
    if word.lower() not in unique:
        unique.append(word.lower())
        print(word, end=' ')
    elif word == '.' or word == ',' or word == '!' or word == '?':
        print(word, end=' ')
print()
