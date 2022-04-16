

#submitted, accepted
#n, m, d = map(int, input().split())
#c = list(map(int, input().split()))

#def get_platforms(n, m, d, c):
#    platforms = []
#    for i in range(m):
#        platforms.append([i+1]*c[i])
#    return platforms

#def get_river(n, m, d, c):
#    platforms = get_platforms(n, m, d, c)
#    river = [0] * n
#    for i in range(n):
#        for j in range(m):
#            if len(platforms[j]) == 0:
#                continue
#            if platforms[j][0] == i+1:
#                river[i] = j+1
#                platforms[j] = platforms[j][1:]
#    return river

#print("YES")
#print(*get_river(n, m, d, c))


#submitted, accepted
#n = int(input())
#a = list(map(int, input().split()))

#def get_min_max(n, a):
#    min_max = []
#    for i in range(n):
#        for j in range(i+1, n):
#            min_max.append(min(a[i], a[j]) * max(a[i], a[j]))
#    return min_max

#print(min(get_min_max(n, a)))



























































