


# My solution
N, A, B, C, D, E = (int(x) for x in input().split())

if N % A != 0:
    train = N // A + 1
else:
    train = N // A

if (N - (A * train)) % B != 0:
    bus = (N - (A * train)) // B + 1
else:
    bus = (N - (A * train)) // B

if (N - (A * train) - (B * bus)) % C != 0:
    taxi = (N - (A * train) - (B * bus)) // C + 1
else:
    taxi = (N - (A * train) - (B * bus)) // C

if (N - (A * train) - (B * bus) - (C * taxi)) % D != 0:
    airplane = (N - (A * train) - (B * bus) - (C * taxi)) // D + 1
else:
    airplane = (N - (A * train) - (B * bus) - (C * taxi)) // D

if (N - (A * train) - (B * bus) - (C * taxi) - (D * airplane)) % E != 0:
    ship = (N - (A * train) - (B * bus) - (C * taxi) - (D * airplane)) // E + 1
else:
    ship = (N - (A * train) - (B * bus) - (C * taxi) - (D * airplane)) // E

print(train + bus + taxi + airplane + ship)

# Best solution

a, b, c, d, e, n = map(int, input().split())

print((n + a - 1) // a + (n + b - 1) // b + (n + c - 1) // c + (n + d - 1) // d + (n + e - 1) // e)
