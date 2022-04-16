

def main():
    n = int(input())
    bricks = [int(x) for x in input().split()]
    towers = 0
    base = bricks[0] + 1
    for i in range(1, n):
        if bricks[i] > base:
            towers += 1
            base = bricks[i]
    towers += 1
    print(towers)

if __name__ == "__main__":
    main()
