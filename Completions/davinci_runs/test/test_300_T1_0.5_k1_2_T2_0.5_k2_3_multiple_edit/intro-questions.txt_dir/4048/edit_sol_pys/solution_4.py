n = int(input())
moves = 0

while n > 1:
    moves += 1
    if n % 2 == 0:
        n = n // 2
    else:
        n += 1

print(moves)
