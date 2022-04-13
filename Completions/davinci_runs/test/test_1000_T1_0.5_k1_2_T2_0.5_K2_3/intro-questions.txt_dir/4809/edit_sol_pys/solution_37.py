

def coconut(n, k):
    players = [1 for x in range(n)]
    curr = 0
    for i in range(k):
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
    n = int(input())
    print(coconut(n, 1))

if __name__ == "__main__":
    main()
