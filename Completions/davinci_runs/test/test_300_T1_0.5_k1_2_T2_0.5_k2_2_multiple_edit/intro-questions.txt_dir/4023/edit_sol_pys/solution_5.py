

def f(n):
    if n % 2 == 1:
        return n
    return f(n // 2)

if n.count(n[0]) == n:
    print("YES")
    exit()

n_sorted = sorted(n)

for i in range(n - 1):
    if n_sorted[i] + 1 != n_sorted[i + 1]:
        print("NO")
        exit()

print("YES")
