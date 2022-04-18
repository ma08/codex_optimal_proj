

def main():
    n = int(input())
    bricks = [int(x) for x in input().split()]
    towers = [bricks[0]]
    for brick in bricks:
        if brick > towers[-1]:
            towers.append(brick)
    print(len(towers))

main()
