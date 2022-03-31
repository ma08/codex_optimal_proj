

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, [input() for _ in range(Q)]))

    players = [K - Q] * N
    for i in range(Q):
        players[A[i] - 1] += 1

    for player in players:
        if player > 0:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()