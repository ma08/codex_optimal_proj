

#Program
n,h,l = map(int,input().split()) #n - number of movies, h - number of horror movies, l - number of similar movies
horror_list = list(map(int,input().split())) #list of horror movies
similar = {}
for _ in range(l):
    a,b = map(int,input().split()) #a,b - similar movies
    if a not in similar:
        similar[a] = [b]
    else:
        similar[a].append(b)
    if b not in similar:
        similar[b] = [a]
    else:
        similar[b].append(a)

hi = [0]*n #list of movies
for i in horror_list:
    hi[i] = 0 #set horror movies to 0
for i in horror_list:
    for j in similar[i]:
        if hi[j] == 0: #if the movie is horror then skip
            continue
        elif hi[j] == 1: #if the movie is non-horror then set it to horror
            hi[j] = 0
        else: #if the movie is undecided then set it to non-horror
            hi[j] = 1

max_hi = max(hi)
max_hi_movies = []
for i in range(n):
    if hi[i] == max_hi: #find all the movies that have the highest horror value
        max_hi_movies.append(i)
print(min(max_hi_movies)) #print the movie with the lowest index
