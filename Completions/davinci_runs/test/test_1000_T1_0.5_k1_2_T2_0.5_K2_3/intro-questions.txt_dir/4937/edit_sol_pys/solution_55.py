

import sys

def main():
    values = sys.stdin.readline().strip().split()
    n = int(values[0])
    a = int(values[1])
    values = sys.stdin.readline().strip().split()
    a = [int(i) for i in values]
    a.sort()
    a.reverse()
    result = 0
    for i in range(n):
        if a >= a[i]:
            a = a - a[i]
            result += 1
        else:
            break
    print(result)

if __name__ == "__main__":
    main()
