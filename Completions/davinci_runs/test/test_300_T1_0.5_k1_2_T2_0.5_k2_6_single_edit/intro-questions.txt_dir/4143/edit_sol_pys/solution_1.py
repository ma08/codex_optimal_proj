
N, A, B, C, D, E = (int(x) for x in input().split())


# My answer
print((N + A - 1) // A + (N + B - 1) // B + (N + C - 1) // C + (N + D - 1) // D + (N + E - 1) // E)

# Best answer
a, b, c, d, e, n = map(int, input().split())

print((n + a - 1) // a + (n + b - 1) // b + (n + c - 1) // c + (n + d - 1) // d + (n + e - 1) // e)
