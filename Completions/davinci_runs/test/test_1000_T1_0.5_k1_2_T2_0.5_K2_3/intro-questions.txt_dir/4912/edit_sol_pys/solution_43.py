
import sys

def main():
    h, w, n = map(int, sys.stdin.readline().split())
    bricks = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

    if sum(bricks) < h * w:
        print("NO")
        return

    i = 0
    while h > 0:
        if i == n:
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
