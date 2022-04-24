

def count(n, k):
    if n % k == 0:
        return "YES"
    else:
        return "NO"

n, k = map(int, input().split())
print(count(n, k))
