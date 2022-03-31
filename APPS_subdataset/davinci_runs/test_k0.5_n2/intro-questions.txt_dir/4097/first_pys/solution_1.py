

import sys

def main():
    n = int(sys.stdin.readline().strip())
    b = list(map(int, sys.stdin.readline().strip().split()))
    if n == 2:
        print(0)
        return
    diff = b[1] - b[0]
    for i in range(2, n):
        if b[i] - b[i-1] != diff:
            if b[i] - b[i-1] == diff + 1:
                if b[i-1] - b[i-2] == diff - 1:
                    b[i-1] -= 1
                    print(1)
                    return
                else:
                    b[i] -= 1
                    print(1)
                    return
            elif b[i] - b[i-1] == diff - 1:
                if b[i-1] - b[i-2] == diff + 1:
                    b[i] += 1
                    print(1)
                    return
                else:
                    b[i-1] += 1
                    print(1)
                    return
            else:
                print(-1)
                return
    print(0)

if __name__ == "__main__":
    main()