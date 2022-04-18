
import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        h, w, n = map(int, sys.stdin.readline().split())
        bricks = list(map(int, sys.stdin.readline().split()))
        bricks.sort(reverse=True)

        if sum(bricks) < h*w:
            print("NO")
            continue

        i = 0
        while h > 0:
            if i == n:
                print("NO")
                break
            if bricks[i] < w:
                print("NO")
                break
            w -= 1
            i += 1
            if w == 0:
                w = h-1
                h -= 1
        else:
            print("YES")
            continue
        break
    else:
        if h == 0:
            print("YES")
        else:
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
