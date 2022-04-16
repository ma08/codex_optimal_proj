

def main():
    n = int(input())
    bricks = [int(x) for x in input().split()]
    count = 0
    while len(bricks) > 0:
        base = bricks[0]
        i = 1
        while i < len(bricks) and bricks[i] > base:
            base = bricks[i]
            i += 1
        bricks = bricks[i:]
        count += 1
    print(count)

if __name__ == "__main__":
    main()
