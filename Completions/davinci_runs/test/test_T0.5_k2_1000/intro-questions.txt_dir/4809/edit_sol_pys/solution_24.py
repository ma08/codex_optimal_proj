

def coconut(n, s, k):
    players = [1 for x in range(n)]
    curr = 0
    for i in range(s - 1):
        curr = (curr + 1) % n
        if players[curr] == 1:
            players[curr] = 0
            for j in range(k):
                curr = (curr + 1) % n
                while players[curr] == 0:
                    curr = (curr + 1) % n
            players[curr] = 1
    for i in range(n):
        if players[i] == 1:
            return i + 1

def main():
    n, s, k = [int(x) for x in input().split()]
    print(coconut(n, s, k))

if __name__ == "__main__":
    main()
