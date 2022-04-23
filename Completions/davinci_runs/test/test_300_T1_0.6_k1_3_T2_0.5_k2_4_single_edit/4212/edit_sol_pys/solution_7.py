

    import sys
    input = sys.stdin.readline
def main():
    N, M, Q = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(Q)]
    ans = 0
    for i in range(1, M + 1):
        score = 0
        for j in range(Q):
            if i - lst[j][2] == 0:
                score += lst[j][3]
        ans = max(ans, score)
        for j in range(Q):
            if lst[j][0] < lst[j][1] and i - lst[j][2] > 0:
                score += lst[j][3]
                ans = max(ans, score)
    print(ans)
    return

if __name__ == '__main__':
    main()
