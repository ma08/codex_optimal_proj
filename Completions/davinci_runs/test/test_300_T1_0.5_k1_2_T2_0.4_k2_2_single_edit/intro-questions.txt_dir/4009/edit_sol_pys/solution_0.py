

n, x, y = map(int, input().split())
n = list(input())[::-1]

if n[x-y-1] == '0':
    n[x-y-1] = '1'
else:
    n[x-y-1] = '0'
    for i in range(x-y, x):
        if n[i] == '1':
            n[i] = '0'
            break
        else:
            n[i] = '0'

print(n.count('0'))
