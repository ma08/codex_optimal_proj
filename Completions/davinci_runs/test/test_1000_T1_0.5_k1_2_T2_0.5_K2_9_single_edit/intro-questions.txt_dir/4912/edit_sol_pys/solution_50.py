


def check(h, w, bricks):
    i = 0
    for _ in range(h):
        layer = 0
        while layer + bricks[i] <= w:
            layer += bricks[i]
            i += 1
            if i == len(bricks):
                return True
        if layer == 0:
            return False
    return False


def main():
    h, w, n = map(int, input().split())
    bricks = list(map(int, input().split()))
    if check(h, w, bricks):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
