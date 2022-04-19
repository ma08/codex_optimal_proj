

# My answer
N, A, B, C, D, E = (int(x) for x in input().split())

train = N // A
if N % A != 0: train += 1

bus = (N - (A * train)) // B
if (N - (A * train)) % B != 0: bus += 1

taxi = (N - (A * train) - (B * bus)) // C
if (N - (A * train) - (B * bus)) % C != 0: taxi += 1

airplane = (N - (A * train) - (B * bus) - (C * taxi)) // D
if (N - (A * train) - (B * bus) - (C * taxi)) % D != 0: airplane += 1

if (N - (A * train) - (B * bus) - (C * taxi) - (D * airplane)) % E != 0:
    ship = (N - (A * train) - (B * bus) - (C * taxi) - (D * airplane)) // E + 1
else:
    ship = (N - (A * train) - (B * bus) - (C * taxi) - (D * airplane)) // E

print(train + bus + taxi + airplane + ship)

# Best answer
a, b, c, d, e, n = map(int, input().split())

print((n + a - 1) // a + (n + b - 1) // b + (n + c - 1) // c + (n + d - 1) // d + (n + e - 1) // e)
