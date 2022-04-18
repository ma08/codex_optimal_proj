
# My answer
N, A, B, C, D, E = (int(x) for x in input().split())

print((N + A - 1) // A + (N - A * ((N + A - 1) // A)) // B + (N - A * ((N + A - 1) // A) - B * ((N - A * ((N + A - 1) // A)) // B)) // C + (N - A * ((N + A - 1) // A) - B * ((N - A * ((N + A - 1) // A)) // B) - C * ((N - A * ((N + A - 1) // A) - B * ((N - A * ((N + A - 1) // A)) // B)) // C)) // D + (N - A * ((N + A - 1) // A) - B * ((N - A * ((N + A - 1) // A)) // B) - C * ((N - A * ((N + A - 1) // A) - B * ((N - A * ((N + A - 1) // A)) // B)) // C) - D * ((N - A * ((N + A - 1) // A) - B * ((N - A * ((N + A - 1) // A)) // B) - C * ((N - A * ((N + A - 1) // A) - B * ((N - A * ((N + A - 1) // A)) // B)) // C)) // D)) // E)

# Best answer
a, b, c, d, e, n = map(int, input().split())

print((n + a - 1) // a + (n + b - 1) // b + (n + c - 1) // c + (n + d - 1) // d + (n + e - 1) // e)
