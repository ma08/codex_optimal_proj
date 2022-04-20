
#-----Solution-----

a = input().split()
b = input()

n = int(a[0])
m = int(b)

if n != m:
    print('NO')
    exit()

for i in range(n):
    if a[i] != b:
        print('YES')
        exit(0)

print('YES')
