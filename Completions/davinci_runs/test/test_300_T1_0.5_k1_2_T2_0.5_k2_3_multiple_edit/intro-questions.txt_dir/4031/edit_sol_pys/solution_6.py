

n = int(input())
strings = sorted(input() for i in range(n), key=len)

is_good = True

for i in range(n):
    for j in range(i+1, n):
        if strings[i] not in strings[j]:
            break
            is_good = False

if is_good:
    print('YES')
    for s in strings:
        print(s)
else:
    print('NO')
