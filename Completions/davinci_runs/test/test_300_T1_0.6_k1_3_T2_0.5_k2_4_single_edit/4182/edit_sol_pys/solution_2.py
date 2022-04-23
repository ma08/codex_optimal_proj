
#%%
"""
n = 3
m = 2
x = 10
y = 20
p = [8, 15, 13]
q = [16, 22]
"""

n, m, x, y = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

if x >= y:
    print("War")
    exit()
if max(p) >= y or min(q) <= x:
    print("War")
    exit()
for i in range(x+1, y):
    if i in p:
        continue
    if i not in q:
        print("No War")
        exit()
print("War")
