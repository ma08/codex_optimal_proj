

def main():
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    b = [1] * n
    for i in range(1, n):
        if a[i] > a[i - 1]:
            b[i] = b[i - 1] + 1
    c = [1] * n
    for i in range(n - 2, -1, -1):
        if a[i] > a[i + 1]:
            c[i] = c[i + 1] + 1
    ans = max(b[i] + c[i] - 1 for i in range(n))
    print(ans, end="\n")
    print("".join("RL"[b[i] >= c[i]] for i in range(n)))

if __name__ == "__main__":
    main()
