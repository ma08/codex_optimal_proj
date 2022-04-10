

def main():
    n = int(input())
    q = list(map(int, input().split()))
    if n - sum(q) < 0 or n - sum(q) % 2 == 1:
        print(-1)
    else:
        p = [0] * n
        p[0] = n - sum(q) // 2
        for i in range(n - 1):
            p[i + 1] = p[i] + q[i]
        print(*p)

if __name__ == "__main__":
    main()