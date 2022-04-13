

k, n = map(int, input().split())
players = [False for i in range(9)]
players[k] = True
for i in range(n):
    time, ans = map(str, input().split())
    time = int(time)
    if ans == 'T':
        pass
    elif ans == 'N':
        players = [False for i in range(9)]
    elif ans == 'P':
        players = [False for i in range(9)]
        players[(k+1)%9] = True
    if time >= 210:
        print(players.index(True))
        break
    else:
        players = [False for i in range(9)]
        players[(players.index(True)+1)%9] = True 
