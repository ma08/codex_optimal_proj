

def solve(a):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    ans = a[0]
    for i in range(1, len(a)):
        ans = gcd(ans, a[i])

    cnt = 0
    i = 1
    while i * i <= ans:
        if ans % i == 0:
            cnt += 2
            if i * i == ans:
                cnt -= 1
        i += 1

    return cnt


n = int(input())
a = [int(x) for x in input().split()]
print(solve(a))