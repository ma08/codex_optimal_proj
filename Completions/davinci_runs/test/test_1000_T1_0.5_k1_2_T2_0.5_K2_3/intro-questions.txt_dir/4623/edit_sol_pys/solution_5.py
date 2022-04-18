

#
# SOLUTION
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return (a * b) // gcd(a, b)


def find_lcm(arr):
    ans = arr[0]
    for i in range(1, len(arr)):
        ans = lcm(ans, arr[i])
    return ans


for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(find_lcm(arr) % k)
