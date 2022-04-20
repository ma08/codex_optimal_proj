

n = int(input())
ai = [int(x) for x in input().split()]
bi = [int(x) for x in input().split()]

def wins(ai, bi):
    a_r, a_s, a_p = ai
    b_r, b_s, b_p = bi
    return min(a_r, b_p) + min(a_s, b_r) + min(a_p, b_s)

min_wins = wins(ai, bi)
max_wins = wins([n-x for x in bi], [n-x for x in ai])

print(min_wins, max_wins)