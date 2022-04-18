import sys

n, m = map(int, input().split())

if n > m:
    print("Dr. Chaz needs {} more piece[s] of chicken!".format(n-m))
else:
    print("Dr. Chaz will have {} piece[s] of chicken left over!".format(m-n))
