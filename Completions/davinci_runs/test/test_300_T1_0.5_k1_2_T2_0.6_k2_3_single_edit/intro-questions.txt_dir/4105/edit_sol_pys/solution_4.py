

def count(n, k):
    if n%2==0:
    elif n%2==1 and k==1:
        return "YES"
    elif n%2==1 and k>1:
        return "NO"
        return "YES"
    else:

        return "NO"

n, k = map(int, input().split())
print(count(n, k))
