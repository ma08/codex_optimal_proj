import sys
sys.setrecursionlimit(10**6)

n,w = map(int, input().split())
a = list(map(int, input().split()))

def check(x):
    if x == n:
        return True
    else:
        if x < n:
            if check(x+1):
                return True
            else:
                return False
        else:
            return False



k = 0
for i in range(w+1):
    if check(i):
        k += 1
print(k)
