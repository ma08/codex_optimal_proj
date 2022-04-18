

n = int(input())

a = []
for i in range(n):
    a.append(int(input()))

for i in range(n):
    if a[i] % 2 == 0:
        if a[i] % 3 == 0 or a[i] % 5 == 0:
            continue
        else:
            print('DENIED')
            exit()

print('APPROVED')
