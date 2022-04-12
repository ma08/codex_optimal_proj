
def main():
    h, w, n = map(int, input().split())
    bricks = list(map(int, input().split()))
    i = 0
    for _ in range(h):
        line = 0
        while line + bricks[i] <= w:
            line += bricks[i]
            i += 1
            if i == n:
                print("YES")
                return
        if line == 0:
            print("NO")
            return
    print("NO")

if __name__ == "__main__":
    main()
