

def main():
    N, M, Q = map(int, input().split())
    a = [0] * Q
    b = [0] * Q
    c = [0] * Q
    d = [0] * Q
    for i in range(Q):
        a[i], b[i], c[i], d[i] = map(int, input().split())
    score = 0
    for m in range(1, M + 2):
        score_m = 0
        for i in range(Q):
            if m - c[i] == 1:
                score_m += d[i] * (b[i] - a[i] + 1)
        score = max(score, score_m)
        for j in range(Q):
            if a[j] < b[j] and m - c[j] > 1:
                score_m += d[j] * (b[j] - a[j])
                score = max(score, score_m)
    print(score)
    return

if __name__ == '__main__':
    main()
