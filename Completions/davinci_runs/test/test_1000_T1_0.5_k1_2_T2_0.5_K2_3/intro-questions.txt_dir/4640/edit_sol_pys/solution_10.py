

# The idea is to sort the points by x-coordinate,
# and then process them in that order.

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        xs = list(map(int, input().split()))
        ys = list(map(int, input().split()))
        points = [(x, y) for x, y in zip(xs, ys)]
        points.sort()
        platforms = []
        count = 0
        for x, y in points:
            while platforms and y > platforms[0][1]:
                platforms.pop(0)
            if not platforms:
                platforms.append((x, y))
                continue
            if y - platforms[0][1] <= k:
                count += 1
                if len(platforms) > 1 and y + k >= platforms[1][1]:
                    platforms.pop(0)
                    continue
            platforms.append((x, y))
        print(count)

if __name__ == '__main__':
    main()
