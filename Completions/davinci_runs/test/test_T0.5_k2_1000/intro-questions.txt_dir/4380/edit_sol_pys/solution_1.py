
"""
A * B * C = odd
A * B * 1 = odd
A * B * 2 = even
A * B * 3 = odd

A * B * 1 = odd => A * B = odd
A * B * 3 = odd => A * B = odd

A * B = odd => A * B * 2 = even

A * B * 2 = even => A * B * C = even => C = 2
"""

a, b = map(int, input().split())

if a * b % 2 == 0:
    print('Yes')
else:
    print('No')
