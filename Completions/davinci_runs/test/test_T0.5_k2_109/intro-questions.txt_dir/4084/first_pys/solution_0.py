

# ε₯ε
N, A, B = map(int, input().split())

# εΊε
print(N//(A+B)*A+min(N%(A+B), A))