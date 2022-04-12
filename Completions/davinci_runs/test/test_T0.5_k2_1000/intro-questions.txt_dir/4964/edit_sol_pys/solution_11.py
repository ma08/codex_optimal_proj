
n,h,l = map(int,input().split())
horror_list = list(map(int,input().split()))
similar = {}
for _ in range(l):
    a,b = map(int,input().split())
    similar.setdefault(a,[]).append(b)
    similar.setdefault(b,[]).append(a)

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
