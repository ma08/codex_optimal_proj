

word = input()

print(word[0], end='')
for i in range(1, len(word)):
    if word[i-1] != word[i]:
        print(word[i], end='')