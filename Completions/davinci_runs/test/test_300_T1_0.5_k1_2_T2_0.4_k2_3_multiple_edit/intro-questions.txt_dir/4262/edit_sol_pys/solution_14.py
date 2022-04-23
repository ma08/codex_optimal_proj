def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    for i in range(N):
        for j in range(i+1, N):
            if P[i] > P[j]:
                P[i], P[j] = P[j], P[i]
            if Q[i] > Q[j]:
                Q[i], Q[j] = Q[j], Q[i]
    print(P, Q)


if __name__ == '__main__':
    main()
