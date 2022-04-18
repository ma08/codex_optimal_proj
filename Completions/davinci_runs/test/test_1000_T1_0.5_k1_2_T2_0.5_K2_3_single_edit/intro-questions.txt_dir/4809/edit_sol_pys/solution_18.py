

def coconut_splat(number, player):
    if number == 9:
        return (player - 1) % 2 + 1
    return (player - 1) % 3 + 1

s, n = map(int, input().split())
print(coconut_splat(s, n))
