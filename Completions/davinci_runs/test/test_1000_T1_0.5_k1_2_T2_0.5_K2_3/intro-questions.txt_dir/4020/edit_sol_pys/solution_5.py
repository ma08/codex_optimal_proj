

import sys

h1, m1 = map(int, sys.stdin.readline().split(':'))
h2, m2 = map(int, sys.stdin.readline().split(':'))
# 분의 평균
m3 = (m1 + m2) // 2
# 시간의 평균
h3 = h1 + (m1 + m2) // 120

print('{:02}:{:02}'.format(h3, m3))
