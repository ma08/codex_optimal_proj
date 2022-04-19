

n = int(input())
a = list(map(int, input().split()))
if n % 2 == 0:
    a1 = a[0:n//2]
    a2 = a[n//2:]
else:
    a1 = a[0:n//2]
    a2 = a[n//2+1:]


print(a1)
print(a2)
