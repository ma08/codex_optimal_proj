

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
a = [int(i) for i in input().split()]
b = []
for i in range(n):
    if a[i] == 0:
        b.append(a[i])
        a.pop(i)
        break
a.sort(reverse=True)
b.extend(a)
print(*b, sep="")

#%%
n = int(input())
a = [int(i) for i in input().split()]
a.sort(reverse=True)
print(*a, sep="")
