


def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


def solve(a):
    n = len(a)
    ans = 1
    ans_i = 1
    ans_j = 2
    for i in range(n):
        for j in range(i + 1, n):
            if lcm(a[i], a[j]) < lcm(a[ans_i], a[ans_j]):
                ans_i = i
                ans_j = j
    return ans_i + 1, ans_j + 1


def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(*solve(a))


if __name__ == "__main__":
    main()