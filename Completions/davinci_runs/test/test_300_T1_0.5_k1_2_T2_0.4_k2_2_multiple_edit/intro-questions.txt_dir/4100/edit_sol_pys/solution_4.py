

def main():
    N, K, Q = [int(i) for i in input().split()]
    players = [K] * N

    for i in range(Q):
        A = int(input()) - 1
        players[A] += 1
        for j in range(N):
            if j != A:
                players[j] -= 1

    for i in range(N):
        if players[i] > 0:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()
