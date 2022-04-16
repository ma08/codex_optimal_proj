

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
n,m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        print(a[i][j] + b[i][j], end = ' ')
    print()

#%%
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        print(a[i][j] + b[i][j], end = ' ')
    print()

#%%
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        print(a[i][j] + b[i][j], end = ' ')
    print()

#%%
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        print(a[i][j] + b[i][j], end = ' ')
    print()
