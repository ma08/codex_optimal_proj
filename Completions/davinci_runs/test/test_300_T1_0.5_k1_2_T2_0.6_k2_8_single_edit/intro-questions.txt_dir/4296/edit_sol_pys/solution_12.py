

n = int(input())

for i in range(n):
    a = input().split()
    if a[0] == 'Simon' and a[1] == 'says':
        print(' '.join(a[2:]))
