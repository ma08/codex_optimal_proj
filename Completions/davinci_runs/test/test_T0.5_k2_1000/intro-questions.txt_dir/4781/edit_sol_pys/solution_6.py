

k, n = map(int, input().split())
players = [False for i in range(8)]
players[k-1] = True
for i in range(n):
    time, ans = map(str, input().split())
    time = int(time)
    if ans == 'T':
        pass
    elif ans == 'N':
        players[(players.index(True)+1)%8] = True
    elif ans == 'P':
        players = [False for i in range(8)]
        players[(players.index(True)+1)%8] = True
    if time >= 210:
        print(players.index(True)+1)
        break
    else:
        players[(players.index(True)+1)%8] = True
