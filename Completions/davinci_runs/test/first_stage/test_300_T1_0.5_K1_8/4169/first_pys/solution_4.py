

def main():
    N, M = map(int, input().split())
    A_B = []
    for _ in range(N):
        A, B = map(int, input().split())
        A_B.append((A, B))
    A_B.sort()
    ans = 0
    for a, b in A_B:
        if b < M:
            M -= b
            ans += a * b
        else:
            ans += a * M
            break
    print(ans)

if __name__ == '__main__':
    main()