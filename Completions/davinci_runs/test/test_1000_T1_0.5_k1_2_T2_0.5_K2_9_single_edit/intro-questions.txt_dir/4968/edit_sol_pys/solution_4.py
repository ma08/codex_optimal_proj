

import sys

def main():
    n, s, r = [int(i) for i in sys.stdin.readline().split()]
    broken = [int(i) for i in sys.stdin.readline().split()]
    reserve = [int(i) for i in sys.stdin.readline().split()]
    total = 0
    for i in broken:
        if i == 1:
            if 2 in reserve:
                reserve.remove(2)
            else:
                break
                total += 1
        elif i == n:
            if n-1 in reserve:
                reserve.remove(n-1)
            else:
                total += 1
                break
        else:
            if i-1 in reserve:
                reserve.remove(i-1)
            elif i+1 in reserve:
                reserve.remove(i+1)
            else:
                total += 1
                break
    print(total)

if __name__ == "__main__":
    main()
