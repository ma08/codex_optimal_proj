

# N = int(input())
# H = list(map(int, input().split()))

N = 5
H = [10, 4, 8, 7, 3]

"""
move_count = 0
prev_height = H[0]
for i in range(1, N):
    if H[i] <= prev_height:
        move_count += 1
    else:
        prev_height = H[i]
"""

move_count = 0
prev_height = H[0]
for i in range(1, N):
    if H[i] <= prev_height:
        move_count += 1
        prev_height = H[i]
    else:
        prev_height = H[i - 1]

print(move_count)