
"""
A x B x C = odd
A x B x 1 = odd
A x B x 2 = even
A x B x 3 = odd

A x B x 1 = odd => A x B = odd
A x B x 3 = odd => A x B = odd

A x B = odd => A x B x 2 = even

A x B x 2 = even => A x B x C = even => C = 2
"""

a, b = map(int, input().split())

if a * b % 2 == 0:
    print('Yes')
else:
    print('No')
