
luka = input()

words = luka.split()

for i in range(len(words)):
    word = words[i]
    decoded = ''

    for j in range(0, len(word), 2):
        decoded += word[j]

  words[i] = decoded

print(' '.join(words))
