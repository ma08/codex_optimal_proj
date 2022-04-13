

luka = input("Enter a sentence: ") #this is a string

words = luka.split() #this is a list

for i in range(len(words)):
  word = words[i]
  decoded = ''

  for j in range(0, len(word), 2):
    decoded += word[j]

  words[i] = decoded

print(' '.join(words))
