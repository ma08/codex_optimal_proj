
import sys

def main():
    h, w, n = map(int, sys.stdin.readline().split())
    bricks = list(map(int, sys.stdin.readline().split()))[:n]
    bricks.sort(reverse=True)

    if sum(bricks) < h*w:
        print("NO")
        return

    i = 0
    while h > 0:
        if i == len(bricks):
            print("NO")
            return
        if bricks[i] < w:
            print("NO")
            return
        w -= 1
        i += 1
        if w == 0:
            w = h-1
            h -= 1

    print("YES")

if __name__ == "__main__":
    main()
