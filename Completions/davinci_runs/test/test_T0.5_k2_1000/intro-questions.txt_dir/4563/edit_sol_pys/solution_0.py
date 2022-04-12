
import sys
from fractions import gcd
from functools import reduce

def lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm

def main():
    N = int(sys.stdin.readline().rstrip())
    T = []
    A = []
    for i in range(N):
        t,a = map(int, sys.stdin.readline().rstrip().split())
        T.append(t)
        A.append(a)
    ans = 1
    for i in range(N):
        if i == 0:
            ans = T[0] + A[0] - 1
        else:
            lcm_num = lcm(T[i],A[i])
            ans = lcm_num - ans
    print(ans)

if __name__ == '__main__':
    main()
