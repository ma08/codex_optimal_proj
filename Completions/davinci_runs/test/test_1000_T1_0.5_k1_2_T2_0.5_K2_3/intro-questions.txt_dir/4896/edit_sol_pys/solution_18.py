

def main():
    n = int(input())
    bricks = [int(x) for x in input().split()]  # list comprehension
    towers = 1
    base = bricks[0]
    for i in range(1, n):
        if bricks[i] > base:
            towers += 1
            base = bricks[i]
    print(towers)

if __name__ == "__main__":
    main()
