
n, m, d = map(int, input().split())
c = list(map(int, input().split())) #input in format "1 2 3 4"

def get_platforms(n, m, d, c):
    platforms = []
    for i in range(m):
        platforms.append([i+1]*c[i]) #will create a list of platforms
    return platforms

def get_river(n, m, d, c):
    platforms = get_platforms(n, m, d, c)
    river = [0] * n #will create a list of 0's
    for i in range(n):
        for j in range(m):
            if len(platforms[j]) == 0:
                continue
            if platforms[j][0] == i+1:
                river[i] = j+1
                platforms[j] = platforms[j][1:]
    return river

print("YES")
print(*get_river(n, m, d, c))
