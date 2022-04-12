


#%%
import sys
sys.stdin = open("input.txt")


#%%
r,n = map(int, input().split())
rooms = set(range(1,r+1))
booked = set(map(int, [input() for _ in range(n)]))
rooms = rooms - booked
if len(rooms) > 0:
    print(min(rooms))
else:


#%%
import sys
sys.stdin = open("input.txt")


#%%
n = int(input())
l = list(map(int, input().split()))
l.sort()
print(l[0])
    print("too late")
