

n = int(input())
a = list(map(int, input().split()))


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


res = []
for i in range(n):
    for j in range(i + 1, n):
        res.append(a[i] * a[j] // gcd(a[i], a[j]))

print(res.index(min(res)) + 1, res.index(min(res)) + 2)

"""
def lcm(a, b):
    return a * b // gcd(a, b)


def find(arr):
    res = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            res.append(lcm(arr[i], arr[j]))
    return res.index(min(res)) + 1, res.index(min(res)) + 2


n = int(input())
a = list(map(int, input().split()))
print(*find(a))
"""
