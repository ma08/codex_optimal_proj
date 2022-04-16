
n, p, m = [int(x) for x in input().split()]
players = {}

for i in range(n):
    players[input()] = 0 #creates dictionary of players

for i in range(m):
    player, points = input().split()
    players[player] += int(points) #adds points to players
    if players[player] >= p: #checks if player has more than or equal to p points
        print(player + " wins!")
        break
else:
    print("No winner!")
