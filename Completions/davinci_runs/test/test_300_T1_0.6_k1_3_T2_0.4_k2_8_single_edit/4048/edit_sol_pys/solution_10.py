
n = int(input())
move_count = 0
while n > 1:
    if n % 2 == 0:
        n //= 2
    else:
        n -= 1
    move_count += 1
print(move_count)
