"""
https://codeforces.com/contest/1369/problem/A
"""



N, P, Q = [int(x) for x in input().split()]

if P % (N + 1) == 0 or Q % (N + 1) == 0:
    print("opponent")
elif Q % (N + 1) == 0:
    print("paul")
else:
    if P // (N + 1) % 2 == 0:
        print("opponent")
    else:
        print("paul")
