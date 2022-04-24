

"""
1. Input A, B, and T
2. Initialize total_biscuits = 0
3. Initialize time = 0
3. While time <= T:
    total_biscuits += B
    time += A
4. Print total_biscuits
"""

A, B, T = map(int, input().split())

total_biscuits = 0
time = 0
while time <= T:
    total_biscuits += B
    time += A

print(total_biscuits)
