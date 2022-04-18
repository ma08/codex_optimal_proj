

"""
a * b * c = odd
a * b * 1 = odd
a * b * 2 = even
a * b * 3 = odd

a * b * 1 = odd => a * b = odd
a * b * 3 = odd => a * b = odd

a * b = odd => a * b * 2 = even

a * b * 2 = even => a * b * c = even => c = 2
"""

a, b = map(int, input().split())

if a * b % 2 == 0:
    print('Yes')
else:
    print('No')
