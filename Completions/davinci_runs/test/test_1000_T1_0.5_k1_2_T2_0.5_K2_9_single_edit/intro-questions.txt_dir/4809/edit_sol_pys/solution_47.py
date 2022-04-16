

def main():
    t = int(input())
    for i in range(t):
        n, s = [int(x) for x in input().split()]
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
        print(curr + 1)


if __name__ == "__main__":
    main()
