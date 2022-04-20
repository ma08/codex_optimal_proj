

def main():
    N, M, Q = map(int, input().split())
    a = [0] * Q
    b = [0] * Q
    c = [0] * Q
    d = [0] * Q
    for i in range(Q):
        a[i], b[i], c[i], d[i] = map(int, input().split())
    a = [a[i] - 1 for i in range(Q)]
    b = [b[i] - 1 for i in range(Q)]
    score = 0
    for m in range(1, M + 1):
        score_m = 0
        for i in range(Q):
            if m - c[i] == 0:
                score_m += d[i]
        score = max(score, score_m)
        for j in range(Q):
            if a[j] < b[j] and m - c[j] > 0:
                score_m += d[j]
                score = max(score, score_m)
    print(score)
    return

if __name__ == '__main__':
    main()
