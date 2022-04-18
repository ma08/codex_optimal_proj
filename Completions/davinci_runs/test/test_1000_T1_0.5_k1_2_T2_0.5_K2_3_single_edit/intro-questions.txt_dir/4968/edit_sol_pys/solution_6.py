import sys

def main():
    n, s, r = map(int, sys.stdin.readline().split())
    damaged = set(map(int, sys.stdin.readline().split()))
    reserve = set(map(int, sys.stdin.readline().split()))
    count = 0
    for i in range(1, n + 1):
        if i in damaged:
            if i - 1 in reserve and i + 1 in reserve:
                reserve.remove(i - 1)
                reserve.remove(i + 1)
            elif i - 1 in reserve:
                reserve.remove(i - 1)
            elif i + 1 in reserve:
                reserve.remove(i + 1)
            else:
                count += 1
    print(count)

if __name__ == '__main__':
    main()
