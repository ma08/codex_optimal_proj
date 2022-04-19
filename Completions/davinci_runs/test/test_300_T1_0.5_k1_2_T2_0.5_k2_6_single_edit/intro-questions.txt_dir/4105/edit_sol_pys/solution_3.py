
def count(n, k):
    return "YES" if n%2==0 else "NO"

n, k = map(int, input().split())
print(count(n, k))
