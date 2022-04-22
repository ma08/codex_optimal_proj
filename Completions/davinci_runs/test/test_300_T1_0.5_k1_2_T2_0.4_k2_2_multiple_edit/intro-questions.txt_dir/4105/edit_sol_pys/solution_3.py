

def count(n, k):
    a = n // 2
    if n%2==0:
        return "YES" if a >= k else "NO"
    else:
        return "YES" if a >= k else "NO"

n, k = map(int, input().split())
print(count(n, k))
