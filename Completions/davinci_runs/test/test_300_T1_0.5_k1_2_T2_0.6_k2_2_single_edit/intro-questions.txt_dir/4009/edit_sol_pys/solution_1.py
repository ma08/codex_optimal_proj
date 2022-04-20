

n, x, y = map(int, input().split())
n = list(input())
if n[y-1] == '0':
    n[y-1] = '1'
else:
    n[y-1] = '0'
    for i in range(y, x):
        if n[i] == '0':
            n[i] = '1'
            break
        else:
            n[i] = '0'

print(n.count('0'))
