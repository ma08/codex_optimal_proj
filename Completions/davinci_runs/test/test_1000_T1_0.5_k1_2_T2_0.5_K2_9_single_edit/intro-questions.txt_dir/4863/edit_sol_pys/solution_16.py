

n = int(input())
a = [input() for i in range(n)]
c = 0
for i in range(n):
    if a[i] == 'A':
        c += 1
print(c)
