

#%%
r,n = map(int, input().split())
rooms = set(range(1,r+1))
booked = set(map(int, [input() for _ in range(n)]))
rooms = rooms - booked
if len(rooms) > 0:
    print(min(rooms))
else:
    print("too late")


r,n = map(int, input().split())
rooms = set(range(1,r+1))
booked = set(map(int, [input() for _ in range(n)]))
rooms = rooms - booked
if len(rooms) > 0:
    print(min(rooms))
else:
    print("too late")
