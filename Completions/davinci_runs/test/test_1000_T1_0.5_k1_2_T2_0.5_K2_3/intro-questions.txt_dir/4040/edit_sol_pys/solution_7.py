

#submitted
n, m, d = map(int, input().split())
c = list(map(int, input().split()))

def get_platforms(n, m, d, c):
    platforms = []  # list of platforms
    for i in range(m):  # iterate over platforms
        platforms.append([i+1]*c[i])  # add platform i+1 c[i] times
    return platforms  # return platforms

def get_river(n, m, d, c):
    platforms = get_platforms(n, m, d, c)  # get platforms
    river = [0] * n  # create river
    for i in range(n):  # iterate over river
        for j in range(m):  # iterate over platforms
            if len(platforms[j]) == 0:  # if platform empty
                continue
            if platforms[j][0] == i+1:
                river[i] = j+1
                platforms[j] = platforms[j][1:]
    return river

print("YES")
print(*get_river(n, m, d, c))
