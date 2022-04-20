

def main():
    n, m = [int(x) for x in input().split()]
    segments = []
    for i in range(n):
        segments.append([int(x) for x in input().split()])
    #print(segments)
    points = []
    for i in range(1,m+1):
        for j in range(n):
            if i in range(segments[j][0], segments[j][1]+1):
                break
            if j == n-1:
                points.append(i)
    print(len(points))
    print(*points)
    return 0

main()