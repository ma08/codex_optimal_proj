
n = int(input())
a = [int(i) for i in input().split()]

for i in range(n):
    if a[i]%2==0:
        if a[i]%3==0 or a[i]%5==0:
            pass
        else:
            print('DENIED')
            exit()
print('APPROVED')
