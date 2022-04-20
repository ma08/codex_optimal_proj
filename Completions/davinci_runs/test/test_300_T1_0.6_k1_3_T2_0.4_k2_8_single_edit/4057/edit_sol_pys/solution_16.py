#https://codeforces.com/contest/1144/problem/A

n = int(input())
a = [int(x) for x in input().split()]
if len(set(a)) == n:
    print("YES")
else:
    print("NO")
