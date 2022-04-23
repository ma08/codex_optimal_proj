n = int(input())
moves = 0

if n == 0:
    print(0)
    exit()

if n == 1:
    print(0)
    exit()

while n > 1:
    moves += 1
    if n % 2 == 0:
        n = n // 2
    else:
        n += 1

print(moves)
