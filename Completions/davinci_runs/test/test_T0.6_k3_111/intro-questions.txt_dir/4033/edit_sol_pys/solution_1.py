

def main():
    a, b = map(int, input().split())
    n = max(a, b)
    m = min(a, b)
    ans = 2 * m + 2 * (n - m) - 1
    print(ans)

if __name__ == "__main__":
    main()
