
def main():
    N, M, Q = map(int, input().split())
    a = [None] * Q
    b = [None] * Q
    c = [None] * Q
    d = [None] * Q
    for i in range(Q):
        a[i], b[i], c[i], d[i] = map(int, input().split())
    a = [a_i - 1 for a_i in a]
    b = [b_i - 1 for b_i in b]
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
