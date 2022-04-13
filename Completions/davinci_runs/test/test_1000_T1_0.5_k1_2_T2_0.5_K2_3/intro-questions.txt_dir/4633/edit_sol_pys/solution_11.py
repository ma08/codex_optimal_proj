

def sum_of_digits(n):
    sum = 0
    for i in n:
        sum += int(i)
    return sum


def get_min_moves(n):
    n_str = str(n)
    n_sum = sum_of_digits(n_str)
    if n_sum <= s:
        return 0
    else:
        moves = 0
        i = 0
        while n_sum > s:
            if i == len(n_str) - 1:
                n_str = str(int(n_str) + 1)
                i = 0
                moves += 1
            else:
                n_str = n_str[:i] + str(int(n_str[i]) - 1) + n_str[i+1:]
                i += 1
            n_sum = sum_of_digits(n_str)
        return moves


t = int(input())

for i in range(t):
    n, s = map(int, input().split())
    print(get_min_moves(n))
