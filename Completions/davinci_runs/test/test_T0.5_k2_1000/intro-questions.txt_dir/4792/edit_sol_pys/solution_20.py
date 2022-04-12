
word = input()

print(word[0], end='') # печатаем первую букву
for i in range(1, len(word)):
    if word[i-1] != word[i]: # если предыдущая буква не равна текущей, то печатаем текущую
        print(word[i], end='')
