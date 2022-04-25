
n, x, y = map(int, input().split())
n = input()

for i in range(x):
    if n[i] == '0':
        n[i] = '1'
    else:
        n[i] = '0'

print(n)
