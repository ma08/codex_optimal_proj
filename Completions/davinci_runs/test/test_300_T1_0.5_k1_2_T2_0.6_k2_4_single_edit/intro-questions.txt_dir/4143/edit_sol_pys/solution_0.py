

# My answer


def ceil_div(a, b):
    return -(-a // b)

N, A, B, C, D, E = (int(x) for x in input().split())

if N % A != 0:
    train = N // A + 1
else:
    train = N // A + 1

if (N - (A * train)) % B == 0:
    bus = ceil_div((N - (A * train)), B)
else:
    bus = ceil_div((N - (A * train)), B) + 1

if (N - (A * train) - (B * bus)) % C == 0:
    taxi = ceil_div((N - (A * train) - (B * bus)), C)
else:
    taxi = ceil_div((N - (A * train) - (B * bus)), C) + 1

if (N - (A * train) - (B * bus) - (C * taxi)) % D != 0:
    airplane = (N - (A * train) - (B * bus) - (C * taxi)) // D + 1
else:
    airplane = (N - (A * train) - (B * bus) - (C * taxi)) // D

if (N - (A * train) - (B * bus) - (C * taxi) - (D * airplane)) % E != 0:
    ship = (N - (A * train) - (B * bus) - (C * taxi) - (D * airplane)) // E + 1
else:
    ship = (N - (A * train) - (B * bus) - (C * taxi) - (D * airplane)) // E

print(train + bus + taxi + airplane + ship)

# Best answer
a, b, c, d, e, n = map(int, input().split())

print((n + a - 1) // a + (n + b - 1) // b + (n + c - 1) // c + (n + d - 1) // d + (n + e - 1) // e)
