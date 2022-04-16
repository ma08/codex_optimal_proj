

def main():
    h, w, n = map(int, input().split())
    bricks = list(map(int, input().split()))
    i, layer = 0, 0
    for _ in range(h):
        while layer + bricks[i] <= w:
            if layer == w:
                layer = 0
                break
            layer += bricks[i]
            i += 1
            if i == n:
                print("YES")
                return
        if layer != 0:
            print("NO")
            return
    print("NO")

if __name__ == "__main__":
    main()
