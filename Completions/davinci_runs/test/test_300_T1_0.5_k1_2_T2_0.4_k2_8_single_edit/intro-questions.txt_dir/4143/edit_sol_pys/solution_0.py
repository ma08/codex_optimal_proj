
N = int(input())
A, B, C, D, E = [int(i) for i in input().split()]

print((N + A - 1) // A + (N + B - 1) // B + (N + C - 1) // C + (N + D - 1) // D + (N + E - 1) // E)
