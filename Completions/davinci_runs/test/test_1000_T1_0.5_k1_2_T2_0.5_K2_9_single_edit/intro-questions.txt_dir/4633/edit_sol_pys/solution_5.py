

def sum_of_digits(n):
    return sum(map(int, str(n)))

def min_moves(n, s):
    n += 1
    while sum_of_digits(n) != s:
        n += 1
    return n

t = int(input())
for i in range(t):
    n, s = map(int, input().split())
    print(min_moves(n, s))
