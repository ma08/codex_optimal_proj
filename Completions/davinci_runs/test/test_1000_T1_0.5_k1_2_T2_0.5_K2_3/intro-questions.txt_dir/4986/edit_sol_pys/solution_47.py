# the code is for the question in the link: https://codeforces.com/contest/1371/problem/A

n = int(input())

for i in range(n):
    x = int(input())
    if x % 2 == 0:
        print(x // 2)
    else:
        print(x // 2 + 1)
