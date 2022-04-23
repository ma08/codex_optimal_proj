
def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    count1 = 0
    count2 = 0
    for i in range(N):
        for j in range(i+1, N):
            if P[i] > P[j]:
                P[i], P[j] = P[j], P[i]
                count1 += 1
            if Q[i] > Q[j]:
                Q[i], Q[j] = Q[j], Q[i]
                count2 += 1
    print(count1)
    print(count2)


if __name__ == '__main__':
    main()
