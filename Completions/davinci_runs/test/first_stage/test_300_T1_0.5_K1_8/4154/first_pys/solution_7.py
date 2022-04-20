


def main():
    N, M = map(int, input().split())
    L = []
    R = []
    for i in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)

    ans = 0
    for i in range(N):
        can_pass = True
        for j in range(M):
            if not (L[j] <= i <= R[j]):
                can_pass = False
                break
        if can_pass:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()