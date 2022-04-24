

"""
1. Input A, B, and T
2. Initialize total_biscuits = 0
3. Initialize time = 0
3. While time <= T:
    total_biscuits += b
    time += a
4. Print total_biscuits
"""

a, b, t = map(int, input().split())

total_biscuits = 0
time = 0
while time <= t:
    total_biscuits += b
    time += a

print(total_biscuits)
