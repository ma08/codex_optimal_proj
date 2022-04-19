

n, x, y = map(int, input().split())
n = list(input().split())

if n[x] == '0':
    n[x] = '1'
else:
    n[x] = '0'
    for i in range(y+1, len(n)):
        if n[i] == '0':
            n[i] = '1'
            break
        else:
            n[i] = '0'

print(n.count('0'))
