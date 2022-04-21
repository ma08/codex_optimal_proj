

# My answer
a, b, c, d, e, n = map(int, input().split())

if n % a != 0:
    train = n // a + 1
else:
    train = n // a

if (n - (a * train)) % b != 0:
    bus = (n - (a * train)) // b + 1
else:
    bus = (n - (a * train)) // b

if (n - (a * train) - (b * bus)) % c != 0:
    taxi = (n - (a * train) - (b * bus)) // c + 1
else:
    taxi = (n - (a * train) - (b * bus)) // c

if (n - (a * train) - (b * bus) - (c * taxi)) % d != 0:
    airplane = (n - (a * train) - (b * bus) - (c * taxi)) // d + 1
else:
    airplane = (n - (a * train) - (b * bus) - (c * taxi)) // d

if (n - (a * train) - (b * bus) - (c * taxi) - (d * airplane)) % e != 0:
    ship = (n - (a * train) - (b * bus) - (c * taxi) - (d * airplane)) // e + 1
else:
    ship = (N - (A * train) - (B * bus) - (C * taxi) - (D * airplane)) // E

print(train + bus + taxi + airplane + ship)

# Best answer
a, b, c, d, e, n = map(int, input().split())

print((n + a - 1) // a + (n + b - 1) // b + (n + c - 1) // c + (n + d - 1) // d + (n + e - 1) // e)
