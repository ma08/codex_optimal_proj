


def swap(p, q):
    temp = p
    p = q
    q = temp
    return p, q


def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    count = 0
    for i in range(N-1):
        if P[i] > P[i+1]:
            P[i], P[i+1] = swap(P[i], P[i+1])
            count += 1
        if Q[i] > Q[i+1]:
            Q[i], Q[i+1] = swap(Q[i], Q[i+1])
            count += 1
    print(count)


if __name__ == '__main__':
    main()
