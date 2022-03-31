

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]

    players = [K - Q] * N # 全員がK-Q点
    for i in range(Q):
        players[A[i] - 1] += 1 # 回答した人は1点加算

    for player in players:
        if player > 0:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()
