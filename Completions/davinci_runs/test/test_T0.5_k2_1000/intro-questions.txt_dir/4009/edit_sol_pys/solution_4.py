

n, x, y = map(int, input().split())
n = input().strip()

if n[y-1] == '0':
    n = n[:y-1] + '1' + n[y:]
else:
    n = n[:y-1] + '0' + n[y:]
    for i in range(y, x):
        if n[i] == '1':
            n = n[:i] + '0' + n[i+1:]
            break
        else:
            n[i] = '0'

print(n.count('0'))
