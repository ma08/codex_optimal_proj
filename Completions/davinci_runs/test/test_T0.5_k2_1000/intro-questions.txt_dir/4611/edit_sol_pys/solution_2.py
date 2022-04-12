n = int(input())

t = [0]*n
x = [0]*n
y = [0]*n

for i in range(n):
    t[i], x[i], y[i] = map(int, input().split())

for i in range(n):
    if abs(x[i]-x[i-1]) + abs(y[i]-y[i-1]) > t[i]-t[i-1]:
        print('No')
        exit()
    if (t[i]-t[i-1])%2 != (abs(x[i]-x[i-1]) + abs(y[i]-y[i-1]))%2:
        print('No')
        exit()

print('Yes')
