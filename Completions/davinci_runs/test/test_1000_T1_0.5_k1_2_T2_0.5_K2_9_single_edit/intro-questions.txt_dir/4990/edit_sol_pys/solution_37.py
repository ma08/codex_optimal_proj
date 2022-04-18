#problem link https://codeforces.com/problemset/problem/1228/A

#SOLUTION

b,k,g = map(int,input().split())
print(b//g+(1 if b%g else 0))
