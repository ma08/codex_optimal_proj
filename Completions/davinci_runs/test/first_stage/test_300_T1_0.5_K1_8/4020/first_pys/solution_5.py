

# SOLUTION

#!/usr/bin/python3

a, b = map(int, input().split(':'))
c, d = map(int, input().split(':'))

if a == c:
    if (b + d) % 2 == 0:
        print('{}:{}'.format(a, (b + d) // 2))
    else:
        print('{}:{}'.format(a, (b + d) // 2 + 1))
else:
    if (b + d) % 2 == 0:
        print('{}:{}'.format((a + c) // 2, (b + d) // 2))
    else:
        print('{}:{}'.format((a + c) // 2, (b + d) // 2 + 1))