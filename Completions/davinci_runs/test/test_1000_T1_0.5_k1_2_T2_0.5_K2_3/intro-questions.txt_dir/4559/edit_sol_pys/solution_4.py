for i in range(int(input())):
    N, K = map(int, input().split())
    print("YES" if K % (2 ** (N - 1)) == 0 else "NO")
