

words = [] # words[0] -> first word in list

while True:
    try:
        line = input()
        words.extend(line.split()) # adds words from line to words list
    except EOFError:
        break

unique = [] # unique[0] -> first unique word in list
for word in words:
    if word.lower() not in unique:
        unique.append(word.lower())
        print(word, end=' ')
    else:
        print('.', end=' ')
print()
