

a, b, c, n = (int(input()) for _ in range(4))
print([[i, j, k] for i in range(a + 1) for j in range(b + 1) for k in range(c + 1) if (i + j + k) != n])
