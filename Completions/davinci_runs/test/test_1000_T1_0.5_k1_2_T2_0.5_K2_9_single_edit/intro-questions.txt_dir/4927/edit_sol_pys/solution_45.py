
#!/usr/bin/env python

# https://codeforces.com/problemset/problem/1360/A

N, P, Q = map(int, input().split())

if P % N == 0:
    if Q % N == 0:
        print('paul')
    else:
        print('opponent')
else:
    if Q % N == 0:
        print('opponent')
    else:
        print('paul')
