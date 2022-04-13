# the code is for the question in the link: https://codeforces.com/contest/1370/problem/B

for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    print(a[-1] - a[0])
