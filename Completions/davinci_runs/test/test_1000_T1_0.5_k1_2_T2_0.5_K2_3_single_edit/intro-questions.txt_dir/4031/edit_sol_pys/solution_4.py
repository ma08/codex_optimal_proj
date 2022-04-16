

n = int(input())
strings = [input() for i in range(n)]
strings.sort(key=lambda x: len(x), reverse=True)

is_good = True

for i in range(n):
    if not is_good:
        break
    for j in range(i+1, n):        
        if strings[j].startswith(strings[i]):
            break
    else:
        is_good = False

if is_good:
    print('YES')
    for s in strings:
        print(s)
else:
    print('NO')
