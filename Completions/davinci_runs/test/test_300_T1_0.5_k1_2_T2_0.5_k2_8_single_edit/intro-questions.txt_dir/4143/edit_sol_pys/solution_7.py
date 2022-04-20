

# My answer
N, A, B, C, D, E = map(int, input().split())

train = (N + A - 1) // A
bus = (N - (A * train) + B - 1) // B
taxi = (N - (A * train) - (B * bus) + C - 1) // C
airplane = (N - (A * train) - (B * bus) - (C * taxi) + D - 1) // D
ship = (N - (A * train) - (B * bus) - (C * taxi) - (D * airplane) + E - 1) // E

print(int(train + bus + taxi + airplane + ship))

# Best answer
a, b, c, d, e, n = map(int, input().split())

print((n + a - 1) // a + (n + b - 1) // b + (n + c - 1) // c + (n + d - 1) // d + (n + e - 1) // e)
