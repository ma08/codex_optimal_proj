

# Programming
n,h,l = map(int,input().split())
horror_list = list(map(int,input().split()))
similar = {}
for _ in range(l):
    a,b = map(int,input().split())
    if a not in similar:
        similar[a] = [b]
    else:
        similar[a].append(b)
    if b not in similar:
        similar[b] = [a]
    else:
        similar[b].append(a)

hi = [0]*n
for i in horror_list:
    hi[i] = 0
for i in horror_list:
    for j in similar[i]:
        if hi[j] == 0:
            continue
        elif hi[j] == 1:
            hi[j] = 0
        else:
            hi[j] = 1

max_hi = max(hi)
max_hi_movies = []
for i in range(n):
    if hi[i] == max_hi:
        max_hi_movies.append(i)
print(min(max_hi_movies))
