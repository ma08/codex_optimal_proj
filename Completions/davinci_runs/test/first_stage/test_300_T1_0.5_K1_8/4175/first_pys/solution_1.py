

N = int(input())
words = []

for i in range(N):
    words.append(input())

for i in range(N - 1):
    if words[i] == words[i + 1]:
        print('No')
        exit(0)

for i in range(N - 1):
    if words[i][-1] != words[i + 1][0]:
        print('No')
        exit(0)

print('Yes')