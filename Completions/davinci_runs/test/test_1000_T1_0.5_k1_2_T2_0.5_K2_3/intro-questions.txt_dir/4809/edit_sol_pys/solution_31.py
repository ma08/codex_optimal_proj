
def coconut(n, s):
    players = [1] * n
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
    n, s = [int(x) for x in input().split()]
    print(coconut(n, s-1))

if __name__ == "__main__":
    main()
