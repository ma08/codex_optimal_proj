

def solve(n, a, b):
    ans = 0
    if n % 2 == 0:
        ans += min(a, b) * (n // 2)
        a -= min(a, b)
        b -= min(a, b)
        ans += min(a, b)
    else:
        ans += min(a, b) * (n // 2)
        a -= min(a, b)
        b -= min(a, b)
        ans += min(a, b)
        ans += 1
    return ans

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    t = input().strip()
    print(solve(n, s, t))
