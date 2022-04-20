

n = int(input())
a = list(map(int, input().split()))

b = []
for i in range(n):
    if a[n - i - 1] not in b:
        b.append(a[n - i - 1])
        
print(len(b))
print(*b[::-1])