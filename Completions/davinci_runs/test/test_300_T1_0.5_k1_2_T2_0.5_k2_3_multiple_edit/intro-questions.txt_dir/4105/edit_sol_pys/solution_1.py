

def count(n, k, x):
    return "YES" if x % 2 == 0 else "NO"

n, k, x = map(int, input().split())
print(count(n, k, x))
