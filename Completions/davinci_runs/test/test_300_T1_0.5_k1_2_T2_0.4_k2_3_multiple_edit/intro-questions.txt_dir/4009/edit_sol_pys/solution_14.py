n, x, y = map(int, input().split())
n = list(input())

if n[x-1] == '0':
    n[x-1] = '1'
else:
    n[x-1] = '0'
    for i in range(x, y):
        if n[i] == '0':
            n[i] = '1'
            break
        else:
            n[i] = '0'

print(n.count('0'))
