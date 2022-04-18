words = [] # empty list

while True:
    try:
        line = input()
        words.extend(line.split()) # split the line into words and add to the list
    except EOFError:
        break
unique = [] # empty list
for word in words:
    if word.lower() not in unique: # compare the word with all lowercase letters
        unique.append(word.lower()) # add the word to list
        print(word, end=' ') # print the word
    else:
        print('.', end=' ') # print a dot
print()
