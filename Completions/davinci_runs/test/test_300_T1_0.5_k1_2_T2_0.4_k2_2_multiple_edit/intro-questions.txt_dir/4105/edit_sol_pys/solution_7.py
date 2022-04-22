

def count(n, k):
    if n % 2 == 0:
        return "YES" if k >= n // 2 else "NO"
    else:
        return "YES" if a >= k else "NO"

n, k = map(int, input().split())
print(count(n, k))
