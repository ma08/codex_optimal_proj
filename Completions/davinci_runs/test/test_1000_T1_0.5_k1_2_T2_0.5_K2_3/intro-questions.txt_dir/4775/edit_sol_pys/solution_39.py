

a, b = input().split()
n = len(a)
m = len(b)

for i in range(n):
    if a[i] in b:
        break

print('.'*(m-1) + a[i])
for j in range(n-1):
    print('.'*(b.index(a[i])) + a[i] + '.'*(m-b.index(a[i])-1))
print(b)
for k in range(n-i-1):
    print('.'*n)
