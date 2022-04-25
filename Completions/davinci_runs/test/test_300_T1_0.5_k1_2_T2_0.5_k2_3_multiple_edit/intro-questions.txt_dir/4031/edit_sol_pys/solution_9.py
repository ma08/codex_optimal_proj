
n = int(input())
words = [input() for i in range(n)]
words.sort(key=lambda x: len(x))

is_good = True

for i in range(n):
    for j in range(i+1, n):
        if words[i] not in words[j]:
            is_good = False

if is_good:
    print('YES')
    for s in words:
        print(s)
else:
    print('NO')
