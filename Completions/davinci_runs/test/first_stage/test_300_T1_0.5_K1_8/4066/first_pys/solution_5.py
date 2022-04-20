

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def solve(a):
    min_lcm = lcm(a[0], a[1])
    min_pair = (0, 1)
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            _lcm = lcm(a[i], a[j])
            if _lcm < min_lcm:
                min_lcm = _lcm
                min_pair = (i, j)
    return min_pair


n = int(input())
a = list(map(int, input().split()))
i, j = solve(a)
print(i + 1, j + 1)