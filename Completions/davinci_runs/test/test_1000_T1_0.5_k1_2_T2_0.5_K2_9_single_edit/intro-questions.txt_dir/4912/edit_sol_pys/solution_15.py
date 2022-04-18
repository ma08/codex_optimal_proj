
def main():
    h, w, n = map(int, input().split())
    bricks = list(map(int, input().split()))
    i = 0
    for _ in range(h):
        layer = 0
        while layer + bricks[i] <= w:
            layer += bricks[i]
            i += 1
            if i == n:
                print("YES")
                return
        if layer == 0:
            print("NO")
            return
    print("NO")

if __name__ == "__main__":
    main()
