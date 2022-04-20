
n = int(input())  # количество строк
strings = [input() for i in range(n)]  # сами строки
strings.sort(key=lambda x: len(x))
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
