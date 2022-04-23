

"""
1. Input A, B, and T
2. Initialize total_biscuits = 0
3. Initialize time = 0
3. While time <= T:
    total_biscuits += B
    time += A
4. Print total_biscuits
"""

a, b, t = map(int, input().split()) # 1 2 3

total_biscuits = 0 # 0
time = 0 # 0
while time <= t:
    total_biscuits += b # 0 + 2 = 2
    time += a # 0 + 1 = 1

print(total_biscuits)
