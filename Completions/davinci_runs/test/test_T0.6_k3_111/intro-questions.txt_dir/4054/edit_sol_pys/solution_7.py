

n = [int(i) for i in input().split()]

# Find the least common multiple
def lcm(n):
    # Find the greatest common divisor
    lcd = n[0]
    for i in n:
        while i % lcd != 0:
            lcd -= 1

    # Find the least common multiple
    lcm = n[0]
    for i in n:
        while lcm % i != 0:
            lcm += lcd

    return lcm

print(lcm(n))
