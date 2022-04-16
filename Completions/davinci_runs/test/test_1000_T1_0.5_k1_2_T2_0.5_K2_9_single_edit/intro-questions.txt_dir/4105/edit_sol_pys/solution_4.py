

def count(n, k):
    if n % 2 == 0:
        return "yes"
    else:
        return "no"

n, k = map(int, input().split())
print(count(n, k))
