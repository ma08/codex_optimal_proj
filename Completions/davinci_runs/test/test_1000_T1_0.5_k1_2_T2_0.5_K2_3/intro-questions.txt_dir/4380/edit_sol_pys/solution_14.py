

"""
A * B * C = odd
A * B * C = even
"""

a, b = map(int, input().split())

if a * b % 2 == 0:
    print('Yes')
else:
    print('No')
