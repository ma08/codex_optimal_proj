

def main():
    N, M, Q = map(int, input().split())
    a = [0] * Q
    b = [0] * Q
    c = [0] * Q
    d = [0] * Q
    for i in range(Q):
        a[i], b[i], c[i], d[i] = map(int, input().split())
    a = [a1 - 1 for a1 in a]
    b = [b1 - 1 for b1 in b]
    for m in range(M):
        for i in range(Q):
            if m - c[i] == 0:  # 初期状態
                a[i] = b[i]
            if a[i] < b[i] and m - c[i] > 0:
                a[i] += 1
        score_m = sum([d[i] for i in range(Q) if a[i] == b[i]])
        print(score_m)

    return

if __name__ == '__main__':
    main()
