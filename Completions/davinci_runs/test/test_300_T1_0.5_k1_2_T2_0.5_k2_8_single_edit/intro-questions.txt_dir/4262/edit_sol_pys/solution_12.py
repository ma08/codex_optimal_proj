


def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    countP = 0
    countQ = 0
    for i in range(N):
        for j in range(i+1, N):
            if P[i] > P[j]:
                P[i], P[j] = P[j], P[i]
                countP += 1
            if Q[i] > Q[j]:
                Q[i], Q[j] = Q[j], Q[i]
                countQ += 1
    print(abs(countP - countQ))


if __name__ == '__main__':
    main()
