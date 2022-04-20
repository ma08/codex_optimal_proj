

# My answer
N, A, B, C, D, E = map(int, input().split())

train = N // A
bus = (N - (A * train)) // B
taxi = (N - (A * train) - (B * bus)) // C
airplane = (N - (A * train) - (B * bus) - (C * taxi)) // D
ship = (N - (A * train) - (B * bus) - (C * taxi) - (D * airplane)) // E

if N % A != 0: train += 1
if (N - (A * train)) % B != 0: bus += 1
if (N - (A * train) - (B * bus)) % C != 0: taxi += 1
if (N - (A * train) - (B * bus) - (C * taxi)) % D != 0: airplane += 1
if (N - (A * train) - (B * bus) - (C * taxi) - (D * airplane)) % E != 0: ship += 1

print(train + bus + taxi + airplane + ship)

# Best answer
a, b, c, d, e, n = map(int, input().split())

print((n + a - 1) // a + (n + b - 1) // b + (n + c - 1) // c + (n + d - 1) // d + (n + e - 1) // e)
