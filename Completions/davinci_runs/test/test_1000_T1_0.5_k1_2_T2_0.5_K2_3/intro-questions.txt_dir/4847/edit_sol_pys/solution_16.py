

def point_in_triangle(x, y, x1, y1, x2, y2, x3, y3):
    # print(x, y, x1, y1, x2, y2, x3, y3)
    if (x2 - x1) * (y - y1) - (x - x1) * (y2 - y1) > 0 and (x3 - x2) * (y - y2) - (x - x2) * (y3 - y2) > 0 and (x1 - x3) * (y - y3) - (x - x3) * (y1 - y3) > 0:
        return True
    return False

def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    n = int(input())
    count = 0
    for _ in range(n):
        x, y = map(int, input().split())
        if point_in_triangle(x, y, x1, y1, x2, y2, x3, y3):
            count += 1
    print(abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)
    print(count)

if __name__ == '__main__':
    main()
