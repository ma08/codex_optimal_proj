
def count(n):
    if n % 2 == 0:
        return "YES"
    else:
        return "NO"

n = map(int, input().split())
print(count(n))
