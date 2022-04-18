

A, B, C, D, E, F = map(int, input().split())

print(min(A+B, A+C, A+D, A+E, A+F, B+C, B+D, B+E, B+F, C+D, C+E, C+F, D+E, D+F, E+F))
