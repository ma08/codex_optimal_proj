
import sys

def main():
    n, s, r = [int(x) for x in sys.stdin.readline().split()]
    damaged = [int(x) for x in sys.stdin.readline().split()]
    reserve = [int(x) for x in sys.stdin.readline().split()]
    damaged = set(damaged) # make set of damaged bikes
    reserve = set(reserve) # make set of reserve bikes
    if len(damaged) != s or len(reserve) != r:
        return 'ERROR' # check if number of bikes is correct
    if n < 2 or n > 10 or s < 2 or s > n or r < 1 or r > n:
        return 'ERROR' # check if number of bikes is correct
    for x in damaged:
        if x < 1 or x > n:
            return 'ERROR' # check if bike number is correct
    for x in reserve:
        if x < 1 or x > n:
            return 'ERROR' # check if bike number is correct
    for x in damaged:
        if x - 1 in reserve and x + 1 in reserve:
            reserve.remove(x - 1) # remove reserve bike
            reserve.remove(x + 1) # remove reserve bike
            damaged.remove(x) # remove damaged bike
        elif x - 1 in reserve:
            reserve.remove(x - 1) # remove reserve bike
            damaged.remove(x) # remove damaged bike
        elif x + 1 in reserve:
            reserve.remove(x + 1) # remove reserve bike
            damaged.remove(x) # remove damaged bike
    return len(damaged)

if __name__ == '__main__':
    print(main())
