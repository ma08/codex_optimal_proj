

# SOLUTION

n, a1, a2, a3 = int(input()), *map(int, input().split())
b1, b2, b3 = map(int, input().split())

min_score = max(0, a2-b1) + max(0, a3-b2)
max_score = min(a2, b3) + min(a3, b1)

print(min_score, max_score)