

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, [input() for _ in range(Q)]))

    players = [K - Q] * N  # 全員がK-Q回正解していると仮定しておく
    for i in range(Q):
        players[A[i] - 1] += 1  # 正解した人は1回正解しているとする

    for player in players:
        if player > 0:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()
