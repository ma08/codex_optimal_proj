# Read input
A, B, C = map(int, input().split())

# Check if he can buy the toy
print("Yes" if A + B >= C else "No")
