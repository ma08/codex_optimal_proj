

n, x, y = map(int, input().split())
n = list(input())

for i in range(y, x):
    if n[i] == '0':
        n[i] = '1'
        break
    else:
        n[i] = '0'

print(n.count('0'))
