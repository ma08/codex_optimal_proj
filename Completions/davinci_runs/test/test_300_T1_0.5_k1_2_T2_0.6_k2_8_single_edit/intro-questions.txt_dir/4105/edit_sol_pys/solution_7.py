

def count(n, k):
    if n%2==0:
        return "YES"
    else:
        return "NO"


for _ in range(int(input())):
    n, k = map(int, input().split())
    print(count(n, k))
