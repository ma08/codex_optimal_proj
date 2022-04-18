

word = input()
for i in range(len(word)-1):
    if word[i] == word[i+1]:
        word = word[:i]+word[i+2:]
        i-=1

print(word)
