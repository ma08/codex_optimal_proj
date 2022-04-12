

#%%
r,n = map(int, input().split())
rooms = set(range(1,r+1))
booked = set(map(int, [input() for _ in range(n)]))
rooms = rooms - booked
if len(rooms) > 0:
    print(min(rooms))
else:
    print("too late")

#%%
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a.sort()
b.sort()
c.sort()

ans = 0
for i in range(n):
    ans += b[i] * (bisect_left(a, b[i]) + bisect_left(c, b[i]))
print(ans)
