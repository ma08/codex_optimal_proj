

def is_valid(prev, cur):
    if cur > prev:
        return True
    return False

def main():
    n = int(input())
    bricks = [int(x) for x in input().split()]
    towers = []
    for brick in bricks:
        if len(towers) == 0:
            towers.append(brick)
        else:
            if is_valid(towers[-1], brick):
                towers.append(brick)
    print(len(towers))

main()
