n = int(input())
words = [input() for i in range(n)]
words.sort(key=lambda x: len(x))


is_good_words = True

is_good = True

for i in range(n):
    for j in range(i+1, n):
        if strings[i] not in strings[j]:
            is_good = False

if is_good:
    print('YES')
    for s in strings:
        print(s)
else:
    print('NO')
