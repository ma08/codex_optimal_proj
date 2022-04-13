
def sum_of_digits(N):
    return sum(map(int, str(N)))

def min_moves(N, S):
    moves = 0
    while sum_of_digits(N) > S:
        Moves += 1
        N += 1
    return Moves

t = int(input())
for i in range(t):
    N, S = map(int, input().split())
    print(min_moves(N, S))
