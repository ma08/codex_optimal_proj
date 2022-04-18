

def main():
    h, w, n = map(int, input().split())
    bricks = list(map(int, input().split()))
    i = 0
    for i in range(h):
        layer = 0
        while layer + bricks[j] <= w:
            layer += bricks[j]
            j += 1
            if j == n:
                print("YES")
                return
        if layer == 0:
            print("NO")
            return
    print("NO")

if __name__ == "__main__":
    main()
