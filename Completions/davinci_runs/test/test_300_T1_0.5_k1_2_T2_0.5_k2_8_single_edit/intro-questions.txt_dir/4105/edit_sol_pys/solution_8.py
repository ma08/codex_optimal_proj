

def count(n, k):
    if n%2==0 and n>=2*k:
        return "YES" 
    return "NO"

n, k = map(int, input().split())
print(count(n, k))
