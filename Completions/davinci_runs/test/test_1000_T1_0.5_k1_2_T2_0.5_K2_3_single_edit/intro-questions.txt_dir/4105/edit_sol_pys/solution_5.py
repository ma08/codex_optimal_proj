

n = int(input())

s = input()

words = s.split()

for word in words:
    if word.isalpha():
        print(word)
    else:
        print(int(word))
