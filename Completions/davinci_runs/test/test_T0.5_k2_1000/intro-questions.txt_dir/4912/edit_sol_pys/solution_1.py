
import sys

def main():
    h, w, n = map(int, sys.stdin.readline().split())
    bricks = sorted(map(int, sys.stdin.readline().split()))

    if sum(bricks) < h*w:
        print("NO") 
    else:
        if h == 1:
            print("YES") 
        else:
            if h == 2:
                if bricks[-1] >= w:
                    bricks.pop() 
                elif bricks[-1] < w:
                    if bricks[-1] + bricks[-2] >= w:
                        bricks.pop()
                        bricks.pop() 
                    elif bricks[-1] + bricks[-2] < w:
                        print("NO")
                        return
            else:
                layer = 0
                while bricks and layer < h-1:
                    if bricks[-1] >= w:
                        bricks.pop()
                        layer += 1
                    elif bricks[-1] < w:
                        bricks.pop()
                        if bricks[-1] == bricks[-2]:
                            bricks.pop()
                            bricks.pop()
                        else:
                            bricks.pop()
            if bricks: 
                print("YES")
            else:
                print("NO")

if __name__ == "__main__":
    main()
