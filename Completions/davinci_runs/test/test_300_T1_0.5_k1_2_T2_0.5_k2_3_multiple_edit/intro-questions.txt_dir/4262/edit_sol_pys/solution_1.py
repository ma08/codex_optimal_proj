def swap(l, i, j):
    temp = l[i]
    l[i] = l[j]
    l[j] = temp
    return l


def main():
    N = int(input())
    P = list(map(int, input().split())[:N])
    Q = list(map(int, input().split())[:N])
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if P[i] > P[j]:
                P = swap(P, i, j)
                count += 1
            if Q[i] > Q[j]:
                Q = swap(Q, i, j)
                count += 1
    print(count)


if __name__ == '__main__':
    main()
