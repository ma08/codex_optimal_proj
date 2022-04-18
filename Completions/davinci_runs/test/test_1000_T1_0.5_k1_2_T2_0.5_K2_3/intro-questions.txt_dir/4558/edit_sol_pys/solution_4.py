import sys

#input
x, t = map(int, sys.stdin.readline().rstrip().split())
#calc
if t <= x - t:  #正の整数なら
    ans = x - 2*t  #2次元問題に帰着できる
else:
    ans = 2*t - x
#output
print(ans)
