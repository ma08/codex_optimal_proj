

n, k = map(int, input().split())

if n < k or n > k*2:
    print("NO")
    exit()

a = [1]*k

n -= k

for i in range(k-1, -1, -1):
    if n >= (2*k-i):
        a[i] += 2*k-i
        n -= 2*k-i
    else:
        a[i] += n
        n = 0

if n > 0:
    print("NO")
    exit()

print("YES")
print(*a)