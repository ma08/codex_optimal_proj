

#-----Solution-----

a = input().split()[1]
b = input().split()[1]

n = len(a)
m = len(b)

if n != m:
    print('NO')
    exit()

for i in range(n):
    if a[i] != b[i]:
        print('NO')
        exit()

print('YES')
