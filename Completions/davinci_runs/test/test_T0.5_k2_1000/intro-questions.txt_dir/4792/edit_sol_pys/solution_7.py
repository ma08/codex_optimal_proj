
word = input() # вводим слово

print(word[0], end='') # выводим первую букву

for i in range(1, len(word)):
    if word[i-1] != word[i]:
        print(word[i], end='')
