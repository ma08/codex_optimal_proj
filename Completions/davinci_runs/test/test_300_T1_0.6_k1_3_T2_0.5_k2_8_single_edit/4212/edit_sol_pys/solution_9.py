

def main():
    N, M, Q = map(int, input().split())
    A = [None] * Q
    B = [None] * Q
    C = [None] * Q
    D = [None] * Q
    for i in range(Q):
        A[i], B[i], C[i], D[i] = map(int, input().split())
    A = [A1 - 1 for A1 in A]
    B = [B1 - 1 for B1 in B]
    score = 0
    for m in range(1, M + 1):
        score_m = 0
        for i in range(Q):
            if m - C[i] == 0:
                score_m += D[i]
        score = max(score, score_m)
        for j in range(Q):
            if A[j] < B[j] and m - C[j] > 0:
                score_m += D[j]
                score = max(score, score_m)
    print(score)
    return

if __name__ == '__main__':
    main()
