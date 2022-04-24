
n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    if a[i] % 2 == 0 and (a[i] % 3 != 0 or a[i] % 5 != 0):
        print('DENIED')
        break
else:
    print('APPROVED')
