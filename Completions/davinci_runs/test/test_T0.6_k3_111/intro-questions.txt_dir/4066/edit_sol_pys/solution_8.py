

from sys import stdin, stdout

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def lcm(a, b):
    return (a * b) // gcd(a, b)

def solve(a, n):
    min_lcm = float('inf') # infinity
    ans = [0, 0]
    for i in range(n):
        for j in range(i + 1, n):
            if lcm(a[i], a[j]) < min_lcm:
                min_lcm = lcm(a[i], a[j])
                ans[0] = i + 1
                ans[1] = j + 1
    return ans[0], ans[1]

if __name__ == '__main__':
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    stdout.write("{} {}\n".format(*solve(a, n)))
