

def count(n, k, a):
    if k%2==0:
        return "NO"
    elif a == n-1:
        return "YES"
    else:
        return "NO"

n, k = map(int, input().split())
a = int(input())
print(count(n, k, a))
