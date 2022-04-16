

def coconut(n, k):
    players = [True for x in range(n)]
    curr = 0
    for i in range(k):
        for j in range(k):
            curr = (curr + 1) % n
            while not players[curr]:
                curr = (curr + 1) % n
        players[curr] = False
        while not players[curr]:
            curr = (curr + 1) % n
    return curr + 1, players

def main():
    n, k = [int(x) for x in input().split()]
    ans, players = coconut(n, k)
    for i in range(len(players)):
        if players[i]:
            print(i + 1)

if __name__ == "__main__":
    main()
