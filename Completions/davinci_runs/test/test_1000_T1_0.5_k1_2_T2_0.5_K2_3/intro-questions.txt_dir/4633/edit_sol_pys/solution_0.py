
for i in range(int(input())):
    N, S = map(int, input().split()) # N is the number and S is the target sum of digits
    Moves = 0
    while sum(map(int, str(N))) > S:
        Moves += 1
        N += 1
    print(Moves)
