
import sys

def main():
    n, s, r = [int(x) for x in sys.stdin.readline().split()]
    damaged = [int(x) for x in sys.stdin.readline().split()]
    reserve = [int(x) for x in sys.stdin.readline().split()]
    damaged = set(damaged)
    reserve = set(reserve)
    if len(damaged) != s or len(reserve) != r:
        print('ERROR')
        return
    if n < 2 or n > 10 or s < 2 or s > n or r < 1 or r > n:
        print('ERROR')
        return
    for x in damaged:
        if x < 1 or x > n:
            print('ERROR')
            return
    for x in reserve:
        if x < 1 or x > n:
            print('ERROR')
            return
    for x in damaged:
        if x - 1 in reserve and x + 1 in reserve:
            reserve.remove(x - 1)
            reserve.remove(x + 1)
            damaged.remove(x)
        elif x - 1 in reserve:
            reserve.remove(x - 1)
            damaged.remove(x)
        elif x + 1 in reserve:
            reserve.remove(x + 1)
            damaged.remove(x)
    print(len(damaged))

if __name__ == '__main__':
    main()
