import sys

def main():
    h, w, n = map(int, sys.stdin.readline().split())
    bricks = sorted(list(map(int, sys.stdin.readline().split())))

    if sum(bricks) < h * w:  # if the sum of bricks is less than the area, it's not possible
        print("NO")
        return

    i = 0
    while h > 0:  # while the height is positive
        if i == n:  # if we've used all the bricks
            print("NO")
            return
        if bricks[i] < w:  # if the brick is less than the width
            print("NO")
            return
        w -= 1
        i += 1
        if w == 0:  # if the width is 0
            w = h - 1  # set the width to the height minus 1
            h -= 1  # decrease the height

    print("YES")

if __name__ == "__main__":
    main()
