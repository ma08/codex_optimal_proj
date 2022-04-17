

def count(n, k):
    if n % 2 == 0:
        return "YES"
    else:
        return "NO"


n, k = map(int, input().split())
print(count(n, k))
