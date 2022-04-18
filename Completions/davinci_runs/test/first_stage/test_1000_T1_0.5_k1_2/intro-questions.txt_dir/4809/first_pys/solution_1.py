

def coconut(n, s):
    players = [1 for x in range(n)]
    curr = 0
    for i in range(s):
        curr = (curr + 1) % n
        if players[curr] == 0:
            while players[curr] == 0:
                curr = (curr + 1) % n
        if players[curr] == 1:
            players[curr] = 2
        elif players[curr] == 2:
            players[curr] = 0
    while players[curr] == 0:
        curr = (curr + 1) % n
    return curr + 1

def main():
    s, n = [int(x) for x in input().split()]
    print(coconut(n, s))

if __name__ == "__main__":
    main()