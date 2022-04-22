


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
    for i in range(N):
        for j in range(i+1, N):
            if P[i] > P[j]:
                P[i], P[j] = swap(P[i], P[j])
                count += 1
            if Q[i] > Q[j]:
                Q[i], Q[j] = swap(Q[i], Q[j])
                count += 1
    print(count)



if __name__ == '__main__':
    main()
