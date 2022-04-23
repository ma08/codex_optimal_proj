

def count(n, k, a):
    for i in range(n):
        if a[i]>k:
            return "NO"
    return "YES"

n, k, a = map(int, input().split())
print(count(n, k, a))
