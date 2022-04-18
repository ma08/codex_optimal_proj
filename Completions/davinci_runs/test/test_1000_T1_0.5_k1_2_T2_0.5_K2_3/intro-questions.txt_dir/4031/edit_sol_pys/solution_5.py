
n = int(input())
strings = [input() for i in range(n)]
strings.sort(key=len)

good = True

for i in range(n):
    for j in range(i+1, n):
        if strings[i] not in strings[j]:
            good = False

if is_good:
    print('YES')
    for s in strings:
        print(s)
else:
    print('NO')
