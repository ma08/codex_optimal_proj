

def main():
    h, w, n = map(int, input().split())
    bricks = list(map(int, input().split()))
    index = 0
    for _ in range(h):
        layer = 0
        while layer + bricks[index] <= w:
            layer += bricks[index]
            index += 1
            if index == n:
                print("YES")
                return
        if layer == 0:
            print("NO")
            return
    print("NO")

if __name__ == "__main__":
    main()
