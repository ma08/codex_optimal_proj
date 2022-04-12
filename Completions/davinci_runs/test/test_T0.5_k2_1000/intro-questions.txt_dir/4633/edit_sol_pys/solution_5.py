
def sum_of_digits(n):
    s = 0
    for i in n:
        s += int(i)
    return s

def get_min_moves(n):
    n = str(n)
    n_sum = sum_of_digits(n)
    if n_sum <= s:
        return 0
    else:
        moves = 0
        i = 0
        while n_sum > s:
            if i == len(n) - 1:
                n = str(int(n) + 1)
                i = 0
                moves += 1
            else:
                n = n[:i] + str(int(n[i]) - 1) + n[i+1:]
                i += 1
            n_sum = sum_of_digits(n)
        return moves

t = int(input())

for i in range(t):
    n, s = map(int, input().split())
    print(get_min_moves(n))
