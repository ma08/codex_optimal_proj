

n = int(input())
moves = 0
while n > 1:
    if n % 6 == 0:
        n /= 6
        moves += 1
    else:
        n *= 2
        moves += 1
print(moves)

