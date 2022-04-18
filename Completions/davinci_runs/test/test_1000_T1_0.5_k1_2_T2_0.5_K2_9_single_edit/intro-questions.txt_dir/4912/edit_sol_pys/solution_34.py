

def main():
    h, w, n = map(int, input().split())  # input
    bricks = list(map(int, input().split()))  # input
    i = 0
    for _ in range(h):
        layer = 0
        while layer + bricks[i] <= w:
            layer += bricks[i]
            i += 1
            if i == n:
                print("YES")  # output
                return
        if layer == 0:
            print("NO")  # output
            return

    print("NO")

if __name__ == "__main__":
    main()
