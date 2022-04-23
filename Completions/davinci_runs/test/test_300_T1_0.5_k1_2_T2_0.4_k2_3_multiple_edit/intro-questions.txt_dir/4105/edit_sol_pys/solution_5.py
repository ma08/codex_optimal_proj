

def count(n, k, a):
    for i in range(n):
        if a[i]>k:
            return "NO"
    return "YES"

n, k = map(int, input().split())
a = list(map(int, input().split()))
print(count(n, k, a))
