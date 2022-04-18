

n, x, y = map(int, input().split())
n = input()

if n[y-1] == '0':
    n = n[:y-1] + '1' + n[y:]
else:
    n = n[:y-1] + '0' + n[y:]
    for i in range(y, x):
        n = n[:i] + '1' + n[i+1:]

print(n.count('0'))
