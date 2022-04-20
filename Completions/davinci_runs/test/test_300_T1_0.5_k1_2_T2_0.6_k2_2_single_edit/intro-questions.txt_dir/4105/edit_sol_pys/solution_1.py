

def count(n, k, c):
    if n%2==0 or k%2==0 or c%2==0:
        return "YES"
    else:
        return "NO"

n, k, c = map(int, input().split())
print(count(n, k, c))
