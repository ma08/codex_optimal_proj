# https://codeforces.com/contest/1244/problem/A


# SOLUTION
q = int(input())

for i in range(q):
    a, b, c, d = map(int, input().split())

    print(min(a, b, c + d))
