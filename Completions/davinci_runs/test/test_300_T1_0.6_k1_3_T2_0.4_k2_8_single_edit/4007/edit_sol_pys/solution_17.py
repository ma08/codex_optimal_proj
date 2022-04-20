

def solve(n, s):
    if n == 0:
        return 0
    elif n == 1:
        return s[0]
    else:
        return solve(n - 1, s) + s[n - 1]

def main():
    n = int(input())
    s = list(map(int, input().split()))
    result = solve(n, s)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
