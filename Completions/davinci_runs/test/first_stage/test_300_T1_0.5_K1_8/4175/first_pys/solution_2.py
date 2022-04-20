

n = int(input())

words = []

for i in range(n):
    words.append(input())

last_word = words[0]

for i in range(1, n):
    if words[i] in words[:i] or last_word[-1] != words[i][0]:
        print("No")
        exit()
    last_word = words[i]

print("Yes")