

def ravioli_sort(n, a):
    if n <= 1:
        return "YES"
    for i in range(n-1):
        if abs(a[i]-a[i+1]) >= 2:
            return "NO"
    return "YES"

n = int(input())
a = list(map(int, input().split()))

print(ravioli_sort(n, a))
