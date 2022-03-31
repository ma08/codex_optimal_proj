

n = [int(i) for i in input().split()]

# Find the lowest common denominator
lcd = n[0]
for i in n:
    while i % lcd != 0:
        lcd -= 1

# Find the lowest common multiple
lcm = n[0]
for i in n:
    while lcm % i != 0:
        lcm += lcd

print(lcm)