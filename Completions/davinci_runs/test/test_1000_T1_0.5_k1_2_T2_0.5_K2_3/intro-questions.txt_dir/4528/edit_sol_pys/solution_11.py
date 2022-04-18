# This is a test

'''
This is a test
'''

t = int(input())

for i in range(t):
    h, m = map(int, input().split())
    h = int(h)
    m = int(m)
    print(1440 - (h * 60 + m))
