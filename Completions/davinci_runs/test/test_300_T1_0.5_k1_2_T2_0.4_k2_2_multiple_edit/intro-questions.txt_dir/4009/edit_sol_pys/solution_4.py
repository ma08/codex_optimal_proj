
n, x, y = map(int, input().split())
n = input()

if n[y-1] == '0':
    n = n[:y-1] + '1' + n[y:]
else:
    n = n[:y-1] + '0' + n[y:]
    for i in range(y, x+1):
        if n[i-1] == '0':
            n = n[:i-1] + '1' + n[i:]
            break
        else:
            n[i] = '0'

print(n.count('0'))
