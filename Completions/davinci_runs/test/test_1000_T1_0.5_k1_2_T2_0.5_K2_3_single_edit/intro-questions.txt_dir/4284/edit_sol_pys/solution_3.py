

def main():
    N, K = map(int, input().split())
    ans = 0
    for b in range(N+1):
        p = (N-b) * b + 1
        c = 0
        while p < K:
            p *= 2
            c += 1
        ans = max(ans, c)
    print(ans)


if __name__ == "__main__":
    main()
