import sys
sys.setrecursionlimit(10000000)


a,b,k = map(int, input().split())


































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































if k <= a:
    a -= k
else:
    k -= a
    a = 0
    if k <= b:
        b -= k
    else:
        b = 0





























































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































print(a,b)
